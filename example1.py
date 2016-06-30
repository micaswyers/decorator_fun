from functools import wraps

# ===== Example 1: Basic Decorator ======
def say_please(func):
    """Decorator that makes you say please."""

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + " Please."
    return wrapper

@say_please
def give_me(item='candy'):
    """Returns request of a bossy child (str)"""

    return "Give me %s." % (item,)

# ====== Example 1.5: Now with functools.wraps ======
def say_excuse_me(func):
    """Decorator that prepends request with 'Excuse me....'"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        pre = "Excuse me...."
        return pre + func(*args, **kwargs)
    return wrapper

@say_excuse_me
def ask_for(item='candy'):
    """Returns a request of a less bossy child (str)"""

    return "Do you have any %s?" % (item, )

