from models.model import Model


class User(Model):
    def __init__(self):
        Model.__init__(self, __class__.__name__.lower())
        self.auth = "username"
