def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("== start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func
