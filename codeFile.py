s,sCode,shif,deShift = [],[],[],[]
s =input()
#s = 'abcd'
# sCode = '*d%#'
# shif = 'abacabadaba'
# deShift = '#*%*d*%'
sCode = input()
shif = input()
deShift = input()
for k in shif:
    for i in s:
        if k==i:
            print(sCode[s.index(i)],end='')
print()
for k in deShift:
    for i in sCode:
        if k==i:
            print(s[sCode.index(i)],end='')