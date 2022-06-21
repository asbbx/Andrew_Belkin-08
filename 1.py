# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

our_str = input('Введите строку: ')

set_for_sort = set()

for i in range(len(our_str)):
    for j in range(len(our_str), i, -1):
        hash_str = hashlib.sha1(our_str[i:j].encode('utf-8')).hexdigest()
        set_for_sort.add(hash_str)

print(f'{len(set_for_sort) - 1} различных подстрок в строке {our_str}')
