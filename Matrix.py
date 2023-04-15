"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который 
должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой 
строки второй матрицы и т.д.
"""


class Matrix:
    def __init__ (self, matrix):
        self.matrix = matrix
       
    def __str__(self):
        lst = []
        for i in range(len(self.matrix)): 
            string =" ".join(map(str,self.matrix[i]))
            lst.append(string)
            matrix_as_str = "\n".join(lst)
        return matrix_as_str
    
    def __add__(self, other):
        for i in range(len(self.matrix)):
            for el in range (len(self.matrix[i])):
                res_1 = self.matrix[i][el]
            return res_1
        for i in range(len(other.matrix)):
            for el in range (len(other.matrix[i])):
                res_2 = other.matrix[i][el]
                matrix = self.matrix[i][el] + other.matrix[i][el]
        return matrix
            
matrix_1 = [[1,2,3],[4,5,6]]
matrix_2 = [[2,3,5],[6,7,8]]
obj_1 = Matrix(matrix_1)
obj_2 = Matrix(matrix_2)
print(obj_1)
print(' ')
print(obj_2)
print(obj_1+obj_2)
