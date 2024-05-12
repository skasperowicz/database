import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn


def add_apparatus(conn, apparatus):
   
   sql = '''INSERT INTO apparatus(apparatus, building, room)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, apparatus)
   conn.commit()
   return cur.lastrowid

def add_task(conn, task):
   """
   Create a new task into the tasks table
   :param conn:
   :param task:
   :return: task id
   """
   sql = '''INSERT INTO tasks(task_id, name, surname, task, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   conn.commit()
   return cur.lastrowid


if __name__ == "__main__":
   apparatus = ("Spektrofotometr", "B", "404")
   conn = create_connection("lab_schedule.db")
   ap_id = add_apparatus(conn, apparatus)
   task = (
       ap_id,
       "Paweł",
       "Lewandowski",
       "Pomiar",
       "2020-05-13 12:00:00",
       "2020-05-13 15:00:00"
   )
   task_id = add_task(conn, task)

   print(ap_id, task_id)
   conn.commit()
   task = (
       ap_id,
       "Anna",
       "Nowak",
       "Pomiar",
       "2020-05-13 12:00:00",
       "2020-05-13 15:00:00"
   )
   task_id = add_task(conn, task)

   print(ap_id, task_id)
   conn.commit()
   task = (
       ap_id,
       "Paweł",
       "Pietrzak",
       "Serwis",
       "2020-05-14 12:00:00",
       "2020-05-14 15:00:00"
   )
   task_id = add_task(conn, task)

   print(ap_id, task_id)
   conn.commit()

   apparatus = ("HPLC", "C", "240")
   ap_id = add_apparatus(conn, apparatus)
   task = (
       ap_id,
       "Anna",
       "Kowalska",
       "Rozdział",
       "2020-05-14 12:00:00",
       "2020-05-14 15:00:00"
   )
   task_id = add_task(conn, task)

   print(ap_id, task_id)
   conn.commit()   
   task = (
       ap_id,
       "Jan",
       "Kowalski",
       "Rozdział",
       "2020-05-16 12:00:00",
       "2020-05-16 15:00:00"
   )
   task_id = add_task(conn, task)

   print(ap_id, task_id)
   conn.commit()   
   task = (
       ap_id,
       "Paweł",
       "Pietrzak",
       "Serwis",
       "2020-05-16 12:00:00",
       "2020-05-16 15:00:00"
   )
   task_id = add_task(conn, task)

   print(ap_id, task_id)
   conn.commit()  