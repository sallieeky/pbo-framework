import sys
import pymysql


host = "localhost"
user = "root"
passwd = ""
database = "tespbo"


def connect(cursor=pymysql.cursors.Cursor):

    try:
        db = pymysql.connect(host=host, user=user,
                             passwd=passwd, db=database, cursorclass=cursor)

        cursor = db.cursor()
        return db, cursor
    except:
        print("GAGAL TERHUBUNG KE DATABASE")
        print(f"Buat database {database} terlebih dahulu")
        sys.exit()
