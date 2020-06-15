from datetime import datetime, timedelta, timezone
import icalendar
from dateutil.rrule import *

icalfile = open('JusticeJune.ics', 'rb')
gcal = icalendar.Calendar.from_ical(icalfile.read())

start_date = input("enter a start date\n")

print(gcal['DTSTART'])
print(start_date)
