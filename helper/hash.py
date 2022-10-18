import bcrypt


def encrypt(data):
    return bcrypt.hashpw(bytes(data.encode()), bcrypt.gensalt())


def decrypt(data, hash_data):
    return bcrypt.checkpw(bytes(data.encode()), hash_data.encode())
