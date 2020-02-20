
import numpy as np
import random
import operator 
from heapq import nlargest 


from os import listdir 
from os.path import isfile, join 

import collections 


class TprogerAndGeekBrainsTasks:
    

    def __init__(self):
        print("Задачи по Python для начинающих от Tproger и GeekBrains")

    def randomIntArray(self, size):
        return np.random.randint(0, 9, size)


    # def randomArray(self, size):
    #     # почему подчеркивает np
    #     return np.random.sample(size)
    


    # Задача 1
    # Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
    # Выведите все элементы, которые меньше N.
    def solveTask1(self, array, N):
        return [elem for elem in array if elem < N]

    # Задача 2
    # Даны списки:
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
    # Нужно вернуть список, который состоит из элементов, общих для этих двух 
    # списков.
    def solveTask2(self, arrayA, arrayB):
        return list(set(arrayA) & set(arrayB))

    # Задача 3
    # Отсортируйте словарь по значению в порядке возрастания и убывания.
    # d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    def sortDictInIncreasingOrder(self, value):
        return dict(sorted(value.items(), key=operator.itemgetter(1)))

    def sortDictInDescendingOrder(self, value):
        return dict(sorted(value.items(), key=operator.itemgetter(1), reverse=True))


    # Задача 4
    # Напишите программу для слияния нескольких словарей в один.
    # dict_a = {1:10, 2:20} 
    # dict_b = {3:30, 4:40} 
    # dict_c = {5:50, 6:60}
    def mergeDictionary(self, arrayWithDictionary):
        return {key:val for d in arrayWithDictionary for key,val in d.items()}


    # Задача 5
    # Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
    def highValueInDictionary(self, dictionary, count):
        return sorted(dictionary, key=dictionary.get, reverse=True)[:count]

    # Задача 7
    # Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на 
    # вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух 
    # расположенных над ним чисел.
    def pascalTriangle(self, n): 
        row = [1] 
        y = [0] 
        for x in range(max(n, 0)): 
            print(row) 
            row = [left + right for left, right in zip(row + y, y + row)] 

    # Задача 8
    # Напишите проверку на то, является ли строка палиндромом. Палиндром — это 
    # слово или фраза, которые одинаково читаются слева направо и справа налево.
    def isPalindrome(self, string): 
        return string == ''.join(reversed(string)) 

    # Задача 9
    # Сделайте так, чтобы число секунд отображалось в виде 
    # дни:часы:минуты:секунды.
    def convertSeconds(self, seconds): 
        days = seconds // (24 * 3600) 
        seconds %= 24 * 3600 
        hours = seconds // 3600 
        seconds %= 3600 
        minutes = seconds // 60 
        seconds %= 60 
        return f'{days} days : {hours} hours : {minutes} minutes : {seconds} seconds'

    # Задача 10
    # Вы принимаете от пользователя последовательность чисел, разделённых запятой. 
    # Составьте список и кортеж с этими числами.
    def listAndTupleWithNumeric(self):
        values = input('Введите числа через запятую: ') 
        ints_as_strings = values.split(',') 
        ints = map(int, ints_as_strings) 
        lst = list(ints) 
        tup = tuple(lst) 
        return {"list": lst, "tuple": tup}

    # Задача 11
    # Выведите первый и последний элемент списка.
    def getFirstAndLastElement(self, array):
        return {"first": array[0], "last": array[-1]}
    
    # Задача 12
    # Напишите программу, которая принимает имя файла и выводит его расширение. 
    # Если расширение у файла определить невозможно, выбросите исключение.
    def getExtension(self, filename): 
        filename_parts = filename.split('.') 
        if len(filename_parts) < 2:  # filename has no dots 
            raise ValueError('the file has no extension') 
        first, *middle, last = filename_parts 
        if not last or not first and not middle: 
            # example filenames: .filename, filename., file.name. 
            raise ValueError('the file has no extension') 
        return filename_parts[-1] 

    # Задача 13
    # При заданном целом числе n посчитайте n + nn + nnn.
    def solveTask13(self, n): 
        return n +  int(str(n) * 2)  + int(str(n) * 3) 

    # Задача 14
    # Напишите программу, которая выводит чётные числа из заданного списка и 
    # останавливается, если встречает число 237.
    # numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217] 
    def getEvenFromArray(self, array, stopNumber):
        for x in array: 
            if x == stopNumber: 
                break 
            elif x % 2 == 0: 
                print(x)

    # Задача 15
    # Напишите программу, которая принимает два списка и выводит все элементы 
    # первого, которых нет во втором.
    def solveTask15(self, listA, listB):
        return set(listA) - set(listB)


    # Задача 16
    # Выведите список файлов в указанной директории.
    def getListFilesInDirectory(self, path):
        return [f for f in listdir(path) if isfile(join(path, f))] 

    # Задача 17
    # Сложите цифры целого числа.
    def sumDigits(self, num): 
        digits = [int(d) for d in str(num)] 
        return sum(digits) 

    # Задача 20
    # С помощью анонимной функции извлеките из списка числа, делимые на 15.
    def numbersDivisibleByInArray(self, array, N):
        return list(filter(lambda x: not x % N, array))

    # Задача 21
    # Нужно проверить, все ли числа в последовательности уникальны.
    def allUnique(self, numbers): 
        return len(numbers) == len(set(numbers)) 


    # Задача 22
    # Напишите программу, которая принимает текст и выводит два слова: наиболее 
    # часто встречающееся и самое длинное.

    def getCommonAndLongestInText(self, text):
        words = text.split() 
        counter = collections.Counter(words) 
        most_common = counter.most_common()[0] 
        longest = max(words, key=len) 
        return {"most_common": most_common, "longest": longest}









tasks = TprogerAndGeekBrainsTasks()
print(tasks.getCommonAndLongestInText("lorem ipsum dolor sit amet amet amet"))