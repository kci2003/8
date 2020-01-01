def update_dictionary(d,key,value):
    if d.get(key):
        d[key].append(value)
    else:
       if d.get(key * 2):
            d[key * 2].append(value)
       else:
           d[key * 2] = [value]
d = {}
print(update_dictionary(d, 1, -1))
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}