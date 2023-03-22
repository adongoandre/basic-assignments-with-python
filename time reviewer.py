from datetime import datetime, timedelta

date = input("do you want to know your  review your dates Y/N : ")
if date.upper() == "Y":
    today = datetime.now()
    before_today = timedelta(days=1)
    yesterday = today - before_today
    week = timedelta(weeks=1)
    last_week = today - week
    print("Today's date is " + str(today))
    print()
    print("Yesterday's date was " + str(yesterday))
    print()
    print("Last week's date was "+ str(last_week))
elif date.upper() == "N":
    print("OK then thank you for your time ")
else: print("Wrong input!! ")
print()