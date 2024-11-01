def get_matrix(n, m, value):  # обявление функции
    matrix = []                # пустой список
    for i in range(n):          #цикл for для кол-ва строк матрицы, n повторов
        line=[]                 #пустой список в список matrix.
        for j in range(m):      # второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            line.append(value)   #добавленный пустой список значениями value
        matrix.append(line)
    return matrix

#результат работы функции get_matrix.
result1 = get_matrix(4, 2, 9)
result2 = get_matrix(3, 4, 42)
result3 = get_matrix(4, 3, 25)

print(result1)
print(result2)
print(result3)

