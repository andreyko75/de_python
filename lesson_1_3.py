user_number = 0
while user_number <= 20:
    if user_number // 10 == 1 or user_number % 10 > 4 or user_number % 10 == 0:
        end_word = 'ов'  # окончание ов в случаях - второго десятка, всех, где остаток от деления на 10 больше 4,
        # где остаток от деления равен 0,
    elif user_number % 10 == 1:
        end_word = ''  # окончание отсутствует для всех где остаток от деления 1, за исключением  числа 11,
        # но 11 учтен в  первом условии
    else:
        end_word = 'а'  # все остальные -  окончания а
    print(user_number, 'процент' + end_word)
    user_number += 1
