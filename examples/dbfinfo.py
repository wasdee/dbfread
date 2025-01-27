#!/usr/bin/env python
import sys

from dbfread2 import DBF


def show(*words):
    print('  ' + ' '.join(str(word) for word in words))

def show_field(field):
    print(f'    {field.name} ({field.type} {field.length})')

def main():
    for filename in sys.argv[1:]:
        print(filename + ':')
        table = DBF(filename, ignore_missing_memo=True)
        show('Name:', table.name)
        show('Memo File:', table.memofilename or '')
        show('DB Version:', table.dbversion)
        show('Records:', len(table))
        show('Deleted Records:', len(table.deleted))
        show('Last Updated:', table.date)
        show('Character Encoding:', table.encoding)
        show('Fields:')
        for field in table.fields:
            show_field(field)

main()
