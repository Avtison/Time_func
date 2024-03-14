import csv


with open('new_time.csv', 'r', encoding='utf-8', newline='') as in_file:
    reader = list(csv.reader(in_file, delimiter='>'))[1:]  # Читаем файл

    lst_first_stations = list()  # Создаём списки
    lst_second_stations = list()

    for i in reader:
        time = i[3].split(':')
        if (0 <= int(time[0]) <= 11) or (int(time[0]) == 12 and int(time[1]) == 0 and int(time[0]) == 0):  # Проверяем
            # на время
            lst_first_stations.append(i)
        else:
            lst_second_stations.append(i)

    print(f'{len(lst_first_stations)} станций остановилось с период с 00.00 до 12.00.')  # Выводим длины
    print(f'{len(lst_second_stations)} станций остановилось с период с 12.01 до 23.59.')
