import sqlite3
from sqlite3 import Error


def db_connect(db_file_name):
    print(sqlite3.verson)
    conn=sqlite3.connect(db_file_name)
    #print(conn)

if __name__=='__database1st__':
    db_connect("student.db")