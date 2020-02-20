#February 19, 2020

from typing import List

def first_last_6(list: List[int]) -> bool:
    isTrue = False
    if list[0] == 6 or list[-1] == 6:
        isTrue = True
    return isTrue
