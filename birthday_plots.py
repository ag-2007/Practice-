from bokeh.plotting import figure, show, output_file
import json
from datetime import datetime
from collections import Counter
import calendar

with open ("birthdays.json","r") as f:
    birthday=json.load(f)

birthdates=birthday.values()
months=[]
for dates in birthdates:
    temp=datetime.strptime(dates, "%d/%m/%Y")
    month=temp.month
    months.append(calendar.month_name[month])
    
c=Counter(months)

output_file("plot.html")

x = list(c.keys())
y = list(c.values())

p = figure(x_range=x)
p.vbar(x=x, top=y, width=0.5)

show(p)

