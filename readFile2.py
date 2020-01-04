line1=[]
with open ('C:\\temp\\text2.txt') as f:
    for line in f:
            line1+=line.lower().strip().split()
a = int(line1.count(line1[0]))
w = line1[0]
for i in line1:
    if a < int(line1.count(i)):
        a = int(line1.count(i))
        w = i
print(w,a)

