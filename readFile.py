#f = open(C:\temp\text1.txt)
#a=[]
with open ('C:\\temp\\text1.txt') as f:
    for line in f:
            line = line.strip()
           # print(line)

for i in range(len(line)):
    if 'A' <= line[i]:
        a = line[i]
        print(a,end='')
        n = '0'
    else:
        n = n + line[i]
        if i+1< len(line):
            if 'A' <= line[i+1]:
                print(a * (int(n)-1),end='')
        else:
            print(a*(int(n)-1), end='')

#print(a)