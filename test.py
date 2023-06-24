# import time
# start_time = time.time()
# x = input("enter the some word ")
# #main()
# print(x,"--- %s seconds ---" % (time.time() - start_time))


# from datetime import datetime
# start_time = datetime.now()
# # do your work here
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))

# buket_name = 'sagemkaker-demo9876'
# s3 = boto3.resource('s3')
# try:
#     if my_region == 'us-east1':
#         s3.create_buket(Bucket=buket_name)
#     else:
#         s3.create_buket(Buket=buket_name, CreateBucketConfiguration={ 'LocationConstratint': my_region })
#     print('S3 buket create successfully')
# except Exception as e:
#     print('S3 error: ',e)

"""for sent mail"""
# import smtplib
# from email.mime.text import MIMEText

# body = "This is a test email. How are you"
# msg = MIMEText(body)
# msg["From"] = "hivecenter@cognizantgoc.com"
# msg["To"] = "hivecenter@cognizantgoc.com"
# msg['Subject'] = "Hello"
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login("hivecenter@cognizantgoc.com", "H!v3C3nT3rI&0")
# server.send_message(msg)
# print("Mail sent")
# server.quit()

a=int(input("ENTER A FIRST NUMBER "))

b=int(input("ENTER THE SECOND NUMBER "))

c=a*b

for i in range(1,c+1):
    if(i%a==0 and i%b==0):
        print("THE LCM IS = ",i)
        break