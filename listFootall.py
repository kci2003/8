n = int(input())
#n = 3
a = []
m = [[]]
s = set()
for i in range(n):
    a = input().split(';')
    s.add(a[0])
    s.add(a[2])
    if i == int(0):
        m[0] += a
    else:
        m.append(a)
#print(m)
team = m[0][0]
for j in s:
    cnt = 0
    v = 0
    nixt = 0
    p = 0
    for r in range(n):
        #print(j,end ='')
        cnt += m[r].count(j)
        if m[r][0]==j:
            if m[r][1]>m[r][3]:
                v += 1
            elif m[r][1]<m[r][3]:
                p +=1
            else:
                nixt +=1
        else:
            if m[r][2] == j:
                if m[r][1] < m[r][3]:
                    v += 1
                elif m[r][1] > m[r][3]:
                    p += 1
                else:
                    nixt += 1

    print(j+':'+str(cnt),v,nixt,p,(v*3+nixt))


