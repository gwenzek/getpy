from collections import MutableMapping
from typing import Iterable

import numpy as np

from .sparsepy_types import _types

class Dict(MutableMapping):
    def __init__(self, key_type, value_type):
        self.__dict = _types[(np.dtype(key_type), np.dtype(value_type))]()

    def __repr__(self):
        return str([(key, value) for key, value in self.items()])

    def __getitem__(self, key):
        if isinstance(key, Iterable):
            return self.__dict.__getitem_vec__(key)
        else:
            return self.__dict.__getitem__(key)

    def __setitem__(self, key, value):
        if isinstance(key, Iterable):
            self.__dict.__setitem_vec__(key, value)
        else:
            self.__dict.__setitem__(key, value)

    def __delitem__(self, key):
        if isinstance(key, Iterable):
            self.__dict.__delitem_vec__(key)
        else:
            self.__dict.__delitem__(key)

    def __contains__(self, key):
        if isinstance(key, Iterable):
            return self.__dict.__contains_vec__(key)
        else:
            return self.__dict.__contains__(key)

    def __len__(self):
        return self.__dict.__len__()

    def __iter__(self):
        for key, value in self.items():
            yield key

    def items(self):
        return self.__dict.items()

    def dump(self, filename):
        return self.__dict.dump(filename)

    def load(self, filename):
        return self.__dict.load(filename)