from datetime import datetime

age=int(input('Enter your age and I shall tell you when you turn 100: '))
current_year = datetime.now().year
print(f"you will turn 100 in the year {(current_year-age)+100}")
