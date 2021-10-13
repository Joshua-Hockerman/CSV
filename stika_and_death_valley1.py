import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file_death = open("death_valley_2018_simple.csv", "r")
open_file_sitka = open("sitka_weather_2018_simple.csv", "r")

csv_death = csv.reader(open_file_death, delimiter=",")
csv_sitka = csv.reader(open_file_sitka, delimiter=",")

header_row_death = next(csv_death)
header_row_sitka = next(csv_sitka)


def data_sctructure_loop(csv_file, header_row):

    highs = []
    dates = []
    lows = []

    for rec in csv_file:
        try:
            date = datetime.strptime(rec[2], "%Y-%m-%d")
            high = int(rec[4])
            low = int(rec[5])
        except ValueError:
            print(f"Missing Data for {date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)


fig = plt.figure()

plt.title("Daily High and Low Temperatures, 2018", fontsize=16)
plt.xlabel("", fontsize=10)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
fig.autofmt_xdate()  # formating the x-label in order to have the label be more conducive to displaying dates

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")
plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Death Valley, CA")

plt.show()
