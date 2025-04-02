import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
try:
    n=int(input('no.of emails:'))
    l=[]
    for i in range(n):
        x=input('enter emails: ')
        temp=x.endswith("@gmail.com")

        if not temp:
            print("invalid email")
        else :
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
                    print("enter valid otp")
                    ccotp=int(input("Enter OTP: "))
                    if otp==ccotp:
                        print("verification succeeful")

                    else:
                        print("invalid otp")
        
except ValueError:
    print("enter  only integer")

except NameError:
    print("some error occured")

except :
    print("check internet connection")



    
            