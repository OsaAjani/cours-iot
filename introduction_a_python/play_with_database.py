#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
import mysql.connector
mysql_connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'your_password', database = 'cours_iot_introduction_python')
mysql_cursor = mysql_connection.cursor()
query_data = {'firstname': 'Bernard', 'lastname' : 'Tessier', 'age' : 55}
mysql_cursor.execute('INSERT INTO user (firstname, lastname, age) VALUES (\'{firstname}\', \'{lastname}\', {age})'.format(query_data))

