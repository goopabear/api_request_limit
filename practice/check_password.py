from functools import wraps

# For practice purposes.
# Obviously, password authentication shouldn't be handled like this.

# Class Example:

# Wrapper function 
def authenticate(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(self.message2) # Inherits from the class that contains decorator!
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
        self.message1 = 'Welcome to the system!'
        self.message2 = 'Wrapper inherits this too!'


    @authenticate # Passes to the wrapper function
    def pay(self):
        print("Login successful!")
        print(self.message1) # Inheritance still behaves the same
        return True


if __name__ == "__main__":
    password = input("Enter password: ")

    login = BaseApp(password)
    login.pay()
