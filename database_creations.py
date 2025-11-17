# Referenced from https://docs.python.org/3/library/sqlite3.html

import sqlite3

# All databases are created here:

# create database connection and cursor object, then create table
con = sqlite3.connect("password_keeper.db")
cursor = con.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS entries (name, username, email, password, note)")




cursor.execute("""
CREATE TABLE IF NOT EXISTS master_account (
    accountID INTEGER PRIMARY KEY AUTOINCREMENT,
    master_user TEXT NOT NULL,
    master_password TEXT NOT NULL)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS entries (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               master_id INTEGER NOT NULL,
               email TEXT NOT NULL, 
               username TEXT NOT NULL, 
               password TEXT NOT NULL, 
               service TEXT NOT NULL, 
               note TEXT,
               FOREIGN KEY (master_id) REFERENCES master_account (accountID))
""")


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS master (
#     student_id INTEGER,
#     course_id INTEGER,
#     PRIMARY KEY (student_id, course_id),
#     FOREIGN KEY (student_id) REFERENCES Students(id),
#     FOREIGN KEY (course_id) REFERENCES Courses(id)
# )
# """)


# save changes and close
con.commit()
con.close()