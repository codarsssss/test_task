def print_num_gt(max_num):
    def decorator(func):
        def wrapper(arg):
            if max_num > arg:
                print('error')
            else:
                func(arg)
        return wrapper
    return decorator


@print_num_gt(3)
def print_num(x: int):
    print(x)


print_num(5)
