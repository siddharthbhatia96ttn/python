#Using datetime, ​​add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time
from datetime import datetime, timedelta

# Given date and time
original_datetime = datetime(2020, 3, 22, 10, 0, 0)

# Add 1 week and 12 hours
new_datetime = original_datetime + timedelta(weeks=1, hours=12)

# Print results
print("Original Date & Time:", original_datetime)
print("New Date & Time:", new_datetime)

#Code to get the dates of yesterday, today, and tomorrow.
from datetime import date, timedelta

# Today's date
today = date.today()

# Yesterday and Tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
import os
cwd = os.getcwd()
print("Current Working Directory:", cwd)

os.mkdir("test")
print("Directory 'test' created")

print("Contents of current directory:")
for item in os.listdir(cwd):
    print(item)

os.rmdir("test")
print("Directory 'test' removed")

#Convert the string "Feb 25 2020 4:20PM" into a Python datetime object

from datetime import datetime

date_string = "Feb 25 2020 4:20PM"

dt = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(dt)

#Subtract 7 days from the date 2025-02-25 and print the result.
from datetime import datetime, timedelta

date_value = datetime(2025, 2, 25)

new_date = date_value - timedelta(days=7)

print(new_date.date())

#Format the date 2020-02-25 as "Tuesday 25 February 2020"
from datetime import datetime

date_value = datetime(2020, 2, 25)

formatted_date = date_value.strftime("%A %d %B %Y")

print(formatted_date)