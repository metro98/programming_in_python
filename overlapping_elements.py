L1 = [10, 15, 6, 9, 12, 8, 4]
L2 = [14, 6, 19, 4, 7, 10, 11]

L3 = []

for i in L1:
    for j in L2:
        if i == j:
            L3.append(i)


print(L3)
