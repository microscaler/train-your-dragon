import re
from pathlib import Path

CHECKLIST_FILE = Path('docs/DATA_PREPARATION_CHECKLIST.md')

PLACEHOLDER_TEXT = {
    '.jsonl': '{}\n',
    '.csv': 'placeholder\n',
    '.ckpt': '',
    '.json': '{}\n',
    '.md': '# Placeholder\n',
}

def parse_paths():
    paths = []
    pattern = re.compile(r'- \[ \] `([^`]+)`')
    for line in CHECKLIST_FILE.read_text().splitlines():
        match = pattern.search(line)
        if match:
            paths.append(match.group(1))
    return paths


def create_placeholder(path_str: str):
    path = Path(path_str)
    if path_str.endswith('/'):
        path.mkdir(parents=True, exist_ok=True)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        suffix = path.suffix
        text = PLACEHOLDER_TEXT.get(suffix, '')
        path.write_text(text)


def main():
    for p in parse_paths():
        create_placeholder(p)
    print('Placeholders created.')


if __name__ == '__main__':
    main()
