### email modules ###
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

### Function to send the email ###
def send_an_email():
	toaddr = 'coeaikkm@cet.edu.in'    
	me = 'priyankapattanaik2013@gmail.com'
	subject="File sending" 
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = me
	msg['To'] = toaddr
	msg.preamble = "test " 	
	#msg.attach(MIMEText(text))
	
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open("dataout.csv", "rb").read())
	encoders.encode_base64(part)	
	part.add_header('Content-Disposition', 'attachment; filename="dataout.csv"')
	msg.attach(part)

	try:
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()	
		s.ehlo()
		s.login(user = 'priyankapattanaik2013@gmail.com', password = 'password')
		#s.send_message(msg)
		s.sendmail(me, toaddr, msg.as_string())
		s.quit()
    #except:
    #   print ("Error: unable to send email")
	except SMTPException as error:
		print ("Error")

send_an_email()
	