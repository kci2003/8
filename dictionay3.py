n = int(0)
a = []
m = [[]]
with open ('C:\\temp\\text3.txt') as f:
    for line in f:
        a = line.lower().strip().split(';')
        print(a)
        #m[[n]]+ = a
        n += 1
print(m)
print(n)
