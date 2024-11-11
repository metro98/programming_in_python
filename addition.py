L1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]

L2 = [[5,6,7,8], [5,6,7,8], [5,6,7,8]]

L3 = []

for i in range(3):
    S = []
    for j in range(3):
        result = L1[i][j] + L2[i][j]
        S.append(result)

    L3.append(S)

print(L3)