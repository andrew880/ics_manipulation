from datetime import datetime, timedelta
import ics
import arrow

filename = input("enter a icsfile name\n")
icsfile = open((filename), 'rb')
c = ics.Calendar.parse_multiple(icsfile.read().decode('utf-8'))[0]

input = input("enter a start date in the following format: YYYY-MM-DD\n")
try:
    start_date = arrow.get(input, 'YYYY-MM-DD')
except Exception as e:
    print("incorrect format, run program again")


if len(list(c.events)) > 0:
    first_event_date = list(c.events)[0].begin
for event in list(c.events):
    print(first_event_date)
    print(event.begin)
    if event.begin - first_event_date <= timedelta(0):
        first_event_date = event.begin
datedif = start_date - arrow.get(first_event_date.year, first_event_date.month, first_event_date.day)
print(datedif)

events = set()
for event in c.events:
    print('---------')
    print(event.begin)
    print(event.end)
    if datedif > timedelta(0):
        event.end += datedif
        event.begin += datedif
    else:
        event.begin += datedif
        event.end += datedif
    if arrow.get(event.end.year, event.end.month, event.end.day) == event.end and arrow.get(event.begin.year, event.begin.month, event.begin.day) == event.begin:
        event.end -= timedelta(days = 1) #to accomodate rounding error from make_all_day
        print(event.begin)
        print(event.end)
        print('allday')
        event.make_all_day()
    print(event.begin)
    print(event.end)
    events.add(event)
c = ics.Calendar(imports = None, events = events, todos = c.todos, creator = c.creator)

with open('MODIFIED.ics', 'w') as f:
    f.write(str(c))
