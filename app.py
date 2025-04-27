def process_payment(user, amount):
    print(f"Processing payment of ${amount} for {user}.")
    
def login(username, password):
    if username == "admin" and password == "password":
        return True
    return False