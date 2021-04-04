import panflute as pf
import typing
import re
index_str = "目录"

inline_const_commands = {
    r'newLine':
    pf.LineBreak(),
    r'tabL':
    pf.RawInline(
        '<w:r><w:ptab w:relativeTo="margin" w:alignment="left" w:leader="none"/></w:r>',
        format="openxml"),
    r'tabR':
    pf.RawInline(
        '<w:r><w:ptab w:relativeTo="margin" w:alignment="right" w:leader="none"/></w:r>',
        format="openxml"),
    r'tabC':
    pf.RawInline(
        '<w:r><w:ptab w:relativeTo="margin" w:alignment="center" w:leader="none"/></w:r>',
        format="openxml"),
    r'tab':
    pf.RawInline("<w:r><w:tab/></w:r>", format="openxml"),
}

block_const_commands = {
    r'\newPage':
    pf.RawBlock("<w:p><w:r><w:br w:type=\"page\" /></w:r></w:p>",
                format="openxml"),
    r'\Reference': lambda x: pf.Div(identifier='refs'),
}


def toc(title='', format=r'TOC \o "1-3" \h \z \u'):
    TOC = pf.RawBlock(
        r'<w:sdt><w:sdtPr><w:docPartObj><w:docPartGallery w:val="Table of Contents"/><w:docPartUnique/></w:docPartObj></w:sdtPr><w:sdtContent><w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve">'
        + format
        + r'</w:instrText><w:fldChar w:fldCharType="separate"/><w:fldChar w:fldCharType="end"/></w:r></w:p></w:sdtContent></w:sdt>', format="openxml")
    return [
        pf.Div(pf.Para(pf.Span(pf.Str(title), identifier="TOC")),
               attributes={"custom-style": "TOC Heading"}),
        TOC
    ] if title else TOC


def newSection(paramStr=""):
    return pf.RawBlock('<w:p><w:pPr><w:sectPr>' + paramStr +
                       '</w:sectPr></w:pPr></w:p>', format='openxml')


null_para = pf.Para(pf.Span())

inline_function_commands = {
    'KeyWord': lambda x: pf.Span(pf.Str(x), attributes={'custom-style': 'Key Word'}),
    'refs': lambda x: pf.RawInline(f'<w:fldSimple w:instr=" REF {x} \\h "/>', format="openxml"),
    'Style': lambda x: pf.RawInline(f'''<w:pPr><w:pStyle w:val="{x}"/></w:pPr>''', format='openxml'),
}

block_function_commands = {
    'newPara': lambda x="1": [null_para] * (1 if x == "" else int(x)),
    'toc': toc,
    'newSection': newSection
}


class ConstTexCommandReplace():
    tex_re = re.compile(r'\\([^{ ]*)({.*})? ?')

    @classmethod
    def _parse_tex(self, tex_str, const_commands, function_commands):
        re_result = self.tex_re.fullmatch(tex_str.strip())
        if re_result:
            if re_result[1] in function_commands:
                return function_commands[re_result[1]](
                    re_result[2][1:-1]) if re_result[2] else function_commands[re_result[1]]()
            elif re_result[1] in const_commands:
                return const_commands[re_result[1]]

    def action(self, elem, doc: pf.Doc):
        # pf.debug('s:', elem)
        pf.debug(list(i.content[0].text for i in doc.metadata['pandoc_args']))
        if isinstance(elem, pf.RawBlock):
            if new_elem := self._parse_tex(elem.text, self.block_const_commands, self.block_function_commands):
                return new_elem
            elif new_elem := self._parse_tex(elem.text, self.inline_const_commands, self.inline_function_commands):
                return pf.Para(new_elem)
        elif isinstance(elem, pf.RawInline):
            return self._parse_tex(elem.text, self.inline_const_commands, self.inline_function_commands)

        return elem

    def __init__(self, inline_const_commands={}, inline_function_commands={},
                 block_const_commands={}, block_function_commands={}):
        self.inline_const_commands = inline_const_commands
        self.inline_function_commands = inline_function_commands
        self.block_const_commands = block_const_commands
        self.block_function_commands = block_function_commands


def main(doc=None):
    replacer = ConstTexCommandReplace(
        inline_const_commands, inline_function_commands, block_const_commands, block_function_commands)
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()
