les_string = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# проверка где есть числа и изменяем список
_ = 0
str_out = ''
for i in les_string:
    for j in i:
        if j == '+':
            les_string[_] = (f'"+{int(les_string[_]):02d}"')
            break
        if j.isdigit():
            les_string[_] = (f'"{int(les_string[_]):02d}"')
            break
    str_out = str_out + les_string[_] + ' '
    _ += 1
print(str_out)
