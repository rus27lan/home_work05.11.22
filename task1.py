"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

class Matrix:

    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2

    def __str__(self):
        print('Матрицы для сложения')
        for row in lst1: print(' '.join(list(map(str, row))))
        print()
        for row in lst2: print(' '.join(list(map(str, row))))
        return ('')

    def __add__(self):
        result = [[lst1[i][j] + lst2[i][j] for j in range
        (len(lst1[0]))] for i in range(len(lst1))]
        for row in result: print(' '.join(list(map(str, row))))
        return ('')

lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
lst = Matrix(lst1, lst2)
print(lst.__str__())
print("Сумма матриц:")
print(lst.__add__())


