#!/usr/bin/python
# -*- coding : utf-8 -*-

import sqlite3

database_file = '/home/heli/test.db'


try:
    con = sqlite3.connect(database_file)
    c = con.cursor()
    print("Connection is established")

except sqlite3.Error as e:
    print(e)