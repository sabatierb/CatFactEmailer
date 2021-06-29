def readList():
  txtfile = open("userList.txt", "r")
  lines = txtfile.readlines()
  txtfile.close()
  print(lines)
  i=0
  while i <= (len(lines)-3):
    tempoary_user_list = []
    tempoary_user_list.append(lines[i].strip('\n'))
    tempoary_user_list.append(lines[i+1].strip('\n'))
    tempoary_user_list.append(lines[i+2].strip('\n'))
    i+=3
  #print(tempoary_user_list)
    user_list.append(tempoary_user_list)
  print(user_list)

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
  print(user_add)
  user_list.append(user_add)
  print(user_list)

def removeUser():
  displayList()
  remove = input("Whats email of user to remove")
  for element in user_list:
    if remove in element:
      user_list.remove(element)
  print(user_list)





#user_list = []