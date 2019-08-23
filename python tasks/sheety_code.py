import datetime

#get information
year, month, day = input().split(" ")
past_days = int(input())

#convert to date format
now = datetime.date(int(year), int(month), int(day))
then = datetime.timedelta(days=past_days)
answer = " ".join([str(int(i)) for i in str(now+then).split("-")])

print(answer)