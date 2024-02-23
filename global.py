a = 10

def some_function():
    a = 1
    globals()["a"] = 14

    print("inside some_function", a)

some_function()
print("outside", a)
