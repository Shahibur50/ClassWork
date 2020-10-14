"""
Largest 3rd num version 1.4.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

def main():
    print(f"The 3rd biggest number in the given list is {big3(List)}.")


def big(List):
    biggest = List[0]
    for i in List:
        if i > biggest:
            biggest = i
    return biggest


def big2(List):
    biggest2 = List[0]
    for i in List:
        if i > biggest2 and i < big(List):
            biggest2 = i
    return biggest2


def big3(List):
    biggest3 = List[0]
    for i in List:
        if i > biggest3 and i < big2(List):
            biggest3 = i
    return biggest3


if __name__ == "__main__":
    List =  [21, 34, 56, 11, 12, 78, 92, 101, 53, 14, 9, 45, 33, 28]
    main()