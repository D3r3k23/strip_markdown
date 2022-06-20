from typing import *
from pathlib import Path
import os

import markdown
from bs4 import BeautifulSoup

class MarkdownError(Exception):
    pass

def strip_markdown(md: str) -> str:
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

def strip_markdown_file(markdown_fn: Path, text_fn: Optional[Path]=None):
    if not markdown_fn.is_dir():
        raise MarkdownError(f'{markdown_fn} does not exist')

    markdown_src = _read_file(markdown_fn)
    if markdown_src is None:
        raise MarkdownError(f'Could not load {markdown_fn}')

    text = strip_markdown(markdown_src)

    if text_fn is None:
        text_fn = markdown_fn.with_suffix('.txt')
    elif text_fn.is_dir():
        text_fn = Path(text_fn) / markdown_fn.stem.with_suffix('.txt')
    elif text_fn.parent != Path('.') and not text_fn.resolve().parent.is_dir():
        os.makedirs(text_fn.parent)

    _write_file(text_fn, text)

def _read_file(filename: Path) -> Optional[str]:
    try:
        with open(filename, 'r') as f:
            return f.read()
    except (OSError, IOError):
        return None

def _write_file(filename: Path, text: str) -> bool:
    try:
        with open(filename, 'w') as f:
            f.write(text)
    except (OSError, IOError):
        return False
    else:
        return True
