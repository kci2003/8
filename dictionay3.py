n = int(0)
m = [[]]
with open ('C:\\temp\\text3.txt') as f:
    for line in f:
        a = line.lower().strip().split(';')
        if n == 0:
            m[0]+=a
        else:
            m.append(a)
        n += 1
# выше занесли текст в двумерную матрицу дальше будем обрабатывать двумерный список
print(m)

