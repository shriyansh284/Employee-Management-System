from tkinter.constants import INSERT
import pymysql
from pyexpat.errors import messages
from tkinter import messagebox


def connect_database():
        global mycursor,conn
        try:
            conn = pymysql.connect(host='localhost', user='root', password='password')
            mycursor = conn.cursor()
        except:
             messagebox.showerror('Error', 'Something Went Wrong, Please open mysql app before running again')
             return
        mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
        mycursor.execute('USE employee_data')
        mycursor.execute('CREATE TABLE IF NOT EXISTS data (ID VARCHAR(10),NAME VARCHAR(10),PHONE VARCHAR(15),ROLE VARCHAR(50) , GENDER VARCHAR(10), SALARY VARCHAR(10))')


def insert(id, name, phone, role, gender, salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)', (id, name, phone, role, gender, salary))
    conn.commit()

def id_exists(id):
    mycursor.execute("select count(*) FROM data WHERE id=%s",(id,))
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('select * from data')
    result=mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()

def search(option ,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return  result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()

connect_database()
