'''===== Словари (dict) ====='''
# изменяемый тип данных, неиндексируемый, упорядоченный, итерируемый тип данных 

# {ключ: значение}

# {} -> литералы
'''Способы создания словарей'''
# dict_ = {}
# print(type(dict_))

# dict_1 = dict(a= 'hello', b= 1),
# print(dict_1)

# dict_ = dict((['key', 'value'],['o', 'v']))

# # dict_ = dict(['12', 'cd', 'ef'])
# # print(dict_)

# key, value = 'ab'
# print(key, value)



# ключи должны быть неизменяемым типом данных 

# {[]: 1} -> TypeError: unhashable type: 'list'

# ключи  -> должны быть уникальными

# a = {1: 'hello', 1: 'world', 1: 1}
# print(a) # {1: 1}

# значение -> могут относиться к любому типу данных

# dict_={
#     'name': 'Aiana',
#     'last_name': None,
#     'email': True,
#     'info': [1, 2, 3, 4]
# }

# print(dict_['info']) -> получение значения по ключу

# dict_['email'] = 'test@gmail.com' # изменение значение по ключу
# print(dict_)
# dict_['email1'] # KeyError: 'email1'
# dict_['email'] = 12 # добавляет новую папку в словарь {..., 'email': 12}

# print(dict_)

'''=== Методы словарей ==='''
# print(dir(dict))
# dict.items() -> возвращает все пары в словаре, в виде списка с кортежами
# print(dict_.items())  -> dict_items([('name', 'Aiana'), ('last_name', None), ('email', True), ('info', [1, 2, 3, 4])])

# for key, value in dict_.items():
#     print(key, '-->', value)

# a, b, c = (1, 2, 3)
# print (a, '-->', b, '-->', c)


# dict.values() -> для получения всех значений в словаре

# print(dict_.values())
# for i in dict_.values():
#     print(i)


# dict.keys() -> для получения всех ключей словаря

# print(dict_.keys())
# for i in dict_.keys():
#     print(i)


# dict.clear() -> используется для очищения словаря 
# dict_.clear()
# print(dict_)

# del dict_ -> удаляет объект
# print(dict_)

# dict.copy -> возвращает копию словаря 
# dict_copy = dict_.copy()
# print(dict_copy) 


# dict.fromkeys(seq, [default]) -> создает словарь с ключами из последовательности и значением default (None)

# list_ = ['name', 'hello', 'test']
# dict_ = dict.fromkeys(list_, 1)
# print(dict_)

# dct = dict.fromkeys('as')
# print(dct)

# dict.get(key, [default]) -> возвращает значение по ключу, если такого ключа нет, не бросает исключение (вызывает ошибку) , а возвращает default, если default  не указан, возвращает None

# dict[key] -> бросает исключение , если такого ключа нет (вызывает ошибку)

# dict_ = {1: 'one', 2: 'two'}
# print(dict_.get(1, 'no such key')) # возвращает one
# print(dict_.get(3, 'no such key')) # возвращает no such key
# print(dict_.get(3)) # возвращает None
# print(dict_[3]) # KeyError: 3

# dict.update(new_dict) -> добавляет new_dict в наш словарь 

# dict_ = {1: 'one', 2: 'two'}

# dict_[5] = 'five' -> добавляет только одну пару
# dict_.update({3: 'three', 4: 'four'})
# new_dict = {5: 'five', 6: 'six'}
# dict_.update(new_dict)
# print(dict_)



# dict.setdefault(key, [default_value]) ->                                                                 1. Работает как get                                                                                        2. если ключа нет, создает новую пару key: default_value, если не указать default_value -> None

# 1.
# dict_ = {1: 'one', 2: 'two'}
# print(dict_.setdefault(1)) #one
2#
# print(dict_.setdefault(3, 'three')) #three
# print(dict_.setdefault(4)) #None
# print(dict_)


'''Удаление элементов словаря'''
# dict.pop(key, [message]) -> удаляет пару ключ, значение и возвращает значение, если ключа нет выводит message (по умолчанию бросает исключение)

# dict_ = {1: 'one', 2: 'two', 3: 'tree'}

# deleted = dict_.pop(1)
# print(dict_, deleted)
# print(dict_.pop(4)) -> # KeyError: 4
# print(dict_.pop (4, 'no such key')) # no such key
# print(dict_, deleted)


# dict.popitem() -> удаляет последнюю пару ключ и значение, и возвращает ключ и значение 

# print(dict_.popitem()) # (3, 'tree')
# print(dict_)

'''поменять местами клюбчи и значения'''


# new_dict = {}
# for key, value in dict_.items():
#     new_dict.update({value: key})
# print(new_dict)





# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# b = {}
# for key, value in a.items():
#     for k, v in value.items():
#         b[key] = v
# print(b)


# dict_ = {'a': 15, 'b': 25, 'c': 40}
# for k, v in dict_.copy().items():
#     if v % 2 == 0:
#         dict_.pop(k)
# print(dict_)

# num = int(input('Введите сумму: '))
# if num < 0:
#     print('сумма не может быть отрицательной')
# else:
#     print(num)