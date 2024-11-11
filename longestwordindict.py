
dict1 = {
'piece': 'portion of an object or of material, produced by cutting',
'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
'area': 'a region or part of a town, a country, or the world',
'visit': 'go to see and spend time with (someone)',
'small': 'less than normal',
'with' : 'having or possessing'
}

dict2 = {}
for key,vlaue in dict1.items():
    dict2[key] = len(dict1[key])

print(dict2)

higher = 0
for i in dict2.values():
    if higher < i:
        higher = i


lower = higher
for j in dict2.values():
    if lower > j:
        lower = j



longest_keys = [keys for keys,values in dict2.items() if values == higher]
shortest_keys = [keys for keys,values in dict2.items() if values == lower]

for i in dict1.keys():
    if i == longest_keys[0]:
        print(f"{i} : {dict1[i]}")

for j in dict1.keys():
    if j == shortest_keys[0]:
        print(f"{j} : {dict1[j]}")


