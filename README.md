# strip_markdown

[![PyPI](https://badge.fury.io/py/strip_markdown.svg)](https://pypi.org/project/strip_markdown)
[![ci](https://github.com/D3r3k23/strip_markdown/actions/workflows/ci.yaml/badge.svg)](https://github.com/D3r3k23/strip_markdown/actions/workflows/ci.yaml)

#### Converts markdown to plain text, including both a command line interface and importable package

## Installation

`$ python -m pip install strip_markdown`

## Usage

### Command line
`$ python -m strip_markdown MD_fn [TXT_fn]`

### Library
```python
>>> import strip_markdown
>>> TXT = strip_markdown.strip_markdown(MD)
>>> strip_markdown.strip_markdown_file(MD_fn, [TXT_fn])
```

* `TXT_fn` is optional: default is `<MD_fn>.md -> <MD_fn>.txt`
