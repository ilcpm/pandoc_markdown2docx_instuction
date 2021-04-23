#!/usr/bin/env python3
import panflute as pf


def suger_replace(elem, doc):
    if hasattr(elem, "attributes"):
        if 'style' in elem.attributes:
            elem.attributes['custom-style'] = elem.attributes['style']
            elem.attributes.pop('style')
    if hasattr(elem, "classes"):
        for i in elem.classes:
            if i == 'U':
                return pf.Underline(elem)


def main(doc=None):
    return pf.run_filter(suger_replace, doc=doc)


if __name__ == "__main__":
    main()
