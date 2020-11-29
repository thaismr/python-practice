""" This is a single line doc string """

from typing import Union


# Takes a float or int and returns a float or int
def number(num: Union[int, float]) -> Union[int, float]:
    return num + 1

