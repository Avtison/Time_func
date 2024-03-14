import csv


with open('new_time.csv', 'r', encoding='utf-8', newline='') as in_file:
    reader = list(csv.reader(in_file, delimiter='>'))[1:]  # Читаем файл

    for i in range(len(reader)):  # Производим сортировку за O(n^2)
        for k in range(len(reader) - 1):
            if reader[k][1] > reader[k + 1][1]:
                reader[k], reader[k + 1] = reader[k + 1], reader[k]

    for i in range(3):  # Выводим нужные нам станции и каюты
        print(f'На станции {reader[i][1]} в каюте {reader[i][2]} восстановлено время. Актуальное время: {reader[i][4]}')
