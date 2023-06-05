print("\033[33m{}\033[0m".format('*** 1. Ввод данных от пользователя и преобразование введённой последовательности в список ***'))
try:
    sequence_of_numbers = input('Введите последовательность целых чисел через пробел: ').split()
    while len(sequence_of_numbers) == 0:
        print("\033[31m{}\033[0m".format('*** Вы ничего не ввели! ***'))
        sequence_of_numbers = input('Введите последовательность целых чисел через пробел: ').split()
    array = list(map(int, sequence_of_numbers))
except ValueError:
    print("\033[31m{}\033[0m".format('*** Неккоректный ввод!!! Запустите программу заново! ***'))
else:
    while ValueError:
        try:
            any_number = int(input('Введите любое целое число: '))
            break
        except ValueError:
            print("\033[31m{}\033[0m".format('    *** Ввод некорректный, повторите ввод! ***'))

    print(f'Получившийся список = {array}')
    print("\033[33m{}\033[0m".format('\n*** 2. Сортировка списка по возрастанию элементов в нем ***'))

    def sort_ascending(array):   # функция сортировки списка по возрастанию
        for i in range(len(array)):
            idx_min = i
            for j in range(i, len(array)):
                if array[j] < array[idx_min]:
                    idx_min = j
            if i != idx_min:
                array[i], array[idx_min] = array[idx_min], array[i]
        return array

    print(f'Отсортированный список = {sort_ascending(array)}')

    print("\033[33m{}\033[0m".format('\n*** 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу. ***'))
    def binary_search(array, any_number, left, right):    # функция алгоритма двоичного поиска
        if left > right:
            return f'Индекс меньшего числа равен {left-1}, индекс большего числа или равного введенному числу равен {right+1}.'
        middle = (right + left) // 2
        if array[middle] == any_number:
            return f'Индекс меньшего числа равен {middle-1}, индекс большего числа или равного введенному числу равен {middle}.'
        elif any_number < array[middle]:
            return binary_search(array, any_number, left, middle - 1)
        else:
            return binary_search(array, any_number, middle + 1, right)

    print(f'Вы ввели число {any_number}.')
# вывод искомых индексов чисел списка
    if array[0] == any_number or array[0] > any_number:
        print('Нет числа меньше введеного, индекс большего числа или равного введенному числу равен 0.')
    elif array[len(array)-1] == any_number:
        print(f'Индекс меньшего числа равен {len(array)-2}, индекс большего числа или равного введенному числу равен {len(array)-1}.')
    elif array[len(array)-1] < any_number:
        print(f'Нет числа больше введеного, индекс меньшего числа равен {len(array)-1}.')
    else:
        print(binary_search(array, any_number, 0, len(array)))