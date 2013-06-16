months = {
	1:31, #jan
	3:31, # mar
	4:30, # apr
	5:31, # may
	6:30, # jun
	7:31, # jul
	8:31, # aug
	9:30, # sept
	10:31, # oct
	11:30, # nov
	12:31, # dec
}

def mdays(mo, yr):
	if mo == 2:
		if (yr%4 == 0 and yr%100 != 0) or yr%400 == 0:
			return 29
		return 28
	return months[mo]


# (weekday, monthday, month, year)
# e.g., (2, 1, 1, 1900) : monday, jan 1, 1900
def nextdate(date):
	wday, mday, mo, yr = date
	wday = wday%7 + 1
	if mday == mdays(mo, yr): # last day of the month
		mday = 1
		if mo == 12: # it was december
			mo = 1
			yr += 1
		else: 
			mo += 1
	else:
		mday += 1
	return (wday, mday, mo, yr,)

date = (2, 1, 1, 1900)
end = (1, 31, 12, 2000)
count = 0

while date[1] != 1 or date[2] != 1 or date[3] != 1901:
	date = nextdate(date)
print 'now at ', date
while date != end:
	if date[0] == date[1] == 1:
		count += 1
	date = nextdate(date)
print count