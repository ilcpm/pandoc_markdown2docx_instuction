# 处理标题样式的编号

import panflute as pf

sec_no_num = '''
<w:pPr>
    <w:numPr>
        <w:numId w:val="0"/>
    </w:numPr>
</w:pPr>
'''


# def apply_style_header(elem: pf.Header, style: str):
#     style_raw = style.replace(' ', '')
#     elem.content.insert(0,
#                         pf.RawInline(f'<w:pPr><w:pStyle w:val="{style_raw}"/></w:pPr>',
#                                      format="openxml"))
#     return elem


appendix = False


def headerConvert(elem, doc):
    global appendix
    if isinstance(elem, pf.Header):
        if elem.level == 1:
            if 'appendix' in elem.classes:
                # appendix = True
                elem.attributes.update({'custom-style': "Appendix Text"})
                elem.classes.append('unnumbered')
            elif 'refs' in elem.classes or 'thank' in elem.classes:
                elem.classes.append('unnumbered')
            # else:
            #     appendix = False
        # 暂时用不到
        # elif appendix:
        #     apply_style_header(elem, f"Appendix Heading {elem.level}")
        # and (elem.level == 1 or not appendix):
        if 'unnumbered' in elem.classes:
            # apply_style_header(elem, f"Unnumbered Heading {elem.level}")
            elem.content.insert(0, pf.RawInline(sec_no_num, format='openxml'))
        if elem.identifier:
            elem.content = [pf.Span(*elem.content, identifier=elem.identifier)]
            elem.identifier = ""

    return elem


def main(doc=None):
    return pf.run_filter(headerConvert, doc=doc)


if __name__ == "__main__":
    main()
