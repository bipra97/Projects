import smtplib

FROM = 'bm9.2.1997@gmail.com'
PSWD = 'biprajit1983'

TO = 'biprajit1983@gmail.com'

#Subject and header
SUB = 'Subject: Alert for Testing \n'
header = 'To:' + TO + '\n' + 'From: ' + FROM + '\n' + SUB

#Message
body = """
MAY DAY! MAY DAY!! MAY DAY!!!
Your webserver for shaikhu.com is DOWN."""
message = header + body
#Define function to send email
def sendalert(msg):

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()

    smtpObj.starttls()
    smtpObj.login(FROM, PSWD)

    smtpObj.sendmail(FROM,TO,msg)
    smtpObj.quit()
if __name__ == '__main__':
    sendalert(message)