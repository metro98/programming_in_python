Scores = [200, 456, 300, 100, 234, 678]

def sum_zero(some_list):
    sum = 0
    for i in some_list:
        if i % 10 == 0:
            sum += i
        else:
            continue

    return sum


print(sum_zero(Scores))