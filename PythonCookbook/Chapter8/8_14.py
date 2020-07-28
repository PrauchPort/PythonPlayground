import collections
import bisect


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is None else []

    # Required sequence methods
    def __getitem__(self, index):
        return len(self._items)

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)
