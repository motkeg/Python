import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


#fp = open(textfile, 'rb')
# Create a text/plain message

content=""" Hello,
               this is mail via Python script NO reply """

msg = MIMEText(content)
#fp.close()

# me == the sender's email address
# you == the recipient's email address

me  = "motiga@ac.sce.ac.il"
you = "motiga14@gmail.com"
 
msg['Subject'] = 'Test mail'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())

print "Send!"
s.quit()