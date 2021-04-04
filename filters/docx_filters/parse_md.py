import panflute as pf
import yaml
import sys
from . import texcommands

def parse_md(text, docinfo):
    return pf.convert_text(text)


block_function_commands = {'parse': parse_md}
inline_function_commands = {'parse': lambda x, docinfo: list(parse_md('placeholder '+x, docinfo)[0].content[2:])
                            }


def main(doc=None):
    replacer = texcommands.ConstTexCommandReplace(
        inline_function_commands=inline_function_commands, block_function_commands=block_function_commands)
    return pf.run_filter(replacer.action, doc=doc)


if __name__ == '__main__':
    sys.exit(main())
