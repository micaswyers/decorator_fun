from functools import wraps

# ===== Example 2: Ordering decorators ======
def bread(func):
    """Func that inplies you're not gluten-free."""

    @wraps(func)
    def wrapper(*args, **kwargs):

        """"
        print "I'm the bread. I go on the top/outside."
        sandwich1 = func(*args, **kwargs)
        print "I'm bottom bread!" # What's going on here?
        return sandwich1
        """
        print "I'm the bread. I come first!"
        return func(*args, **kwargs)
    return wrapper

def lettuce(func):
    """Func that says you're making an attempt at health."""

    @wraps(func)
    def wrapper(*args, **kwargs):

        print "I'm the lettuce, I go next to the filling."
        return func(*args, **kwargs)
    return wrapper

def condiment(func, sauce='mayonnaise'):
    """Func that confirms that you like condiments."""

    @wraps(func)
    def wrapper(*args, **kwargs):

        print "I'm %s. I go on the bread." % (sauce,)
        return func(*args, **kwargs)
    return wrapper

# What will the request look like?
@bread
@condiment
@lettuce
def sandwich(filling='liverwurst'):
    """Function that tells you what kind of sandwich you have."""

    print "I'm %s. I'm the heart of this sandwich." % (filling, )


# ====== Example 2.5: Sandwich bread =======

# How can we make the string representing bread print at both ends?
