# UTS_Python-2023
V3922018 TID Fadhilla Yunandrika Putra Adyatma

import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

#preparing a cursor
cursorObject = dataBase.cursor()

#createdb
cursorObject.execute("CREATE DATABASE db_sales_V3922018")


import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='db_sales_V3922018'
)

# preparing cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE data_stok_barang (
                   id_barang VARCHAR(15) NOT NULL PRIMARY KEY,
                   nama_barang VARCHAR(70) NOT NULL,
                   harga_barang INT,
                   stok_awal INT,
                   barang_masuk INT,
                   barang_keluar INT,
                   stok_akhir INT
                   )"""

# table created
cursorObject.execute(studentRecord)

# disconnect from server
dataBase.close()
