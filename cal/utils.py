from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import *

from datetime import date
import holidays



class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day,i):
		hol = holidays.India(years=self.year)
		d = ''
		hol=hol.get(str(self.month)+'-'+str(day)+'-'+str(self.year),'') if day!=0 else ''
		if hol and day!=0:
			return f"<td class='date-hol'><span class='date'>{day}{hol}</span></td>"
		if day != 0 and (i!=5 and i!=6):
			return f"<td ><a href='?month={self.year}-{self.month}&date={day}'><span class='date'>{day}</span></a></td>"
		elif day!=0:
			return f"<td class='date-weekend'><span >{day}</span></td>"
		return f"<td class='date-empty'></td>"

	# formats a week as a tr
	def formatweek(self, theweek):
		week = ''
		i=0
		for d, weekday in theweek:
			week += self.formatday(d,i)
			i+=1
		return f"<tr> {week} </tr>"

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		cal = f'<table  border="0" cellpadding="0" cellspacing="0" class="calendar table-responsive">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f"{self.formatweekheader()}\n"
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week)}\n'
		cal+=f'</table>'
		return cal
