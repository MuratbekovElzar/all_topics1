'''======== Обработка исключений ========'''

'''
Ошибки -> проблемы с синтаксисом
1. SyntaxError: забыли двоеточие, скобку
2. IndentationError: неправильный отступ
3. TabError: неправильная табуляция
'''
# 2f = 8

# Исключения: (код написан правильно, но работает не так, как ожидалось)
# 1.  ArithmeticError 
#    ZeroDivisioError
# 2. ValueError 
# 3. NameError
# 4. TypeError
# 5. KeyError
# 6. IndexError
# 7. AttributeError
# 8. ImportError
# 9. BaseException (прородитель)

ZeroDivisionError # при делении на 0
# 8 / 0
# 4 // 0
# 3 % 0

ValueError # вызывается при распаковке, переводе одного типа данных в другой
# int('hello')
# a = 'asd'
# k, b = a

NameError # когда обращаемся к несуществующей переменной

# print(b)


TypeError # когда передаем в функцию, метод меньше или больше аргументов, чем требуется

# for i in 2345677:
#     print(i)
# [].append()
# [].append(1, 2, 3)
# '5' + 5

KeyError # при обращении к несуществующему ключу

dict_ = {'a': 1}
# dict_['b']
# dict_.pop('b')

IndexError # при обращении к несуществующему индексу

list_ = ['a', 'b', 'c']
# list_[4]
# list_.pop(3)


AttributeError # когда обращаемся к несуществцющему методу или атрибуту объекта

# a = 12341
# a.upper()
# b = [1, 2, 3]
# b.discard()

ImportError # неправильный импорт

# import math
# from math import pi2


# BaseException -> прородитель


'''===== try except ====='''
# чтобы код не прекращал свою работу

'''Синтаксис'''

# try:
#     тело try
#     # код, который может вызвать ошибку
# except:
#     тело except
#     # код, который сработает, если в try возникнет ошибка
# else:
#     тело else
#     # код, котрый отработает, если в блоке try не возникло ошибки
# finally:
#     тело finally
#     # код, который отработает в любом случае

# def division(num1, num2):
#     return num1/num2

# try:
#     num = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     res = num / num2
#     # res = division(num, num2)
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели не число или на ноль делить нельзя')
    
#     num = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     res = num / num2
#     # res = division(num, num2)
#     print(res)

# # except ZeroDivisionError:
# #     print('На ноль делить нельзя')
# else:
#     print(f'{num} / {num2} = {res}')

# finally:
#     print('Пока')


# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')

# dict_ = {key: key  2 for key in range(11)if key % 2 == 0}
# print(dict_)
# try:
#     dict_ = {key: key  2 for key in range(11)if key % 2 == 0}
#     # print(dict__)
#     value = dict_[100]
#     print(value)
# # except:
# #     pass
# except NameError:
#     print('Переменна dict__ не объявленна ')
# except KeyError:
#     print('такого ключа нет')
#     print(dict_)
#     key = int(input('Введите ключ: '))
#     print(dict_[key])

# from math import factorial as fact 
# fact()

# try:
#     i = int(input())
# except Exception as e:
#     print(e)

"""напишите программу, в которая будет принимать от пользователя два числа и складывать их"""

# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
# except ValueError:
#     # print('Вы ввели не число')
#     # num1 = 10
#     # num2 = 99
#     print(num1 + num2)
# else: 
#     print('ошибка не возникла')
# finally:
#     print(num1 + num2)

# count = 0
# while True:
    
#     try:
#         a = int(input('Введите число: '))
#         b = int(input('Введите число: '))
#         res = a + b
#     except ValueError:
#         a = int(input('Введите число: '))
#         b = int(input('Введите число: '))
#         res = a + b
    
#     count += 1
#     print(res, count)
#     if count == 3:
#         break


'''======   raise   ======'''
# Исскуственно вызывать ошибки
# try:
#     age = int(input('введите возраст: '))
#     if age < 18:
#         raise ValueError('Доступ закрыт')
#     print('чек')
# except ValueError:
#     print('вы ввели не число или вам нет 18')



# try:
#     age = int(input())
     
#     if age < 18:
#         raise ValueError('Доступ запрещён') 
# except:
#     print('Введён некорректный возраст') 
# else: 
#     print('Спасибо') 
# finally: 
#     print('До свидания!')

# try: 
#     num1 = int(input()) 
#     num2 = int(input()) 
#     print(num1/num2) 
# except(ValueError, ZeroDivisionError)as error:
    
#     print('Произошла ошибка!')


# try: 
#     cash = int(input()) 
#     if cash < 0: 
#         raise Exception ('ValueError') 
#     print(cash) 
# except: 
#     print('Сумма не может быть отрицательной!')


# try: 
#     password = 'short' 
#     if len(password) < 6: 
#         raise ValueError() 
# except ValueError: 
#     raise ValueError



# def to_fahrenheit(k:int) -> float:
#     assert k>=0,'Холоднее абсолютного нуля!' 
#     res=(k-273.15)*9/5+32 
#     return res 
#     print(to_fahrenheit(3))


# def add_(a, b): 
#     return a + b 
# def sub_(a, b):
#     return a - b
# def mult_(a, b):
#     return a * b 
# def div_(a, b):
#     return a / b 
# def calc(num1,num2, operation):
#     if operation == "+":
#         return add_(num1, num2)
#     elif operation == "-":
#         return sub_(num1, num2)
#     elif operation == "*":
#         return mult_(num1, num2)
#     elif operation == "/":
#         return div_(num1, num2)
#     print(calc(40, 20, operation = "+"))

# users = [ { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'}, { 'name': 'Helen', 'age': 35, 'work': 'Nurse'}, { 'name': 'Bob', 'age': 35, 'work': 'Driver'}, { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'}, { 'name': 'Helga', 'age': 35, 'work': 'IT-HR'} ] 
# def func15(users):
#     r=[] 
#     for i in users:
#         if i['work'].startswith('IT'):
#             r.append(f"{i['name']}, скидки в магазине компьютерной техники!\n")
#             h=''.join(i for i in r) 
#     return h 
# print(func15(users))

