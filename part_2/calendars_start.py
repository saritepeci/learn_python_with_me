import calendar


c = calendar.TextCalendar(calendar.MONDAY)
#thestr = c.formatmonth(2026,1,0,0) 
# thestr = c.formatmonth(1985,5,0,0) 

# print(thestr)

# create an Html format
html_calendar = calendar.HTMLCalendar(calendar.MONDAY)

thestr = html_calendar.formatmonth(2026,1)
#print(thestr)


# for i in c.itermonthdays(2026, 8):
#     print(i)

for name in calendar.month_name:
    print(name)