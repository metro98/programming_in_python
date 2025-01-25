before = {"a": 10, "b": 20, "c": 30, "d":40}

def new_dict(after):
    new_dict = {}
    for k,v in after.items():
        new_dict[v] = k

    return new_dict

print(new_dict(before))
