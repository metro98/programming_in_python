L1 = ["A", "B", "C", "D", "E", "A", "B", "E", "B", "D", "B", "E"]

result = []

for i in L1:
    if i not in result:
        result.append(i)
        count = L1.count(i)
        result.append(count)

print(result)    
    