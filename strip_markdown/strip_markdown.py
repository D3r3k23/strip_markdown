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

def strip_markdown_file(markdown_fn: str, text_fn: Optional[str]=None):
    if not os.path.isfile(markdown_fn):
        raise MarkdownError(f'{markdown_fn} does not exist')

    markdown_src = _read_file(markdown_fn)
    if not markdown_src:
        raise MarkdownError(f'Could not load {markdown_fn}')

    text = strip_markdown(markdown_src)

    if text_fn is None:
        text_fn = str(Path(markdown_fn).with_suffix('.txt'))
    elif os.path.isdir(text_fn):
        text_fn = os.path.join(text_fn, str(Path(markdown_fn).with_suffix('.txt').name))
    else:
        text_path = Path(text_fn).resolve()
        if not text_path.parent.is_dir():
            os.makedirs(text_path.parent)

    _write_file(text_fn, text)

def _read_file(filename: str) -> Optional[str]:
    try:
        with open(filename, 'r') as f:
            return f.read()
    except (OSError, IOError):
        return None

def _write_file(filename: str, text: str) -> bool:
    try:
        with open(filename, 'w') as f:
            f.write(text)
    except (OSError, IOError):
        return False
    else:
        return True
