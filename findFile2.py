import os
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

a=[]
for top, dirs, files in os.walk('c:\\my\\фото\\'):
    for nm in files:
        if nm.endswith('.jpg'):
            a.append(os.path.join(top, nm))
#print(len(a))
r = random.randrange(0, len(a), 1)
#print(r)
os.system(a[r])
