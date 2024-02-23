# Compile time Error (Syntax Error)
# Logical Error
# Runtime Error impotence

a = 7
b = 0

try:
    # print("open")
    # print(a/b)
    # print("closed in try")
    k = int(input("enter"))
    print(k)
#     Exception在所有错误最上层，
except ValueError:
    print("not a number")
except Exception as e:
    print("Error", e)
except ZeroDivisionError as e:
    print("cannot divide by zero", e)
    print("closed")

finally:
    print("finally closed")

