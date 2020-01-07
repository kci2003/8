import requests
e = True
cnt = 0
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
fRead = '699991.txt'
while e:
    r = requests.get(url + fRead)
    cnt += 1
    fRead = r.text
    print (r.text, cnt)
    if r.text.startswith('We'):
        txt = r.text
        e = False
print(txt)
#https://stepic.org/media/attachments/course67/3.6.3/699991.txt


