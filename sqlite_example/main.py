import sqlite3
from sqlite3 import Error
import Student

def db_connect(db_file_name):
    #print(sqlite3.verson)
    conn=sqlite3.connect(db_file_name)
    #print(conn)
    return conn

def create_tables(conn):
    student_table="""CREATE TABLE student(
                    sid INT PRIMARY KEY,
                    snm TEXT NOT NULL);
                    """
    cursor=conn.cursor()
    cursor.execute(student_table)

def insert_student(conn,sid,snm):
    sql="INSERT INTO student values(?,?)"
    cur=conn.cursor()
    cur.execute(sql,(sid, snm))
    conn.commit()

def select_student(conn):
    sql="SELECT *FROM student"
    cur=conn.cursor()
    cur.execute(sql)

    dataRows=cur.fetchall()
    for row in dataRows:
        print(row)


if __name__=='__main__':
    print(sqlite3.version);
    conn=db_connect("student.db")
    #create_tables(conn)
    #insert_student(conn,1,"Payal")
    #insert_student(conn, 2, "Ketan")
    select_student(conn)

    s1=Student.Student()
    s1.say_hello()
    s1.say_good_bye()