from helper.hash import encrypt
from models.User import User


class UserSeeder:
    def __init__(self):
        self.model = User()

    def seed(self):
        self.model.create({
            'username': 'admin',
            'password': encrypt('admin123'),
        })
        self.model.create({
            'username': 'admin2',
            'password': encrypt('admin123'),
        })
