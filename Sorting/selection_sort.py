a = [12, 34, 45, 56, 98, 14, 51]

# Traverse array elements
for i in range(len(a)):

    lowest = i
    for index in range(i + 1, len(a)):
        if a[lowest] > a[index]:
            lowest = index

# Swapping the elements
    a[i], a[lowest] = a[lowest], a[i]

# Printing elements
print("Sorted array", a)