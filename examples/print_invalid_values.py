"""
A field parser that returns invalid values as InvalidValue objects
instead of raising ValueError.
"""
from dbfread2 import DBF, FieldParser, InvalidValue


class MyFieldParser(FieldParser):
    def parse(self, field, data):
        try:
            return FieldParser.parse(self, field, data)
        except ValueError:
            return InvalidValue(data)

table = DBF('files/invalid_value.dbf', parser_class=MyFieldParser)
for i, record in enumerate(table):
    for name, value in record.items():
        if isinstance(value, InvalidValue):
            print(f'records[{i}][{name!r}] == {value!r}')
