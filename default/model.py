from models.model import Model


class ClassName(Model):
    def __init__(self):
        Model.__init__(self, self.__class__.__name__.lower())
