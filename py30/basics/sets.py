'''Множества -> set()'''
# изменяемыый, неупорядоченный, неиндексируемый, итерирукмый тип данных, который хранит в себе только уникальные значения
# литералы -> {}

''' Создание пустого множества '''
# set_a = set()
# print(type(set_a))

# set_b = {1, 2, 3}
# print(set_b)

''' Элементами множества могут быть только неизменяемые типы данных '''


# set_ = set({1: 'a', 2: 'b', 3: 'c'})
# set_= set([1, 2, 3, 4])
# set_ = set ('Makersaaaaad')
# print(set_)

''' Методы множества '''
# print(dir(set))

# set.add(element) -> добавляет element во множество 
''' Если добавляем tuple, то все его элементы должны быть неизменяемыми'''
# set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'test', 'world'}
# set_a.add('hello') -> добавить слово целеком
# a = 4
# set_a.add(a)
# print(set_a)

# for i in range(101):
#     set_a.add(i)
# print(set_a)


# set.update(iterable) -> добовляет элементы из последовательности во множество 
# set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'test', 'world'}
# set_a.update([1, 2, 3, 'Makers', 'makers'])
# set_a.update('hello') -> добавляет по элементам (т.е по отдельности)
# print(set_a)
# set_b =set()
# a = [[1, 2, 3], [4, 5 ,6], [7, 8, 9]]
# for i in a:
#     print(i)
#     set_b.update(i)
    
# print(set_b)



# set.clear() -> очищает множество 
# set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'test', 'world'}
# set_a.clear()
# print(set_a)

# set.pop() -> удаляет рандомный элемент из множества (первый в текущем порядке)
# set_a = {'world', 8, 9, 'hello', 'test', }
# print(set_a)
# print(set_a.pop())
# print(set_a)
# print(set_a.pop())
# print(set_a)
# print(set_a.pop())
# print(set_a)


# set_a.difference(set) -> возвращает элементы, которые есть в set_a но нет в set_b (можно использовать минус ('-'))

# set_a = {1, 2, 3, 4, 5, 'hello', 'test'}
# set_b = {4, 5, 6, 7, 8, 'test'}
# print(set_b-set_a)
# print(set_a.difference(set_b))
# print(set_b.difference(set_a))


#  set_a.symmetric_difference(set_b) -> возвращает уникальные элементы для set_a и set_b (уникальные для обоих множеств)

# set_a = {1, 2, 3, 4, 5, 'hello', 'test'}
# set_b = {4, 5, 6, 7, 8, 'test'}
# print(set_a.symmetric_difference(set_b))
# print(set_b ^ set_a)


# set_a.intersection(set_b) -> возвращает схожие элементы обоих множеств
# set_a = {1, 2, 3, 4, 5, 'hello', 'test'}
# set_b = {4, 5, 6, 7, 8, 'test'}
# # print(set_a.intersection(set_b))
# print(set_a & set_b)


# set_a.union(set_b) -> соединяет два множества 
# set_a = {1, 2, 3, 4, 5, 'hello', 'test'}
# set_b = {4, 5, 6, 7, 8, 'test'}
# list_ = [8, 9, 0, 't']
# print(set_a.union(set_b))
# print(set_a | set_b)
# print(set_a.union(list_))
# print(set_a | list_) -> выйдет ошибка Error

''' Д/З
set.difference_update()
set.intersection_update()
set.symmetric_difference_update()
set.isdisjoint()
set.issuperset()
set.issubset()
'''




