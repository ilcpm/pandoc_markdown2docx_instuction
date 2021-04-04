# 将 `{xxx}`{=field} 这样的写法转变为域代码
# 并且可以嵌套 `{Ref {Ref test_ref_ref}}`{=field}
# 借鉴自https://github.com/centixkadon/nju-thesis-markdown/blob/33bdc591d25f7b2a4fd96ea58bae450c2f99db9d/src/thesis.lua#L634

import panflute as pf

fieldPrefix = """<w:fldChar w:fldCharType="begin"/><w:instrText xml:space="preserve">"""
fieldSuffix = """</w:instrText><w:fldChar w:fldCharType="end"/>"""


class fieldCode():
    def action(self, elem, doc):
        if isinstance(elem, pf.RawInline):
            elem: pf.RawInline
            if elem.format in ["docx", "field"]:
                fieldStr: str = elem.text.strip()
                if not (fieldStr.startswith('{') and fieldStr.endswith('}')):
                    return
                # 通过匹配'{'和'}'中间的字符来实现
                # TODO .replace('|', '')
                return pf.RawInline('<w:r>' + fieldStr.replace('{', fieldPrefix).replace('}', fieldSuffix) + '</w:r>', format='openxml')
                # text = ""
                # instr = ""
                # for i in elem.text:
                #     if i == '{':
                #         if len(instr) > 0:
                #             text += '<w:instrText xml:space="preserve">%s</w:instrText>' % instr
                #         text += r'<w:fldChar w:fldCharType="begin"/>'
                #         instr = ""
                #     elif i == '}':
                #         pass
                #     else:
                #         instr += i

    def __init__(self) -> None:
        pass


def main(doc=None):
    replacer = fieldCode()
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == "__main__":
    main()
