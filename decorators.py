from functools import wraps


def timer_func(orig_func):
    """Gives the runtime of a function."""

    import time

    def wrapper(*args, **kwargs):

        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} seconds'.format(orig_func.__name__, t2))

        return result
    return wrapper


def repeat(n=1):
    """Repeats a function n times."""

    def decorator(func):
        @wraps(func)
        def wrapper(args):
            args = func(args)
            for i in range(n - 1):
                args = func(args)
            return args
        return wrapper
    return decorator


def cache(func):
    """Caches a look-up."""

    saved = {}

    @wraps(func)
    def new_func(*args):
        if args in saved:
            return new_func(*args)
        result = func(*args)
        saved[args] = result
        return result
    return new_func


def memoise(func):

    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper
