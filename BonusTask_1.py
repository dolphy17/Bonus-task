import smtplib

name1=['Spider-Man','Captain America','Thor','Iron Man']
name2=['The Hulk','Black Panther','Doctor Strange']

name3=name1+name2
print(name3)

name3.append('Dolphy Dhingra')
print(name3)

name3.remove('Doctor Strange')
print(name3)

Power_points = {'Spider-Man': 70 , 'Captain America': 70 ,
               'The Thor': 85,'Iron Man': 50,
               'The Hulk':70,'Black Panther': 66,
               'Dolphy Dhingra': 90}
print(Power_points)

Most_powerful_hero = max(Power_points,key = Power_points.get)
print(Most_powerful_hero)

# split first and last
firstname,lastname=Most_powerful_hero.split(" ")
print(firstname)
print(lastname)

fullname = lastname + " " +firstname
print(fullname)

hero_name = fullname.upper()

gmail_user = "dolphydhingra29@gmail.com"
gmail_pwd = "Dolphy@1048"
TO = ['cu.18bcs1048@gmail.com']
SUBJECT = "Bonus task by Dolphy Dhingra "
TEXT = "Testing...... sending mail using Gmail with the help of python..." + hero_name + " Link to your branch file here"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
for i in range(len(TO)):
    BODY = '\r\n'.join(['To: %s' % TO[i],
                        'From: %s' % gmail_user,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    server.sendmail(gmail_user, [TO[i]], BODY)
    print('email sent to '+ str(TO[i]))

server.close()





