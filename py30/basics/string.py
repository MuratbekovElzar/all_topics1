'''======= Строки  ======='''
#  неизменяемый тип данных, который предназначен для хранения последовательности символов, заключенной в одинарные или двойные кавычки


string = "Строка"
string = 'Строка'
# string = "неправильно' (" ')
string = "don't"
string = 'he: "hello"'

string6 = '''
hello
hkdl
adghghwg'
djsvsljkds
'''
string7 = """
hello
hkdl
adghghwg'
djsvsljkds
"""


# print(string6)


'''Экранированные последовательности'''
# последовательность символов, начинающихся c -> \
'\n' # -> перенос на слудующую строку 
'\t' # -> табуляция 
'\\' # -> для отображения ( \ )
'\'' # -> для отображения одной ковычки ( ' )
'\"' # -> для отображения двойной ковычки ( " )
'\r' # -> возвращает каретку в начало строки
'\v' # -> вертикальная табуляция 



# string = 'sjdgbskjdgslgdlsj;\n\tkghlgjksdglksglkdjg\\'
# string = 'hello\vmakers\vincubator'
# print (string)

'''Конкатенация -> склеивание строк'''
# str_1 = 'hello'
# str_2 = 'world'

# print (str_1 + ' ' + str_2)


'''Дублирование строк'''

# print (str_1, str_1, str_1)
# print (str_1 * 10) (чобы было не слитно, нужно сделать пробел в самой строке str_1 = 'hello ')
'''====== Форматирование строк ====='''
# 1. с использованием %
# 2. с ипользованием метода .format()
# 3. интерполяция строк (f- строки)

# %
# name = input ('Enter your name: ')
# result = 'Hello, %s' %name
# print (result)

# .format()
# name = input ('Enter your name: ')
# age = input ('Enter your age: ')
# test = input ('Enter your age: ')
# result = 'hello, {} {} {}'.format(name,age,test)
# print(result)

# f - строки
# name = input ('Enter you name: ')
# age = input ('Enter your age: ')
# test = input ('Enter your age: ')
# result = f'hello {name} your {age} years old {test}'
# print(result)


'''======= Индексы ======='''
#  Порядковый номер символов в строке 
' h e l l o   w o r l d '
# 0 1 2 3 4 5 6 7 8 9 10
#-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
str_ = 'hello world'
# print(str_[0]) # получение первого элемента 'h'
str_[1] # 'e'
str_[2] # получение послденего элемента строки 'd'

'''===== Срезы ====='''
# получение подстраки (какой-то части строки)
# Синтаксис [начало : конец : шаг]
# print(str_[:5])
# print(str_[6:])
# print(str_[:-2])

'переверните строку используя сразы'
'''
пример: str_ = 'hello'
вывод : 'olleh'
'''
# str_ = 'hello'
# print(str_[::-1])
# Cрезы по индексу -> [3:] -> начиная с 3 индекса до самого конца [:6] -> с 0 индекса до 6 (не включительно), [::]  [:] [0::1] -> вся строка, [::-1] -> перевернуть строку 

'''======= Методы строк ======'''
# метод - та же самая функция, но обращаемая к нему через точку
# print(dir('hello'))

# методы на is
# возвращают True/False
# str.isalnum() # -> состоит ли строка только из букв и/или чисел
# str.isalpha() # -> состоит ли строка только из букв
# str.isdigit() # -> состоит ли строка только из чисел
# str.islower() # -> находится ли строка в нижем регистре 
# str.isupper() # -> состоит ли строка из символов верхнего регистра
# str.isspace() # -> состоит ли строка из неотображаемых символов (пробелы и экранированные последовательности)
# str.isnumeric() -> состоит ли строка только из чисел 


# print('hello'.isalpha()) True
# print('hello9'.isalpha()) False (потому что есть цифра 9)
# print('12344'.isdigit()) True
# print('123445 '.isdigit()) False (потому что есть пробел после цифры 5 ')

# str.upper() -> переводит в верхний регистр
# str.lower() -> переводит в нижний регистр

# str_ = 'Makers'
# a = str_.lower() #makers
# print(a)

# str_ = 'makers'
# a = str_.upper() #MAKERS
# print(a)

# str.title() -> каждое слово в строке пишется с заглавной буквы

# str.capitalize() -> только самое первое слово в строке запишет с заглавной буквы
# str_ = 'hello Mekers'
# print(str_.title()) # Hello Makers
# print(str_.capitalize()) #Hello makers 

# strip() -> убирает пробелы в начале и в конце строки (rstrip, lstrip)
# len() -> возвращает длину строки
# 
# a = input('here: ')
# b = a.strip()
# print(len(a), a, len(b), b)


# str.replace(old, new, count) -> заменяет old значение в строке на new, count - отвечает за кол-во замен

# str_ = 'ha ha ha a'
# new_str = str_.replace('ha', 'new', 1)
# print(new_str)

# str.split('разделитель') -> делит строку по разделителю и возвращает список. разделитель по умолчанию -> пробел

# a = 'hello makers boot incubator test'
# b = a.split('t')
# print(b)
# a = 5
# b = 10
# print (a + b)


# name_of_list = ['1234567'] 
# new_list = name_of_list[0] 
# i = len(new_list) 
# if i%2==0:
#     new_list = name_of_list[0][i//2:] + name_of_list[0][:i//2] 
# else:
#     new_list = name_of_list[0][i//2+1:] + name_of_list[0][:i//2+1] 
#     print(list(new_list))