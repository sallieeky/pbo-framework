from helper.db import DB


a = DB.insert(
    "INSERT INTO user(username,password) VALUES ('aa', 'adad');")
print(a)
a = DB.select("SELECT * FROM user")
print(a)
