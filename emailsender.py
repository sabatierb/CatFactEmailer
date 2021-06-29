#Import modules (smtplib used to connect to email servers to send emails)
import smtplib, random, requests, time, datetime
#-----email modules-----#
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #<-- allows one variable ("msg") to contain all parts of email

#-----get image urls-----# Definitly use API here
'''def getImage():
    imageUrls = []
    g = open('images.txt', 'r')
    for line in g:
        imageUrls.append(line)
        url = random.choice(imageUrls)
    return url'''

#---get local time on machine---#
def getTime():
    return time.strftime("%H:%M", time.localtime())

def getDay():
  return (datetime.datetime.now()).strftime("%A")

#-----get image urls using API for "Article"-----#
def getImage():
    url = "https://api.thecatapi.com/v1/images/search?size=full"
    headers = {
    'Content-Type': 'application/json',
    'x-api-key': '7da13f64-25c1-48f3-8992-c65ec347c0f0'
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    image_url =  data[0]['url']
    return image_url


#-----cat facts from text file for "Article"-----# Maybe use API here
def getFact():
    catFacts = []
    f = open('catFacts.txt', 'r')
    for line in f:
        catFacts.append(line)
    fact = random.choice(catFacts)
    return fact

#----cat jokes from text file for the "announcements"-----#
def getJoke():
    catJokes = []
    g = open('jokes.txt', 'r')
    for line in g:
        catJokes.append(line)
    joke = random.choice(catJokes)
    return joke

#------Splits user list into induvidual lists for each frequency and content type
#1->Article   2->Announcement | Weekly can only have announcements digest
def getList(frequency, content):
    daily_users_1 = []
    daily_users_2 = []
    weekly_users_1 = []
    #print(user_list)
    #a = input()
    for row in user_list:
        #print(row)
        for column in row:
            #print(column)
            if column == '1' and row[1] == 'daily':
                daily_users_1.append(row[0])
            if column == '2' and row[1] == 'daily':
                daily_users_2.append(row[0])
            if column == '1' and row[1] == 'weekly':
                weekly_users_1.append(row[0])


    if frequency == 'daily' and content == '1':
        #print("\n HERRE\n")
        #print(daily_users_1)
        return daily_users_1
    
    if frequency == 'daily' and content == '2':
        return daily_users_2
    if frequency == 'weekly' and content == '1':
        return weekly_users_1
    
    #g = input("STOP")

#-----send emails-----#
def sendEmail():
    msg.attach(MIMEText(body,'html'))#Formats body so email outputs the HTML not just the code as text
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)#Setting server details
    server.starttls()
    server.login('autoemail096@gmail.com','123456789*MuO')#Logging into gmail smtp server
    server.sendmail(email_user,email_recipents,text)#Sending email
    print("Sending emails to: ",email_recipents, "Type:",email_type, "Timestamp:",email_timestamp)
    server.quit()#Cutting connection to SMTP server

#------Userlist and storage management--------#
def readList():
  txtfile = open("userList.txt", "r")
  lines = txtfile.readlines()
  txtfile.close()
  #print(lines)
  i=0
  while i <= (len(lines)-3):
    tempoary_user_list = []
    tempoary_user_list.append(lines[i].strip('\n'))
    tempoary_user_list.append(lines[i+1].strip('\n'))
    tempoary_user_list.append(lines[i+2].strip('\n'))
    i+=3
  #print(tempoary_user_list)
    user_list.append(tempoary_user_list)
  #print(user_list)

def writeList():
  txtfile = open("userList.txt", "w")
  for row in user_list:
    for column in row:
      txtfile.write(column + "\n")
  txtfile.close()

def displayList():
  for element in user_list:
    print(element)

def addUser():
  #Users can have ......
  user_add = []
  print("Enter details(email, frequency, content)")
  for i in range (3):#Check format
    user_add.append(input())
  #print(user_add)
  user_list.append(user_add)
  #print(user_list)

def removeUser():
  remove = input("Whats email of user to remove\n")
  for element in user_list:
    if remove in element:
      user_list.remove(element)
  #print(user_list)



#---Big user list contains all users with preferences---#
user_list = []

#for testing
#user_list = [['bensab63@gmail.com', 'daily', 2],
            # ['bensab62@gmail.com', 'daily', 2],
             #['bensab63+python@gmail.com', 'daily', 2],
            # ['bensab62+article@gmail.com', 'weekly', 1]]


#-----sender email address,password,recipents,subject,body-----#
email_user = 'autoemail096@gmail.com'
email_password = '123456789*MuO'

test_time = "12:00"
test_day = "Wednesday"
start_time = getTime()
announcement_history = []

#-----MENU----#
run = False
while not run:
    a = input("1.Add User 2.Remove User 3.Run\n")
    if a == '1':
        readList()#Read list from file to memory
        addUser()#Add user to userlist in memory
        writeList()#Save userlist from memory to file
        
        print("\nCurrent Users in File\n")
        displayList()#Display user list from memory
        user_list = []
    if a == '2':
        readList()#Read userlist from file into memory
        print("\nCurrent Users\n")
        displayList()
        #print(user_list)
        removeUser()#Remove user from list in memory
        writeList()#Save list from memory to file
        print("\nNew User List\n")
        displayList()#Display userlist from file
        user_list=[]
    if a=='3':
        readList()#Read file into memory
        run = True#Run email engine

while run:
    email_recipents = []
    subject = ''
    body = ''
    email_timestamp = getTime()
    send_email = False
    
    #---Daily Article----# ****Replace "test_time" with getTime()*****
    if test_time == "12:00" or test_time == "11:59":#Checks if time is 12PM, to send 1 "Article" email once a day
        send_email = True#Boolean to control if sendEmail function is ran
        email_type = "Article"#Store email type for nice console ouput
        print("\nGetting Recipents\n")
        email_recipents = getList('daily', '1')#Stores list of users who want to recive Daily Articles
        print('\n',email_recipents,'\n')
        i = input()
        subject = 'Cat Fact of The Day!'
        body = """<html>
                <body>
                    <h1><strong> Cat Fact of the Day!</strong></h1>
                    <img src="{}" height=500>
                    <br><br>
                    <h2>{}<h2>
                    <br><br>
                    <h4>{}<h4>
                </body>
            </html>
            """.format(getImage(), getFact(), email_timestamp)
    
    #----Daily Announcement----#
    if test_time == "13:00":#Send announcment email to correct recipents at 1PM everyday
        send_email = True
        email_type = "Announcement"
        email_recipents = getList('daily', '2')#Stores list of users who want to recive Daily Announcements
        subject = 'ANNOUNCEMENT!!!!!'
        joke = getJoke()
        announcement_history.append(getDay())
        announcement_history.append(joke)
        announcement_history.append("")
        body = "{}\n{}".format(joke,email_timestamp)

    #----Weekly Digest of Announcements-----#
    if test_day == "Wednesday" and len(announcement_history) == 14:
        send_email = True
        email_type = "Weekly Digest"
        email_recipents = getList('weekly', '1' )
        subject = 'Weekly Digest'
        body_html = ""
        i=0
        while i < 13:
            body_html = body_html + "<h3>"+ announcement_history[i] +"</h3>" +"<h2>" + announcement_history[i+1] + "</h2>" + "\n<br></br>\n"
            #print(i)
            i+=2
        body = "<html><body>" + body_html + "</body></html>"
        print(body)
        #announcement_history = [] clear list for next week

#-----msg variable contains all parts of the email (body is attached in sendEmail function)-----#
    msg = ""    
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['Subject'] = subject
    msg['To'] = ", ".join(email_recipents)#Converts list to comma seperated string

#-----run sendEmail function-----#
    if send_email:
        sendEmail()
        print("I have sent email")#Testing without sending email
        time.sleep(300)
    else:
        print("Time till next Article: 12PM - CURRENT TIME")
        print("Time till next Announcement: 1PM - CURRENT TIME")