sec_minutes = 60  # секунд в минуте
sec_hours = sec_minutes * 60  # секунд в часе
sec_days = sec_hours * 24  # секунд в сутках
sec_month = sec_days * 30  # секунд в месяце (для упрощения в году 30 дней)
sec_years = sec_month * 12  # секунд в году
date_print = ''  # инициализируем переменную куда будем писать результат
duration = int(input("Сколько секунд перевести? "))
if duration // sec_years >= 1:  # проверка больше ли года в наших секундах? здесь и далее >=1 указал для восприятия,
    # можно было написать >0 и занесение количества лет в строку
    date_print = date_print + (str(duration // sec_years) + ' лет ')
    duration = duration % sec_years  # убираем подсчитанные года
if duration // sec_month >= 1:  # аналогично для месяцев, дней, часов, минут
    date_print = date_print + (str(duration // sec_month) + ' месяцев ')
    duration = duration % sec_month
if duration // sec_days >= 1:
    date_print = date_print + (str(duration // sec_days) + ' дней ')
    duration = duration % sec_days
if duration // sec_hours >= 1:
    date_print = date_print + (str(duration // sec_hours) + ' часов ')
    duration = duration % sec_hours
if duration // sec_minutes >= 1:
    date_print = date_print + (str(duration // sec_minutes) + ' минут ')
    duration = duration % sec_minutes
if duration != 0:  # проверяем количество секунд, чтоб если будет ноль, они не прописывались в результате
    date_print = date_print + str(duration) + ' секунд '
print(date_print)
