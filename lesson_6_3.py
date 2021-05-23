def made_list(file_name):
    """
    made list from files whith replaced \n
    :param file_name
    :return: list of data
    """
    list_name = []
    with open(file_name, 'r') as _:
        list_temp = (list(_))
    for _ in list_temp:
        list_name.append(_.replace('\n', ''))
    return list_name


result = {}
user_names = made_list('users.csv')
hobby = made_list('hobby.csv')
for _ in range(len(user_names)):
    result.update({user_names[_]: None if len(hobby) <= _ else hobby[_]})
with open('result.csv', 'w') as _:
    for i in result.keys():
        _.writelines(str(i) + ' ' + str(result.get(i)) + '\n')
