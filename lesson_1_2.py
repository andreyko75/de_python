num_count = 1
odd_list = []
while num_count < 1001:
    if num_count % 2 != 0:  # Заполняем список нечетными числами
        odd_list.append(num_count**3)
    num_count += 1
# print(odd_list) #для проверки что идут кубы
sum_cube = 0
sum_cube_plus_17 = 0
# перебираем вкесь список
for number_from_list in odd_list:
    odds_sum = 0
    # перебираем цифры в числе из списка
    for odd_from_number in str(number_from_list):
        odds_sum = odds_sum + int(odd_from_number)
        if odds_sum % 7 == 0:
            sum_cube = sum_cube + number_from_list
    odds_sum = 0
    # перебираем цифры в числе из списка увеличенного на 17
    for odd_from_number in str(number_from_list + 17):
        odds_sum = odds_sum + int(odd_from_number)
        if odds_sum % 7 == 0:
            sum_cube_plus_17 = sum_cube_plus_17 + number_from_list + 17
print(sum_cube)
print(sum_cube_plus_17)
