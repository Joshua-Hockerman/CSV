import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

# testing the datetime strptime function

# mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(mydate)
# print(type(mydate))


for rec in csv_file:
    highs.append(int(rec[5]))
    dates.append(datetime.strptime(rec[2], "%Y-%m-%d"))

print(highs)
print(dates)

fig = plt.figure()

plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=10)
plt.ylabel("Temperature in F", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
fig.autofmt_xdate()  # formating the x-label in order to have the label be more conducive to displaying dates

plt.plot(dates, highs, c="red")
plt.show()
