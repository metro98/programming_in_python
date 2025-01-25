def minimum(*val, low_limit = None):
    if low_limit == None:
        lowest = min(val)
        return lowest

    else:
        L = [x for x in val if x>= low_limit]
        return min(L)
    

print(minimum(2,4,1, low_limit= 3 ))