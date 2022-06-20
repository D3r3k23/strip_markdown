# strip_markdown
[![PyPI](https://img.shields.io/pypi/v/strip_markdown?style=for-the-badge)](https://pypi.org/project/strip_markdown)
[![ci](https://img.shields.io/github/workflow/status/D3r3k23/strip_markdown/ci?label=ci&style=for-the-badge)](https://github.com/D3r3k23/strip_markdown/actions/workflows/ci.yaml)

#### Converts markdown to plain text, including both a command line interface and importable library

## Example

### Markdown
---
# Title

## Section

This is a line of text

**Bold text**

---

### Markdown source
---
```
# Title

## Section

This is a line of text

**Bold text**
```
---

### Text
---
```
Title
Section
This is a line of text
Bold text
```
---

## Installation

`$ pip install strip_markdown`

## Usage

### Command line
`$ python -m strip_markdown MD_fn [TXT_fn]`

### Library
```python
>>> import strip_markdown
>>>
>>> TXT: str = strip_markdown.strip_markdown(MD: str)
>>> strip_markdown.strip_markdown_file(MD_fn: Path, TXT_fn: Optional[Path])
```

* `TXT_fn` is optional: default is `<MD_fn>.md -> <MD_fn>.txt`
* If `TXT_fn` is a directory, `<MD_fn>.txt` is placed in that directory
