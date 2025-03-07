import schedule
import time
import smtplib


def welcome():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('srini.pit21@gmail.com', 'rjvm kavs rybv sqvp')
    server.sendmail('srini.pit21@gmail.com', 'rajesh.kambattan@gmail.com', 'good morning.test mail from python')
    server.quit()


schedule.every(5).seconds.do(welcome)

while True:
    schedule.run_pending()

    time.sleep(1)
