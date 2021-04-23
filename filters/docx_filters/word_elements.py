from . import texcommands
import panflute as pf
import sys

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
    r'newPage':
    pf.RawBlock("<w:p><w:r><w:br w:type=\"page\" /></w:r></w:p>",
                format="openxml"),
    r'Reference': pf.Div(identifier='refs'),
}


def tocRaw(title='', format=r'TOC \o "1-3" \h \z \u', docinfo=None):
    TOC = pf.RawBlock(
        r'<w:sdt><w:sdtPr><w:docPartObj><w:docPartGallery w:val="Table of Contents"/><w:docPartUnique/></w:docPartObj></w:sdtPr><w:sdtContent><w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve">'
        + format
        + r'</w:instrText><w:fldChar w:fldCharType="separate"/><w:fldChar w:fldCharType="end"/></w:r></w:p></w:sdtContent></w:sdt>', format="openxml")
    return [
        pf.Div(pf.Para(pf.Span(pf.Str(title), identifier="TOC")),
               attributes={"custom-style": "TOC Heading"}),
        TOC
    ] if title else TOC


def newSection(paramStr="", docinfo=None):
    return pf.RawBlock('<w:p><w:pPr><w:sectPr>' + paramStr +
                       '</w:sectPr></w:pPr></w:p>', format='openxml')


null_para = pf.Para(pf.Span())


inline_function_commands = {
    'Space': lambda x, docinfo=None: [pf.Space()] * (1 if x == "" else int(x)),
    'KeyWord': lambda x, docinfo=None: pf.Span(pf.Str(x), attributes={'custom-style': 'Key Word'}),
    'refs': lambda x, docinfo=None: pf.RawInline(f'<w:fldSimple w:instr=" REF {x} \\h "/>', format="openxml"),
    'Style': lambda x, docinfo=None: pf.RawInline(f'''<w:pPr><w:pStyle w:val="{x}"/></w:pPr>''', format='openxml')}

block_function_commands = {
    'newPara': lambda x="1", docinfo=None: [null_para] * (1 if x == "" else int(x)),
    'tocRaw': tocRaw,
    'newSection': newSection
}


def main(doc=None):
    replacer = texcommands.ConstTexCommandReplace(
        inline_const_commands, inline_function_commands, block_const_commands, block_function_commands)
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == '__main__':
    sys.exit(main())
