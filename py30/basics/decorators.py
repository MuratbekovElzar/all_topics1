'''Декораторы'''


# def outer(x):
#     def inner(y):
#         return x+y
#     return inner

# inner_func = outer(9)
# print(inner_func(8))
# print(inner_func)
# a = print
# a('hello')
# print(a)



'''
функция высшего порядка -> это функция которая может принимать в качестве аргумента другую функцию и/или возвращать функцию как результат 
'''

# def test_func(func):
#     def inner_test_func():
#         func()
#         # <тело>
#     return inner_test_func

# def hello(func):
#     # <тело>
#     pass


'''
Декоратор -> функция высшего порядка (в качестве аргумента принимает функцию и возвращает функцию), которая оборачивает другую функцию для расширения ее функционала, при этом не изменяя ее код
'''

# def test(func):
#     func()
#     print('hello')
    
# def a():
#     print('привет')
    
# test(a)



# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     end = time.time()
#     print(f'Время работы функции {func.__name__}, заняло {end - start}')
    

# def loop():
#     i = 0
#     while i < 1000000:
#         print(i)
#         i += 1
        
# benchmark(loop)

# def test_for_loop():
#     for i in range(1000000):
#         # pass
#         print(i)
        
# benchmark(test_for_loop)
# print(dir(loop))


'''Синтаксик'''
# def decorator(func):
#     def wrapper():
#         print('Функция-обертка!')
#         print(f'Оборачиваем функцию {func.__name__}')
#         func()
#         print('Выходим из обертки')
#     return wrapper

# # @decorator
# def say_hi():
#     print('Hiiiiiiiiiiiiiiii')
    
# say_hi()
# как работает @ под капотом
'''
@ -> синтаксический сахар, позволяет нам явно указать какой декоратор применяется для функции

под копотом вызывает функцию decorator и результат выполнения этой функции сохраняет в переменной с точно таким же названием как и обернутая функция
say_hi = decorator(say_hi)
say_hi()
'''

# def uppercase_decorator(func):
#     def wrapper():
#         func_ = func()
#         upper_str = func_.upper()
#         return upper_str
#     return wrapper

# @uppercase_decorator
# def inp_str():
#     str_ = input('Введите текст: ')
#     return str_


# print(inp_str())



# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Время работы функции {func.__name__}, заняло {end - start}')
#     return wrapper
        
# @benchmark
# def loop():
#    i = 0
#    while i < 1000000:
#        print(i)
#        i += 1
# loop()
# benchmark(loop)

# def smart(func):
#     def wrapper(x, y):
#         print('=======')
#         if y == 0:
#             return
#         return func(x, y)
#     return wrapper        

# @smart
# def division(x, y):
#     return x / y

# print(division(7, 0))
# print(division(7, 3))


'''напишите декоратор для вызова функции определенного количетсво раз'''


# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range (num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(7)
# def test(x, y):
#     print(f'========{x}\n+++++++{y}')
    
# test(3, 4)


# def strong(func):
#     def wrapper():
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper():
#         return '<div>' + func() + ' Зима близко' + '</div>'
#     return wrapper

# @str'ong
# @div
# def get():'
#     return 'Jhon Snow'
# print(get())

    
    
                
        
# def call_function(func):
#     def wrapper():
#         print(f'Вызываю функцию{func.__name__}')
#         func()
#         print(f'Вызов функции{func.__name__} прошел успешно')
#     return wrapper

# @call_function  
# def first():
#     print('hello world')

# first()



# def make_bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper


# def make_italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper

# def make_underline(func):
#     def wrapper():
#         return '<u>' + func() + '</u>'
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
# print(hello())






# import time

# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Время выполнения: {execution_time:.2f} секунд.")
#         return result
#     return wrapper

# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
#     # здесь можно выполнять дополнительные операции с веб-страницей

# # Вызов функции fetch_webpage с применением декоратора
# fetch_webpage()





# def is_admin(func):
#     def wrapper(user_dict):
#         if 'is_admin' in user_dict and user_dict['is_admin']:
#             print(f"Доступ разрешен {user_dict['username']}")
#         else:
#             print(f"Доступ запрещен {user_dict['username']}")
#     return wrapper

# @is_admin
# def get_user(user_dict):
#     return user_dict

# # Примеры вызова функции get_user с разными словарями пользователей
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})