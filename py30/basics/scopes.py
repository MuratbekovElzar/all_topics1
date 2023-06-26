'''Области видимости и пространства имен'''


'''Пространства имен'''
'''
1. builtins (встроенное) -> все, что встроенно в стандартную библиотеку питона 
(print, input, len ...)
'''

'''
2. Global -> (глобальное) все переменные внутри файла, которые мы создали (без табуляции)
'''
name = 'Sam'


'''
3. Enclosed -> (не локальное, замкнутое) находится между двумя пространствами 
'''

'''
4. Local -> (локальное) 
'''

# def test():
#     hello = 'hello'


# print(globals()) -> возвращает все глобальные переменные 

# print(dir(__builtins__)) -> возвращает все встроенные имена


# x = 100
y = 0
z = 99

# # x = 77
# globals()['x'] = 45
# print(z is globals()['z'])
# print(globals())


'''
Локальные -> переменные (в функциях)
'''

#locals() -> возвращает все локальные имена 

# def fund(test):
#     a = 10
#     b = 0
#     print(locals()) # {'test': 6, 'a': 10, 'b': 0}
    
# fund(6)

# print(locals().items()) -> когда применяем на глобальном уровне, возвращает все глобальные имена

# a = 5
# b = 6
# def func1():
#     a = 0
#     b = 9
#     print(a, b)
    
# func1()

# print(a, b)

'''Enclosed'''
# возникает только тогда, когда внутри функции объявляется еще функция (при вложенности функций)

# string = 'я глобальная'
# def outer_func():
#     # string = 'не локальная переменная(enclose)'
#     print(string)
#     def inner_func():
#         string = 'локальная переменная'
#         print(string)
#         # print(locals())
#     inner_func()
#     # print(locals())
        
# outer_func()
# inner_func() -> (NameError) будет ошибка так как она в нелокальной области 
# print(outer)


'''Порядок поиска переменных'''
# Local -> Enclosed -> Global -> Builtins

# import this # краткий гайд по Дзен Питону


'''
global -> позволяет изменить значение глобальной переменной , находясь в локальной области вмдимости
'''
# x = 10

# def func(): 
#     global x 
#     x = 20
#     print(x)
    
    
# func()
# print(x)



# count = 0

# def counter():
#     global count
#     print(count)
#     count += 1
    
# counter()
# counter()
# counter()



# count = 0

# def counter():
#     # global count
#     try:
#         print(count)
#         count += 1
#     except:
#         print('f')
    
# counter()
# counter()
# counter()



# count = 0

# def counter():
#     global count
#     count += 1
#     return count
  
    
# print(counter())
# print(counter())
# print(counter())



# name = input()
# age = input()
# print({'id': counter(), 'name': name, 'age': age})

# a = 0
# def outer():
#     global a
#     a = 8
#     def inner():
#         global a
#         a = 10
#         print('inner a = ', a)
#     inner()
#     print('outer a = ', a)

# outer()
# print('global a = ', a)



'''
nonlocal -> позволяет изменить значение enclosed(не локальная) переменной в локальной области видимости
'''

# a = 0

# def outer():
#     a = 8
#     def inner():
#         nonlocal a
#         a = 10
#         print('inner a = ', a)
#     inner()
#     print('outer a = ', a)

# outer()

# from time import sleep
# def counter (number):
#     count = 0
    
#     def add():
#         nonlocal count
#         count += 1
#         print(count)
#         sleep(1)
#     for i in range(number):
        
#         add()
    
# counter(10)



#ТАСКИ

# var = 'переменная в foo' 
# def foo(): 
#     global var 
# var = 'переменная foo' 
# print('переменная в foo: ', var) 
# def bar(): 
#     global var 
# var = 'переменная bar' 
# bar() 
# foo() 
# print('переменная в foo: ', var)

# num = 3
# def mul():
#     global num
#     num = num ** 2
#     return num 
# mul()
# mul()
# mul()
# print(num)

# balance = 0
# def get_salary(amount): 
#     global balance 
#     balance = balance + amount 
# def pay_bills(amount, long_name): 
#     global balance 
#     balance = balance - amount 
#     print(f'Вы заплатили {amount} сом за {long_name}') 
#     return balance 
# def get_balance(): 
#     global balance 
#     print(f'У вас на счету {balance} сом') 
# get_salary(1000) 
# get_balance() 
# pay_bills(400, 'кабельное тв') 
# get_balance()

# result = 0 
# def pow_first(x,y):
#     global result 
#     result = x ** y 
# def pow_second(z): 
#     global result 
#     result = result % z 
# pow_first(2, 3)
# pow_second(3)
# print(result)

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16} 
# for k, v in a.items():
#     if v >= 17: 
#         print(f'{k}, Вы можете войти в клуб') 
#     else: 
#         print(f'{k}, извините, Вы не проходите по age-control')

# def count_symbols(word): 
#     glasnye = 0
#     soglasnye = 0
#     drugie = 0
#     for letter in word:
#         if letter.lower() in 'аяуюоеёэиы': 
#             glasnye += 1
#         elif letter.lower() in 'бвгджзйклмнпрстфхцчшщ':
#             soglasnye += 1
#         else: 
#             drugie += 1
#     return (f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {drugie}')
# print(count_symbols('Мурат супер!'))

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3] 
# def lower_7():
#     b = [] 
#     global a 
#     for i in a:
#         if i < 7:
#             b.append(i)
#     return b
# print(lower_7())


# ДЕКОРАТОРЫ


# def call_function(func):
#     def wrapper(): 
#         print(f"Вызываю функцию {func.__name__}") 
#     func() 
#     print(f"Вызов функции {func.__name__} прошёл успешно") 
#     return wrapper 
# @call_function
# def first():
#     print("hello world") 
#     return 'hello world' 
# first()



# import datetime 
# def func_start_time(func):
#     def wrapper():
#         print('Функция запущена ' + str(datetime.datetime.now())) 
#         func()
#     return wrapper 
# @func_start_time
# def func():
#     print('Hello world')
# func()


# name = 'Alex'
# def change_name():
#     global name
#     name ='Cody'
# print(name)