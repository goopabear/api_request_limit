from functools import wraps

# For practice purposes.
# Obviously, password authentication shouldn't be handled like this.

# Class Example:

# Decorator function 
def authenticate(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.password == '1234':
            print("Password correct!")
            return func(self, *args, **kwargs)
        else:
            print("Authentication failed!")
            return False
    return wrapper


class BaseApp:
    def __init__(self, password):
        self.password = password
        self.message = 'Welcome to the system!'


    @authenticate # Passes to the decorator function
    def pay(self):
        print("Login successful!")
        print(self.message) # Inheritance still behaves the same
        return True


if __name__ == "__main__":
    password = input("Enter password: ")

    login = BaseApp(password)
    login.pay()
