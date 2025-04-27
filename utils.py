def encrypt(data):
    return ''.join([chr(ord(char) + 2) for char in data])
def calculate_tax(amount):
    return amount * 0.18

def decrypt(data):
    return ''.join([chr(ord(char) - 2) for char in data])

def decrypt(data):
    return ''.join([chr(ord(char) - 2) for char in data])
def log_login(username):
    print(f"[LOGIN] User {username} logged in.")