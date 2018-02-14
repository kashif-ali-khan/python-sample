# smtplib module send mail

import smtplib

TO = 'kashif.khan@tavant.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

sender = "kashif.7373@gmail.com"

server = smtplib.SMTP('BLRCSWEXV02.in.corp.tavant.', 25)


BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()