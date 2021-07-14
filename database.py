import sqlite3

def generate_string(lenght):
    import string, random
    id = ""
    for elements in range(lenght):
        id += random.choice(string.digits + string.ascii_letters)
    return id

def return_links():
  database = sqlite3.connect('database.db')
  mycursor = database.cursor()
  mycursor.execute("SELECT * FROM links")
  return mycursor.fetchall()