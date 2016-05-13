import MySQLdb

def connection():
    conn = MySQLdb.connect(host = "localhost",
                            user = "root",
                            password = "metromg1",
                            db = "test")
    c = conn.cursor()
    return c, conn

if __name__ == "__main__":
    c, conn = connection()
    print("It worked !")
    