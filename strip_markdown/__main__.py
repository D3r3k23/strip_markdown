from typing import *
import argparse
import sys

from strip_markdown import *

def main() -> Optional[int]:
    parser = argparse.ArgumentParser(description='Converts markdown file to plain text')
    parser.add_argument('md',  type=str, help='markdown input file')
    parser.add_argument('txt', type=str, help='text output file', nargs='?', default='')
    args = parser.parse_args()

    try:
        if len(args.txt) > 0:
            strip_markdown_file(args.md, args.txt)
        else:
            strip_markdown_file(args.md)
    except MarkdownError as e:
        print(f'Error: {e}')
        return 1

if __name__ == '__main__':
    sys.exit(main())
