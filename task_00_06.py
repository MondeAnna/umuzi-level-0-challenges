def maximum(a, *args):
    current_max = a
    for arg in args:
        if arg > current_max:
            current_max = arg
    return current_max
