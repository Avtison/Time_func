import csv


with open('astronaut_time.csv', 'r', encoding='utf-8', newline='') as in_file:  # Открываем исходный файл
    reader_in = list(csv.reader(in_file, delimiter='>'))
    with open('new_time.csv', 'w+', encoding='utf-8', newline='') as out_file:  # Открываем для записи новый файл
        writer = csv.writer(out_file, delimiter='>')

        first_line = reader_in[0]
        first_line[-1] = 'timeNow'
        writer.writerow(first_line)  # Записываем названия столбцов

        for i in reader_in[1:]:  # Начинаем проходиться по исходному файлу
            line = i
            time = line[3].split(':')
            time = list(map(int, time))

            time[2] += int(line[4])
            if time[2] >= 60:
                time[1] += 1
                time[2] = time[2] % 60
            if time[1] >= 60:
                time[0] += 1
                time[1] = time[1] % 60  # Здесь мы добавляем секунды к нашему времени смотрим,
                # если нужно прибавить часы/минуты

            time = list(map(str, time))
            for k in range(len(time)):
                if len(time[k]) == 1:
                    time[k] = '0' + time[k]
            line[4] = ':'.join(time)
            writer.writerow(line)  # Здесь мы просто записываем новое время

    with open('new_time.csv', 'r', encoding='utf-8', newline='') as search_file:  # В этом блоке кода
        # мы ищем нужную каюту
        reader = csv.reader(search_file, delimiter='>')
        for i in reader:
            if i[2] == '98-OYE':
                print(f'{i[4]} - действительное время для каюты: {i[2]}')
