from collections import namedtuple


def make_namedtuple(class_name, **fields):
    return namedtuple(class_name, fields)(*fields.values())
