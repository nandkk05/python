import sqlite3 as lite


#functionality goes here

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXIST course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create to a Database!")

# TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private)
                    VALUES (?,?,?,?)", data
                    )
        except Exception:
            return False


# TODO: read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM courses") 
                return cur.fetchall()
        except Exception:
            return False

# TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur=con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
        execute Exception:
        return False


# TODO: provide interface to user