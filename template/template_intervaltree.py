# Contains the following license
# - https://github.com/chaimleib/intervaltree
# - https://github.com/grantjenks/python-sortedcontainers/

# Copyright 2014-2019 Grant Jenks

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



"""Sorted List
==============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted list implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedList`
* :class:`SortedKeyList`

"""
# pylint: disable=too-many-lines

import sys
import traceback

from bisect import bisect_left, bisect_right, insort
from itertools import chain, repeat, starmap
from math import log2
from operator import add, eq, ne, gt, ge, lt, le, iadd
from textwrap import dedent

###############################################################################
# BEGIN Python 2/3 Shims
###############################################################################

try:
    from collections.abc import Sequence, MutableSequence
except ImportError:
    from collections import Sequence, MutableSequence

from functools import wraps
from sys import hexversion

if hexversion < 0x03000000:
    from itertools import imap as map  # pylint: disable=redefined-builtin
    from itertools import izip as zip  # pylint: disable=redefined-builtin
    try:
        from thread import get_ident
    except ImportError:
        from dummy_thread import get_ident
else:
    from functools import reduce
    try:
        from _thread import get_ident
    except ImportError:
        from _dummy_thread import get_ident


def recursive_repr(fillvalue='...'):
    "Decorator to make a repr function return fillvalue for a recursive call."
    # pylint: disable=missing-docstring
    # Copied from reprlib in Python 3
    # https://hg.python.org/cpython/file/3.6/Lib/reprlib.py

    def decorating_function(user_function):
        repr_running = set()

        @wraps(user_function)
        def wrapper(self):
            key = id(self), get_ident()
            if key in repr_running:
                return fillvalue
            repr_running.add(key)
            try:
                result = user_function(self)
            finally:
                repr_running.discard(key)
            return result

        return wrapper

    return decorating_function

###############################################################################
# END Python 2/3 Shims
###############################################################################


class SortedList(MutableSequence):
    """Sorted list is a sorted mutable sequence.

    Sorted list values are maintained in sorted order.

    Sorted list values must be comparable. The total ordering of values must
    not change while they are stored in the sorted list.

    Methods for adding values:

    * :func:`SortedList.add`
    * :func:`SortedList.update`
    * :func:`SortedList.__add__`
    * :func:`SortedList.__iadd__`
    * :func:`SortedList.__mul__`
    * :func:`SortedList.__imul__`

    Methods for removing values:

    * :func:`SortedList.clear`
    * :func:`SortedList.discard`
    * :func:`SortedList.remove`
    * :func:`SortedList.pop`
    * :func:`SortedList.__delitem__`

    Methods for looking up values:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.count`
    * :func:`SortedList.index`
    * :func:`SortedList.__contains__`
    * :func:`SortedList.__getitem__`

    Methods for iterating values:

    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList.__iter__`
    * :func:`SortedList.__reversed__`

    Methods for miscellany:

    * :func:`SortedList.copy`
    * :func:`SortedList.__len__`
    * :func:`SortedList.__repr__`
    * :func:`SortedList._check`
    * :func:`SortedList._reset`

    Sorted lists use lexicographical ordering semantics when compared to other
    sequences.

    Some methods of mutable sequences are not supported and will raise
    not-implemented error.

    """
    DEFAULT_LOAD_FACTOR = 1000


    def __init__(self, iterable=None, key=None):
        """Initialize sorted list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted list.

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList()
        >>> sl
        SortedList([])
        >>> sl = SortedList([3, 1, 2, 5, 4])
        >>> sl
        SortedList([1, 2, 3, 4, 5])

        :param iterable: initial values (optional)

        """
        assert key is None
        self._len = 0
        self._load = self.DEFAULT_LOAD_FACTOR
        self._lists = []
        self._maxes = []
        self._index = []
        self._offset = 0

        if iterable is not None:
            self._update(iterable)


    def __new__(cls, iterable=None, key=None):
        """Create new sorted list or sorted-key list instance.

        Optional `key`-function argument will return an instance of subtype
        :class:`SortedKeyList`.

        >>> sl = SortedList()
        >>> isinstance(sl, SortedList)
        True
        >>> sl = SortedList(key=lambda x: -x)
        >>> isinstance(sl, SortedList)
        True
        >>> isinstance(sl, SortedKeyList)
        True

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)
        :return: sorted list or sorted-key list instance

        """
        # pylint: disable=unused-argument
        if key is None:
            return object.__new__(cls)
        else:
            if cls is SortedList:
                return object.__new__(SortedKeyList)
            else:
                raise TypeError('inherit SortedKeyList for key argument')


    @property
    def key(self):  # pylint: disable=useless-return
        """Function used to extract comparison key from values.

        Sorted list compares values directly so the key function is none.

        """
        return None


    def _reset(self, load):
        """Reset sorted list load factor.

        The `load` specifies the load-factor of the list. The default load
        factor of 1000 works well for lists from tens to tens-of-millions of
        values. Good practice is to use a value that is the cube root of the
        list size. With billions of elements, the best load factor depends on
        your usage. It's best to leave the load factor at the default until you
        start benchmarking.

        See :doc:`implementation` and :doc:`performance-scale` for more
        information.

        Runtime complexity: `O(n)`

        :param int load: load-factor for sorted list sublists

        """
        values = reduce(iadd, self._lists, [])
        self._clear()
        self._load = load
        self._update(values)


    def clear(self):
        """Remove all values from sorted list.

        Runtime complexity: `O(n)`

        """
        self._len = 0
        del self._lists[:]
        del self._maxes[:]
        del self._index[:]
        self._offset = 0

    _clear = clear


    def add(self, value):
        """Add `value` to sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.add(3)
        >>> sl.add(1)
        >>> sl.add(2)
        >>> sl
        SortedList([1, 2, 3])

        :param value: value to add to sorted list

        """
        _lists = self._lists
        _maxes = self._maxes

        if _maxes:
            pos = bisect_right(_maxes, value)

            if pos == len(_maxes):
                pos -= 1
                _lists[pos].append(value)
                _maxes[pos] = value
            else:
                insort(_lists[pos], value)

            self._expand(pos)
        else:
            _lists.append([value])
            _maxes.append(value)

        self._len += 1


    def _expand(self, pos):
        """Split sublists with length greater than double the load-factor.

        Updates the index when the sublist length is less than double the load
        level. This requires incrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        """
        _load = self._load
        _lists = self._lists
        _index = self._index

        if len(_lists[pos]) > (_load << 1):
            _maxes = self._maxes

            _lists_pos = _lists[pos]
            half = _lists_pos[_load:]
            del _lists_pos[_load:]
            _maxes[pos] = _lists_pos[-1]

            _lists.insert(pos + 1, half)
            _maxes.insert(pos + 1, half[-1])

            del _index[:]
        else:
            if _index:
                child = self._offset + pos
                while child:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1


    def update(self, iterable):
        """Update sorted list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.update([3, 1, 2])
        >>> sl
        SortedList([1, 2, 3])

        :param iterable: iterable of values to add

        """
        _lists = self._lists
        _maxes = self._maxes
        values = sorted(iterable)

        if _maxes:
            if len(values) * 4 >= self._len:
                _lists.append(values)
                values = reduce(iadd, _lists, [])
                values.sort()
                self._clear()
            else:
                _add = self.add
                for val in values:
                    _add(val)
                return

        _load = self._load
        _lists.extend(values[pos:(pos + _load)]
                      for pos in range(0, len(values), _load))
        _maxes.extend(sublist[-1] for sublist in _lists)
        self._len = len(values)
        del self._index[:]

    _update = update


    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list.

        ``sl.__contains__(value)`` <==> ``value in sl``

        Runtime complexity: `O(log(n))`

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> 3 in sl
        True

        :param value: search for value in sorted list
        :return: true if `value` in sorted list

        """
        _maxes = self._maxes

        if not _maxes:
            return False

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            return False

        _lists = self._lists
        idx = bisect_left(_lists[pos], value)

        return _lists[pos][idx] == value


    def discard(self, value):
        """Remove `value` from sorted list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.discard(5)
        >>> sl.discard(0)
        >>> sl == [1, 2, 3, 4]
        True

        :param value: `value` to discard from sorted list

        """
        _maxes = self._maxes

        if not _maxes:
            return

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            return

        _lists = self._lists
        idx = bisect_left(_lists[pos], value)

        if _lists[pos][idx] == value:
            self._delete(pos, idx)


    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.remove(5)
        >>> sl == [1, 2, 3, 4]
        True
        >>> sl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted list
        :raises ValueError: if `value` is not in sorted list

        """
        _maxes = self._maxes

        if not _maxes:
            raise ValueError('{0!r} not in list'.format(value))

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            raise ValueError('{0!r} not in list'.format(value))

        _lists = self._lists
        idx = bisect_left(_lists[pos], value)

        if _lists[pos][idx] == value:
            self._delete(pos, idx)
        else:
            raise ValueError('{0!r} not in list'.format(value))


    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`.

        Combines lists that are less than half the load level.

        Updates the index when the sublist length is more than half the load
        level. This requires decrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        :param int pos: lists index
        :param int idx: sublist index

        """
        _lists = self._lists
        _maxes = self._maxes
        _index = self._index

        _lists_pos = _lists[pos]

        del _lists_pos[idx]
        self._len -= 1

        len_lists_pos = len(_lists_pos)

        if len_lists_pos > (self._load >> 1):
            _maxes[pos] = _lists_pos[-1]

            if _index:
                child = self._offset + pos
                while child > 0:
                    _index[child] -= 1
                    child = (child - 1) >> 1
                _index[0] -= 1
        elif len(_lists) > 1:
            if not pos:
                pos += 1

            prev = pos - 1
            _lists[prev].extend(_lists[pos])
            _maxes[prev] = _lists[prev][-1]

            del _lists[pos]
            del _maxes[pos]
            del _index[:]

            self._expand(prev)
        elif len_lists_pos:
            _maxes[pos] = _lists_pos[-1]
        else:
            del _lists[pos]
            del _maxes[pos]
            del _index[:]


    def _loc(self, pos, idx):
        """Convert an index pair (lists index, sublist index) into a single
        index number that corresponds to the position of the value in the
        sorted list.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree from a leaf node to the root. The
        parent of each node is easily computable at ``(pos - 1) // 2``.

        Left-child nodes are always at odd indices and right-child nodes are
        always at even indices.

        When traversing up from a right-child node, increment the total by the
        left-child node.

        The final index is the sum from traversal and the index in the sublist.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Converting an index pair (2, 3) into a single index involves iterating
        like so:

        1. Starting at the leaf node: offset + alpha = 3 + 2 = 5. We identify
           the node as a left-child node. At such nodes, we simply traverse to
           the parent.

        2. At node 9, position 2, we recognize the node as a right-child node
           and accumulate the left-child in our total. Total is now 5 and we
           traverse to the parent at position 0.

        3. Iteration ends at the root.

        The index is then the sum of the total and sublist index: 5 + 3 = 8.

        :param int pos: lists index
        :param int idx: sublist index
        :return: index in sorted list

        """
        if not pos:
            return idx

        _index = self._index

        if not _index:
            self._build_index()

        total = 0

        # Increment pos to point in the index to len(self._lists[pos]).

        pos += self._offset

        # Iterate until reaching the root of the index tree at pos = 0.

        while pos:

            # Right-child nodes are at odd indices. At such indices
            # account the total below the left child node.

            if not pos & 1:
                total += _index[pos - 1]

            # Advance pos to the parent node.

            pos = (pos - 1) >> 1

        return total + idx


    def _pos(self, idx):
        """Convert an index into an index pair (lists index, sublist index)
        that can be used to access the corresponding lists position.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree to a leaf node. Each node has two
        children which are easily computable. Given an index, pos, the
        left-child is at ``pos * 2 + 1`` and the right-child is at ``pos * 2 +
        2``.

        When the index is less than the left-child, traversal moves to the
        left sub-tree. Otherwise, the index is decremented by the left-child
        and traversal moves to the right sub-tree.

        At a child node, the indexing pair is computed from the relative
        position of the child node as compared with the offset and the remaining
        index.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Indexing position 8 involves iterating like so:

        1. Starting at the root, position 0, 8 is compared with the left-child
           node (5) which it is greater than. When greater the index is
           decremented and the position is updated to the right child node.

        2. At node 9 with index 3, we again compare the index to the left-child
           node with value 4. Because the index is the less than the left-child
           node, we simply traverse to the left.

        3. At node 4 with index 3, we recognize that we are at a leaf node and
           stop iterating.

        4. To compute the sublist index, we subtract the offset from the index
           of the leaf node: 5 - 3 = 2. To compute the index in the sublist, we
           simply use the index remaining from iteration. In this case, 3.

        The final index pair from our example is (2, 3) which corresponds to
        index 8 in the sorted list.

        :param int idx: index in sorted list
        :return: (lists index, sublist index) pair

        """
        if idx < 0:
            last_len = len(self._lists[-1])

            if (-idx) <= last_len:
                return len(self._lists) - 1, last_len + idx

            idx += self._len

            if idx < 0:
                raise IndexError('list index out of range')
        elif idx >= self._len:
            raise IndexError('list index out of range')

        if idx < len(self._lists[0]):
            return 0, idx

        _index = self._index

        if not _index:
            self._build_index()

        pos = 0
        child = 1
        len_index = len(_index)

        while child < len_index:
            index_child = _index[child]

            if idx < index_child:
                pos = child
            else:
                idx -= index_child
                pos = child + 1

            child = (pos << 1) + 1

        return (pos - self._offset, idx)


    def _build_index(self):
        """Build a positional index for indexing the sorted list.

        Indexes are represented as binary trees in a dense array notation
        similar to a binary heap.

        For example, given a lists representation storing integers::

            0: [1, 2, 3]
            1: [4, 5]
            2: [6, 7, 8, 9]
            3: [10, 11, 12, 13, 14]

        The first transformation maps the sub-lists by their length. The
        first row of the index is the length of the sub-lists::

            0: [3, 2, 4, 5]

        Each row after that is the sum of consecutive pairs of the previous
        row::

            1: [5, 9]
            2: [14]

        Finally, the index is built by concatenating these lists together::

            _index = [14, 5, 9, 3, 2, 4, 5]

        An offset storing the start of the first row is also stored::

            _offset = 3

        When built, the index can be used for efficient indexing into the list.
        See the comment and notes on ``SortedList._pos`` for details.

        """
        row0 = list(map(len, self._lists))

        if len(row0) == 1:
            self._index[:] = row0
            self._offset = 0
            return

        head = iter(row0)
        tail = iter(head)
        row1 = list(starmap(add, zip(head, tail)))

        if len(row0) & 1:
            row1.append(row0[-1])

        if len(row1) == 1:
            self._index[:] = row1 + row0
            self._offset = 1
            return

        size = 2 ** (int(log2(len(row1) - 1)) + 1)
        row1.extend(repeat(0, size - len(row1)))
        tree = [row0, row1]

        while len(tree[-1]) > 1:
            head = iter(tree[-1])
            tail = iter(head)
            row = list(starmap(add, zip(head, tail)))
            tree.append(row)

        reduce(iadd, reversed(tree), self._index)
        self._offset = size * 2 - 1


    def __delitem__(self, index):
        """Remove value at `index` from sorted list.

        ``sl.__delitem__(index)`` <==> ``del sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> del sl[2]
        >>> sl
        SortedList(['a', 'b', 'd', 'e'])
        >>> del sl[:2]
        >>> sl
        SortedList(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        """
        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)

            if step == 1 and start < stop:
                if start == 0 and stop == self._len:
                    return self._clear()
                elif self._len <= 8 * (stop - start):
                    values = self._getitem(slice(None, start))
                    if stop < self._len:
                        values += self._getitem(slice(stop, None))
                    self._clear()
                    return self._update(values)

            indices = range(start, stop, step)

            # Delete items from greatest index to least so
            # that the indices remain valid throughout iteration.

            if step > 0:
                indices = reversed(indices)

            _pos, _delete = self._pos, self._delete

            for index in indices:
                pos, idx = _pos(index)
                _delete(pos, idx)
        else:
            pos, idx = self._pos(index)
            self._delete(pos, idx)


    def __getitem__(self, index):
        """Lookup value at `index` in sorted list.

        ``sl.__getitem__(index)`` <==> ``sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl[1]
        'b'
        >>> sl[-1]
        'e'
        >>> sl[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
        _lists = self._lists

        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)

            if step == 1 and start < stop:
                # Whole slice optimization: start to stop slices the whole
                # sorted list.

                if start == 0 and stop == self._len:
                    return reduce(iadd, self._lists, [])

                start_pos, start_idx = self._pos(start)
                start_list = _lists[start_pos]
                stop_idx = start_idx + stop - start

                # Small slice optimization: start index and stop index are
                # within the start list.

                if len(start_list) >= stop_idx:
                    return start_list[start_idx:stop_idx]

                if stop == self._len:
                    stop_pos = len(_lists) - 1
                    stop_idx = len(_lists[stop_pos])
                else:
                    stop_pos, stop_idx = self._pos(stop)

                prefix = _lists[start_pos][start_idx:]
                middle = _lists[(start_pos + 1):stop_pos]
                result = reduce(iadd, middle, prefix)
                result += _lists[stop_pos][:stop_idx]

                return result

            if step == -1 and start > stop:
                result = self._getitem(slice(stop + 1, start + 1))
                result.reverse()
                return result

            # Return a list because a negative step could
            # reverse the order of the items and this could
            # be the desired behavior.

            indices = range(start, stop, step)
            return list(self._getitem(index) for index in indices)
        else:
            if self._len:
                if index == 0:
                    return _lists[0][0]
                elif index == -1:
                    return _lists[-1][-1]
            else:
                raise IndexError('list index out of range')

            if 0 <= index < len(_lists[0]):
                return _lists[0][index]

            len_last = len(_lists[-1])

            if -len_last < index < 0:
                return _lists[-1][len_last + index]

            pos, idx = self._pos(index)
            return _lists[pos][idx]

    _getitem = __getitem__


    def __setitem__(self, index, value):
        """Raise not-implemented error.

        ``sl.__setitem__(index, value)`` <==> ``sl[index] = value``

        :raises NotImplementedError: use ``del sl[index]`` and
            ``sl.add(value)`` instead

        """
        message = 'use ``del sl[index]`` and ``sl.add(value)`` instead'
        raise NotImplementedError(message)


    def __iter__(self):
        """Return an iterator over the sorted list.

        ``sl.__iter__()`` <==> ``iter(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return chain.from_iterable(self._lists)


    def __reversed__(self):
        """Return a reverse iterator over the sorted list.

        ``sl.__reversed__()`` <==> ``reversed(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return chain.from_iterable(map(reversed, reversed(self._lists)))


    def reverse(self):
        """Raise not-implemented error.

        Sorted list maintains values in ascending sort order. Values may not be
        reversed in-place.

        Use ``reversed(sl)`` for an iterator over values in descending sort
        order.

        Implemented to override `MutableSequence.reverse` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``reversed(sl)`` instead

        """
        raise NotImplementedError('use ``reversed(sl)`` instead')


    def islice(self, start=None, stop=None, reverse=False):
        """Return an iterator that slices sorted list from `start` to `stop`.

        The `start` and `stop` index are treated inclusive and exclusive,
        respectively.

        Both `start` and `stop` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.islice(2, 6)
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param int start: start index (inclusive)
        :param int stop: stop index (exclusive)
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        _len = self._len

        if not _len:
            return iter(())

        start, stop, _ = slice(start, stop).indices(self._len)

        if start >= stop:
            return iter(())

        _pos = self._pos

        min_pos, min_idx = _pos(start)

        if stop == _len:
            max_pos = len(self._lists) - 1
            max_idx = len(self._lists[-1])
        else:
            max_pos, max_idx = _pos(stop)

        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)


    def _islice(self, min_pos, min_idx, max_pos, max_idx, reverse):
        """Return an iterator that slices sorted list using two index pairs.

        The index pairs are (min_pos, min_idx) and (max_pos, max_idx), the
        first inclusive and the latter exclusive. See `_pos` for details on how
        an index is converted to an index pair.

        When `reverse` is `True`, values are yielded from the iterator in
        reverse order.

        """
        _lists = self._lists

        if min_pos > max_pos:
            return iter(())

        if min_pos == max_pos:
            if reverse:
                indices = reversed(range(min_idx, max_idx))
                return map(_lists[min_pos].__getitem__, indices)

            indices = range(min_idx, max_idx)
            return map(_lists[min_pos].__getitem__, indices)

        next_pos = min_pos + 1

        if next_pos == max_pos:
            if reverse:
                min_indices = range(min_idx, len(_lists[min_pos]))
                max_indices = range(max_idx)
                return chain(
                    map(_lists[max_pos].__getitem__, reversed(max_indices)),
                    map(_lists[min_pos].__getitem__, reversed(min_indices)),
                )

            min_indices = range(min_idx, len(_lists[min_pos]))
            max_indices = range(max_idx)
            return chain(
                map(_lists[min_pos].__getitem__, min_indices),
                map(_lists[max_pos].__getitem__, max_indices),
            )

        if reverse:
            min_indices = range(min_idx, len(_lists[min_pos]))
            sublist_indices = range(next_pos, max_pos)
            sublists = map(_lists.__getitem__, reversed(sublist_indices))
            max_indices = range(max_idx)
            return chain(
                map(_lists[max_pos].__getitem__, reversed(max_indices)),
                chain.from_iterable(map(reversed, sublists)),
                map(_lists[min_pos].__getitem__, reversed(min_indices)),
            )

        min_indices = range(min_idx, len(_lists[min_pos]))
        sublist_indices = range(next_pos, max_pos)
        sublists = map(_lists.__getitem__, sublist_indices)
        max_indices = range(max_idx)
        return chain(
            map(_lists[min_pos].__getitem__, min_indices),
            chain.from_iterable(sublists),
            map(_lists[max_pos].__getitem__, max_indices),
        )


    def irange(self, minimum=None, maximum=None, inclusive=(True, True),
               reverse=False):
        """Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.irange('c', 'f')
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        _maxes = self._maxes

        if not _maxes:
            return iter(())

        _lists = self._lists

        # Calculate the minimum (pos, idx) pair. By default this location
        # will be inclusive in our calculation.

        if minimum is None:
            min_pos = 0
            min_idx = 0
        else:
            if inclusive[0]:
                min_pos = bisect_left(_maxes, minimum)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_left(_lists[min_pos], minimum)
            else:
                min_pos = bisect_right(_maxes, minimum)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_right(_lists[min_pos], minimum)

        # Calculate the maximum (pos, idx) pair. By default this location
        # will be exclusive in our calculation.

        if maximum is None:
            max_pos = len(_maxes) - 1
            max_idx = len(_lists[max_pos])
        else:
            if inclusive[1]:
                max_pos = bisect_right(_maxes, maximum)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_lists[max_pos])
                else:
                    max_idx = bisect_right(_lists[max_pos], maximum)
            else:
                max_pos = bisect_left(_maxes, maximum)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_lists[max_pos])
                else:
                    max_idx = bisect_left(_lists[max_pos], maximum)

        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)


    def __len__(self):
        """Return the size of the sorted list.

        ``sl.__len__()`` <==> ``len(sl)``

        :return: size of sorted list

        """
        return self._len


    def bisect_left(self, value):
        """Return an index to insert `value` in the sorted list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_left(12)
        2

        :param value: insertion index of value in sorted list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_left(_maxes, value)

        if pos == len(_maxes):
            return self._len

        idx = bisect_left(self._lists[pos], value)
        return self._loc(pos, idx)


    def bisect_right(self, value):
        """Return an index to insert `value` in the sorted list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_right(12)
        3

        :param value: insertion index of value in sorted list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_right(_maxes, value)

        if pos == len(_maxes):
            return self._len

        idx = bisect_right(self._lists[pos], value)
        return self._loc(pos, idx)

    bisect = bisect_right
    _bisect_right = bisect_right


    def count(self, value):
        """Return number of occurrences of `value` in the sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        >>> sl.count(3)
        3

        :param value: value to count in sorted list
        :return: count

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos_left = bisect_left(_maxes, value)

        if pos_left == len(_maxes):
            return 0

        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], value)
        pos_right = bisect_right(_maxes, value)

        if pos_right == len(_maxes):
            return self._len - self._loc(pos_left, idx_left)

        idx_right = bisect_right(_lists[pos_right], value)

        if pos_left == pos_right:
            return idx_right - idx_left

        right = self._loc(pos_right, idx_right)
        left = self._loc(pos_left, idx_left)
        return right - left


    def copy(self):
        """Return a shallow copy of the sorted list.

        Runtime complexity: `O(n)`

        :return: new sorted list

        """
        return self.__class__(self)

    __copy__ = copy


    def append(self, value):
        """Raise not-implemented error.

        Implemented to override `MutableSequence.append` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        """
        raise NotImplementedError('use ``sl.add(value)`` instead')


    def extend(self, values):
        """Raise not-implemented error.

        Implemented to override `MutableSequence.extend` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.update(values)`` instead

        """
        raise NotImplementedError('use ``sl.update(values)`` instead')


    def insert(self, index, value):
        """Raise not-implemented error.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        """
        raise NotImplementedError('use ``sl.add(value)`` instead')


    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list.

        Raise :exc:`IndexError` if the sorted list is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.pop()
        'e'
        >>> sl.pop(2)
        'c'
        >>> sl
        SortedList(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        """
        if not self._len:
            raise IndexError('pop index out of range')

        _lists = self._lists

        if index == 0:
            val = _lists[0][0]
            self._delete(0, 0)
            return val

        if index == -1:
            pos = len(_lists) - 1
            loc = len(_lists[pos]) - 1
            val = _lists[pos][loc]
            self._delete(pos, loc)
            return val

        if 0 <= index < len(_lists[0]):
            val = _lists[0][index]
            self._delete(0, index)
            return val

        len_last = len(_lists[-1])

        if -len_last < index < 0:
            pos = len(_lists) - 1
            loc = len_last + index
            val = _lists[pos][loc]
            self._delete(pos, loc)
            return val

        pos, idx = self._pos(index)
        val = _lists[pos][idx]
        self._delete(pos, idx)
        return val


    def index(self, value, start=None, stop=None):
        """Return first index of value in sorted list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.index('d')
        3
        >>> sl.index('z')
        Traceback (most recent call last):
          ...
        ValueError: 'z' is not in list

        :param value: value in sorted list
        :param int start: start index (default None, start of sorted list)
        :param int stop: stop index (default None, end of sorted list)
        :return: index of value
        :raises ValueError: if value is not present

        """
        _len = self._len

        if not _len:
            raise ValueError('{0!r} is not in list'.format(value))

        if start is None:
            start = 0
        if start < 0:
            start += _len
        if start < 0:
            start = 0

        if stop is None:
            stop = _len
        if stop < 0:
            stop += _len
        if stop > _len:
            stop = _len

        if stop <= start:
            raise ValueError('{0!r} is not in list'.format(value))

        _maxes = self._maxes
        pos_left = bisect_left(_maxes, value)

        if pos_left == len(_maxes):
            raise ValueError('{0!r} is not in list'.format(value))

        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], value)

        if _lists[pos_left][idx_left] != value:
            raise ValueError('{0!r} is not in list'.format(value))

        stop -= 1
        left = self._loc(pos_left, idx_left)

        if start <= left:
            if left <= stop:
                return left
        else:
            right = self._bisect_right(value) - 1

            if start <= right:
                return start

        raise ValueError('{0!r} is not in list'.format(value))


    def __add__(self, other):
        """Return new sorted list containing all values in both sequences.

        ``sl.__add__(other)`` <==> ``sl + other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(n*log(n))`

        >>> sl1 = SortedList('bat')
        >>> sl2 = SortedList('cat')
        >>> sl1 + sl2
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: new sorted list

        """
        values = reduce(iadd, self._lists, [])
        values.extend(other)
        return self.__class__(values)

    __radd__ = __add__


    def __iadd__(self, other):
        """Update sorted list with values from `other`.

        ``sl.__iadd__(other)`` <==> ``sl += other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList('bat')
        >>> sl += 'cat'
        >>> sl
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: existing sorted list

        """
        self._update(other)
        return self


    def __mul__(self, num):
        """Return new sorted list with `num` shallow copies of values.

        ``sl.__mul__(num)`` <==> ``sl * num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl * 3
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: new sorted list

        """
        values = reduce(iadd, self._lists, []) * num
        return self.__class__(values)

    __rmul__ = __mul__


    def __imul__(self, num):
        """Update the sorted list with `num` shallow copies of values.

        ``sl.__imul__(num)`` <==> ``sl *= num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl *= 3
        >>> sl
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: existing sorted list

        """
        values = reduce(iadd, self._lists, []) * num
        self._clear()
        self._update(values)
        return self


    def __make_cmp(seq_op, symbol, doc):
        "Make comparator method."
        def comparer(self, other):
            "Compare method for sorted list and sequence."
            if not isinstance(other, Sequence):
                return NotImplemented

            self_len = self._len
            len_other = len(other)

            if self_len != len_other:
                if seq_op is eq:
                    return False
                if seq_op is ne:
                    return True

            for alpha, beta in zip(self, other):
                if alpha != beta:
                    return seq_op(alpha, beta)

            return seq_op(self_len, len_other)

        seq_op_name = seq_op.__name__
        comparer.__name__ = '__{0}__'.format(seq_op_name)
        doc_str = """Return true if and only if sorted list is {0} `other`.

        ``sl.__{1}__(other)`` <==> ``sl {2} other``

        Comparisons use lexicographical order as with sequences.

        Runtime complexity: `O(n)`

        :param other: `other` sequence
        :return: true if sorted list is {0} `other`

        """
        comparer.__doc__ = dedent(doc_str.format(doc, seq_op_name, symbol))
        return comparer


    __eq__ = __make_cmp(eq, '==', 'equal to')
    __ne__ = __make_cmp(ne, '!=', 'not equal to')
    __lt__ = __make_cmp(lt, '<', 'less than')
    __gt__ = __make_cmp(gt, '>', 'greater than')
    __le__ = __make_cmp(le, '<=', 'less than or equal to')
    __ge__ = __make_cmp(ge, '>=', 'greater than or equal to')
    __make_cmp = staticmethod(__make_cmp)


    def __reduce__(self):
        values = reduce(iadd, self._lists, [])
        return (type(self), (values,))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted list.

        ``sl.__repr__()`` <==> ``repr(sl)``

        :return: string representation

        """
        return '{0}({1!r})'.format(type(self).__name__, list(self))


    def _check(self):
        """Check invariants of sorted list.

        Runtime complexity: `O(n)`

        """
        try:
            assert self._load >= 4
            assert len(self._maxes) == len(self._lists)
            assert self._len == sum(len(sublist) for sublist in self._lists)

            # Check all sublists are sorted.

            for sublist in self._lists:
                for pos in range(1, len(sublist)):
                    assert sublist[pos - 1] <= sublist[pos]

            # Check beginning/end of sublists are sorted.

            for pos in range(1, len(self._lists)):
                assert self._lists[pos - 1][-1] <= self._lists[pos][0]

            # Check _maxes index is the last value of each sublist.

            for pos in range(len(self._maxes)):
                assert self._maxes[pos] == self._lists[pos][-1]

            # Check sublist lengths are less than double load-factor.

            double = self._load << 1
            assert all(len(sublist) <= double for sublist in self._lists)

            # Check sublist lengths are greater than half load-factor for all
            # but the last sublist.

            half = self._load >> 1
            for pos in range(0, len(self._lists) - 1):
                assert len(self._lists[pos]) >= half

            if self._index:
                assert self._len == self._index[0]
                assert len(self._index) == self._offset + len(self._lists)

                # Check index leaf nodes equal length of sublists.

                for pos in range(len(self._lists)):
                    leaf = self._index[self._offset + pos]
                    assert leaf == len(self._lists[pos])

                # Check index branch nodes are the sum of their children.

                for pos in range(self._offset):
                    child = (pos << 1) + 1
                    if child >= len(self._index):
                        assert self._index[pos] == 0
                    elif child + 1 == len(self._index):
                        assert self._index[pos] == self._index[child]
                    else:
                        child_sum = self._index[child] + self._index[child + 1]
                        assert child_sum == self._index[pos]
        except:
            traceback.print_exc(file=sys.stdout)
            print('len', self._len)
            print('load', self._load)
            print('offset', self._offset)
            print('len_index', len(self._index))
            print('index', self._index)
            print('len_maxes', len(self._maxes))
            print('maxes', self._maxes)
            print('len_lists', len(self._lists))
            print('lists', self._lists)
            raise


def identity(value):
    "Identity function."
    return value


class SortedKeyList(SortedList):
    """Sorted-key list is a subtype of sorted list.

    The sorted-key list maintains values in comparison order based on the
    result of a key function applied to every value.

    All the same methods that are available in :class:`SortedList` are also
    available in :class:`SortedKeyList`.

    Additional methods provided:

    * :attr:`SortedKeyList.key`
    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Some examples below use:

    >>> from operator import neg
    >>> neg
    <built-in function neg>
    >>> neg(1)
    -1

    """
    def __init__(self, iterable=None, key=identity):
        """Initialize sorted-key list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted-key list.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default is the identity function.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl
        SortedKeyList([], key=<built-in function neg>)
        >>> skl = SortedKeyList([3, 1, 2], key=neg)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        """
        self._key = key
        self._len = 0
        self._load = self.DEFAULT_LOAD_FACTOR
        self._lists = []
        self._keys = []
        self._maxes = []
        self._index = []
        self._offset = 0

        if iterable is not None:
            self._update(iterable)


    def __new__(cls, iterable=None, key=identity):
        return object.__new__(cls)


    @property
    def key(self):
        "Function used to extract comparison key from values."
        return self._key


    def clear(self):
        """Remove all values from sorted-key list.

        Runtime complexity: `O(n)`

        """
        self._len = 0
        del self._lists[:]
        del self._keys[:]
        del self._maxes[:]
        del self._index[:]

    _clear = clear


    def add(self, value):
        """Add `value` to sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.add(3)
        >>> skl.add(1)
        >>> skl.add(2)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param value: value to add to sorted-key list

        """
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes

        key = self._key(value)

        if _maxes:
            pos = bisect_right(_maxes, key)

            if pos == len(_maxes):
                pos -= 1
                _lists[pos].append(value)
                _keys[pos].append(key)
                _maxes[pos] = key
            else:
                idx = bisect_right(_keys[pos], key)
                _lists[pos].insert(idx, value)
                _keys[pos].insert(idx, key)

            self._expand(pos)
        else:
            _lists.append([value])
            _keys.append([key])
            _maxes.append(key)

        self._len += 1


    def _expand(self, pos):
        """Split sublists with length greater than double the load-factor.

        Updates the index when the sublist length is less than double the load
        level. This requires incrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        """
        _lists = self._lists
        _keys = self._keys
        _index = self._index

        if len(_keys[pos]) > (self._load << 1):
            _maxes = self._maxes
            _load = self._load

            _lists_pos = _lists[pos]
            _keys_pos = _keys[pos]
            half = _lists_pos[_load:]
            half_keys = _keys_pos[_load:]
            del _lists_pos[_load:]
            del _keys_pos[_load:]
            _maxes[pos] = _keys_pos[-1]

            _lists.insert(pos + 1, half)
            _keys.insert(pos + 1, half_keys)
            _maxes.insert(pos + 1, half_keys[-1])

            del _index[:]
        else:
            if _index:
                child = self._offset + pos
                while child:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1


    def update(self, iterable):
        """Update sorted-key list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.update([3, 1, 2])
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: iterable of values to add

        """
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes
        values = sorted(iterable, key=self._key)

        if _maxes:
            if len(values) * 4 >= self._len:
                _lists.append(values)
                values = reduce(iadd, _lists, [])
                values.sort(key=self._key)
                self._clear()
            else:
                _add = self.add
                for val in values:
                    _add(val)
                return

        _load = self._load
        _lists.extend(values[pos:(pos + _load)]
                      for pos in range(0, len(values), _load))
        _keys.extend(list(map(self._key, _list)) for _list in _lists)
        _maxes.extend(sublist[-1] for sublist in _keys)
        self._len = len(values)
        del self._index[:]

    _update = update


    def __contains__(self, value):
        """Return true if `value` is an element of the sorted-key list.

        ``skl.__contains__(value)`` <==> ``value in skl``

        Runtime complexity: `O(log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> 3 in skl
        True

        :param value: search for value in sorted-key list
        :return: true if `value` in sorted-key list

        """
        _maxes = self._maxes

        if not _maxes:
            return False

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return False

        _lists = self._lists
        _keys = self._keys

        idx = bisect_left(_keys[pos], key)

        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                return False
            if _lists[pos][idx] == value:
                return True
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return False
                len_sublist = len(_keys[pos])
                idx = 0


    def discard(self, value):
        """Remove `value` from sorted-key list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.discard(1)
        >>> skl.discard(0)
        >>> skl == [5, 4, 3, 2]
        True

        :param value: `value` to discard from sorted-key list

        """
        _maxes = self._maxes

        if not _maxes:
            return

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return

        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                return
            if _lists[pos][idx] == value:
                self._delete(pos, idx)
                return
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return
                len_sublist = len(_keys[pos])
                idx = 0


    def remove(self, value):
        """Remove `value` from sorted-key list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> skl.remove(5)
        >>> skl == [4, 3, 2, 1]
        True
        >>> skl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted-key list
        :raises ValueError: if `value` is not in sorted-key list

        """
        _maxes = self._maxes

        if not _maxes:
            raise ValueError('{0!r} not in list'.format(value))

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            raise ValueError('{0!r} not in list'.format(value))

        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                raise ValueError('{0!r} not in list'.format(value))
            if _lists[pos][idx] == value:
                self._delete(pos, idx)
                return
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    raise ValueError('{0!r} not in list'.format(value))
                len_sublist = len(_keys[pos])
                idx = 0


    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`.

        Combines lists that are less than half the load level.

        Updates the index when the sublist length is more than half the load
        level. This requires decrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        :param int pos: lists index
        :param int idx: sublist index

        """
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes
        _index = self._index
        keys_pos = _keys[pos]
        lists_pos = _lists[pos]

        del keys_pos[idx]
        del lists_pos[idx]
        self._len -= 1

        len_keys_pos = len(keys_pos)

        if len_keys_pos > (self._load >> 1):
            _maxes[pos] = keys_pos[-1]

            if _index:
                child = self._offset + pos
                while child > 0:
                    _index[child] -= 1
                    child = (child - 1) >> 1
                _index[0] -= 1
        elif len(_keys) > 1:
            if not pos:
                pos += 1

            prev = pos - 1
            _keys[prev].extend(_keys[pos])
            _lists[prev].extend(_lists[pos])
            _maxes[prev] = _keys[prev][-1]

            del _lists[pos]
            del _keys[pos]
            del _maxes[pos]
            del _index[:]

            self._expand(prev)
        elif len_keys_pos:
            _maxes[pos] = keys_pos[-1]
        else:
            del _lists[pos]
            del _keys[pos]
            del _maxes[pos]
            del _index[:]


    def irange(self, minimum=None, maximum=None, inclusive=(True, True),
               reverse=False):
        """Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange(14.5, 11.5)
        >>> list(it)
        [14, 13, 12]

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        min_key = self._key(minimum) if minimum is not None else None
        max_key = self._key(maximum) if maximum is not None else None
        return self._irange_key(
            min_key=min_key, max_key=max_key,
            inclusive=inclusive, reverse=reverse,
        )


    def irange_key(self, min_key=None, max_key=None, inclusive=(True, True),
                   reverse=False):
        """Create an iterator of values between `min_key` and `max_key`.

        Both `min_key` and `max_key` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange_key(-14, -12)
        >>> list(it)
        [14, 13, 12]

        :param min_key: minimum key to start iterating
        :param max_key: maximum key to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
        _maxes = self._maxes

        if not _maxes:
            return iter(())

        _keys = self._keys

        # Calculate the minimum (pos, idx) pair. By default this location
        # will be inclusive in our calculation.

        if min_key is None:
            min_pos = 0
            min_idx = 0
        else:
            if inclusive[0]:
                min_pos = bisect_left(_maxes, min_key)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_left(_keys[min_pos], min_key)
            else:
                min_pos = bisect_right(_maxes, min_key)

                if min_pos == len(_maxes):
                    return iter(())

                min_idx = bisect_right(_keys[min_pos], min_key)

        # Calculate the maximum (pos, idx) pair. By default this location
        # will be exclusive in our calculation.

        if max_key is None:
            max_pos = len(_maxes) - 1
            max_idx = len(_keys[max_pos])
        else:
            if inclusive[1]:
                max_pos = bisect_right(_maxes, max_key)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_keys[max_pos])
                else:
                    max_idx = bisect_right(_keys[max_pos], max_key)
            else:
                max_pos = bisect_left(_maxes, max_key)

                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_keys[max_pos])
                else:
                    max_idx = bisect_left(_keys[max_pos], max_key)

        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)

    _irange_key = irange_key


    def bisect_left(self, value):
        """Return an index to insert `value` in the sorted-key list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_left(1)
        4

        :param value: insertion index of value in sorted-key list
        :return: index

        """
        return self._bisect_key_left(self._key(value))


    def bisect_right(self, value):
        """Return an index to insert `value` in the sorted-key list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_right(1)
        5

        :param value: insertion index of value in sorted-key list
        :return: index

        """
        return self._bisect_key_right(self._key(value))

    bisect = bisect_right


    def bisect_key_left(self, key):
        """Return an index to insert `key` in the sorted-key list.

        If the `key` is already present, the insertion point will be before (to
        the left of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_left(-1)
        4

        :param key: insertion index of key in sorted-key list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return self._len

        idx = bisect_left(self._keys[pos], key)

        return self._loc(pos, idx)

    _bisect_key_left = bisect_key_left


    def bisect_key_right(self, key):
        """Return an index to insert `key` in the sorted-key list.

        Similar to `bisect_key_left`, but if `key` is already present, the
        insertion point will be after (to the right of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_right(-1)
        5

        :param key: insertion index of key in sorted-key list
        :return: index

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        pos = bisect_right(_maxes, key)

        if pos == len(_maxes):
            return self._len

        idx = bisect_right(self._keys[pos], key)

        return self._loc(pos, idx)

    bisect_key = bisect_key_right
    _bisect_key_right = bisect_key_right


    def count(self, value):
        """Return number of occurrences of `value` in the sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([4, 4, 4, 4, 3, 3, 3, 2, 2, 1], key=neg)
        >>> skl.count(2)
        2

        :param value: value to count in sorted-key list
        :return: count

        """
        _maxes = self._maxes

        if not _maxes:
            return 0

        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            return 0

        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        total = 0
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                return total
            if _lists[pos][idx] == value:
                total += 1
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return total
                len_sublist = len(_keys[pos])
                idx = 0


    def copy(self):
        """Return a shallow copy of the sorted-key list.

        Runtime complexity: `O(n)`

        :return: new sorted-key list

        """
        return self.__class__(self, key=self._key)

    __copy__ = copy


    def index(self, value, start=None, stop=None):
        """Return first index of value in sorted-key list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted-key list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.index(2)
        3
        >>> skl.index(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 is not in list

        :param value: value in sorted-key list
        :param int start: start index (default None, start of sorted-key list)
        :param int stop: stop index (default None, end of sorted-key list)
        :return: index of value
        :raises ValueError: if value is not present

        """
        _len = self._len

        if not _len:
            raise ValueError('{0!r} is not in list'.format(value))

        if start is None:
            start = 0
        if start < 0:
            start += _len
        if start < 0:
            start = 0

        if stop is None:
            stop = _len
        if stop < 0:
            stop += _len
        if stop > _len:
            stop = _len

        if stop <= start:
            raise ValueError('{0!r} is not in list'.format(value))

        _maxes = self._maxes
        key = self._key(value)
        pos = bisect_left(_maxes, key)

        if pos == len(_maxes):
            raise ValueError('{0!r} is not in list'.format(value))

        stop -= 1
        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])

        while True:
            if _keys[pos][idx] != key:
                raise ValueError('{0!r} is not in list'.format(value))
            if _lists[pos][idx] == value:
                loc = self._loc(pos, idx)
                if start <= loc <= stop:
                    return loc
                elif loc > stop:
                    break
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    raise ValueError('{0!r} is not in list'.format(value))
                len_sublist = len(_keys[pos])
                idx = 0

        raise ValueError('{0!r} is not in list'.format(value))


    def __add__(self, other):
        """Return new sorted-key list containing all values in both sequences.

        ``skl.__add__(other)`` <==> ``skl + other``

        Values in `other` do not need to be in sorted-key order.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl1 = SortedKeyList([5, 4, 3], key=neg)
        >>> skl2 = SortedKeyList([2, 1, 0], key=neg)
        >>> skl1 + skl2
        SortedKeyList([5, 4, 3, 2, 1, 0], key=<built-in function neg>)

        :param other: other iterable
        :return: new sorted-key list

        """
        values = reduce(iadd, self._lists, [])
        values.extend(other)
        return self.__class__(values, key=self._key)

    __radd__ = __add__


    def __mul__(self, num):
        """Return new sorted-key list with `num` shallow copies of values.

        ``skl.__mul__(num)`` <==> ``skl * num``

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([3, 2, 1], key=neg)
        >>> skl * 2
        SortedKeyList([3, 3, 2, 2, 1, 1], key=<built-in function neg>)

        :param int num: count of shallow copies
        :return: new sorted-key list

        """
        values = reduce(iadd, self._lists, []) * num
        return self.__class__(values, key=self._key)


    def __reduce__(self):
        values = reduce(iadd, self._lists, [])
        return (type(self), (values, self.key))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted-key list.

        ``skl.__repr__()`` <==> ``repr(skl)``

        :return: string representation

        """
        type_name = type(self).__name__
        return '{0}({1!r}, key={2!r})'.format(type_name, list(self), self._key)


    def _check(self):
        """Check invariants of sorted-key list.

        Runtime complexity: `O(n)`

        """
        try:
            assert self._load >= 4
            assert len(self._maxes) == len(self._lists) == len(self._keys)
            assert self._len == sum(len(sublist) for sublist in self._lists)

            # Check all sublists are sorted.

            for sublist in self._keys:
                for pos in range(1, len(sublist)):
                    assert sublist[pos - 1] <= sublist[pos]

            # Check beginning/end of sublists are sorted.

            for pos in range(1, len(self._keys)):
                assert self._keys[pos - 1][-1] <= self._keys[pos][0]

            # Check _keys matches _key mapped to _lists.

            for val_sublist, key_sublist in zip(self._lists, self._keys):
                assert len(val_sublist) == len(key_sublist)
                for val, key in zip(val_sublist, key_sublist):
                    assert self._key(val) == key

            # Check _maxes index is the last value of each sublist.

            for pos in range(len(self._maxes)):
                assert self._maxes[pos] == self._keys[pos][-1]

            # Check sublist lengths are less than double load-factor.

            double = self._load << 1
            assert all(len(sublist) <= double for sublist in self._lists)

            # Check sublist lengths are greater than half load-factor for all
            # but the last sublist.

            half = self._load >> 1
            for pos in range(0, len(self._lists) - 1):
                assert len(self._lists[pos]) >= half

            if self._index:
                assert self._len == self._index[0]
                assert len(self._index) == self._offset + len(self._lists)

                # Check index leaf nodes equal length of sublists.

                for pos in range(len(self._lists)):
                    leaf = self._index[self._offset + pos]
                    assert leaf == len(self._lists[pos])

                # Check index branch nodes are the sum of their children.

                for pos in range(self._offset):
                    child = (pos << 1) + 1
                    if child >= len(self._index):
                        assert self._index[pos] == 0
                    elif child + 1 == len(self._index):
                        assert self._index[pos] == self._index[child]
                    else:
                        child_sum = self._index[child] + self._index[child + 1]
                        assert child_sum == self._index[pos]
        except:
            traceback.print_exc(file=sys.stdout)
            print('len', self._len)
            print('load', self._load)
            print('offset', self._offset)
            print('len_index', len(self._index))
            print('index', self._index)
            print('len_maxes', len(self._maxes))
            print('maxes', self._maxes)
            print('len_keys', len(self._keys))
            print('keys', self._keys)
            print('len_lists', len(self._lists))
            print('lists', self._lists)
            raise


SortedListWithKey = SortedKeyList


"""Sorted Set
=============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted set implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedSet`

"""

from itertools import chain
from operator import eq, ne, gt, ge, lt, le
from textwrap import dedent

###############################################################################
# BEGIN Python 2/3 Shims
###############################################################################

try:
    from collections.abc import MutableSet, Sequence, Set
except ImportError:
    from collections import MutableSet, Sequence, Set

###############################################################################
# END Python 2/3 Shims
###############################################################################


class SortedSet(MutableSet, Sequence):
    """Sorted set is a sorted mutable set.

    Sorted set values are maintained in sorted order. The design of sorted set
    is simple: sorted set uses a set for set-operations and maintains a sorted
    list of values.

    Sorted set values must be hashable and comparable. The hash and total
    ordering of values must not change while they are stored in the sorted set.

    Mutable set methods:

    * :func:`SortedSet.__contains__`
    * :func:`SortedSet.__iter__`
    * :func:`SortedSet.__len__`
    * :func:`SortedSet.add`
    * :func:`SortedSet.discard`

    Sequence methods:

    * :func:`SortedSet.__getitem__`
    * :func:`SortedSet.__delitem__`
    * :func:`SortedSet.__reversed__`

    Methods for removing values:

    * :func:`SortedSet.clear`
    * :func:`SortedSet.pop`
    * :func:`SortedSet.remove`

    Set-operation methods:

    * :func:`SortedSet.difference`
    * :func:`SortedSet.difference_update`
    * :func:`SortedSet.intersection`
    * :func:`SortedSet.intersection_update`
    * :func:`SortedSet.symmetric_difference`
    * :func:`SortedSet.symmetric_difference_update`
    * :func:`SortedSet.union`
    * :func:`SortedSet.update`

    Methods for miscellany:

    * :func:`SortedSet.copy`
    * :func:`SortedSet.count`
    * :func:`SortedSet.__repr__`
    * :func:`SortedSet._check`

    Sorted list methods available:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.index`
    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList._reset`

    Additional sorted list methods available, if key-function used:

    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Sorted set comparisons use subset and superset relations. Two sorted sets
    are equal if and only if every element of each sorted set is contained in
    the other (each is a subset of the other). A sorted set is less than
    another sorted set if and only if the first sorted set is a proper subset
    of the second sorted set (is a subset, but is not equal). A sorted set is
    greater than another sorted set if and only if the first sorted set is a
    proper superset of the second sorted set (is a superset, but is not equal).

    """
    def __init__(self, iterable=None, key=None):
        """Initialize sorted set instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted set.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default, none, compares values directly.

        Runtime complexity: `O(n*log(n))`

        >>> ss = SortedSet([3, 1, 2, 5, 4])
        >>> ss
        SortedSet([1, 2, 3, 4, 5])
        >>> from operator import neg
        >>> ss = SortedSet([3, 1, 2, 5, 4], neg)
        >>> ss
        SortedSet([5, 4, 3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        """
        self._key = key

        # SortedSet._fromset calls SortedSet.__init__ after initializing the
        # _set attribute. So only create a new set if the _set attribute is not
        # already present.

        if not hasattr(self, '_set'):
            self._set = set()

        self._list = SortedList(self._set, key=key)

        # Expose some set methods publicly.

        _set = self._set
        self.isdisjoint = _set.isdisjoint
        self.issubset = _set.issubset
        self.issuperset = _set.issuperset

        # Expose some sorted list methods publicly.

        _list = self._list
        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset

        if key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key

        if iterable is not None:
            self._update(iterable)


    @classmethod
    def _fromset(cls, values, key=None):
        """Initialize sorted set from existing set.

        Used internally by set operations that return a new set.

        """
        sorted_set = object.__new__(cls)
        sorted_set._set = values
        sorted_set.__init__(key=key)
        return sorted_set


    @property
    def key(self):
        """Function used to extract comparison key from values.

        Sorted set compares values directly when the key function is none.

        """
        return self._key


    def __contains__(self, value):
        """Return true if `value` is an element of the sorted set.

        ``ss.__contains__(value)`` <==> ``value in ss``

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> 3 in ss
        True

        :param value: search for value in sorted set
        :return: true if `value` in sorted set

        """
        return value in self._set


    def __getitem__(self, index):
        """Lookup value at `index` in sorted set.

        ``ss.__getitem__(index)`` <==> ``ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss[2]
        'c'
        >>> ss[-1]
        'e'
        >>> ss[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
        return self._list[index]


    def __delitem__(self, index):
        """Remove value at `index` from sorted set.

        ``ss.__delitem__(index)`` <==> ``del ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> del ss[2]
        >>> ss
        SortedSet(['a', 'b', 'd', 'e'])
        >>> del ss[:2]
        >>> ss
        SortedSet(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        """
        _set = self._set
        _list = self._list
        if isinstance(index, slice):
            values = _list[index]
            _set.difference_update(values)
        else:
            value = _list[index]
            _set.remove(value)
        del _list[index]


    def __make_cmp(set_op, symbol, doc):
        "Make comparator method."
        def comparer(self, other):
            "Compare method for sorted set and set."
            if isinstance(other, SortedSet):
                return set_op(self._set, other._set)
            elif isinstance(other, Set):
                return set_op(self._set, other)
            return NotImplemented

        set_op_name = set_op.__name__
        comparer.__name__ = '__{0}__'.format(set_op_name)
        doc_str = """Return true if and only if sorted set is {0} `other`.

        ``ss.__{1}__(other)`` <==> ``ss {2} other``

        Comparisons use subset and superset semantics as with sets.

        Runtime complexity: `O(n)`

        :param other: `other` set
        :return: true if sorted set is {0} `other`

        """
        comparer.__doc__ = dedent(doc_str.format(doc, set_op_name, symbol))
        return comparer


    __eq__ = __make_cmp(eq, '==', 'equal to')
    __ne__ = __make_cmp(ne, '!=', 'not equal to')
    __lt__ = __make_cmp(lt, '<', 'a proper subset of')
    __gt__ = __make_cmp(gt, '>', 'a proper superset of')
    __le__ = __make_cmp(le, '<=', 'a subset of')
    __ge__ = __make_cmp(ge, '>=', 'a superset of')
    __make_cmp = staticmethod(__make_cmp)


    def __len__(self):
        """Return the size of the sorted set.

        ``ss.__len__()`` <==> ``len(ss)``

        :return: size of sorted set

        """
        return len(self._set)


    def __iter__(self):
        """Return an iterator over the sorted set.

        ``ss.__iter__()`` <==> ``iter(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return iter(self._list)


    def __reversed__(self):
        """Return a reverse iterator over the sorted set.

        ``ss.__reversed__()`` <==> ``reversed(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        """
        return reversed(self._list)


    def add(self, value):
        """Add `value` to sorted set.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet()
        >>> ss.add(3)
        >>> ss.add(1)
        >>> ss.add(2)
        >>> ss
        SortedSet([1, 2, 3])

        :param value: value to add to sorted set

        """
        _set = self._set
        if value not in _set:
            _set.add(value)
            self._list.add(value)

    _add = add


    def clear(self):
        """Remove all values from sorted set.

        Runtime complexity: `O(n)`

        """
        self._set.clear()
        self._list.clear()


    def copy(self):
        """Return a shallow copy of the sorted set.

        Runtime complexity: `O(n)`

        :return: new sorted set

        """
        return self._fromset(set(self._set), key=self._key)

    __copy__ = copy


    def count(self, value):
        """Return number of occurrences of `value` in the sorted set.

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.count(3)
        1

        :param value: value to count in sorted set
        :return: count

        """
        return 1 if value in self._set else 0


    def discard(self, value):
        """Remove `value` from sorted set if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.discard(5)
        >>> ss.discard(0)
        >>> ss == set([1, 2, 3, 4])
        True

        :param value: `value` to discard from sorted set

        """
        _set = self._set
        if value in _set:
            _set.remove(value)
            self._list.remove(value)

    _discard = discard


    def pop(self, index=-1):
        """Remove and return value at `index` in sorted set.

        Raise :exc:`IndexError` if the sorted set is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss.pop()
        'e'
        >>> ss.pop(2)
        'c'
        >>> ss
        SortedSet(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        """
        # pylint: disable=arguments-differ
        value = self._list.pop(index)
        self._set.remove(value)
        return value


    def remove(self, value):
        """Remove `value` from sorted set; `value` must be a member.

        If `value` is not a member, raise :exc:`KeyError`.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.remove(5)
        >>> ss == set([1, 2, 3, 4])
        True
        >>> ss.remove(0)
        Traceback (most recent call last):
          ...
        KeyError: 0

        :param value: `value` to remove from sorted set
        :raises KeyError: if `value` is not in sorted set

        """
        self._set.remove(value)
        self._list.remove(value)


    def difference(self, *iterables):
        """Return the difference of two or more sets as a new sorted set.

        The `difference` method also corresponds to operator ``-``.

        ``ss.__sub__(iterable)`` <==> ``ss - iterable``

        The difference is all values that are in this sorted set but not the
        other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.difference([4, 5, 6, 7])
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: new sorted set

        """
        diff = self._set.difference(*iterables)
        return self._fromset(diff, key=self._key)

    __sub__ = difference


    def difference_update(self, *iterables):
        """Remove all values of `iterables` from this sorted set.

        The `difference_update` method also corresponds to operator ``-=``.

        ``ss.__isub__(iterable)`` <==> ``ss -= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: itself

        """
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _set.difference_update(values)
            _list.clear()
            _list.update(_set)
        else:
            _discard = self._discard
            for value in values:
                _discard(value)
        return self

    __isub__ = difference_update


    def intersection(self, *iterables):
        """Return the intersection of two or more sets as a new sorted set.

        The `intersection` method also corresponds to operator ``&``.

        ``ss.__and__(iterable)`` <==> ``ss & iterable``

        The intersection is all values that are in this sorted set and each of
        the other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.intersection([4, 5, 6, 7])
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: new sorted set

        """
        intersect = self._set.intersection(*iterables)
        return self._fromset(intersect, key=self._key)

    __and__ = intersection
    __rand__ = __and__


    def intersection_update(self, *iterables):
        """Update the sorted set with the intersection of `iterables`.

        The `intersection_update` method also corresponds to operator ``&=``.

        ``ss.__iand__(iterable)`` <==> ``ss &= iterable``

        Keep only values found in itself and all `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.intersection_update([4, 5, 6, 7])
        >>> ss
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: itself

        """
        _set = self._set
        _list = self._list
        _set.intersection_update(*iterables)
        _list.clear()
        _list.update(_set)
        return self

    __iand__ = intersection_update


    def symmetric_difference(self, other):
        """Return the symmetric difference with `other` as a new sorted set.

        The `symmetric_difference` method also corresponds to operator ``^``.

        ``ss.__xor__(other)`` <==> ``ss ^ other``

        The symmetric difference is all values tha are in exactly one of the
        sets.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.symmetric_difference([4, 5, 6, 7])
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: new sorted set

        """
        diff = self._set.symmetric_difference(other)
        return self._fromset(diff, key=self._key)

    __xor__ = symmetric_difference
    __rxor__ = __xor__


    def symmetric_difference_update(self, other):
        """Update the sorted set with the symmetric difference with `other`.

        The `symmetric_difference_update` method also corresponds to operator
        ``^=``.

        ``ss.__ixor__(other)`` <==> ``ss ^= other``

        Keep only values found in exactly one of itself and `other`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.symmetric_difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: itself

        """
        _set = self._set
        _list = self._list
        _set.symmetric_difference_update(other)
        _list.clear()
        _list.update(_set)
        return self

    __ixor__ = symmetric_difference_update


    def union(self, *iterables):
        """Return new sorted set with values from itself and all `iterables`.

        The `union` method also corresponds to operator ``|``.

        ``ss.__or__(iterable)`` <==> ``ss | iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.union([4, 5, 6, 7])
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: new sorted set

        """
        return self.__class__(chain(iter(self), *iterables), key=self._key)

    __or__ = union
    __ror__ = __or__


    def update(self, *iterables):
        """Update the sorted set adding values from all `iterables`.

        The `update` method also corresponds to operator ``|=``.

        ``ss.__ior__(iterable)`` <==> ``ss |= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: itself

        """
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _list = self._list
            _set.update(values)
            _list.clear()
            _list.update(_set)
        else:
            _add = self._add
            for value in values:
                _add(value)
        return self

    __ior__ = update
    _update = update


    def __reduce__(self):
        """Support for pickle.

        The tricks played with exposing methods in :func:`SortedSet.__init__`
        confuse pickle so customize the reducer.

        """
        return (type(self), (self._set, self._key))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted set.

        ``ss.__repr__()`` <==> ``repr(ss)``

        :return: string representation

        """
        _key = self._key
        key = '' if _key is None else ', key={0!r}'.format(_key)
        type_name = type(self).__name__
        return '{0}({1!r}{2})'.format(type_name, list(self), key)


    def _check(self):
        """Check invariants of sorted set.

        Runtime complexity: `O(n)`

        """
        _set = self._set
        _list = self._list
        _list._check()
        assert len(_set) == len(_list)
        assert all(value in _set for value in _list)



"""Sorted Dict
==============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted dict implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedDict`
* :class:`SortedKeysView`
* :class:`SortedItemsView`
* :class:`SortedValuesView`

"""

import sys
import warnings

from itertools import chain

###############################################################################
# BEGIN Python 2/3 Shims
###############################################################################

try:
    from collections.abc import (
        ItemsView, KeysView, Mapping, ValuesView, Sequence
    )
except ImportError:
    from collections import ItemsView, KeysView, Mapping, ValuesView, Sequence

###############################################################################
# END Python 2/3 Shims
###############################################################################


class SortedDict(dict):
    """Sorted dict is a sorted mutable mapping.

    Sorted dict keys are maintained in sorted order. The design of sorted dict
    is simple: sorted dict inherits from dict to store items and maintains a
    sorted list of keys.

    Sorted dict keys must be hashable and comparable. The hash and total
    ordering of keys must not change while they are stored in the sorted dict.

    Mutable mapping methods:

    * :func:`SortedDict.__getitem__` (inherited from dict)
    * :func:`SortedDict.__setitem__`
    * :func:`SortedDict.__delitem__`
    * :func:`SortedDict.__iter__`
    * :func:`SortedDict.__len__` (inherited from dict)

    Methods for adding items:

    * :func:`SortedDict.setdefault`
    * :func:`SortedDict.update`

    Methods for removing items:

    * :func:`SortedDict.clear`
    * :func:`SortedDict.pop`
    * :func:`SortedDict.popitem`

    Methods for looking up items:

    * :func:`SortedDict.__contains__` (inherited from dict)
    * :func:`SortedDict.get` (inherited from dict)
    * :func:`SortedDict.peekitem`

    Methods for views:

    * :func:`SortedDict.keys`
    * :func:`SortedDict.items`
    * :func:`SortedDict.values`

    Methods for miscellany:

    * :func:`SortedDict.copy`
    * :func:`SortedDict.fromkeys`
    * :func:`SortedDict.__reversed__`
    * :func:`SortedDict.__eq__` (inherited from dict)
    * :func:`SortedDict.__ne__` (inherited from dict)
    * :func:`SortedDict.__repr__`
    * :func:`SortedDict._check`

    Sorted list methods available (applies to keys):

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.count`
    * :func:`SortedList.index`
    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList._reset`

    Additional sorted list methods available, if key-function used:

    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Sorted dicts may only be compared for equality and inequality.

    """
    def __init__(self, *args, **kwargs):
        """Initialize sorted dict instance.

        Optional key-function argument defines a callable that, like the `key`
        argument to the built-in `sorted` function, extracts a comparison key
        from each dictionary key. If no function is specified, the default
        compares the dictionary keys directly. The key-function argument must
        be provided as a positional argument and must come before all other
        arguments.

        Optional iterable argument provides an initial sequence of pairs to
        initialize the sorted dict. Each pair in the sequence defines the key
        and corresponding value. If a key is seen more than once, the last
        value associated with it is stored in the new sorted dict.

        Optional mapping argument provides an initial mapping of items to
        initialize the sorted dict.

        If keyword arguments are given, the keywords themselves, with their
        associated values, are added as items to the dictionary. If a key is
        specified both in the positional argument and as a keyword argument,
        the value associated with the keyword is stored in the
        sorted dict.

        Sorted dict keys must be hashable, per the requirement for Python's
        dictionaries. Keys (or the result of the key-function) must also be
        comparable, per the requirement for sorted lists.

        >>> d = {'alpha': 1, 'beta': 2}
        >>> SortedDict([('alpha', 1), ('beta', 2)]) == d
        True
        >>> SortedDict({'alpha': 1, 'beta': 2}) == d
        True
        >>> SortedDict(alpha=1, beta=2) == d
        True

        """
        if args and (args[0] is None or callable(args[0])):
            _key = self._key = args[0]
            args = args[1:]
        else:
            _key = self._key = None

        self._list = SortedList(key=_key)

        # Reaching through ``self._list`` repeatedly adds unnecessary overhead
        # so cache references to sorted list methods.

        _list = self._list
        self._list_add = _list.add
        self._list_clear = _list.clear
        self._list_iter = _list.__iter__
        self._list_reversed = _list.__reversed__
        self._list_pop = _list.pop
        self._list_remove = _list.remove
        self._list_update = _list.update

        # Expose some sorted list methods publicly.

        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect_right
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset

        if _key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key

        self._update(*args, **kwargs)


    @property
    def key(self):
        """Function used to extract comparison key from keys.

        Sorted dict compares keys directly when the key function is none.

        """
        return self._key


    @property
    def iloc(self):
        """Cached reference of sorted keys view.

        Deprecated in version 2 of Sorted Containers. Use
        :func:`SortedDict.keys` instead.

        """
        # pylint: disable=attribute-defined-outside-init
        try:
            return self._iloc
        except AttributeError:
            warnings.warn(
                'sorted_dict.iloc is deprecated.'
                ' Use SortedDict.keys() instead.',
                DeprecationWarning,
                stacklevel=2,
            )
            _iloc = self._iloc = SortedKeysView(self)
            return _iloc


    def clear(self):

        """Remove all items from sorted dict.

        Runtime complexity: `O(n)`

        """
        dict.clear(self)
        self._list_clear()


    def __delitem__(self, key):
        """Remove item from sorted dict identified by `key`.

        ``sd.__delitem__(key)`` <==> ``del sd[key]``

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> del sd['b']
        >>> sd
        SortedDict({'a': 1, 'c': 3})
        >>> del sd['z']
        Traceback (most recent call last):
          ...
        KeyError: 'z'

        :param key: `key` for item lookup
        :raises KeyError: if key not found

        """
        dict.__delitem__(self, key)
        self._list_remove(key)


    def __iter__(self):
        """Return an iterator over the keys of the sorted dict.

        ``sd.__iter__()`` <==> ``iter(sd)``

        Iterating the sorted dict while adding or deleting items may raise a
        :exc:`RuntimeError` or fail to iterate over all keys.

        """
        return self._list_iter()


    def __reversed__(self):
        """Return a reverse iterator over the keys of the sorted dict.

        ``sd.__reversed__()`` <==> ``reversed(sd)``

        Iterating the sorted dict while adding or deleting items may raise a
        :exc:`RuntimeError` or fail to iterate over all keys.

        """
        return self._list_reversed()


    def __setitem__(self, key, value):
        """Store item in sorted dict with `key` and corresponding `value`.

        ``sd.__setitem__(key, value)`` <==> ``sd[key] = value``

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict()
        >>> sd['c'] = 3
        >>> sd['a'] = 1
        >>> sd['b'] = 2
        >>> sd
        SortedDict({'a': 1, 'b': 2, 'c': 3})

        :param key: key for item
        :param value: value for item

        """
        if key not in self:
            self._list_add(key)
        dict.__setitem__(self, key, value)

    _setitem = __setitem__


    def __or__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(self.items(), other.items())
        return self.__class__(self._key, items)


    def __ror__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(other.items(), self.items())
        return self.__class__(self._key, items)


    def __ior__(self, other):
        self._update(other)
        return self


    def copy(self):
        """Return a shallow copy of the sorted dict.

        Runtime complexity: `O(n)`

        :return: new sorted dict

        """
        return self.__class__(self._key, self.items())

    __copy__ = copy


    @classmethod
    def fromkeys(cls, iterable, value=None):
        """Return a new sorted dict initailized from `iterable` and `value`.

        Items in the sorted dict have keys from `iterable` and values equal to
        `value`.

        Runtime complexity: `O(n*log(n))`

        :return: new sorted dict

        """
        return cls((key, value) for key in iterable)


    def keys(self):
        """Return new sorted keys view of the sorted dict's keys.

        See :class:`SortedKeysView` for details.

        :return: new sorted keys view

        """
        return SortedKeysView(self)


    def items(self):
        """Return new sorted items view of the sorted dict's items.

        See :class:`SortedItemsView` for details.

        :return: new sorted items view

        """
        return SortedItemsView(self)


    def values(self):
        """Return new sorted values view of the sorted dict's values.

        See :class:`SortedValuesView` for details.

        :return: new sorted values view

        """
        return SortedValuesView(self)


    if sys.hexversion < 0x03000000:
        def __make_raise_attributeerror(original, alternate):
            # pylint: disable=no-self-argument
            message = (
                'SortedDict.{original}() is not implemented.'
                ' Use SortedDict.{alternate}() instead.'
            ).format(original=original, alternate=alternate)
            def method(self):
                # pylint: disable=missing-docstring,unused-argument
                raise AttributeError(message)
            method.__name__ = original  # pylint: disable=non-str-assignment-to-dunder-name
            method.__doc__ = message
            return property(method)

        iteritems = __make_raise_attributeerror('iteritems', 'items')
        iterkeys = __make_raise_attributeerror('iterkeys', 'keys')
        itervalues = __make_raise_attributeerror('itervalues', 'values')
        viewitems = __make_raise_attributeerror('viewitems', 'items')
        viewkeys = __make_raise_attributeerror('viewkeys', 'keys')
        viewvalues = __make_raise_attributeerror('viewvalues', 'values')


    class _NotGiven(object):
        # pylint: disable=too-few-public-methods
        def __repr__(self):
            return '<not-given>'

    __not_given = _NotGiven()

    def pop(self, key, default=__not_given):
        """Remove and return value for item identified by `key`.

        If the `key` is not found then return `default` if given. If `default`
        is not given then raise :exc:`KeyError`.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.pop('c')
        3
        >>> sd.pop('z', 26)
        26
        >>> sd.pop('y')
        Traceback (most recent call last):
          ...
        KeyError: 'y'

        :param key: `key` for item
        :param default: `default` value if key not found (optional)
        :return: value for item
        :raises KeyError: if `key` not found and `default` not given

        """
        if key in self:
            self._list_remove(key)
            return dict.pop(self, key)
        else:
            if default is self.__not_given:
                raise KeyError(key)
            return default


    def popitem(self, index=-1):
        """Remove and return ``(key, value)`` pair at `index` from sorted dict.

        Optional argument `index` defaults to -1, the last item in the sorted
        dict. Specify ``index=0`` for the first item in the sorted dict.

        If the sorted dict is empty, raises :exc:`KeyError`.

        If the `index` is out of range, raises :exc:`IndexError`.

        Runtime complexity: `O(log(n))`

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.popitem()
        ('c', 3)
        >>> sd.popitem(0)
        ('a', 1)
        >>> sd.popitem(100)
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param int index: `index` of item (default -1)
        :return: key and value pair
        :raises KeyError: if sorted dict is empty
        :raises IndexError: if `index` out of range

        """
        if not self:
            raise KeyError('popitem(): dictionary is empty')

        key = self._list_pop(index)
        value = dict.pop(self, key)
        return (key, value)


    def peekitem(self, index=-1):
        """Return ``(key, value)`` pair at `index` in sorted dict.

        Optional argument `index` defaults to -1, the last item in the sorted
        dict. Specify ``index=0`` for the first item in the sorted dict.

        Unlike :func:`SortedDict.popitem`, the sorted dict is not modified.

        If the `index` is out of range, raises :exc:`IndexError`.

        Runtime complexity: `O(log(n))`

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> sd.peekitem()
        ('c', 3)
        >>> sd.peekitem(0)
        ('a', 1)
        >>> sd.peekitem(100)
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param int index: index of item (default -1)
        :return: key and value pair
        :raises IndexError: if `index` out of range

        """
        key = self._list[index]
        return key, self[key]


    def setdefault(self, key, default=None):
        """Return value for item identified by `key` in sorted dict.

        If `key` is in the sorted dict then return its value. If `key` is not
        in the sorted dict then insert `key` with value `default` and return
        `default`.

        Optional argument `default` defaults to none.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict()
        >>> sd.setdefault('a', 1)
        1
        >>> sd.setdefault('a', 10)
        1
        >>> sd
        SortedDict({'a': 1})

        :param key: key for item
        :param default: value for item (default None)
        :return: value for item identified by `key`

        """
        if key in self:
            return self[key]
        dict.__setitem__(self, key, default)
        self._list_add(key)
        return default


    def update(self, *args, **kwargs):
        """Update sorted dict with items from `args` and `kwargs`.

        Overwrites existing items.

        Optional arguments `args` and `kwargs` may be a mapping, an iterable of
        pairs or keyword arguments. See :func:`SortedDict.__init__` for
        details.

        :param args: mapping or iterable of pairs
        :param kwargs: keyword arguments mapping

        """
        if not self:
            dict.update(self, *args, **kwargs)
            self._list_update(dict.__iter__(self))
            return

        if not kwargs and len(args) == 1 and isinstance(args[0], dict):
            pairs = args[0]
        else:
            pairs = dict(*args, **kwargs)

        if (10 * len(pairs)) > len(self):
            dict.update(self, pairs)
            self._list_clear()
            self._list_update(dict.__iter__(self))
        else:
            for key in pairs:
                self._setitem(key, pairs[key])

    _update = update


    def __reduce__(self):
        """Support for pickle.

        The tricks played with caching references in
        :func:`SortedDict.__init__` confuse pickle so customize the reducer.

        """
        items = dict.copy(self)
        return (type(self), (self._key, items))


    @recursive_repr()
    def __repr__(self):
        """Return string representation of sorted dict.

        ``sd.__repr__()`` <==> ``repr(sd)``

        :return: string representation

        """
        _key = self._key
        type_name = type(self).__name__
        key_arg = '' if _key is None else '{0!r}, '.format(_key)
        item_format = '{0!r}: {1!r}'.format
        items = ', '.join(item_format(key, self[key]) for key in self._list)
        return '{0}({1}{{{2}}})'.format(type_name, key_arg, items)


    def _check(self):
        """Check invariants of sorted dict.

        Runtime complexity: `O(n)`

        """
        _list = self._list
        _list._check()
        assert len(self) == len(_list)
        assert all(key in self for key in _list)


def _view_delitem(self, index):
    """Remove item at `index` from sorted dict.

    ``view.__delitem__(index)`` <==> ``del view[index]``

    Supports slicing.

    Runtime complexity: `O(log(n))` -- approximate.

    >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
    >>> view = sd.keys()
    >>> del view[0]
    >>> sd
    SortedDict({'b': 2, 'c': 3})
    >>> del view[-1]
    >>> sd
    SortedDict({'b': 2})
    >>> del view[:]
    >>> sd
    SortedDict({})

    :param index: integer or slice for indexing
    :raises IndexError: if index out of range

    """
    _mapping = self._mapping
    _list = _mapping._list
    dict_delitem = dict.__delitem__
    if isinstance(index, slice):
        keys = _list[index]
        del _list[index]
        for key in keys:
            dict_delitem(_mapping, key)
    else:
        key = _list.pop(index)
        dict_delitem(_mapping, key)


class SortedKeysView(KeysView, Sequence):
    """Sorted keys view is a dynamic view of the sorted dict's keys.

    When the sorted dict's keys change, the view reflects those changes.

    The keys view implements the set and sequence abstract base classes.

    """
    __slots__ = ()


    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)


    def __getitem__(self, index):
        """Lookup key at `index` in sorted keys views.

        ``skv.__getitem__(index)`` <==> ``skv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> skv = sd.keys()
        >>> skv[0]
        'a'
        >>> skv[-1]
        'c'
        >>> skv[:]
        ['a', 'b', 'c']
        >>> skv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: key or list of keys
        :raises IndexError: if index out of range

        """
        return self._mapping._list[index]


    __delitem__ = _view_delitem


class SortedItemsView(ItemsView, Sequence):
    """Sorted items view is a dynamic view of the sorted dict's items.

    When the sorted dict's items change, the view reflects those changes.

    The items view implements the set and sequence abstract base classes.

    """
    __slots__ = ()


    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)


    def __getitem__(self, index):
        """Lookup item at `index` in sorted items view.

        ``siv.__getitem__(index)`` <==> ``siv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> siv = sd.items()
        >>> siv[0]
        ('a', 1)
        >>> siv[-1]
        ('c', 3)
        >>> siv[:]
        [('a', 1), ('b', 2), ('c', 3)]
        >>> siv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: item or list of items
        :raises IndexError: if index out of range

        """
        _mapping = self._mapping
        _mapping_list = _mapping._list

        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [(key, _mapping[key]) for key in keys]

        key = _mapping_list[index]
        return key, _mapping[key]


    __delitem__ = _view_delitem


class SortedValuesView(ValuesView, Sequence):
    """Sorted values view is a dynamic view of the sorted dict's values.

    When the sorted dict's values change, the view reflects those changes.

    The values view implements the sequence abstract base class.

    """
    __slots__ = ()


    def __getitem__(self, index):
        """Lookup value at `index` in sorted values view.

        ``siv.__getitem__(index)`` <==> ``siv[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
        >>> svv = sd.values()
        >>> svv[0]
        1
        >>> svv[-1]
        3
        >>> svv[:]
        [1, 2, 3]
        >>> svv[100]
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
        _mapping = self._mapping
        _mapping_list = _mapping._list

        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [_mapping[key] for key in keys]

        key = _mapping_list[index]
        return _mapping[key]


    __delitem__ = _view_delitem



# -*- coding: utf-8 -*-

"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Core logic: internal tree nodes.

Copyright 2013-2018 Chaim Leib Halbert
Modifications Copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from operator import attrgetter
from math import floor, log2


class Node(object):
    __slots__ = (
        'x_center',
        's_center',
        'left_node',
        'right_node',
        'depth',
        'balance'
    )
    def __init__(self,
                 x_center=None,
                 s_center=set(),
                 left_node=None,
                 right_node=None):
        self.x_center = x_center
        self.s_center = set(s_center)
        self.left_node = left_node
        self.right_node = right_node
        self.depth = 0    # will be set when rotated
        self.balance = 0  # ditto
        self.rotate()

    @classmethod
    def from_interval(cls, interval):
        """
        :rtype : Node
        """
        center = interval.begin
        return Node(center, [interval])

    @classmethod
    def from_intervals(cls, intervals):
        """
        :rtype : Node
        """
        if not intervals:
            return None
        return Node.from_sorted_intervals(sorted(intervals))

    @classmethod
    def from_sorted_intervals(cls, intervals):
        """
        :rtype : Node
        """
        if not intervals:
            return None
        node = Node()
        node = node.init_from_sorted(intervals)
        return node

    def init_from_sorted(self, intervals):
        # assumes that intervals is a non-empty collection.
        # Else, next line raises IndexError
        center_iv = intervals[len(intervals) // 2]
        self.x_center = center_iv.begin
        self.s_center = set()
        s_left = []
        s_right = []
        for k in intervals:
            if k.end <= self.x_center:
                s_left.append(k)
            elif k.begin > self.x_center:
                s_right.append(k)
            else:
                self.s_center.add(k)
        self.left_node = Node.from_sorted_intervals(s_left)
        self.right_node = Node.from_sorted_intervals(s_right)
        return self.rotate()

    def center_hit(self, interval):
        """Returns whether interval overlaps self.x_center."""
        return interval.contains_point(self.x_center)

    def hit_branch(self, interval):
        """
        Assuming not center_hit(interval), return which branch
        (left=0, right=1) interval is in.
        """
        return interval.begin > self.x_center

    def refresh_balance(self):
        """
        Recalculate self.balance and self.depth based on child node values.
        """
        left_depth = self.left_node.depth if self.left_node else 0
        right_depth = self.right_node.depth if self.right_node else 0
        self.depth = 1 + max(left_depth, right_depth)
        self.balance = right_depth - left_depth

    def compute_depth(self):
        """
        Recursively computes true depth of the subtree. Should only
        be needed for debugging. Unless something is wrong, the
        depth field should reflect the correct depth of the subtree.
        """
        left_depth = self.left_node.compute_depth() if self.left_node else 0
        right_depth = self.right_node.compute_depth() if self.right_node else 0
        return 1 + max(left_depth, right_depth)

    def rotate(self):
        """
        Does rotating, if necessary, to balance this node, and
        returns the new top node.
        """
        self.refresh_balance()
        if abs(self.balance) < 2:
            return self
        # balance > 0  is the heavy side
        my_heavy = self.balance > 0
        child_heavy = self[my_heavy].balance > 0
        if my_heavy == child_heavy or self[my_heavy].balance == 0:
            ## Heavy sides same
            #    self     save
            #  save   -> 1   self
            # 1
            #
            ## Heavy side balanced
            #    self     save         save
            #  save   -> 1   self  -> 1  self.rot()
            #  1  2         2
            return self.srotate()
        else:
            return self.drotate()

    def srotate(self):
        """Single rotation. Assumes that balance is +-2."""
        #     self        save         save
        #   save 3  ->   1   self  -> 1   self.rot()
        #  1   2            2   3
        #
        #  self            save                save
        # 3   save  ->  self  1    -> self.rot()   1
        #    2   1     3   2

        #assert(self.balance != 0)
        heavy = self.balance > 0
        light = not heavy
        save = self[heavy]
        #print("srotate: bal={},{}".format(self.balance, save.balance))
        #self.print_structure()
        self[heavy] = save[light]   # 2
        #assert(save[light])
        save[light] = self.rotate()  # Needed to ensure the 2 and 3 are balanced under new subnode

        # Some intervals may overlap both self.x_center and save.x_center
        # Promote those to the new tip of the tree
        promotees = [iv for iv in save[light].s_center if save.center_hit(iv)]
        if promotees:
            for iv in promotees:
                save[light] = save[light].remove(iv)  # may trigger pruning
            # TODO: Use Node.add() here, to simplify future balancing improvements.
            # For now, this is the same as augmenting save.s_center, but that may
            # change.
            save.s_center.update(promotees)
        save.refresh_balance()
        return save

    def drotate(self):
        # First rotation
        my_heavy = self.balance > 0
        self[my_heavy] = self[my_heavy].srotate()
        self.refresh_balance()

        # Second rotation
        result = self.srotate()

        return result

    def add(self, interval):
        """
        Returns self after adding the interval and balancing.
        """
        if self.center_hit(interval):
            self.s_center.add(interval)
            return self
        else:
            direction = self.hit_branch(interval)
            if not self[direction]:
                self[direction] = Node.from_interval(interval)
                self.refresh_balance()
                return self
            else:
                self[direction] = self[direction].add(interval)
                return self.rotate()

    def remove(self, interval):
        """
        Returns self after removing the interval and balancing.

        If interval is not present, raise ValueError.
        """
        # since this is a list, called methods can set this to [1],
        # making it true
        done = []
        return self.remove_interval_helper(interval, done, should_raise_error=True)

    def discard(self, interval):
        """
        Returns self after removing interval and balancing.

        If interval is not present, do nothing.
        """
        done = []
        return self.remove_interval_helper(interval, done, should_raise_error=False)

    def remove_interval_helper(self, interval, done, should_raise_error):
        """
        Returns self after removing interval and balancing.
        If interval doesn't exist, raise ValueError.

        This method may set done to [1] to tell all callers that
        rebalancing has completed.

        See Eternally Confuzzled's jsw_remove_r function (lines 1-32)
        in his AVL tree article for reference.
        """
        #trace = interval.begin == 347 and interval.end == 353
        #if trace: print('\nRemoving from {} interval {}'.format(
        #   self.x_center, interval))
        if self.center_hit(interval):
            #if trace: print('Hit at {}'.format(self.x_center))
            if not should_raise_error and interval not in self.s_center:
                done.append(1)
                #if trace: print('Doing nothing.')
                return self
            try:
                # raises error if interval not present - this is
                # desired.
                self.s_center.remove(interval)
            except:
                self.print_structure()
                raise KeyError(interval)
            if self.s_center:     # keep this node
                done.append(1)    # no rebalancing necessary
                #if trace: print('Removed, no rebalancing.')
                return self

            # If we reach here, no intervals are left in self.s_center.
            # So, prune self.
            return self.prune()
        else:  # interval not in s_center
            direction = self.hit_branch(interval)

            if not self[direction]:
                if should_raise_error:
                    raise ValueError
                done.append(1)
                return self

            #if trace:
            #   print('Descending to {} branch'.format(
            #       ['left', 'right'][direction]
            #       ))
            self[direction] = self[direction].remove_interval_helper(interval, done, should_raise_error)

            # Clean up
            if not done:
                #if trace:
                #    print('Rotating {}'.format(self.x_center))
                #    self.print_structure()
                return self.rotate()
            return self

    def search_overlap(self, point_list):
        """
        Returns all intervals that overlap the point_list.
        """
        result = set()
        for j in point_list:
            self.search_point(j, result)
        return result

    def search_point(self, point, result):
        """
        Returns all intervals that contain point.
        """
        for k in self.s_center:
            if k.begin <= point < k.end:
                result.add(k)
        if point < self.x_center and self[0]:
            return self[0].search_point(point, result)
        elif point > self.x_center and self[1]:
            return self[1].search_point(point, result)
        return result

    def prune(self):
        """
        On a subtree where the root node's s_center is empty,
        return a new subtree with no empty s_centers.
        """
        if not self[0] or not self[1]:    # if I have an empty branch
            direction = not self[0]       # graft the other branch here
            #if trace:
            #    print('Grafting {} branch'.format(
            #       'right' if direction else 'left'))

            result = self[direction]
            #if result: result.verify()
            return result
        else:
            # Replace the root node with the greatest predecessor.
            heir, self[0] = self[0].pop_greatest_child()
            #if trace:
            #    print('Replacing {} with {}.'.format(
            #        self.x_center, heir.x_center
            #        ))
            #    print('Removed greatest predecessor:')
            #    self.print_structure()

            #if self[0]: self[0].verify()
            #if self[1]: self[1].verify()

            # Set up the heir as the new root node
            (heir[0], heir[1]) = (self[0], self[1])
            #if trace: print('Setting up the heir:')
            #if trace: heir.print_structure()

            # popping the predecessor may have unbalanced this node;
            # fix it
            heir.refresh_balance()
            heir = heir.rotate()
            #heir.verify()
            #if trace: print('Rotated the heir:')
            #if trace: heir.print_structure()
            return heir

    def pop_greatest_child(self):
        """
        Used when pruning a node with both a left and a right branch.
        Returns (greatest_child, node), where:
          * greatest_child is a new node to replace the removed node.
          * node is the subtree after:
              - removing the greatest child
              - balancing
              - moving overlapping nodes into greatest_child

        Assumes that self.s_center is not empty.

        See Eternally Confuzzled's jsw_remove_r function (lines 34-54)
        in his AVL tree article for reference.
        """
        #print('Popping from {}'.format(self.x_center))
        if not self.right_node:         # This node is the greatest child.
            # To reduce the chances of an overlap with a parent, return
            # a child node containing the smallest possible number of
            # intervals, as close as possible to the maximum bound.
            ivs = sorted(self.s_center, key=attrgetter('end', 'begin'))
            max_iv = ivs.pop()
            new_x_center = self.x_center
            while ivs:
                next_max_iv = ivs.pop()
                if next_max_iv.end == max_iv.end: continue
                new_x_center = max(new_x_center, next_max_iv.end)
            def get_new_s_center():
                for iv in self.s_center:
                    if iv.contains_point(new_x_center): yield iv

            # Create a new node with the largest x_center possible.
            child = Node(new_x_center, get_new_s_center())
            self.s_center -= child.s_center

            #print('Pop hit! Returning child   = {}'.format(
            #    child.print_structure(tostring=True)
            #    ))
            #assert not child[0]
            #assert not child[1]

            if self.s_center:
                #print('     and returning newnode = {}'.format( self ))
                #self.verify()
                return child, self
            else:
                #print('     and returning newnode = {}'.format( self[0] ))
                #if self[0]: self[0].verify()
                return child, self[0]  # Rotate left child up

        else:
            #print('Pop descent to {}'.format(self[1].x_center))
            (greatest_child, self[1]) = self[1].pop_greatest_child()

            # Move any overlaps into greatest_child
            for iv in set(self.s_center):
                if iv.contains_point(greatest_child.x_center):
                    self.s_center.remove(iv)
                    greatest_child.add(iv)

            #print('Pop Returning child   = {}'.format(
            #    greatest_child.print_structure(tostring=True)
            #    ))
            if self.s_center:
                #print('and returning newnode = {}'.format(
                #    new_self.print_structure(tostring=True)
                #    ))
                #new_self.verify()
                self.refresh_balance()
                new_self = self.rotate()
                return greatest_child, new_self
            else:
                new_self = self.prune()
                #print('and returning prune = {}'.format(
                #    new_self.print_structure(tostring=True)
                #    ))
                #if new_self: new_self.verify()
                return greatest_child, new_self

    def contains_point(self, p):
        """
        Returns whether this node or a child overlaps p.
        """
        for iv in self.s_center:
            if iv.contains_point(p):
                return True
        branch = self[p > self.x_center]
        return branch and branch.contains_point(p)

    def all_children(self):
        return self.all_children_helper(set())

    def all_children_helper(self, result):
        result.update(self.s_center)
        if self[0]:
            self[0].all_children_helper(result)
        if self[1]:
            self[1].all_children_helper(result)
        return result

    def verify(self, parents=set()):
        """
        ## DEBUG ONLY ##
        Recursively ensures that the invariants of an interval subtree
        hold.
        """
        assert(isinstance(self.s_center, set))

        bal = self.balance
        assert abs(bal) < 2, \
            "Error: Rotation should have happened, but didn't! \n{}".format(
                self.print_structure(tostring=True)
            )
        self.refresh_balance()
        assert bal == self.balance, \
            "Error: self.balance not set correctly! \n{}".format(
                self.print_structure(tostring=True)
            )

        assert self.s_center, \
            "Error: s_center is empty! \n{}".format(
                self.print_structure(tostring=True)
            )
        for iv in self.s_center:
            assert hasattr(iv, 'begin')
            assert hasattr(iv, 'end')
            assert iv.begin < iv.end
            assert iv.overlaps(self.x_center)
            for parent in sorted(parents):
                assert not iv.contains_point(parent), \
                    "Error: Overlaps ancestor ({})! \n{}\n\n{}".format(
                        parent, iv, self.print_structure(tostring=True)
                    )
        if self[0]:
            assert self[0].x_center < self.x_center, \
                "Error: Out-of-order left child! {}".format(self.x_center)
            self[0].verify(parents.union([self.x_center]))
        if self[1]:
            assert self[1].x_center > self.x_center, \
                "Error: Out-of-order right child! {}".format(self.x_center)
            self[1].verify(parents.union([self.x_center]))

    def __getitem__(self, index):
        """
        Returns the left child if input is equivalent to False, or
        the right side otherwise.
        """
        if index:
            return self.right_node
        else:
            return self.left_node

    def __setitem__(self, key, value):
        """Sets the left (0) or right (1) child."""
        if key:
            self.right_node = value
        else:
            self.left_node = value

    def __str__(self):
        """
        Shows info about this node.

        Since Nodes are internal data structures not revealed to the
        user, I'm not bothering to make this copy-paste-executable as a
        constructor.
        """
        return "Node<{0}, depth={1}, balance={2}>".format(
            self.x_center,
            self.depth,
            self.balance
        )
        #fieldcount = 'c_count,has_l,has_r = <{}, {}, {}>'.format(
        #    len(self.s_center),
        #    bool(self.left_node),
        #    bool(self.right_node)
        #)
        #fields = [self.x_center, self.balance, fieldcount]
        #return "Node({}, b={}, {})".format(*fields)

    def count_nodes(self):
        """
        Count the number of Nodes in this subtree.
        :rtype: int
        """
        count = 1
        if self.left_node:
            count += self.left_node.count_nodes()
        if self.right_node:
            count += self.right_node.count_nodes()
        return count

    def depth_score(self, n, m):
        """
        Calculates flaws in balancing the tree.
        :param n: size of tree
        :param m: number of Nodes in tree
        :rtype: real
        """
        if n == 0:
            return 0.0

        # dopt is the optimal maximum depth of the tree
        dopt = 1 + int(floor(log2(m)))
        f = 1 / float(1 + n - dopt)
        return f * self.depth_score_helper(1, dopt)

    def depth_score_helper(self, d, dopt):
        """
        Gets a weighted count of the number of Intervals deeper than dopt.
        :param d: current depth, starting from 0
        :param dopt: optimal maximum depth of a leaf Node
        :rtype: real
        """
        # di is how may levels deeper than optimal d is
        di = d - dopt
        if di > 0:
            count = di * len(self.s_center)
        else:
            count = 0
        if self.right_node:
            count += self.right_node.depth_score_helper(d + 1, dopt)
        if self.left_node:
            count += self.left_node.depth_score_helper(d + 1, dopt)
        return count

    def print_structure(self, indent=0, tostring=False):
        """
        For debugging.
        """
        nl = '\n'
        sp = indent * '    '

        rlist = [str(self) + nl]
        if self.s_center:
            for iv in sorted(self.s_center):
                rlist.append(sp + ' ' + repr(iv) + nl)
        if self.left_node:
            rlist.append(sp + '<:  ')  # no CR
            rlist.append(self.left_node.print_structure(indent + 1, True))
        if self.right_node:
            rlist.append(sp + '>:  ')  # no CR
            rlist.append(self.right_node.print_structure(indent + 1, True))
        result = ''.join(rlist)
        if tostring:
            return result
        else:
            print(result)



# -*- coding: utf-8 -*-

"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Interval class

Copyright 2013-2018 Chaim Leib Halbert
Modifications copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from numbers import Number
from collections import namedtuple


# noinspection PyBroadException
class Interval(namedtuple('IntervalBase', ['begin', 'end', 'data'])):
    __slots__ = ()  # Saves memory, avoiding the need to create __dict__ for each interval

    def __new__(cls, begin, end, data=None):
        return super(Interval, cls).__new__(cls, begin, end, data)
    
    def overlaps(self, begin, end=None):
        """
        Whether the interval overlaps the given point, range or Interval.
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: True or False
        :rtype: bool
        """
        if end is not None:
            # An overlap means that some C exists that is inside both ranges:
            #   begin <= C < end
            # and 
            #   self.begin <= C < self.end
            # See https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap/3269471#3269471
            return begin < self.end and end > self.begin
        try:
            return self.overlaps(begin.begin, begin.end)
        except:
            return self.contains_point(begin)

    def overlap_size(self, begin, end=None):
        """
        Return the overlap size between two intervals or a point
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: Return the overlap size, None if not overlap is found
        :rtype: depends on the given input (e.g., int will be returned for int interval and timedelta for
        datetime intervals)
        """
        overlaps = self.overlaps(begin, end)
        if not overlaps:
            return 0

        if end is not None:
            # case end is given
            i0 = max(self.begin, begin)
            i1 = min(self.end, end)
            return i1 - i0
        # assume the type is interval, in other cases, an exception will be thrown
        i0 = max(self.begin, begin.begin)
        i1 = min(self.end, begin.end)
        return i1 - i0

    def contains_point(self, p):
        """
        Whether the Interval contains p.
        :param p: a point
        :return: True or False
        :rtype: bool
        """
        return self.begin <= p < self.end
    
    def range_matches(self, other):
        """
        Whether the begins equal and the ends equal. Compare __eq__().
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return (
            self.begin == other.begin and 
            self.end == other.end
        )
    
    def contains_interval(self, other):
        """
        Whether other is contained in this Interval.
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return (
            self.begin <= other.begin and
            self.end >= other.end
        )
    
    def distance_to(self, other):
        """
        Returns the size of the gap between intervals, or 0 
        if they touch or overlap.
        :param other: Interval or point
        :return: distance
        :rtype: Number
        """
        if self.overlaps(other):
            return 0
        try:
            if self.begin < other.begin:
                return other.begin - self.end
            else:
                return self.begin - other.end
        except:
            if self.end <= other:
                return other - self.end
            else:
                return self.begin - other

    def is_null(self):
        """
        Whether this equals the null interval.
        :return: True if end <= begin else False
        :rtype: bool
        """
        return self.begin >= self.end

    def length(self):
        """
        The distance covered by this Interval.
        :return: length
        :type: Number
        """
        if self.is_null():
            return 0
        return self.end - self.begin

    def __hash__(self):
        """
        Depends on begin and end only.
        :return: hash
        :rtype: Number
        """
        return hash((self.begin, self.end))

    def __eq__(self, other):
        """
        Whether the begins equal, the ends equal, and the data fields
        equal. Compare range_matches().
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return (
            self.begin == other.begin and
            self.end == other.end and
            self.data == other.data
        )

    def __cmp__(self, other):
        """
        Tells whether other sorts before, after or equal to this
        Interval.

        Sorting is by begins, then by ends, then by data fields.

        If data fields are not both sortable types, data fields are
        compared alphabetically by type name.
        :param other: Interval
        :return: -1, 0, 1
        :rtype: int
        """
        s = self[0:2]
        try:
            o = other[0:2]
        except:
            o = (other,)
        if s != o:
            return -1 if s < o else 1
        try:
            if self.data == other.data:
                return 0
            return -1 if self.data < other.data else 1
        except TypeError:
            s = type(self.data).__name__
            o = type(other.data).__name__
            if s == o:
                return 0
            return -1 if s < o else 1

    def __lt__(self, other):
        """
        Less than operator. Parrots __cmp__()
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        return self.__cmp__(other) < 0

    def __gt__(self, other):
        """
        Greater than operator. Parrots __cmp__()
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        return self.__cmp__(other) > 0

    def _raise_if_null(self, other):
        """
        :raises ValueError: if either self or other is a null Interval
        """
        if self.is_null():
            raise ValueError("Cannot compare null Intervals!")
        if hasattr(other, 'is_null') and other.is_null():
            raise ValueError("Cannot compare null Intervals!")

    def lt(self, other):
        """
        Strictly less than. Returns True if no part of this Interval
        extends higher than or into other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        return self.end <= getattr(other, 'begin', other)

    def le(self, other):
        """
        Less than or overlaps. Returns True if no part of this Interval
        extends higher than other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        return self.end <= getattr(other, 'end', other)

    def gt(self, other):
        """
        Strictly greater than. Returns True if no part of this Interval
        extends lower than or into other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        if hasattr(other, 'end'):
            return self.begin >= other.end
        else:
            return self.begin > other

    def ge(self, other):
        """
        Greater than or overlaps. Returns True if no part of this Interval
        extends lower than other.
        :raises ValueError: if either self or other is a null Interval
        :param other: Interval or point
        :return: True or False
        :rtype: bool
        """
        self._raise_if_null(other)
        return self.begin >= getattr(other, 'begin', other)

    def _get_fields(self):
        """
        Used by str, unicode, repr and __reduce__.

        Returns only the fields necessary to reconstruct the Interval.
        :return: reconstruction info
        :rtype: tuple
        """
        if self.data is not None:
            return self.begin, self.end, self.data
        else:
            return self.begin, self.end
    
    def __repr__(self):
        """
        Executable string representation of this Interval.
        :return: string representation
        :rtype: str
        """
        if isinstance(self.begin, Number):
            s_begin = str(self.begin)
            s_end = str(self.end)
        else:
            s_begin = repr(self.begin)
            s_end = repr(self.end)
        if self.data is None:
            return "Interval({0}, {1})".format(s_begin, s_end)
        else:
            return "Interval({0}, {1}, {2})".format(s_begin, s_end, repr(self.data))

    __str__ = __repr__

    def copy(self):
        """
        Shallow copy.
        :return: copy of self
        :rtype: Interval
        """
        return Interval(self.begin, self.end, self.data)
    
    def __reduce__(self):
        """
        For pickle-ing.
        :return: pickle data
        :rtype: tuple
        """
        return Interval, self._get_fields()



# -*- coding: utf-8 -*-

"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Core logic.

Copyright 2013-2018 Chaim Leib Halbert
Modifications Copyright 2014 Konstantin Tretyakov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from numbers import Number
from copy import copy
from warnings import warn

try:
    from collections.abc import MutableSet  # Python 3?
except ImportError:
    from collections import MutableSet

try:
    xrange  # Python 2?
except NameError:  # pragma: no cover
    xrange = range


# noinspection PyBroadException
class IntervalTree(MutableSet):
    """
    A binary lookup tree of intervals.
    The intervals contained in the tree are represented using ``Interval(a, b, data)`` objects.
    Each such object represents a half-open interval ``[a, b)`` with optional data.

    Examples:
    ---------

    Initialize a blank tree::

        >>> tree = IntervalTree()
        >>> tree
        IntervalTree()

    Initialize a tree from an iterable set of Intervals in O(n * log n)::

        >>> tree = IntervalTree([Interval(-10, 10), Interval(-20.0, -10.0)])
        >>> tree
        IntervalTree([Interval(-20.0, -10.0), Interval(-10, 10)])
        >>> len(tree)
        2

    Note that this is a set, i.e. repeated intervals are ignored. However,
    Intervals with different data fields are regarded as different::

        >>> tree = IntervalTree([Interval(-10, 10), Interval(-10, 10), Interval(-10, 10, "x")])
        >>> tree
        IntervalTree([Interval(-10, 10), Interval(-10, 10, 'x')])
        >>> len(tree)
        2

    Insertions::
        >>> tree = IntervalTree()
        >>> tree[0:1] = "data"
        >>> tree.add(Interval(10, 20))
        >>> tree.addi(19.9, 20)
        >>> tree
        IntervalTree([Interval(0, 1, 'data'), Interval(10, 20), Interval(19.9, 20)])
        >>> tree.update([Interval(19.9, 20.1), Interval(20.1, 30)])
        >>> len(tree)
        5

        Inserting the same Interval twice does nothing::
            >>> tree = IntervalTree()
            >>> tree[-10:20] = "arbitrary data"
            >>> tree[-10:20] = None  # Note that this is also an insertion
            >>> tree
            IntervalTree([Interval(-10, 20), Interval(-10, 20, 'arbitrary data')])
            >>> tree[-10:20] = None  # This won't change anything
            >>> tree[-10:20] = "arbitrary data" # Neither will this
            >>> len(tree)
            2

    Deletions::
        >>> tree = IntervalTree(Interval(b, e) for b, e in [(-10, 10), (-20, -10), (10, 20)])
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(-10, 10), Interval(10, 20)])
        >>> tree.remove(Interval(-10, 10))
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(10, 20)])
        >>> tree.remove(Interval(-10, 10))
        Traceback (most recent call last):
        ...
        ValueError
        >>> tree.discard(Interval(-10, 10))  # Same as remove, but no exception on failure
        >>> tree
        IntervalTree([Interval(-20, -10), Interval(10, 20)])

    Delete intervals, overlapping a given point::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.1)
        >>> tree
        IntervalTree([Interval(-1.1, 1.1)])

    Delete intervals, overlapping an interval::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_overlap(0, 0.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.7, 1.8)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.6, 1.6)  # Null interval does nothing
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_overlap(1.6, 1.5)  # Ditto
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])

    Delete intervals, enveloped in the range::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> tree.remove_envelop(-1.0, 1.5)
        >>> tree
        IntervalTree([Interval(-1.1, 1.1), Interval(0.5, 1.7)])
        >>> tree.remove_envelop(-1.1, 1.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_envelop(0.5, 1.5)
        >>> tree
        IntervalTree([Interval(0.5, 1.7)])
        >>> tree.remove_envelop(0.5, 1.7)
        >>> tree
        IntervalTree()

    Point queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree[-1.1]   == set([Interval(-1.1, 1.1)])
        >>> assert tree.at(1.1) == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])   # Same as tree[1.1]
        >>> assert tree.at(1.5) == set([Interval(0.5, 1.7)])                        # Same as tree[1.5]

    Interval overlap queries

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree.overlap(1.7, 1.8) == set()
        >>> assert tree.overlap(1.5, 1.8) == set([Interval(0.5, 1.7)])
        >>> assert tree[1.5:1.8] == set([Interval(0.5, 1.7)])                       # same as previous
        >>> assert tree.overlap(1.1, 1.8) == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree[1.1:1.8] == set([Interval(-0.5, 1.5), Interval(0.5, 1.7)])  # same as previous

    Interval envelop queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> assert tree.envelop(-0.5, 0.5) == set()
        >>> assert tree.envelop(-0.5, 1.5) == set([Interval(-0.5, 1.5)])

    Membership queries::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> Interval(-0.5, 0.5) in tree
        False
        >>> Interval(-1.1, 1.1) in tree
        True
        >>> Interval(-1.1, 1.1, "x") in tree
        False
        >>> tree.overlaps(-1.1)
        True
        >>> tree.overlaps(1.7)
        False
        >>> tree.overlaps(1.7, 1.8)
        False
        >>> tree.overlaps(-1.2, -1.1)
        False
        >>> tree.overlaps(-1.2, -1.0)
        True

    Sizing::

        >>> tree = IntervalTree([Interval(-1.1, 1.1), Interval(-0.5, 1.5), Interval(0.5, 1.7)])
        >>> len(tree)
        3
        >>> tree.is_empty()
        False
        >>> IntervalTree().is_empty()
        True
        >>> not tree
        False
        >>> not IntervalTree()
        True
        >>> print(tree.begin())    # using print() because of floats in Python 2.6
        -1.1
        >>> print(tree.end())      # ditto
        1.7

    Iteration::

        >>> tree = IntervalTree([Interval(-11, 11), Interval(-5, 15), Interval(5, 17)])
        >>> [iv.begin for iv in sorted(tree)]
        [-11, -5, 5]
        >>> assert tree.items() == set([Interval(-5, 15), Interval(-11, 11), Interval(5, 17)])

    Copy- and typecasting, pickling::

        >>> tree0 = IntervalTree([Interval(0, 1, "x"), Interval(1, 2, ["x"])])
        >>> tree1 = IntervalTree(tree0)  # Shares Interval objects
        >>> tree2 = tree0.copy()         # Shallow copy (same as above, as Intervals are singletons)
        >>> import pickle
        >>> tree3 = pickle.loads(pickle.dumps(tree0))  # Deep copy
        >>> list(tree0[1])[0].data[0] = "y"  # affects shallow copies, but not deep copies
        >>> tree0
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree1
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree2
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['y'])])
        >>> tree3
        IntervalTree([Interval(0, 1, 'x'), Interval(1, 2, ['x'])])

    Equality testing::

        >>> IntervalTree([Interval(0, 1)]) == IntervalTree([Interval(0, 1)])
        True
        >>> IntervalTree([Interval(0, 1)]) == IntervalTree([Interval(0, 1, "x")])
        False
    """
    @classmethod
    def from_tuples(cls, tups):
        """
        Create a new IntervalTree from an iterable of 2- or 3-tuples,
         where the tuple lists begin, end, and optionally data.
        """
        ivs = [Interval(*t) for t in tups]
        return IntervalTree(ivs)

    def __init__(self, intervals=None):
        """
        Set up a tree. If intervals is provided, add all the intervals
        to the tree.

        Completes in O(n*log n) time.
        """
        intervals = set(intervals) if intervals is not None else set()
        for iv in intervals:
            if iv.is_null():
                raise ValueError(
                    "IntervalTree: Null Interval objects not allowed in IntervalTree:"
                    " {0}".format(iv)
                )
        self.all_intervals = intervals
        self.top_node = Node.from_intervals(self.all_intervals)
        self.boundary_table = SortedDict()
        for iv in self.all_intervals:
            self._add_boundaries(iv)

    def copy(self):
        """
        Construct a new IntervalTree using shallow copies of the
        intervals in the source tree.

        Completes in O(n*log n) time.
        :rtype: IntervalTree
        """
        return IntervalTree(iv.copy() for iv in self)

    def _add_boundaries(self, interval):
        """
        Records the boundaries of the interval in the boundary table.
        """
        begin = interval.begin
        end = interval.end
        if begin in self.boundary_table:
            self.boundary_table[begin] += 1
        else:
            self.boundary_table[begin] = 1

        if end in self.boundary_table:
            self.boundary_table[end] += 1
        else:
            self.boundary_table[end] = 1

    def _remove_boundaries(self, interval):
        """
        Removes the boundaries of the interval from the boundary table.
        """
        begin = interval.begin
        end = interval.end
        if self.boundary_table[begin] == 1:
            del self.boundary_table[begin]
        else:
            self.boundary_table[begin] -= 1

        if self.boundary_table[end] == 1:
            del self.boundary_table[end]
        else:
            self.boundary_table[end] -= 1

    def add(self, interval):
        """
        Adds an interval to the tree, if not already present.

        Completes in O(log n) time.
        """
        if interval in self:
            return

        if interval.is_null():
            raise ValueError(
                "IntervalTree: Null Interval objects not allowed in IntervalTree:"
                " {0}".format(interval)
            )

        if not self.top_node:
            self.top_node = Node.from_interval(interval)
        else:
            self.top_node = self.top_node.add(interval)
        self.all_intervals.add(interval)
        self._add_boundaries(interval)
    append = add

    def addi(self, begin, end, data=None):
        """
        Shortcut for add(Interval(begin, end, data)).

        Completes in O(log n) time.
        """
        return self.add(Interval(begin, end, data))
    appendi = addi

    def update(self, intervals):
        """
        Given an iterable of intervals, add them to the tree.

        Completes in O(m*log(n+m), where m = number of intervals to
        add.
        """
        for iv in intervals:
            self.add(iv)

    def remove(self, interval):
        """
        Removes an interval from the tree, if present. If not, raises
        ValueError.

        Completes in O(log n) time.
        """
        #self.verify()
        if interval not in self:
            #print(self.all_intervals)
            raise ValueError
        self.top_node = self.top_node.remove(interval)
        self.all_intervals.remove(interval)
        self._remove_boundaries(interval)
        #self.verify()

    def removei(self, begin, end, data=None):
        """
        Shortcut for remove(Interval(begin, end, data)).

        Completes in O(log n) time.
        """
        return self.remove(Interval(begin, end, data))

    def discard(self, interval):
        """
        Removes an interval from the tree, if present. If not, does
        nothing.

        Completes in O(log n) time.
        """
        if interval not in self:
            return
        self.all_intervals.discard(interval)
        self.top_node = self.top_node.discard(interval)
        self._remove_boundaries(interval)

    def discardi(self, begin, end, data=None):
        """
        Shortcut for discard(Interval(begin, end, data)).

        Completes in O(log n) time.
        """
        return self.discard(Interval(begin, end, data))

    def difference(self, other):
        """
        Returns a new tree, comprising all intervals in self but not
        in other.
        """
        ivs = set()
        for iv in self:
            if iv not in other:
                ivs.add(iv)
        return IntervalTree(ivs)

    def difference_update(self, other):
        """
        Removes all intervals in other from self.
        """
        for iv in other:
            self.discard(iv)

    def union(self, other):
        """
        Returns a new tree, comprising all intervals from self
        and other.
        """
        return IntervalTree(set(self).union(other))

    def intersection(self, other):
        """
        Returns a new tree of all intervals common to both self and
        other.
        """
        ivs = set()
        shorter, longer = sorted([self, other], key=len)
        for iv in shorter:
            if iv in longer:
                ivs.add(iv)
        return IntervalTree(ivs)

    def intersection_update(self, other):
        """
        Removes intervals from self unless they also exist in other.
        """
        ivs = list(self)
        for iv in ivs:
            if iv not in other:
                self.remove(iv)

    def symmetric_difference(self, other):
        """
        Return a tree with elements only in self or other but not
        both.
        """
        if not isinstance(other, set): other = set(other)
        me = set(self)
        ivs = me.difference(other).union(other.difference(me))
        return IntervalTree(ivs)

    def symmetric_difference_update(self, other):
        """
        Throws out all intervals except those only in self or other,
        not both.
        """
        other = set(other)
        ivs = list(self)
        for iv in ivs:
            if iv in other:
                self.remove(iv)
                other.remove(iv)
        self.update(other)

    def remove_overlap(self, begin, end=None):
        """
        Removes all intervals overlapping the given point or range.

        Completes in O((r+m)*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * r = size of the search range (this is 1 for a point)
        """
        hitlist = self.at(begin) if end is None else self.overlap(begin, end)
        for iv in hitlist:
            self.remove(iv)

    def remove_envelop(self, begin, end):
        """
        Removes all intervals completely enveloped in the given range.

        Completes in O((r+m)*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * r = size of the search range
        """
        hitlist = self.envelop(begin, end)
        for iv in hitlist:
            self.remove(iv)

    def chop(self, begin, end, datafunc=None):
        """
        Like remove_envelop(), but trims back Intervals hanging into
        the chopped area so that nothing overlaps.
        """
        insertions = set()
        begin_hits = [iv for iv in self.at(begin) if iv.begin < begin]
        end_hits = [iv for iv in self.at(end) if iv.end > end]

        if datafunc:
            for iv in begin_hits:
                insertions.add(Interval(iv.begin, begin, datafunc(iv, True)))
            for iv in end_hits:
                insertions.add(Interval(end, iv.end, datafunc(iv, False)))
        else:
            for iv in begin_hits:
                insertions.add(Interval(iv.begin, begin, iv.data))
            for iv in end_hits:
                insertions.add(Interval(end, iv.end, iv.data))

        self.remove_envelop(begin, end)
        self.difference_update(begin_hits)
        self.difference_update(end_hits)
        self.update(insertions)

    def slice(self, point, datafunc=None):
        """
        Split Intervals that overlap point into two new Intervals. if
        specified, uses datafunc(interval, islower=True/False) to
        set the data field of the new Intervals.
        :param point: where to slice
        :param datafunc(interval, isupper): callable returning a new
        value for the interval's data field
        """
        hitlist = set(iv for iv in self.at(point) if iv.begin < point)
        insertions = set()
        if datafunc:
            for iv in hitlist:
                insertions.add(Interval(iv.begin, point, datafunc(iv, True)))
                insertions.add(Interval(point, iv.end, datafunc(iv, False)))
        else:
            for iv in hitlist:
                insertions.add(Interval(iv.begin, point, iv.data))
                insertions.add(Interval(point, iv.end, iv.data))
        self.difference_update(hitlist)
        self.update(insertions)

    def clear(self):
        """
        Empties the tree.

        Completes in O(1) tine.
        """
        self.__init__()

    def find_nested(self):
        """
        Returns a dictionary mapping parent intervals to sets of
        intervals overlapped by and contained in the parent.

        Completes in O(n^2) time.
        :rtype: dict of [Interval, set of Interval]
        """
        result = {}

        def add_if_nested():
            if parent.contains_interval(child):
                if parent not in result:
                    result[parent] = set()
                result[parent].add(child)

        long_ivs = sorted(self.all_intervals, key=Interval.length, reverse=True)
        for i, parent in enumerate(long_ivs):
            for child in long_ivs[i + 1:]:
                add_if_nested()
        return result

    def overlaps(self, begin, end=None):
        """
        Returns whether some interval in the tree overlaps the given
        point or range.

        Completes in O(r*log n) time, where r is the size of the
        search range.
        :rtype: bool
        """
        if end is not None:
            return self.overlaps_range(begin, end)
        elif isinstance(begin, Number):
            return self.overlaps_point(begin)
        else:
            return self.overlaps_range(begin.begin, begin.end)

    def overlaps_point(self, p):
        """
        Returns whether some interval in the tree overlaps p.

        Completes in O(log n) time.
        :rtype: bool
        """
        if self.is_empty():
            return False
        return bool(self.top_node.contains_point(p))

    def overlaps_range(self, begin, end):
        """
        Returns whether some interval in the tree overlaps the given
        range. Returns False if given a null interval over which to
        test.

        Completes in O(r*log n) time, where r is the range length and n
        is the table size.
        :rtype: bool
        """
        if self.is_empty():
            return False
        elif begin >= end:
            return False
        elif self.overlaps_point(begin):
            return True
        return any(
            self.overlaps_point(bound)
            for bound in self.boundary_table
            if begin < bound < end
        )

    def split_overlaps(self):
        """
        Finds all intervals with overlapping ranges and splits them
        along the range boundaries.

        Completes in worst-case O(n^2*log n) time (many interval
        boundaries are inside many intervals), best-case O(n*log n)
        time (small number of overlaps << n per interval).
        """
        if not self:
            return
        if len(self.boundary_table) == 2:
            return

        bounds = sorted(self.boundary_table)  # get bound locations

        new_ivs = set()
        for lbound, ubound in zip(bounds[:-1], bounds[1:]):
            for iv in self[lbound]:
                new_ivs.add(Interval(lbound, ubound, iv.data))

        self.__init__(new_ivs)

    def merge_overlaps(self, data_reducer=None, data_initializer=None, strict=True):
        """
        Finds all intervals with overlapping ranges and merges them
        into a single interval. If provided, uses data_reducer and
        data_initializer with similar semantics to Python's built-in
        reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initializer created with copy.copy(data_initializer).

        If strict is True (default), intervals are only merged if
        their ranges actually overlap; adjacent, touching intervals
        will not be merged. If strict is False, intervals are merged
        even if they are only end-to-end adjacent.

        Completes in O(n*logn) time.
        """
        if not self:
            return

        sorted_intervals = sorted(self.all_intervals)  # get sorted intervals
        merged = []
        # use mutable object to allow new_series() to modify it
        current_reduced = [None]
        higher = None  # iterating variable, which new_series() needs access to

        def new_series():
            if data_initializer is None:
                current_reduced[0] = higher.data
                merged.append(higher)
                return
            else:  # data_initializer is not None
                current_reduced[0] = copy(data_initializer)
                current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                merged.append(Interval(higher.begin, higher.end, current_reduced[0]))

        for higher in sorted_intervals:
            if merged:  # series already begun
                lower = merged[-1]
                if (higher.begin < lower.end or
                    not strict and higher.begin == lower.end):  # should merge
                    upper_bound = max(lower.end, higher.end)
                    if data_reducer is not None:
                        current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                    else:  # annihilate the data, since we don't know how to merge it
                        current_reduced[0] = None
                    merged[-1] = Interval(lower.begin, upper_bound, current_reduced[0])
                else:
                    new_series()
            else:  # not merged; is first of Intervals to merge
                new_series()

        self.__init__(merged)

    def merge_equals(self, data_reducer=None, data_initializer=None):
        """
        Finds all intervals with equal ranges and merges them
        into a single interval. If provided, uses data_reducer and
        data_initializer with similar semantics to Python's built-in
        reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initiazer created with
            copy.copy(data_initializer).

        Completes in O(n*logn) time.
        """
        if not self:
            return

        sorted_intervals = sorted(self.all_intervals)  # get sorted intervals
        merged = []
        # use mutable object to allow new_series() to modify it
        current_reduced = [None]
        higher = None  # iterating variable, which new_series() needs access to

        def new_series():
            if data_initializer is None:
                current_reduced[0] = higher.data
                merged.append(higher)
                return
            else:  # data_initializer is not None
                current_reduced[0] = copy(data_initializer)
                current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                merged.append(Interval(higher.begin, higher.end, current_reduced[0]))

        for higher in sorted_intervals:
            if merged:  # series already begun
                lower = merged[-1]
                if higher.range_matches(lower):  # should merge
                    upper_bound = max(lower.end, higher.end)
                    if data_reducer is not None:
                        current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                    else:  # annihilate the data, since we don't know how to merge it
                        current_reduced[0] = None
                    merged[-1] = Interval(lower.begin, upper_bound, current_reduced[0])
                else:
                    new_series()
            else:  # not merged; is first of Intervals to merge
                new_series()

        self.__init__(merged)

    def merge_neighbors(
        self,
        data_reducer=None,
        data_initializer=None,
        distance=1,
        strict=True,
    ):
        """
        Finds all adjacent intervals with range terminals less than or equal to
        the given distance and merges them into a single interval. If provided,
        uses data_reducer and data_initializer with similar semantics to
        Python's built-in reduce(reducer_func[, initializer]), as follows:

        If data_reducer is set to a function, combines the data
        fields of the Intervals with
            current_reduced_data = data_reducer(current_reduced_data, new_data)
        If data_reducer is None, the merged Interval's data
        field will be set to None, ignoring all the data fields
        of the merged Intervals.

        On encountering the first Interval to merge, if
        data_initializer is None (default), uses the first
        Interval's data field as the first value for
        current_reduced_data. If data_initializer is not None,
        current_reduced_data is set to a shallow copy of
        data_initiazer created with
            copy.copy(data_initializer).

        If strict is True (default), only discrete intervals are merged if
        their ranges are within the given distance; overlapping intervals
        will not be merged. If strict is False, both neighbors and overlapping
        intervals are merged.

        Completes in O(n*logn) time.
        """
        if not self:
            return

        sorted_intervals = sorted(self.all_intervals)  # get sorted intervals
        merged = []
        # use mutable object to allow new_series() to modify it
        current_reduced = [None]
        higher = None  # iterating variable, which new_series() needs access to

        def new_series():
            if data_initializer is None:
                current_reduced[0] = higher.data
                merged.append(higher)
                return
            else:  # data_initializer is not None
                current_reduced[0] = copy(data_initializer)
                current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                merged.append(Interval(higher.begin, higher.end, current_reduced[0]))

        for higher in sorted_intervals:
            if merged:  # series already begun
                lower = merged[-1]
                margin = higher.begin - lower.end
                if margin <= distance:  # should merge
                    if strict and margin < 0:
                        new_series()
                        continue
                    else:
                        upper_bound = max(lower.end, higher.end)
                        if data_reducer is not None:
                            current_reduced[0] = data_reducer(current_reduced[0], higher.data)
                        else:  # annihilate the data, since we don't know how to merge it
                            current_reduced[0] = None
                        merged[-1] = Interval(lower.begin, upper_bound, current_reduced[0])
                else:
                    new_series()
            else:  # not merged; is first of Intervals to merge
                new_series()

        self.__init__(merged)

    def items(self):
        """
        Constructs and returns a set of all intervals in the tree.

        Completes in O(n) time.
        :rtype: set of Interval
        """
        return set(self.all_intervals)

    def is_empty(self):
        """
        Returns whether the tree is empty.

        Completes in O(1) time.
        :rtype: bool
        """
        return 0 == len(self)

    def at(self, p):
        """
        Returns the set of all intervals that contain p.

        Completes in O(m + log n) time, where:
          * n = size of the tree
          * m = number of matches
        :rtype: set of Interval
        """
        root = self.top_node
        if not root:
            return set()
        return root.search_point(p, set())

    def envelop(self, begin, end=None):
        """
        Returns the set of all intervals fully contained in the range
        [begin, end).

        Completes in O(m + k*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range
        :rtype: set of Interval
        """
        root = self.top_node
        if not root:
            return set()
        if end is None:
            iv = begin
            return self.envelop(iv.begin, iv.end)
        elif begin >= end:
            return set()
        result = root.search_point(begin, set()) # bound_begin might be greater
        boundary_table = self.boundary_table
        bound_begin = boundary_table.bisect_left(begin)
        bound_end = boundary_table.bisect_left(end)  # up to, but not including end
        result.update(root.search_overlap(
            # slice notation is slightly slower
            boundary_table.keys()[index] for index in xrange(bound_begin, bound_end)
        ))

        # TODO: improve envelop() to use node info instead of less-efficient filtering
        result = set(
            iv for iv in result
            if iv.begin >= begin and iv.end <= end
        )
        return result

    def overlap(self, begin, end=None):
        """
        Returns a set of all intervals overlapping the given range.

        Completes in O(m + k*log n) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range
        :rtype: set of Interval
        """
        root = self.top_node
        if not root:
            return set()
        if end is None:
            iv = begin
            return self.overlap(iv.begin, iv.end)
        elif begin >= end:
            return set()
        result = root.search_point(begin, set())  # bound_begin might be greater
        boundary_table = self.boundary_table
        bound_begin = boundary_table.bisect_left(begin)
        bound_end = boundary_table.bisect_left(end)  # up to, but not including end
        result.update(root.search_overlap(
            # slice notation is slightly slower
            boundary_table.keys()[index] for index in xrange(bound_begin, bound_end)
        ))
        return result

    def begin(self):
        """
        Returns the lower bound of the first interval in the tree.

        Completes in O(1) time.
        """
        if not self.boundary_table:
            return 0
        return self.boundary_table.keys()[0]

    def end(self):
        """
        Returns the upper bound of the last interval in the tree.

        Completes in O(1) time.
        """
        if not self.boundary_table:
            return 0
        return self.boundary_table.keys()[-1]

    def range(self):
        """
        Returns a minimum-spanning Interval that encloses all the
        members of this IntervalTree. If the tree is empty, returns
        null Interval.
        :rtype: Interval
        """
        return Interval(self.begin(), self.end())

    def span(self):
        """
        Returns the length of the minimum-spanning Interval that
        encloses all the members of this IntervalTree. If the tree
        is empty, return 0.
        """
        if not self:
            return 0
        return self.end() - self.begin()

    def print_structure(self, tostring=False):
        """
        ## FOR DEBUGGING ONLY ##
        Pretty-prints the structure of the tree.
        If tostring is true, prints nothing and returns a string.
        :rtype: None or str
        """
        if self.top_node:
            return self.top_node.print_structure(tostring=tostring)
        else:
            result = "<empty IntervalTree>"
            if not tostring:
                print(result)
            else:
                return result

    def verify(self):
        """
        ## FOR DEBUGGING ONLY ##
        Checks the table to ensure that the invariants are held.
        """
        if self.all_intervals:
            ## top_node.all_children() == self.all_intervals
            try:
                assert self.top_node.all_children() == self.all_intervals
            except AssertionError as e:
                print(
                    'Error: the tree and the membership set are out of sync!'
                )
                tivs = set(self.top_node.all_children())
                print('top_node.all_children() - all_intervals:')
                try:
                    pprint
                except NameError:
                    from pprint import pprint
                pprint(tivs - self.all_intervals)
                print('all_intervals - top_node.all_children():')
                pprint(self.all_intervals - tivs)
                raise e

            ## All members are Intervals
            for iv in self:
                assert isinstance(iv, Interval), (
                    "Error: Only Interval objects allowed in IntervalTree:"
                    " {0}".format(iv)
                )

            ## No null intervals
            for iv in self:
                assert not iv.is_null(), (
                    "Error: Null Interval objects not allowed in IntervalTree:"
                    " {0}".format(iv)
                )

            ## Reconstruct boundary_table
            bound_check = {}
            for iv in self:
                if iv.begin in bound_check:
                    bound_check[iv.begin] += 1
                else:
                    bound_check[iv.begin] = 1
                if iv.end in bound_check:
                    bound_check[iv.end] += 1
                else:
                    bound_check[iv.end] = 1

            ## Reconstructed boundary table (bound_check) ==? boundary_table
            assert set(self.boundary_table.keys()) == set(bound_check.keys()),\
                'Error: boundary_table is out of sync with ' \
                'the intervals in the tree!'

            # For efficiency reasons this should be iteritems in Py2, but we
            # don't care much for efficiency in debug methods anyway.
            for key, val in self.boundary_table.items():
                assert bound_check[key] == val, \
                    'Error: boundary_table[{0}] should be {1},' \
                    ' but is {2}!'.format(
                        key, bound_check[key], val)

            ## Internal tree structure
            self.top_node.verify(set())
        else:
            ## Verify empty tree
            assert not self.boundary_table, \
                "Error: boundary table should be empty!"
            assert self.top_node is None, \
                "Error: top_node isn't None!"

    def score(self, full_report=False):
        """
        Returns a number between 0 and 1, indicating how suboptimal the tree
        is. The lower, the better. Roughly, this number represents the
        fraction of flawed Intervals in the tree.
        :rtype: float
        """
        if len(self) <= 2:
            return 0.0

        n = len(self)
        m = self.top_node.count_nodes()

        def s_center_score():
            """
            Returns a normalized score, indicating roughly how many times
            intervals share s_center with other intervals. Output is full-scale
            from 0 to 1.
            :rtype: float
            """
            raw = n - m
            maximum = n - 1
            return raw / float(maximum)

        report = {
            "depth": self.top_node.depth_score(n, m),
            "s_center": s_center_score(),
        }
        cumulative = max(report.values())
        report["_cumulative"] = cumulative
        if full_report:
            return report
        return cumulative


    def __getitem__(self, index):
        """
        Returns a set of all intervals overlapping the given index or
        slice.

        Completes in O(k * log(n) + m) time, where:
          * n = size of the tree
          * m = number of matches
          * k = size of the search range (this is 1 for a point)
        :rtype: set of Interval
        """
        try:
            start, stop = index.start, index.stop
            if start is None:
                start = self.begin()
                if stop is None:
                    return set(self)
            if stop is None:
                stop = self.end()
            return self.overlap(start, stop)
        except AttributeError:
            return self.at(index)

    def __setitem__(self, index, value):
        """
        Adds a new interval to the tree. A shortcut for
        add(Interval(index.start, index.stop, value)).

        If an identical Interval object with equal range and data
        already exists, does nothing.

        Completes in O(log n) time.
        """
        self.addi(index.start, index.stop, value)

    def __delitem__(self, point):
        """
        Delete all items overlapping point.
        """
        self.remove_overlap(point)

    def __contains__(self, item):
        """
        Returns whether item exists as an Interval in the tree.
        This method only returns True for exact matches; for
        overlaps, see the overlaps() method.

        Completes in O(1) time.
        :rtype: bool
        """
        # Removed point-checking code; it might trick the user into
        # thinking that this is O(1), which point-checking isn't.
        #if isinstance(item, Interval):
        return item in self.all_intervals
        #else:
        #    return self.contains_point(item)

    def containsi(self, begin, end, data=None):
        """
        Shortcut for (Interval(begin, end, data) in tree).

        Completes in O(1) time.
        :rtype: bool
        """
        return Interval(begin, end, data) in self

    def __iter__(self):
        """
        Returns an iterator over all the intervals in the tree.

        Completes in O(1) time.
        :rtype: collections.Iterable[Interval]
        """
        return self.all_intervals.__iter__()
    iter = __iter__

    def __len__(self):
        """
        Returns how many intervals are in the tree.

        Completes in O(1) time.
        :rtype: int
        """
        return len(self.all_intervals)

    def __eq__(self, other):
        """
        Whether two IntervalTrees are equal.

        Completes in O(n) time if sizes are equal; O(1) time otherwise.
        :rtype: bool
        """
        return (
            isinstance(other, IntervalTree) and
            self.all_intervals == other.all_intervals
        )

    def __repr__(self):
        """
        :rtype: str
        """
        ivs = sorted(self)
        if not ivs:
            return "IntervalTree()"
        else:
            return "IntervalTree({0})".format(ivs)

    __str__ = __repr__

    def __reduce__(self):
        """
        For pickle-ing.
        :rtype: tuple
        """
        return IntervalTree, (sorted(self.all_intervals),)


# all intervals are [inclusive, exclusive)

