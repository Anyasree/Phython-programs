import datetime
import calendar
city = input("Enter your city: ")
temperature = int(input("Enter your temperature: "))

if temperature >= 35:
    print("Hot")

elif temperature >= 25:
    print("Warm")

elif temperature >= 15:
    print("Cold")

else:
    print("Very Cold")

now = datetime.datetime.now()
print(now.date())
print(now.time())

year = now.year
print(calendar.calendar(year))
