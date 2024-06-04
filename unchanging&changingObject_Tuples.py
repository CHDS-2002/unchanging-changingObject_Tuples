# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными

import os
import random

# Зададим цвет шрифта консоли - голубой
os.system('COLOR B')

LEFT = 0  # LEFT - левая граница
RIGHT = 20  # RIGHT - правая граница
TYPE_COUNT = 10  # TYPE_COUNT - количество типов данных
MULTIPLIER = 100  # MULTIPLIER - множитель

LEFT0 = ord('A')  # LEFT0 - код символа A
RIGHT0 = ord('Z')  # RIGHT0 - код символа Z
LEFT1 = ord('a')  # LEFT1 - код символа a
RIGHT1 = ord('z')  # RIGHT1 - код символа z
LEFT2 = ord('А')  # LEFT2 - код символа А
RIGHT2 = ord('я')  # RIGHT2 - код символа я

# Типы данных
# int, float, complex, str, bool
# list, tuple, dict, set, frozenset

immutable_var = []  # immutable_var - кортеж
mutable_var = []  # mutable_var - список
RANGE = random.randint(LEFT, RIGHT)  # RANGE - диапозон
INTERVAL = random.randint(LEFT, RIGHT)  # INTERVAL - интервал

for i in range(INTERVAL):
    RANGE = random.randint(LEFT, RIGHT)

    integer = random.randint(LEFT, RIGHT)
    # integer - целочисленное число
    double = random.random() * MULTIPLIER
    # double - вещественное число
    comp = complex(random.random() * MULTIPLIER,
                   random.random() * MULTIPLIER)
    # comp - комплексное число
    boolean = bool(random.choice([0, 1]))
    # boolean - логическое значение
    string = ''.join([random.choice([
        random.choice([
            chr(random.randint(LEFT0, RIGHT0)),
            chr(random.randint(LEFT1, RIGHT1))
        ]),
        chr(random.randint(LEFT2, RIGHT2)),
        ' ',
        '.',
        ';',
        ',']
    )  # string - строка
        for _ in range(RANGE)])

    info = [integer, double, comp, string, boolean]
    # info - список различных данных
    lis = list([random.choice(info) for _ in range(RANGE)])
    # lis - список различных данных
    tup = tuple([random.choice(info) for _ in range(RANGE)])
    # tup - кортеж различных данных
    dictionary = dict(
        (random.choice(info[:len(info) - 2]), random.choice(info)) for _ in range(RANGE)
    )
    # dictionary - словарь различных данных
    sets = set([random.choice(info) for _ in range(RANGE)])
    # sets - множество различных данных
    frozensets = frozenset([random.choice(info) for _ in range(RANGE)])
    # frozensets - фиксированное множество различных данных

    data = [
        integer,
        double,
        comp,
        boolean,
        string,
        lis,
        tup,
        dictionary,
        sets,
        frozensets
    ]
    # data - список различных типов и структур данных

    immutable_var.append(random.choice(data))  # заполняем кортеж
    mutable_var.append(random.choice(data))  # заполняем список

immutable_var = tuple(immutable_var)
# преобразование из списка в кортеж

# Выводим информацию о кортеже и списке
print('\nИНФОРМАЦИЯ О КОРТЕЖЕ И СПИСКЕ:\n')
print('Кортеж:', immutable_var, end='.\n')

try:
    index = random.randint(LEFT, RIGHT)
    # index - случайный индекс
    immutable_var[index] = random.choice(data)
    # пытаемся изменить кортеж
    # отказ в изменении обусловлен наличием
    # фиксированной памяти
except:
    print('Попытка изменения кортежа!\n')

print('Список:', mutable_var, end='.\n')
size = mutable_var.__len__()  # size - размер mutable_var

for i in range(size):
    mutable_var[i] = random.choice(data)
    # заполняем mutable_var

print('Изменённый список:', mutable_var, end='.\n\n')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
