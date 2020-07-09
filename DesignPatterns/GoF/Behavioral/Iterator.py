import typing
from typing import Union, List

Number = Union[int]


class NumberIterator(object):

    def __init__(self, container: List[Number]):
        self.__container = container
        self.position = 0

    def __is_odd(self, number):
        return number % 2 == 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self.__container[self.position]
            self.position += 1
            while not self.__is_odd(value):
                value = self.__container[self.position]
                self.position += 1
        except IndexError:
            raise StopIteration()
        return value


if __name__ == "__main__":
    a = [1, 2, 3, 4, 6, 5]

    ni = NumberIterator(a)

    for number in ni:
        print(number)
