from migrations.schema import Schema


class User(Schema):
    def __init__(self):
        Schema.__init__(self)

    def schema(self):
        self.query += Schema.id()
        self.query += Schema.varchar("username", unique=True)
        self.query += Schema.varchar("password")
        self.query += Schema.timestamps()
        return self.query

    def create(self, table):
        return f"""
        CREATE TABLE IF NOT EXISTS 
        {table} 
        (
            {self.schema()}
        );
        """

    def drop(self, table):
        return f"""
        DROP TABLE IF EXISTS {table};
        """
