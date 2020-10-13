import pandas as pd
import psycopg2
import csv
from schemas import tables
from etl import FILEPATH

class DatabaseConnection():
    def __init__(self):
        print('Connection Established')
        self.con = psycopg2.connect("dbname=test_db user=jimhlee23")
        self.cur = self.con.cursor()

    def create_table(self, table_name):
        print('Creating Table')
        self.cur.execute(f'DROP TABLE IF EXISTS {table_name}')
        col_list = []
        for col_name, data_type in tables[table_name]:
            full = f'{col_name} {data_type}'
            col_list.append(full)
        col_str = ','.join(col_list)
        self.cur.execute(f'''
            CREATE TABLE {table_name} ({col_str});''')
        self.con.commit()
        print('Table Created')

    def create_primary_key(self, table_name):
        self.cur.execute(f'''
            ALTER TABLE{table_name} PRIMARY KEY {table_name[0][0]}''')
        self.con.commit()

    def copy_table(self, table_name, filepath):
        print('Copy Table Initiated')
        self.cur.execute(f'''COPY {table_name} FROM '{filepath}'
        DELIMITER ',' CSV HEADER;''')
        self.con.commit()
        print('Table Copied')

    def select_from_table(self, table):
        postgresql_select_query = f"SELECT * FROM {table}"
        self.db.cur.execute(postgresql_select_query)
        print(f"Selecting rows from {table} table using cursor.fetchall")
        table_data = self.db.cur.fetchall()
        return table_data

    def run_query(self, string):
        print(f'This is the query:\n{string}')
        self.cur.execute(string)
        return self.cur.fetchall()

    def __del__(self):
        print('Dunder del worked')
        self.con.close()

if __name__ == '__main__':
    db = DatabaseConnection()
    db.create_table('location_table')
    db.create_primary_key('location_table')
    db.create_table('weather_table')
    db.create_primary_key('weather_table')
    db.copy_table('weather_table', FILEPATH)

# IS_CON = False

# # Open a connection to the db, set is open to true
# def open_con(db):
#     IS_CON = True
#     try:
#         con = psycopg2.connect(f"dbname='{db}' user=jimhlee23")
#         cur = con.cursor()
#     except ValueError:
#         print('Not a valid database')
#         IS_CON = False


# def copy_to_table(table, filepath):
#     if IS_CON:
#         cur.execute(f"DROP TABLE IF EXISTS '{table}'")
#         cur.execute(f'''COPY '{table}' FROM '{filepath}'
#         DELIMITER ',' CSV HEADER;''')
#     else:
#         response = input('Which database do you want to connect to?')
#         cur.execute(f'''COPY '{table}' FROM '{filepath}'
#         DELIMITER ',' CSV HEADER;''')


# Old code saved for posterity
# conn = psycopg2.connect("dbname=test_db user=jimhlee23")
# cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS death_valley')
# cur.execute('''CREATE TABLE death_valley (
#     station varchar,
#     name varchar,
#     date varchar,
#     prcp float,
#     snow float,
#     snwd float,
#     tmax int,
#     tmin int,
#     tobs float
#     );''')

# Can i place functions in the arg field for psycopg commands?

# def test_func(cur, filepath):
#     print('This works')
#     return cur.execute(f'''COPY death_valley FROM '{FILEPATH}'
#     DELIMITER ',' CSV HEADER;''')

# test_func(cur, FILEPATH)

# cur.execute(f'''COPY death_valley FROM '{FILEPATH}'
# DELIMITER ',' CSV HEADER;''')

# review row below, also limit rows to 5
# for index, row in df.iterrows():
#     cur.execute("INSERT INTO death_valley (station, name, date, prcp, snow, snwd, tmax, tmin, tobs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (row['STATION'], row['NAME'], row['DATE'], row['PRCP'],row['SNOW'], row['SNWD'], row['TMAX'], row['TMIN'], row['TOBS']))

# def table_dict_creater():
#     with open(file_name) as f:
#         reader = csv.reader(f)
#         header_row = next(reader)
#         precip_table = {'name': 'death_valley', 
#             'cols': (
#                 (header_row[0], 'varchar'),
#                 (header_row[1], 'varchar'),
#                 (header_row[2], 'varchar'),
#                 (header_row[3], 'float'),
#                 (header_row[4], 'float'),
#                 (header_row[5], 'float'),
#                 (header_row[6], 'int'),
#                 (header_row[7], 'int'),
#                 (header_row[8], 'float')
#         )}
#     return precip_table