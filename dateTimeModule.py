import datetime
user_input = input("please enter your schedule and format of date with semi colon: \n")
## enter a sting value as scheduled thing, then enter a date on same linem like below line
# Learn_Python:11.12.2022 or learn English:15.4.2022
dateList = user_input.split(":")
schedul = dateList[0]
date = dateList[1]
time = datetime.datetime.strptime(date,"%d.%m.%Y")
print(dateList)