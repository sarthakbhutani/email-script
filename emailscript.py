import os
import email
import smtplib
import config
# message/email details
my_email = config.email
my_passw = config.password
recipients = ['email1@someemail.com', 'email2@someemail.com']
subject = 'This is the subject of the email'
message = 'This is the main body of the email.'

# build the message
msg = email.mime.multipart.MIMEMultipart()
msg['From'] = my_email
msg['To'] = ', '.join(recipients)
msg['Date'] = email.utils.formatdate(localtime=True)
msg['Subject'] = subject
msg.attach(email.mime.text.MIMEText(message))

# send the message
server = smtplib.SMTP('smtp.gmail.com', 587) #by default, configured to sendmail via the host's gmail account
server.ehlo()
server.starttls()
server.login(my_email, my_passw)
server.sendmail(my_email, recipients, msg.as_string())