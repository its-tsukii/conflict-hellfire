def encrypt(data):
    return ''.join([chr(ord(char) + 2) for char in data])

def decrypt(data):
    return ''.join([chr(ord(char) - 2) for char in data])

