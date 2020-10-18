"""
<<<<<<< HEAD
Mode by grouping version 1.12.10.20
=======
Mode by grouping version 1.15.10.20
>>>>>>> Development

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

import statistics
import animation
import time

size = []  # Class Interval
freq = []  # Frequency

groups = []


def main():
<<<<<<< HEAD
    class_size_input()
    frequncy_input()
    table(size, freq)
    estimation_table()
    analyze()
    print(f"\nThe mode of given data is |> {mode()} <|.\n")
=======
   class_intervals()
   print("_______________________________________")
   print("Calculating mode ", end="")
   print("The mode is:", mode())
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
>>>>>>> Development


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


wheel = ('-', '/', '|', '\\')
@animation.wait(wheel)
def mode():
    time.sleep(3)
    z = round(l1() + ((f1() - f0()) / ((2 * f1()) - f0() - f2()) * h()), 2)
    return z


<<<<<<< HEAD
def table(intervals, freq):
    print("________________________________")
    print("             TABLE")
    print("________________________________")
    j = 0
    print("CLASS INTERVALS        FREQUENCY")
    for i in intervals:
        if len(i) <= 3:
            space = 2
        elif len(i) <= 4:
            space = 1
        else:
            space = 0
        print("   ", i, " " * (15 + space), freq[j])
        j += 1
    print("")


def estimation_table():
    global interv
    print("________________________________")
    print("           ESTIMATION")
    print("________________________________")
    print("\nGROUPS", " " * 2, "BIG. VALUES     CLASS \n")

    biggest_classes = [group1(size, freq), group2(size, freq), group3(size, freq),
                      group4(size, freq), group5(size, freq), group6(size, freq)]
    j = 0
    for i in biggest_classes:
        if j == 0:
            interv[j] = size[ms[j].index(i)]
            print("GROUP", j + 1, " " * 5, i, " " * (10 - len(str(i))), interv[j])
        elif j == 1:
            interv[j] = size[ms[j].index(i) * 2 + 1]
            print("GROUP", j + 1, " " * 5, i, " " * (10 - len(str(i))), interv[j])
        elif j == 2:
            interv[j] = size[ms[j].index(i) * 2 + 2]
            print("GROUP", j + 1, " " * 5, i, " " * (10 - len(str(i))), interv[j])
        else:
            interv[j] = size[ms[j].index(i) * 2 + 3]
            print("GROUP", j + 1, " " * 5, i, " " * (10 - len(str(i))), interv[j])
        j += 1


def analyze():
    global interv
    global modal

    print("_________________________________________")
    print("               ANALYSIS")
    print("_________________________________________")
    print("        BIGGEST CLASSES IN GROUPS\n")
    for i in range(len(interv)):
        if i == len(interv) - 1:
            print(interv[i])
        else:
            print(interv[i], end = ", ")
=======
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
>>>>>>> Development


def f1():
    f1 = freq[size.index(modal_class())]
    return f1


<<<<<<< HEAD
    print("_________________________________________")
=======
def f2():
    f2 = freq[size.index(modal_class()) + 1]
    return f2

>>>>>>> Development

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

<<<<<<< HEAD
    l1 = int(l1)

    if freq[size.index(modal)] == freq[-1]:
        f2 = 0
    else:
        f2 = freq[size.index(modal) + 1]

    if freq[size.index(modal)] == freq[0]:
        f0 = 0
    else:
        f0 = freq[size.index(modal) - 1]

    f1 = freq[size.index(modal)]
    
=======

def table():
    print("_______________________________________")
    print("                TABLE")
    print("---------------------------------------")
    print("CLASS INTERVALS               FREQUENCY")

>>>>>>> Development

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
