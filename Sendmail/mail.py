import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()

#we have to enable less secure apps
#https://myaccount.google.com/lesssecureapps
conn.login('yourmail@gmail.com','yourpassword')

conn.sendmail('yourmail@gmail.com','mailyouwanttosend@mail.com','Subject: Hi again!\n\nDear Friend,\n this is your first python mail.\n\n - Your Friend')

conn.quit()
