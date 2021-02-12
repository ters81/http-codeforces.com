
# B. Прошлогодняя подстрока
# https://codeforces.com/problemset/problem/1462/B

# У Поликарпа есть строка s[1…n] длины n, состоящая из десятичных цифр. Поликарп делает следующую операцию со строкой s
# не более одного раза (то есть делает операцию 0 или 1 раз):
#
# Поликарп выбирает два числа i и j (1≤i≤j≤n) и удаляет из строки s символы на позициях i,i+1,i+2,…,j (то есть удаляет
# подстроку s[i…j]). Более формально, Поликарп превращает строку s в строку s1s2…si−1sj+1sj+2…sn.
# Например, строку s=«20192020» Поликарп может превратить в строки:
#
# «2020» (в таком случае (i,j)=(3,6) или (i,j)=(1,4));
# «2019220» (в таком случае (i,j)=(6,6));
# «020» (в таком случае (i,j)=(1,5));
# возможны и другие ходы, выше перечислены лишь только некоторые из них.
# Поликарпу очень нравится строка «2020», поэтому ему интересно, можно ли превратить строку s в строку «2020» не более
# чем за одну операцию? Заметьте, что проводить ноль операций допустимо.
#
# Входные данные
# В первой строке находится целое число t (1≤t≤1000) — количество наборов входных данных. Далее следуют t наборов
# входных данных.
#
# В первой строке каждого набора содержится целое число n (4≤n≤200) — длина строки s. В следующей строке находится
# строка s длины n, состоящая из десятичных цифр. Допустимо, что строка s начинается с цифры 0.
#
# Выходные данные
# Для каждого набора входных данных в отдельной строке выведите:
#
# «YES», если Поликарп может превратить строку s в строку «2020» не более чем за одну операцию (то есть за 0 или 1 операцию);
# «NO» в противном случае.
# Вы можете выводить «YES» и «NO» в любом регистре (например, строки yEs, yes, Yes и YES будут распознаны как положительный ответ).
#
# Пример
# входные данные
# 6
# 8
# 20192020
# 8
# 22019020
# 4
# 2020
# 5
# 20002
# 6
# 729040
# 6
# 200200
# выходные данные
# YES
# YES
# YES
# NO
# NO
# NO
# Примечание
# В первом наборе входных данных Поликарп мог выбрать i=3 и j=6.
#
# Во втором наборе входных данных Поликарп мог выбрать i=2 и j=5.
#
# В третьем наборе входных данных Поликарп не делал ни одну операцию со строкой.



for _ in range(int(input())):
    n = int(input())
    s = input()

    if s[0:4] == '2020' or s[-4::] == '2020':
        print("YES")
    elif s[0] == '2' and s[-3::] == '020':
        print("YES")
    elif s[0:2] == '20' and s[-2::] == '20':
        print("YES")
    elif s[0:3] == '202' and s[-1] == '0':
        print("YES")
    else:
        print("NO")






