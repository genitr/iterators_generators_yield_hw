"""Class FlatIterator"""

class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.stopped = False
        self.main_cursor = 0
        self.nested_cursor = 0
        return self

    def __next__(self):
        if not self.stopped:
            while self.main_cursor < len(self.list_of_list):
                if self.nested_cursor < len(self.list_of_list[self.main_cursor]):
                    item = self.list_of_list[self.main_cursor][self.nested_cursor]
                    self.nested_cursor += 1
                    return item

                self.main_cursor += 1
                self.nested_cursor = 0

            self.stopped = True
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

