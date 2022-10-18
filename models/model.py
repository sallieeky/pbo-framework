import pymysql

import config


db, cursor = config.connection.connect(pymysql.cursors.DictCursor)


class Model:
    def __init__(self, table_name):
        self.table_name = table_name

    def all(self):
        cursor.execute(f"SELECT * FROM {self.table_name}")
        return cursor.fetchall()

    def find(self, id):
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = '{id}'")
        return cursor.fetchone()

    def first(self):
        cursor.execute(f"SELECT * FROM {self.table_name} LIMIT 1")
        return cursor.fetchone()

    def last(self):
        cursor.execute(
            f"SELECT * FROM {self.table_name} ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()

    def whereMany(self, column, operator, value):
        cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE {column} {operator} '{value}'")
        return cursor.fetchall()

    def whereOnly(self, column, operator, value):
        cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE {column} {operator} '{value}' LIMIT 1")
        return cursor.fetchone()

    def create(self, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        cursor.execute(
            f"INSERT INTO {self.table_name} ({keys}) VALUES ({values})", tuple(data.values()))
        db.commit()
        return True

    def update(self, id, data):
        cursor.execute(
            'UPDATE {table} SET {} WHERE id={id}'.format(
                ', '.join('{}=%s'.format(k) for k in data), table=self.table_name, id=id), tuple(data.values())
        )
        db.commit()
        return True

    def delete(self, id):
        cursor.execute(f"DELETE FROM {self.table_name} WHERE id = {id}")
        db.commit()
        return True

    def truncate(self):
        cursor.execute(f"TRUNCATE TABLE {self.table_name}")
        db.commit()
        return True
