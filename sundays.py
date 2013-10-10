def get_days(year, month):
  if month == 3 or month == 5 or month == 8 or month == 10:
    return 30
  elif month != 1:
    return 31
  else:
    if year % 4 == 0:
      if year % 400 == 0:
        return 29
      elif year % 100 == 0:
        return 28
      return 29
    else:
      return 28

def firstsunday(startDayOfWeek):
  return startDayOfWeek == 0


allsundays = 0
dayOfWeek = 1
for year in range(1900, 2001):
  for month in range(12):
    if year != 1900:
      allsundays += firstsunday(dayOfWeek)
    dayOfWeek = (dayOfWeek + get_days(year, month)) % 7

print allsundays
      
    
    
  
