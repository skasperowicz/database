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



def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)
if __name__ == "__main__":

   create_apparatus_sql = """
   -- apparatus table
   CREATE TABLE IF NOT EXISTS apparatus (
      id integer PRIMARY KEY,
      apparatus text NOT NULL,
      building text,
      room text
   );
   """

   create_tasks_sql = """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      task_id integer NOT NULL,
      name TEXT,
      surname TEXT,
      task TEXT,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (task_id) REFERENCES projects (id)
   );
   """

   db_file = "lab_schedule.db"

   conn = create_connection(db_file)
   if conn is not None:
      execute_sql(conn, create_apparatus_sql)
      execute_sql(conn, create_tasks_sql)
      conn.close()

