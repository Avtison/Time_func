import csv


with open('astronaut_time.csv', 'r', encoding='utf-8', newline='') as in_file:
    reader = list(csv.reader(in_file, delimiter='>'))[1:]  # Читаем файл
    hash_tab = dict()

    for i in reader:  # Проходимся по нему и добавляем всё в словарь
        if i[2] not in hash_tab:
            hash_tab[i[2]] = [i[0], i[1], i[3], i[4]]
        else:
            print('Oops')  # Данная часть кода нужна, чтобы избежать ошибок в выполнении при неправильном файле

    for i in range(10):
        print({sorted(hash_tab)[i]: hash_tab[sorted(hash_tab)[i]]})  # Здесь мы сортируем хэш таблицу и пробегаемся по
        #  первым 10 элементам
