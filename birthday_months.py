import json
from datetime import datetime
from collections import Counter
import calendar

birthdays={"Anika":"20/07/2007", "Jake":"09/07/2008","Jill":"03/03/2006","John":"05/12/2007"}

with open("birthdays.json","w") as b:
    json.dump(birthdays, b)


with open ("birthdays.json","r") as f:
    birthday=json.load(f)

birthdates=birthday.values()
months=[]
for dates in birthdates:
    temp=datetime.strptime(dates, "%d/%m/%Y")
    month=temp.month
    months.append(calendar.month_name[month])
    
c=Counter(months)
print(c)