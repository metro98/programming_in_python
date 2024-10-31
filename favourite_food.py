fav1 = ["pizza", "nuggets", "hotdog", "noodles", "pasta", "burger"]
fav2 = ["burger", "hotdog", "noodles", "pasta", "nuggets", "pizza"]

fav_index = []

for i in fav1:
    for j in fav2:
        if i == j:
            fav_index.append((fav1.index(i) + fav2.index(j)))
        else:
            continue

print(fav_index)
favourite_food = fav1[min(fav_index) - 1]
print(f"They ordered {favourite_food}")
