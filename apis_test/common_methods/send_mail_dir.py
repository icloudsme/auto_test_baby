#coding:utf8

"""
亮点
1、发送过的文件在日志文件夹会被删除掉；
2、发送邮件时，会显示发送文件的进度百分比；
"""

from smtplib import SMTP, quotedata, CRLF, SMTPDataError
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders
from sys import stderr, stdout
import os
import sys
import time

# 测试日志文件夹，要指到最后一个文件夹
logs_dir=os.path.join(sys.path[0],'logs/2017/03/26')

class ExtendedSMTP(SMTP):
    def data(self, msg):
        self.putcmd("data")
        (code, repl) = self.getreply()
        if self.debuglevel > 0: print >> stderr, "data:", (code, repl)
        if code != 354:
            raise SMTPDataError(code, repl)
        else:
            q = quotedata(msg)
            if q[-2:] != CRLF:
                q = q + CRLF
            q = q + "." + CRLF

            # begin modified send code
            chunk_size = 2048
            bytes_sent = 0

            while bytes_sent != len(q):
                chunk = q[bytes_sent:bytes_sent + chunk_size]
                self.send(chunk)
                bytes_sent += len(chunk)
                if hasattr(self, "callback"):
                    self.callback(bytes_sent, len(q))
            # end modified send code

            (code, msg) = self.getreply()
            if self.debuglevel > 0: print>> stderr, "data:", (code, msg)
            return (code, msg)


def callback(progress, total):
    percent = 100. * progress / total
    stdout.write('\r')
    stdout.write("%s bytes sent of %s [%2.0f%%]" % (progress, total, percent))
    stdout.flush()
    if percent >= 100: stdout.write('\n')


def sendmail(subject):
    MAIL_FROM = 'renyx@ppmiao.cn'
    MAIL_TO = ['506540345@qq.com']
    BAK_DIR = logs_dir

    msg = MIMEMultipart()
    msg['From'] = MAIL_FROM
    msg['Subject'] = subject

    nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msg.attach(MIMEText(nowtime+'\n'+'测试结果详见附件'))
    for filename in os.listdir(BAK_DIR):
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(os.path.join(BAK_DIR, filename), "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filename))
        msg.attach(part)

    try:
        smtp = ExtendedSMTP()
        smtp.callback = callback
        smtp.connect('smtp.exmail.qq.com', 25)
        smtp.login('renyx@ppmiao.cn', 'Zxm506540345')
        smtp.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
        smtp.close()
        os.system('rm -f %s/*' % BAK_DIR)
    except Exception, e:
        print e

#test执行
sendmail("测试结果")

#
# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         print 'Please specific a subject'
#         print 'Usage: send_files <MAIL_SUBJECT>'
#     else:
#         sendmail(sys.argv[1])


