# Python

import csv


with open('new_time.csv', 'r', encoding='utf-8', newline='') as in_file:
    reader = list(csv.reader(in_file, delimiter='>'))[1:]  # Читаем файл
    num = ''
    while num != 'none':  # Начинаем цикл поиска
        num = input('Введите номер каюты: ')
        if num == 'none':  # Это сделано, чтобы при none не выводился else у цикла for
            break
        for i in reader:  # Поиск за O(n)
            if i[2] == num:
                print(f'В каюте {i[2]} восстановлено время (время остановки: {i[3]}). Актуальное время: {i[4]}')
                break
        else:  # Если мы не нашли каюту, то выводим эту строку
            print('В этой каюте все хорошо')
