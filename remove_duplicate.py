List1 = [1,2,3,4,5,6,3,4,7,8,9,9,0,2]

List2 = []

for i in List1:
    if i not in List2:
        List2.append(i)
    else:
        continue

print(List2)
    