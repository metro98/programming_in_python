def maximum(a, b, c):
    highest = 0 
    if a >= b:
        highest = a
    else:
        highest = b

    if c >= highest:
        highest = c

    return highest
print(maximum(5,2,1))