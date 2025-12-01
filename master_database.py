# Dummy Data







# import sqlite3


# con = sqlite3.connect("password_keeper.db")
# cursor = con.cursor()
# # cursor.execute("CREATE TABLE IF NOT EXISTS entries (name, username, email, password, note)")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS MasterStuff (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     password TEXT NOT NULL)
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Master (
#     master_id INTEGER,
#     PRIMARY KEY (master_id)
#     FOREIGN KEY (master_id) REFERENCES MUN(id))
# """)



# # save changes and close
# con.commit()
# con.close()