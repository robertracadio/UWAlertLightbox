import twitter
import time

# This call does not need to be authenticated since I am retrieving data from a public timeline
api = twitter.Api()
statuses = api.GetUserTimeline("uwalert")


# Return the most recent tweet into an array called Collection. First convert to string since Python is in Unicode (try removing the string conversion!)
collection = str(statuses[0].text).split()

# Collect the date and time of the most recent tweet and convert to string so that it can be parsed by strptime
date_raw = str(statuses[0].created_at)

# Convert the string and return to time formate
date_formatted = time.strptime(date_raw, "%a %b %d %H:%M:%S +0000 %Y")

#testing values
print date_raw
print date_formatted
print statuses[0].text
print collection