class Schema:
    def __init__(self):
        self.query = ""

    def id(field='id'):
        return f"{field} INTEGER PRIMARY KEY AUTO_INCREMENT,"

    def timestamps():
        return "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"

    def varchar(field, length=255, null=False, unique=False):
        return f"{field} VARCHAR({length}) {'NOT NULL' if null == False else ''} {'UNIQUE' if unique == True else ''},"

    def integer(field, length=20, null=False, unique=False):
        return f"{field} INTEGER({length}) {'NOT NULL' if null == False else ''} {'UNIQUE' if unique == True else ''},"

    def char(field, length=255, null=False, unique=False):
        return f"{field} CHAR({length}) {'NOT NULL' if null == False else ''} {'UNIQUE' if unique == True else ''},"

    def text(field, null=False, unique=False):
        return f"{field} TEXT {'NOT NULL' if null == False else ''} {'UNIQUE' if unique == True else ''},"

    def boolean(field, null=False):
        return f"{field} BOOLEAN {'NOT NULL' if null == False else ''},"

    def float(field, null=False):
        return f"{field} FLOAT {'NOT NULL' if null == False else ''},"

    def datetime(field, null=False):
        return f"{field} DATETIME {'NOT NULL' if null == False else ''},"

    def date(field, null=False):
        return f"{field} DATE {'NOT NULL' if null == False else ''},"
