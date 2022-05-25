import time

# TODO Delay Decorator is a function that wraps another function and gives it additional functionalities and modifies it
# TODO @ is called Syntactic Sugar
def delay_decorator(function):
    def wrapper_function():
        function()
        time.sleep(5)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello World!")

def say_greeting():
    print("Say Greeting")

say_hello()

# decorated_func = delay_decorator(say_greeting())
# decorated_func()