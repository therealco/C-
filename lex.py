import re

def tokenize(code):
    tokens = []
    token_specification = [
        ('NUMBER',    r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',    r'='),            # Assignment operator
        ('END',       r';'),            # Statement terminator
        ('ID',        r'[A-Za-z]+'),    # Identifiers
        ('OP',        r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',   r'\n'),           # Line endings
        ('SKIP',      r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH',  r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value == 'print':
            kind = 'PRINT'
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        tokens.append((kind, value))
    return tokens
