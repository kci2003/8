def modify_list(l):
    a = []
    for i in l:
         if i%2==0:
             a.append(i//2)
    print(a)
    del l[:]
    l += a

l=[1,2,3,4,8]
modify_list(l)
print(l)