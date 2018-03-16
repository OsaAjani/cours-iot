#!/usr/bin/env python3.6

import mysql.connector

mysql_connection = mysql.connector.connect(host='localhost', user='root', password='root', database='cours_iot_introduction_python')
mysql_cursor = mysql_connection.cursor()

mysql_cursor.execute('SELECT * FROM user')
users = mysql_cursor.fetchall()

for user in users:
    print(f'id: {user[0]}, firstname: {user[1]}, lastname: {user[2]}, age: {user[3]}')

query_data = {'firstname': 'Elisabeth', 'lastname': 'Tessier', 'age': 80}
mysql_cursor.execute('INSERT INTO user (firstname, lastname, age) VALUES (%(firstname)s, %(lastname)s, %(age)s)', query_data)
mysql_connection.commit()
