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
#print(m)
#print(len(m))

fiz = 0
mat = 0
rus = 0
for r in range(len(m)):
     avP = 0
     for c in range(1,len(m[r])):
         avP += int(m[r][c])
         #print(m[r][c])
     print(avP/(len(m[r])-1))
     fiz += int(m[r][1])
     mat += int(m[r][2])
     rus += int(m[r][3])
     #break
print(fiz/len(m),mat/len(m),rus/len(m))


