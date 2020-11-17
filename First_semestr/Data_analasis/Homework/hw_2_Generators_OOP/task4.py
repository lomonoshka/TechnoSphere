import functools


def counter(func):
    func.current_depth = 0
    func.rdepth = 0
    func.ncalls = 0

    @functools.wraps(func)
    def wrapper(*args, **argv):
        if(wrapper.current_depth == 0):
            wrapper.ncalls, wrapper.rdepth = 0, 0
        wrapper.current_depth += 1
        wrapper.ncalls += 1
        result = func(*args, **argv)
        wrapper.rdepth = max(wrapper.current_depth, wrapper.rdepth)
        wrapper.current_depth -= 1
        return result
    return wrapper


@counter
def func2(n, steps):
    if steps == 0:
        return

    func2(n + 1, steps - 1)
    func2(n - 1, steps - 1)
