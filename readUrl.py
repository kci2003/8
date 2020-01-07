import requests

url = ''
with open ('C:\\temp\\text5.txt') as f:
    for line in f:
            line = line.strip()
            #print(line)
url = str(line)
print(url)
r = requests.get(url)
#print(r.text.splitlines().count('/n'))
n = 0
for i in r.text.splitlines():
    n += 1
print(n)
