import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
n=int(input('no.ok emails:'))
l=[]
for i in range(n):
    x=input('enter emails: ')
    l.append(x)

for i in l:
    otp = random.randint(1111,9999)
    msg = MIMEMultipart()
    body=f"OTP for verification {otp}"
    msg["From"] = "subhashbathala03@gmail.com"
    msg["TO"] = i
    msg["Subject"]="OTP For Validation"
    msg.attach(MIMEText(body,"plain"))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("subhashbathala03@gmail.com","guru rrlq prsf uhhy")
    server.send_message(msg)
    server.quit()

    cotp=int(input("Enter OTP: "))

    if otp==cotp:
        print("validation Success")

    else:
        print("invalid OTP")