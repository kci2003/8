#m = set()
objects = [1, 2, 1, 2, 3]
m = []
m.append(objects[0])

#print(m[0])
for obj in objects: # доступная переменная objects
    cnt = 0
    for i in m:
        if obj is i:
            cnt =1
    if cnt == 0:
        m.append(obj)
print(len(m))
