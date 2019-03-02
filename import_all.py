# minor change from original created by Austine Ikechukwu
# https://github.com/Austyns/sqlite-to-json-python

# added argparse, removed second db connection, and printing to screen only if -p is used

import sqlite3
import argparse

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


parser = argparse.ArgumentParser()
parser.add_argument("db", help="database")
parser.add_argument("-p", action='store_true', help="print output")
args = parser.parse_args()

db = args.db

# connect to the SQlite databases
connection = sqlite3.connect(db)
connection.row_factory = dict_factory

cursor = connection.cursor()

# select all the tables from the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
# for each of the tables , select all the records from the table
for table_name in tables:
		# table_name = table_name[0]
		print table_name['name']
		    

		#conn = sqlite3.connect(db)
		#conn.row_factory = dict_factory
		 
		cur1 = connection.cursor()
		 
		cur1.execute("SELECT * FROM "+table_name['name'])
		 
		# fetch all or one we'll go for all.
		 
		results = cur1.fetchall()
		 
		if (args.p):
			print results

		# generate and save JSON files with the table name for each of the database tables
		with open(table_name['name']+'.json', 'a') as the_file:
		    the_file.write(format(results).replace(" u'", "'").replace("'", "\""))

connection.close()
