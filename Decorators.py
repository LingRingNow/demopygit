def div(a, b):
    return a/b

def dec_div(func):
    def wrapper(a, b):
        if a>b:
            return func(b,a)
        else:
            return func()
    return wrapper

div1 = dec_div(div)

print(div1(4, 2))