#coding=gbk  
import smtplib, mimetypes  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage  
  
msg = MIMEMultipart()  
msg['From'] = 'from-zhaoyong@data58.cn' 
msg['To'] = 'to--zhaoyong@hylon.com.cn'  
msg['Subject'] = 'email for tesing'  
  
#添加邮件内容  
txt = MIMEText("这是邮件内容~~")  
msg.attach(txt)  
  
#添加二进制附件  
fileName = r'f:/attach1.txt'  
ctype, encoding = mimetypes.guess_type(fileName)  
if ctype is None or encoding is not None:  
    ctype = 'application/octet-stream'  
maintype, subtype = ctype.split('/', 1)  
att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype = subtype)  
att1.add_header('Content-Disposition', 'attachment', filename = fileName)  
msg.attach(att1)  
  
#发送邮件  
smtp = smtplib.SMTP()  
print "begin to connect"
smtp.connect('smtp.qq.com:465')  
smtp.login('495373856@qq.com', 'Shu606')  
smtp.sendmail('495373856@qq.com', 'zhaoyong@hylom.com.cn', msg.as_string())  
smtp.quit()  
print '邮件发送成功--20180225'