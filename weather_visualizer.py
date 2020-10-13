import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
from db_connector import DatabaseConnection
from seaborn import color_palette
import requests as r

headers = {'token': 'ISXLkoppxlzAjWSsvSHGHptpzxHEaDRH'}
limit = '?limit=1000'
pack = {

}
noaa_data = r.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/'+limit,params=pack,headers=headers)
decoded_data = noaa_data.json()
print(decoded_data)

class GraphCreator():
    def __init__(self):
        self.db = DatabaseConnection()

    # Columns must always be a tuple
    def create_query(self, location, columns, date_range):
        return f''' 
        SELECT  station, name, date, {', '.join(columns)}
        FROM weather_table
        WHERE 
            station = '{location}' AND
            date BETWEEN '{date_range[0]}' AND '{date_range[1]}';
        '''

    def create_precip_graph(self, station, date_range, cumulative=False):
        query = self.create_query(station, ('prcp','name',), date_range)
        data = self.db.run_query(query)
        # x_data is the dates
        x_data = []
        # y_data is the precipitation
        y_data = []
        # This loop will add things to the x and y data lists
        for row in data:
            current_date = row[2]
            x_data.append(current_date)
            if cumulative:
                y_data.append(y_data[-1] + row[3])
            else:
                y_data.append(row[3])
        self.plot_data(x_data, {'dummy': y_data}, title, 'Daily Rainfall', 'Rainfall(in)')

    def get_location(self, station):
        return f''' 
        SELECT  station, name
        FROM weather_table
        WHERE 
            station = '{station}'
        LIMIT 1;
        '''
    
    def title_maker(self, station):
        raw_loc = self.db.run_query(self.get_location(station))
        raw_title = raw_loc[0][1].split(',')
        title = raw_title[0]

    def create_temp_graph(self, location, date_range):
        query = self.create_query(location, ('tmax', 'tmin'), date_range)
        data = self.db.run_query(query)
        # x_data is the dates
        x_data = []
        # y_data is the temps
        y_data = {'Max': [], 'Min': []}
        # This loop will add things to the x and y data lists
        for row in data:
            current_date = row[2]
            x_data.append(current_date)

            y_data['Max'].append(row[3])
            y_data['Min'].append(row[4])
        self.plot_data(x_data, y_data, location, 'Daily High and Low Temps', 'Temp(˚F)')

    def plot_data(self, dates, columns_data, location, raw_title, ylabel):
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        # review this line
        for index, (col, col_values) in enumerate(columns_data.items()):
            ax.plot(dates, col_values, c=color_palette()[index], lw=0.5)
        # location is still fucked up, showing station not location 
        title = f'{raw_title} {dates[0]} - {dates[-1]}\n{location}'
        plt.title(title, fontsize=20)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel(ylabel, fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        # plt.show()

if __name__ == '__main__':
    a = GraphCreator()
    a.create_precip_graph('USC00042319', ('2010-01-01', '2010-12-31'))
    # a.get_location('USC00042319')
    # a.create_temp_graph('USC00042319', ('2010-01-01', '2010-12-31'))
    plt.show()
