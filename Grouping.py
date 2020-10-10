size = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
frequency = [2, 3, 6, 12, 20, 24, 25, 7, 5, 3, 1]

print(f"Sizes: {size}")
print(f"Frequency: {frequency}\n")

print("-------------------------------------")
print("I Group")
m0 = []

for i in range(len(size)):
    group0 = frequency[i]
    m0.append(group0)

mode0 = max(m0)
m0_index = m0.index(mode0)

print(m0)
print("Biggest size for this group:", big_size0 := size[m0_index])


print("-------------------------------------")
print("II Group")
m1 = []

for i in range(0, len(size) - 1, 2):
    group1 = frequency[i] + frequency[i + 1] 
    m1.append(group1)

mode1 = max(m1)
m1_index = m1.index(mode1)

print(m1)
print("Biggest size for this group:", big_size1 := size[m1_index * 2 + 1])


print("-------------------------------------")
print("III Group")
m2 = []

for i in range(1, len(size) - 1, 2):
    group2 = frequency[i] + frequency[i + 1] 
    m2.append(group2)

mode2 = max(m2)
m2_index = m2.index(mode2)

print(m2)
print("Biggest size for this group:", big_size2 := size[m2_index * 2 + 2])


print("-------------------------------------")
print("IV Group")
m3 = []

for i in range(0, len(size) - 2, 3):
    group3 = frequency[i] + frequency[i + 1] + frequency[i + 2]
    m3.append(group3)

mode3 = max(m3)
m3_index = m3.index(mode3)

print(m3)
print("Biggest size for this group:", big_size3 := size[m3_index * 2 + 3])


print("-------------------------------------")
print("V Group")
m4 = []

for i in range(1, len(size) - 2, 3):
    group4 = frequency[i] + frequency[i + 1] + frequency[i + 2]
    m4.append(group4)

mode4 = max(m4)
m4_index = m4.index(mode4)

print(m4)
print("Biggest size for this group:", big_size4 := size[m4_index * 2 + 3])


print("-------------------------------------")
print("VI Group")
m5 = []

for i in range(2, len(size) - 2, 3):
    group5 = frequency[i] + frequency[i + 1] + frequency[i + 2]
    m5.append(group5)

mode5 = max(m5)
m5_index = m5.index(mode5)

print(m5)
print("Biggest size for this group:", big_size5 := size[m5_index * 2 + 3])


biggest_sizes = [big_size0, big_size1, big_size2, big_size3, big_size4, big_size5]

print(f"\nBiggest sizes occuring in all of the groups are {biggest_sizes}\n")
