from functools import wraps

# ====== Example 3: Decorators that take arguments ======

def share_blood_type(blood_type='O+'):
    """Appends introduction with blood type declaration. Because it matters."""

    def wrapper(func):
        def wrapped(*args, **kwargs):
            blood_type_str = " My blood type is %s." % (blood_type,)
            return func(*args, **kwargs) + blood_type_str
        return wrapped
    return wrapper

@share_blood_type(blood_type='A+')
def introduce_yourself(name=None):
    if name is None:
        return "A girl has no name."
    return "My name is %s." % (name, )

if __name__ == '__main__':
    print introduce_yourself()


