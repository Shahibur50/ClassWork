import statistics  # Importing/adding a module which gives us extra functionality.


size = ["0-5", "5-10", "10-15", "15-20", "20-25", "25-30", "30-35", "35-40"]  # Class Interval
freq = [3, 7, 15, 30, 20, 10, 5, 15]  # Frequency
 
print(f"Class interval: {size}")
print(f"Frequency: {freq}\n")

print("-" * 50)
print("I Group")

m0 = []  # Creating an array/list where the values can be stored.

for i in range(len(size)):
    group0 = freq[i]
    m0.append(group0)

mode0 = max(m0)  # Getting the biggest value from the array/list.
m0_index = m0.index(mode0)  # Getting index number related to the frequency of rescpective class.

print(m0)
print("\nBiggest class interval for this group:", big_size0 := size[m0_index])


print("-" * 50)
print("II Group")

m1 = []

for i in range(0, len(size) - 1, 2):
    group1 = freq[i] + freq[i + 1]
    m1.append(group1)

mode1 = max(m1)
m1_index = m1.index(mode1)

print(m1)
print("\nBiggest class interval for this group:", big_size1 := size[m1_index * 2 + 1])


print("-" * 50)
print("III Group")

m2 = []

for i in range(1, len(size) - 1, 2):
    group2 = freq[i] + freq[i + 1]
    m2.append(group2)

mode2 = max(m2)
m2_index = m2.index(mode2)

print(m2)
print("\nBiggest class interval for this group:", big_size2 := size[m2_index * 2 + 2])


print("-" * 50)
print("IV Group")
m3 = []

for i in range(0, len(size) - 2, 3):
    group3 = freq[i] + freq[i + 1] + freq[i + 2]
    m3.append(group3)

mode3 = max(m3)
m3_index = m3.index(mode3)

print(m3)
print("\nBiggest class interval for this group:", big_size3 := size[m3_index * 2 + 3])


print("-" * 50)
print("V Group")
m4 = []

for i in range(1, len(size) - 2, 3):
    group4 = freq[i] + freq[i + 1] + freq[i + 2]
    m4.append(group4)

mode4 = max(m4)
m4_index = m4.index(mode4)

print(m4)
print("\nBiggest class interval for this group:", big_size4 := size[m4_index * 2 + 3])


print("-" * 50)
print("VI Group")
m5 = []

for i in range(2, len(size) - 2 , 3):
    group5 = freq[i] + freq[i + 1] + freq[i + 2]
    m5.append(group5)

mode5 = max(m5)
m5_index = m5.index(mode5)

print(m5)
print("\nBiggest class interval for this group:", big_size5 := size[m5_index * 2 + 3])
print("-" * 50)

biggest_sizes = [big_size0, big_size1, big_size2, big_size3, big_size4, big_size5]

print(f"\nBiggest class intervals occuring in all of the groups are {biggest_sizes}.\n")

modal = statistics.mode(biggest_sizes)
print(f"Therefore the modal class of given data is {modal}.")

# Setting up the values required for calculating the mode of the modal class.

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

Z = l1 + ((f1 - f0) / (2 * f1 - f0 - f2) * h)
print(f"\nThe mode of given data is {Z}.")
print("\nCalculations Done.")