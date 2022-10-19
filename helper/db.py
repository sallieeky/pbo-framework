import pymysql
import config

db, cursor = config.connect(pymysql.cursors.DictCursor)


class DB:
    def __init__(self):
        pass

    def select(query):
        cursor.execute(query)
        return cursor.fetchall()

    def create(query):
        cursor.execute(query)
        db.commit()
        return True

    def update(query):
        cursor.execute(query)
        db.commit()
        return True

    def delete(query):
        cursor.execute(query)
        db.commit()
        return True
