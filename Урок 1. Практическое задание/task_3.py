"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

companies = {'comp_1' : 20000, 'comp_2' : 40000, 'comp_3' : 50000,
             'comp_4' : 110000, 'comp_5' : 30000, 'comp_6' : 40000}

# Сложность O(n) -- Линейная

best_3 = []                             # O(1)
while len(best_3) < 3:                  # O(1)
    max_value = 0                       # O(1)
    for i, j in companies.items():      # O(n)
        if j > max_value:               # O(1)
            best_c = i                  # O(1)
            max_value = j               # O(1)
    best_3.append(best_c)               # O(1)
    companies.pop(best_c)               # O(1)

print(best_3)

# Сложность O(n*log(n)) - Линейно-логарифмическая

companies = sorted(companies.items(), reverse=True, key=lambda item: item[1])   # O(n*log(n))
for i in range(3):                                                              # O(1)
    print(companies[i])                                                         # O(1)

# Первое решение с линейной сложностью оптимальнее, т.к. при линейно-логарифмический сложности
# количество операций растет быстрее при увеличении n
