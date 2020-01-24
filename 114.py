#1005425
# import re
# a = []
# sum = 0
# regex = '<td>\s(.*)\s</td>'
# with open ('C:\\temp\\3.html') as f:
#     for line in f:
#             line = line.strip()
#            #print(line)
#             a += (re.findall(regex, line))
# for i in a:
#      sum = sum + int(i)
# print(sum)
from bs4 import BeautifulSoup
from urllib.request import urlopen
sum = 0
html = urlopen("https://stepik.org/media/attachments/lesson/209723/3.html").read().decode('utf-8')
s = str(html)
#print('1111')
soup = BeautifulSoup(s,'html.parser')
#print(soup.find_all('td'))
for tag in soup.find_all("td"):
        #print("{0}: {1}".format(tag.name, tag.text))
        sum = sum + int(tag.text)
print(sum)
#print(soup.prettify())
#print(list(soup.children))
# pos = s.find('<a href=')
