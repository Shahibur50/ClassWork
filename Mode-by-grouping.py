"""
Mode by grouping version 1.7.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

import statistics
import time

m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
m6 = []
ms = [m1, m2, m3, m4, m5, m6]

interv = ['', '', '', '', '', '']
modal = 0


def main():
    print("Starting up", end="")
    for i in range(3):
        print('.', end="")
        time.sleep(1)
    print("")
    
    table(size, freq)
    estimation_table()
    analyze()
    
    print("_________________________________________")
    print("Calculating the mode of given data...")
    time.sleep(1)
    print("Please wait", end="")
    for i in range(3):
        print('.', end="")
        time.sleep(1)
    print("")
    print(f"\nThe mode of given data is |> {mode()} <|.\n")


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
            print("GROUP", j + 1, " " * 5, i, " " * 8, interv[j])
        elif j == 1:
            interv[j] = size[ms[j].index(i) * 2 + 1]
            print("GROUP", j + 1, " " * 5, i, " " * 8, interv[j])
        elif j == 2:
            interv[j] = size[ms[j].index(i) * 2 + 2]
            print("GROUP", j + 1, " " * 5, i, " " * 8, interv[j])
        else:
            interv[j] = size[ms[j].index(i) * 2 + 3]
            print("GROUP", j + 1, " " * 5, i, " " * 8, interv[j])
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

    modal = statistics.mode(interv)
    print(f"\n=> The modal class after analyzing the data is {modal}.")


def mode():
    global modal
    global freq

    freq.append(0)
    freq.insert(freq[0], 0)

    l1 = ""
    h2 = ""
    for i in modal:
        if i == "-":
            break
        else:
            l1 += i
    h1 = l1

    for i in range(len(modal)):
        i += 1
        if modal[-i] == "-":
            break
        else:
            h2 += modal[-i]

    h2 = int(h2[::-1])
    h1 = int(h1)
    h = h2 - h1

    l1 = int(l1)

    f1 = freq[size.index(modal)]

    f0 = freq[size.index(modal) - 1]

    f2 = freq[size.index(modal) + 1]

    # Calculating mode.

    z = l1 + ((f1 - f0) / (2 * f1 - f0 - f2) * h)
    return z

def group1(intervals, freq):
    global m1
    for i in range(len(intervals)):
        group = freq[i]
        m1.append(group)

    mode = max(m1)
    return mode


def group2(intervals, freq):
    global m2
    for i in range(0, len(intervals) - 1, 2):
        group = freq[i] + freq[i + 1]
        m2.append(group)

    mode = max(m2)
    return mode


def group3(intervals, freq):
    global m3
    for i in range(1, len(intervals) - 1, 2):
        group = freq[i] + freq[i + 1]
        m3.append(group)

    mode = max(m3)
    return mode


def group4(intervals, freq):
    global m4
    for i in range(0, len(intervals) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m4.append(group)

    mode = max(m4)
    return mode


def group5(intervals, freq):
    global m5
    for i in range(1, len(intervals) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m5.append(group)

    mode = max(m5)
    return mode


def group6(intervals, freq):
    global m6
    for i in range(2, len(intervals) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m6.append(group)

    mode = max(m6)
    return mode


if __name__ == "__main__":
    size = ["0-5", "5-10", "10-15", "15-20", "20-25", "25-30", "30-35", '35-40', '40-45', '45-50', '50-55', '55-60']  # Class Interval
    freq = [3, 7, 15, 30, 20, 10, 5, 5, 3, 1, 6, 50]  # Frequency
    main()
