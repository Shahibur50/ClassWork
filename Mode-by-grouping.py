"""
Mode by grouping version 1.15.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

import statistics
import time

size = []  # Class Interval
freq = []  # Frequency

groups = []


def main():
    class_intervals()
    print("_______________________________________")
    print("           MODE (Z) =", mode())
    print("---------------------------------------")


def class_intervals():
    n = int(input("Enter the number of class intervals: "))
    lower = input("Enter the lower limit of first class: ")
    upper = input("Enter the upper limit of first class: ")
    diff = int(upper) - int(lower)
    table()
    for i in range(n):
        lower = str(lower)
        upper = str(upper)
        if len(lower + upper)  + 1 <= 3:
            space = 2
        elif len(lower + upper) + 1 <= 4:
            space = 1
        else:
            space = 0

        print("    ", lower + '-' + upper, " " * (23 + space), end="")
        frequency()
        size.append(lower + '-' + upper)
        lower = int(lower) + diff
        upper = int(upper) + diff


def frequency():
    value = int(input())
    freq.append(value)


def modal_class():
    analyzer()
    modal = statistics.mode(groups)
    return modal


def analyzer():
    group1()
    group2() 
    group3() 
    group4() 
    group5() 
    group6()


def mode():
    z = round(l1() + ((f1() - f0()) / ((2 * f1()) - f0() - f2()) * h()), 2)
    return z


def l1():
    l1 = ""
    for i in modal_class():
        if i == "-":
            break
        else:
            l1 += i
    l1 = int(l1)
    return l1


def f0():
    f0 = freq[size.index(modal_class()) - 1]
    return f0


def f1():
    f1 = freq[size.index(modal_class())]
    return f1


def f2():
    f2 = freq[size.index(modal_class()) + 1]
    return f2


def h():
    h1 = l1()
    h2 = ""
    for i in modal_class()[::-1]:
        if i == "-":
            break
        else:
            h2 = i + h2
    h2 = int(h2)
    h = h2 - h1
    return h


def table():
    print("_______________________________________")
    print("                TABLE")
    print("---------------------------------------")
    print("CLASS INTERVALS               FREQUENCY")


def group1():
    m1 = []
    for i in range(len(size)):
        group = freq[i]
        m1.append(group)

    mode = max(m1)
    groups.append(size[freq.index(mode)])
    return mode


def group2():
    m2 = []
    for i in range(0, len(size) - 1, 2):
        group = freq[i] + freq[i + 1]
        m2.append(group)

    mode = max(m2)
    groups.append(size[m2.index(mode) * 2])
    groups.append(size[m2.index(mode) * 2 + 1])
    return mode


def group3():
    m3 = []
    for i in range(1, len(size) - 1, 2):
        group = freq[i] + freq[i + 1]
        m3.append(group)

    mode = max(m3)
    groups.append(size[m3.index(mode) * 2 + 1])
    groups.append(size[m3.index(mode) * 2 + 2])
    return mode


def group4():
    m4 = []
    for i in range(0, len(size) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m4.append(group)

    mode = max(m4)
    groups.append(size[m4.index(mode) * 3])
    groups.append(size[m4.index(mode) * 3 + 1])
    groups.append(size[m4.index(mode) * 3 + 2])
    return mode


def group5():
    m5 = []
    for i in range(1, len(size) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m5.append(group)

    mode = max(m5)
    groups.append(size[m5.index(mode) * 3 + 1])
    groups.append(size[m5.index(mode) * 3 + 2])
    groups.append(size[m5.index(mode) * 3 + 3])
    return mode


def group6():
    m6 = []
    for i in range(2, len(size) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m6.append(group)

    mode = max(m6)
    groups.append(size[m6.index(mode) * 3 + 2])
    groups.append(size[m6.index(mode) * 3 + 3])
    groups.append(size[m6.index(mode) * 3 + 4])
    return mode


if __name__ == "__main__":
    main()
