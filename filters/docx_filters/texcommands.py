import panflute as pf
import re


class ConstTexCommandReplace():
    tex_re = re.compile(r'\\([^{ ]*)({.*})? ?')

    @classmethod
    def _parse_tex(self, tex_str, const_commands, function_commands, docinfo):
        re_result = self.tex_re.fullmatch(tex_str.strip())
        if re_result:
            if re_result[1] in function_commands:
                return function_commands[re_result[1]](
                    re_result[2][1:-1], docinfo=docinfo) if re_result[2] \
                    else function_commands[re_result[1]](docinfo=docinfo)
            elif re_result[1] in const_commands:
                return const_commands[re_result[1]]

    def action(self, elem, doc: pf.Doc):
        docinfo = [elem, doc]
        if isinstance(elem, pf.RawBlock):
            new_elem = self._parse_tex(elem.text, self.block_const_commands, self.block_function_commands, docinfo)
            if new_elem:
                return new_elem
            else:
                new_elem = self._parse_tex(elem.text, self.inline_const_commands, self.inline_function_commands, docinfo)
                if new_elem:
                    return pf.Para(new_elem)
        elif isinstance(elem, pf.RawInline):
            return self._parse_tex(elem.text, self.inline_const_commands, self.inline_function_commands, docinfo)

        return elem

    def __init__(self, inline_const_commands={}, inline_function_commands={},
                 block_const_commands={}, block_function_commands={}):
        self.inline_const_commands = inline_const_commands
        self.inline_function_commands = inline_function_commands
        self.block_const_commands = block_const_commands
        self.block_function_commands = block_function_commands
