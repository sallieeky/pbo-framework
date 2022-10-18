import bcrypt

from models.User import User


class Auth(User):
    def __init__(self):
        User.__init__(self)

    def login(self, auth, password):
        user = self.whereOnly(self.auth, "=", auth)
        if user != None:
            db_pass = user["password"]
            if bcrypt.checkpw(bytes(password.encode()), db_pass.encode()):
                return True
            else:
                return False

        else:
            return False
