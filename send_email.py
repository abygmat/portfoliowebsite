import smtplib,ssl



host = "smtp.gmail.com"
port =465

password="ixtj jfxy urbu vcww"
username = "abygeorgemathew007@gmail.com"
reciever = "abygeorgemathew007@gmail.com"
context = ssl.create_default_context()
message="""
Hi !
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,reciever,message )
