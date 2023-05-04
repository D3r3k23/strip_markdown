from typing import *
from pathlib import Path
from argparse import ArgumentParser
import sys

from strip_markdown import *

def main() -> Optional[int]:
    parser = ArgumentParser(description='Converts markdown file to plain text')
    parser.add_argument('md',  type=str, help='markdown input file')
    parser.add_argument('txt', type=str, help='text output file', nargs='?', default='')
    args = parser.parse_args()

    md_path = args.md
    txt_path = args.txt if len(args.txt) > 0 else None
    try:
        strip_markdown_file(md_path, txt_path)
    except MarkdownError as e:
        print(f'Error: {e}')
        return 1

if __name__ == '__main__':
    sys.exit(main())
