import psycopg2
import pandas as pd
# import sqlite3 

# boots is the table
conn = psycopg2.connect("dbname=test_db user=jimhlee23")
cur = conn.cursor()
df = pd.read_csv('~/learnpython/weather_database/data/2247973.csv')
# this inserts the data in boots
cur.execute("INSERT INTO boots (a, b) VALUES (%s, %s)", (100, 800))
cur.execute("SELECT * FROM boots;")
# print(cur.fetchone())
# conn.commit()
# conn = sqlite3.connect('test_db')
# cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS death_valley')
# df.to_sql('death_valley', con=conn, )
conn.commit()
cur.close()
conn.close()
# cur.close()
# conn.close()

'''
create table
insert table
commit
leave
'''