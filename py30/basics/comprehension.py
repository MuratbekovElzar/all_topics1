'''==== Comprehension ===='''
# Генератор последовательности в одну строку используя цикл for (синтаксический сахар)

# for  переменная in диапазон:
#     тело 

''' Синтаксис '''
# 1. результат for элемент in итерируемый объкт

# 2. результат for элемент in итерируемый объкт if фильтр 


'''=== List comprehensoin ==='''
# упрощение процесса создание списков 

# list_ = []
# for i in 'hello':
#     list_.append(i)
    
# print(list_)

# list_1 = [i for i in 'hello']
# print(list_1)

# list_0 = list((i for i in 'hello'))

# list_1 = [i for i in 'hello']
# print(list_1)

# import time
# start_time = time.time()
# list_ = []
# for i in range(1, 1000001):
#     list_.append(i)
    
# print(time.time() - start_time)
# # print(list_)

# start_time = time.time()
# list_num = [number for number in range(1, 1000001)]
# print(time.time() - start_time)

'''создайте список от 1 до 10, состоящих только из четных элементов'''
# list_ = [i for i in range(1, 11) if i % 2 == 0]
# print(list_)

# list_ = [i for i in range(2, 11, 2)]
# print(list_)

# list_ = []
# for i in range(1, 11):
#     if i % 2 ==0:
#         list_.append(i)
# print(list_)

# print(['hello' for i in range(10)])

# print([input() for i in range(10)])

# [элемент if условие else элемент2 for i in итерируемый объект]

# a = ['четное ' 
#     if i % 2 == 0 
#     else 'нечетное' 
#     for i in range (1, 11)
#     ]
# print(a)

# list_str = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list_str.append('четное')
#     else:
#         list_str.append('нечетное')
#     print(list_str)


'''=== Set comprehension ==='''
# list_ = [1, 2, 1, 1, 2, 'test', 3, 5, 'Python', 6, 6, 'hello']
# set_l = {i + 'world' for i in list_ if type (i) == str}

# set_l = {i + ' world' if type(i) == str else i + 1 for i in list_}
# print(set_l)


# set_ = set()
# for i in list_:
#     set_.add(i)
    
# print(set_)

'''=== Dict comprehension ==='''
# dict_ = {1: 'a', 2: 'b', 3: 'c'}

# dict_1 = {}
# for k, v in dict_.items():
#     dict_1.update({v: k})

# print(dict_1)    

# dict_1 = {v: k for k, v in dict_.items()}
# print(dict_1)

# dict_ = {}
# for i in range(1, 11):
#     dict_.update({i: i**2})
    
# print(dict_)

# # [(1, 2), (3, 4)]
# dict_1 = {i: i ** 2 for i in range(1, 11)}
# print(dict_1)


# list_ = [1, 1, 2, 3, 5, 5, 6, 6, 8, 7]
# dict_1 ={i: list_.count(i) for i in list_}
# print(dict_1)


# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# {'a': 'нечетное', 'b': 'честное'}

# dict_abc = {k: ('четное' if v % 2 == 0 else 'нечетное') for k, v in dict_.items()}
# print(dict_abc)

'даны 2 списка, создайте словарь, где ключи - элементы 1 списка, а значения - второго'
# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# dict_list = {
#     list1[index]: '->'.join (list2) 
#     for index in range(len(list2))
#     }

# print(dict_list)

# 'объединитель'.join(list_) -> переводит список в тип данных строки

# ''.join(['a', 'b', 'c',]) -> 'abc'


'''=== вложенные comprehension ==='''

# dct = {
#     i: 
#     [j for j in range(1, i+1)] 
#     for i in range(1, 6)
#     }
# print(dct) 

# list_ = [
#     ['hello world' for i in range(2)] # element (i)
#     for i in range(3)
#     ]
# print(list_)

employees = {
    'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
            }
}


# dct = {
#     key:
#     {k: float(v)
#     if k =='age' else v 
#     for k, v in value.items()
#     }
#     for key, value in 
#     employees.items()
#     }

# print(dct)


# for info in employees.values():
#     for k, v in info.items():
#         if k == 'age':
#             info[k] = float(v)

# print(employees)