a = ['aaa','abc','aa','ac','abc','bcd','a']
a = [s  for s in input().upper().split()]
s = set()
for i in a:
    s.add(i)
for j in s:
    print(j,a.count(j))
print (a)
print (s)