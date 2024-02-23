# def fib(n):
#     if n == 0:
#         return 0
#     elif n== 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(6))

# def fib(n):
#     a = 0
#     b = 1
#     if n < 2:
#         return n
#     for i in range(2, n):
#         c = a + b;
#         a = b
#         b = c
#     return c
# print(fib(6))

def fibonacciLess100():
   a = 0
   b = 1
   for i in range(2, 100):
       c= a + b
       if c> 100:
           break
       a = b
       b = c
       print(c)
fibonacciLess100()