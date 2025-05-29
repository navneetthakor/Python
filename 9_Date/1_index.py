"""
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
"""

import datetime

# current date and time
curr_dt = datetime.datetime.now()
print(curr_dt)

# get year
print(curr_dt.year)

# more mentioned in notion doc
# https://www.notion.so/datetime-module-202e2b52c37b8063b1baddbacc7c1aab

# also w3schools website
# https://www.w3schools.com/python/python_datetime.asp