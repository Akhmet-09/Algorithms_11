# def add(a,b):
#     return a+b
# def multiply(a,b):
#     return a*b
# def minus(a,b):
#     return a-b
# def divide(a,b):
#     return a/b
# def execute_function(func,a,b):
#     return func(a,b)
# result = execute_function(add,10,5)
# print(execute_function(multiply,5,6))
# print(execute_function(minus,10,2))
# print(execute_function(divide,10,2))

# def outer():
#     message = 'Hello from Python'
#     def inner():
#         print(message)
#     return inner 
# result = outer()
# result()    

# def my_decorator(func):
#     def wrapper():
#         print('Before function execution ')
#         func()
#         print('After function execution')
#     return wrapper 

# def say_hello():
#     print('Hello from Python')
# say_hello = my_decorator(say_hello)
# say_hello()




# n  = int(input())
# sonlar = list(map(int,input().split()))
# juft_sonlar = [x for x in sonlar if x%2==0]
# if juft_sonlar:
#     print(max(juft_sonlar))
# else:
#     print('-1')

n,k = map(int,input().split())
num = int(pow(n,k))
print(num%10)

































