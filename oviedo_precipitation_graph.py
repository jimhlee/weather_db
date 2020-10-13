import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/oviedo_precipitation.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    # high_index = header_row.index('TMAX')
    # low_index = header_row.index('TMIN')
    precipitation_index = header_row.index('PRCP')

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, prcps, cumulative = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        place_name = row[name_index]
        try:
            prcp = float(row[precipitation_index])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            prcps.append(prcp)
            if cumulative:
                cumulative.append(cumulative[-1] + prcp)
            else:
                cumulative.append(prcp)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, cumulative, c = 'blue')
    plt.fill_between(dates, cumulative, facecolor='blue', alpha=0.1)

    title = f'Cumulative Precipitation - Jan-Jul 2020\n{place_name}'
    plt.title(title, fontsize = 20)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Precipitation(in)', fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

    plt.show()