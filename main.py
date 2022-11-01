#!/bin/python3

if __name__ == '__main__':
    s = input()

s_set = set(s) # создает список уникальных ключей для дальнейшей итерации
s_dict = dict()

for i in s_set:
    s_dict[i] = s.count(i)
    
# Двойная сортировка дает нужный результат: сначала алфавитный порядок, потом по количеству вхождений.
final_ordered_suite = sorted(sorted(list(s_dict.items())), key=lambda item: item[1], reverse=True)

count = 0 # счетчик для вывода на печать (по условиям требуется только 3 символа)
for i in final_ordered_suite:
    print(*i)
    count += 1 
    if count == 3:
        break
