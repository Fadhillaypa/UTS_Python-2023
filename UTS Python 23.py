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
