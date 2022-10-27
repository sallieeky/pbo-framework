from helper.auth import Auth


class AuthController:
    def login(self, data):
        return Auth().login(data["username"], data["password"])
