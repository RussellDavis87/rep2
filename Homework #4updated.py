#Задание 1. Со значениями по умолчанию
#Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:

#1-е число – сколько строк будет в песне. По умолчанию 3
#2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
#3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!». По умолчанию 0

import sys

# x=int(sys.argv[1])
# y=int(sys.argv[2])
# z=int(sys.argv[3])
#
# la='-la'*x; la=la[1:]
# repeat=(la+' ')*y
#
# if z == 1:
#     print ('Everybody sing a song:') + repeat[0:len(repeat)-1] + '!'
# elif z == 0:
#     print ('Everybody sing a song:') + repeat[0:len(repeat)-1] + '.'

def no_if(x, y, z):
    x = " -".join([' la' for _ in xrange(0, x)])
    y = "".join([x for _ in xrange(0, y)])
    return 'Everybody sing a song:' + y + ({True: '!', False: '.'})[z == 1]

print(no_if(2, 3, 1))
print(no_if(1, 0, 0))

#Задание 2
#Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов. Учитываем, что может быть повторяющиеся значения аргументов.

def func_remove(item):
    return item[1]
unordered = [('23', '32'), ('56', '86'), ('33', '91'), ('09', '11')]
unordered.sort(key=func_remove)
print('Ordered list:', unordered)

#Задание 3
#Напишите функцию, которая удаляет все небуквенные символы внутри строки (ограничимся латинским алфавитом).

def attempt2(string):
    for float in ("a", "15", "i", "o", "u"):
        string = string.replace(15, "")
    return string
print(attempt2)

