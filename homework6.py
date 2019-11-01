import smtplib
help(smtplib)

smtp_object  = smtplib.SMTP('smtp.ukr.net', 2525)
smtp_object.starttls()
smtp_object.login('fredmail@ukr.net', 'russell87')
help(smtp_object.sendmail)
smtp_object.sendmail(from_addr='fredmail@ukr.net',
                     to_addrs='mr.freddy2000@gmail.com',
                     msg='Dummy email blast using Python!')

smtp_object.sendmail(from_addr='fredmail@ukr.net',
                     to_addrs='mr.freddy2000@gmail.com',
                     msg='Dummy email blast using Python')
smtp_object.quit()
#
# import smtplib
# help(smtplib)
#
# smtp_object  = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_object.starttls()
# smtp_object.login('mr.freddy2000@gmail.com', 'snoopduck')
# help(smtp_object.sendmail)
# smtp_object.sendmail(from_addr='mr.freddy2000@gmail.com',
#                      to_addrs='fredmail@ukr.net',
#                      msg='Dummy email blast using Python!')
#
# smtp_object.sendmail(from_addr='mr.freddy2000@gmail.com',
#                      to_addrs='fredmail@ukr.net',
#                      msg='Dummy email blast using Python')
# smtp_object.quit()