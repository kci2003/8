def f(x):
    return x*2
n = int(input())
#n = 3
a = []
for i in range(n):
    a.append(input())
#print(a)
dict={}
for j in a:
   if j not in dict:
        dict[j] = f(j)
        #print(dict[j])
for k in a:
     print(k,dict[k])

#    print (f(j))


