
# B. Азбука Борзе
# https://codeforces.com/problemset/problem/32/B

# Сейчас в Берляндии популярна троичная система счисления. Для телеграфной передачи чисел,
# записанных в троичной системе счисления, используется азбука Борзе. Цифра 0 передается как «.», 1 как «-.», 2 как «--».
# Расшифровка кода Борзе чисел — очень важная и ответственная работа. Ваша задача — расшифровать заданное в коде Борзе троичное число.
#
# Входные данные
# В первой строке записано число в коде Борзе. Длина кода не меньше 1 и не больше 200 символов.
# Гарантируется, что заданная строка — корректный код Борзе некоторого числа в троичной системе счисления (число могло содержать лидирующие нули).
#
# Выходные данные
# Выведите расшифровку заданного кода Борзе. Расшифрованное число может содержать лидирующие нули.
#
# Примеры
# входные данные
# .-.--
# выходные данные
# 012

# входные данные
# --.
# выходные данные
# 20

# входные данные
# -..-.--
# выходные данные
# 1012


s = list(input())

item = ''

while len(s) > 0:
    if s[0] == '.':
        del s[0]
        item = item + '0'
    elif s[0] == '-' and s[1] == '.':
        del s[0:2]
        item = item + '1'
    else:
        del s[0:2]
        item = item + '2'

print(item)