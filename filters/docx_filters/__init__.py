import panflute as pf
from . import equations_no
from . import figures_no
from . import header_convert
from . import refs
from . import section_break
from . import texcommands
import sys

def main(doc=None):
    if not doc:
        doc = pf.load()
        from_exec = True
    else:
        from_exec = False
    for mod in (header_convert, equations_no, figures_no, refs, texcommands):
        doc = mod.main(doc=doc)
    if from_exec:
        pf.dump(doc)
        return None
    else:
        return doc


if __name__ == '__main__':
    sys.exit(main())
