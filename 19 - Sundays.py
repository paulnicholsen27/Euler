import datetime

sundays = 0
for year in range(1901,2001):
	for month in range(1,13):
		first_of_month = datetime.date(year, month, 1)
		if first_of_month.weekday() == 6:
			sundays += 1
print sundays