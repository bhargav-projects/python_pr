import datetime as dt
v=dt.datetime.now()
print(v.strftime("%x")) #local d-m-y format
print(v.strftime("%X")) #local time 
print(v.strftime("%a")) #week short name
print(v.strftime("%A")) #full name
print(v.strftime("%U")) #week of the year sun
print(v.strftime("%w")) #weak day as number 0-6 0 is sun
print(v.strftime("%W")) #week of the year monday
print(v.strftime("%j")) #day of the year
print(v.strftime("%y")) #year short version
print(v.strftime("%Y")) #year full version
print(v.strftime("%b")) #month short name
print(v.strftime("%B")) #month full name
print(v.strftime("%H")) #railway time
print(v.strftime("%I")) #normal time
print(v.strftime("%p")) # am/pm
print(v.strftime("%c")) #week month date time year
print(v.strftime("%m")) #months as number 0-12
print(v.strftime("%M")) # minutes
print(v.strftime("%S")) #seconds
print(v.strftime("%f")) #fractional seconds 6zero-6nines
print(v.strftime("%d")) #day of the month
print(v.strftime("%z")) #utc offset
print(v.strftime("%Z")) #cst
print(v.strftime("%%")) #%


