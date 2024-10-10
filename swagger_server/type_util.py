# coding: utf-8

import sys

if sys.version_info < (3, 7):
    import typing

    def is_generic(klass):
        """ Determine whether klass is a generic class. """
        return isinstance(klass, typing.GenericMeta)

    def is_dict(klass):
        """ Determine whether klass is a Dict. """
        return klass.__extra__ == dict

    def is_list(klass):
        """ Determine whether klass is a List. """
        return klass.__extra__ == list

else:
    def is_generic(klass):
        """ Determine whether klass is a generic class. """
        return hasattr(klass, '__origin__') and klass.__origin__ is not None

    def is_dict(klass):
        """ Determine whether klass is a Dict. """
        return getattr(klass, '__origin__', None) == dict

    def is_list(klass):
        """ Determine whether klass is a List. """
        return getattr(klass, '__origin__', None) == list
