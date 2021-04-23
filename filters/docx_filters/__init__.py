import panflute as pf
from . import equations_no
from . import figures_no
from . import header_convert
from . import refs
from . import section_break
from . import word_elements
from . import parse_md
from . import fieldCode
from . import sugar_replace
import sys
import panflute as pf


def main(doc=None):
    # 为了适配域代码的"field"写法，需要在RawInline和RawBlock的支持类型中增加"field"，否则会报错
    pf.elements.RAW_FORMATS.add('field')

    if not doc:
        doc = pf.load()
        from_exec = True
    else:
        from_exec = False
    for mod in (parse_md, sugar_replace, fieldCode, header_convert, equations_no, figures_no, refs, word_elements):
        doc = mod.main(doc=doc)
        if parse_md.parse_only:
            break
    if from_exec:
        pf.dump(doc)
        return None
    else:
        return doc


if __name__ == '__main__':
    sys.exit(main())
