import pandas as pd
import datetime

dt1 = pd.to_datetime("2012-01-15")
print("Date time for Jan 15, 2012:", dt1)

dt2 = pd.to_datetime("2012-01-15 21:20")
print("Specific date and time (9:20 pm):", dt2)

dt3 = pd.Timestamp.now()
print("Local date and time:", dt3)

dt4 = dt3.date()
print("A date without time:", dt4)

dt5 = pd.Timestamp.today().date()
print("Current date:", dt5)

dt6 = dt3.time()
print("Time from a date time:", dt6)

dt7 = datetime.datetime.now().time()
print("Current local time:", dt7)
