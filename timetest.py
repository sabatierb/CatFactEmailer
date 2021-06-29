import datetime

def getDay():
  return (datetime.datetime.now()).strftime("%A")

print(getDay())