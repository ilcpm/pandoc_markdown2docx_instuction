import panflute as pf
import yaml
import sys
from . import texcommands

parse_only = None


def parse_md(text, docinfo):
    return pf.convert_text(text, extra_args=['--metadata', 'parse_only: True', '-F', sys.argv[0]])


block_function_commands = {'parse': parse_md}
inline_function_commands = {'parse': lambda x, docinfo: list(parse_md('placeholder '+x, docinfo)[0].content[2:])
                            }


def check_isparse(doc):
    global parse_only
    parse_only = doc.get_metadata('parse_only')


def main(doc=None):
    replacer = texcommands.ConstTexCommandReplace(
        inline_function_commands=inline_function_commands, block_function_commands=block_function_commands)
    return pf.run_filters([replacer.action], prepare=check_isparse, doc=doc)


if __name__ == '__main__':
    sys.exit(main())
