"""
Largest smallest num version 1.1.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

def big(List):
    biggest = List[0]
    for i in List:
        if i > biggest:
            biggest = i
    return biggest

def small(List):
    smallest = List[0]
    for i in List:
        if i < smallest:
            smallest = i
    return smallest

List = [21, 34, 56, 11, 12, 78, 92, 101, 53, 14, 9, 45, 33, 28]

print(f"\nThe biggest number in the list is {big(List)} and the smallest numer in the list is {small(List)}.\n")
