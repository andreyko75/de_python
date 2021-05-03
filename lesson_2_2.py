les_string = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# проверка где есть числа и изменяем список
_ = 0
str_out = ''
for i in les_string:
    for j in i:
        if j.isdigit():
            les_string[_] = (f'"{int(les_string[_]):02d}"') if les_string[_][0].isdigit() else \
                            (f'"{les_string[_][0]}{int(pow(int(les_string[_]) ** 2, .5)):02d}"')
            ## использовалось возведение в квадрат температуры  и извлечение корня
            ## для того, что бы отрицательные температуры обрабатывались нормально
            break
    _ += 1
print(' '.join(les_string))
