def thesaurus(args):
    """
    type dictionary, where key is first letter of name, value - list of names
    :param args: list of names
    """
    for i in args:
        list_names = workers_result.get(i[0])

        if list_names != None:
            list_names.append(i)
            workers_result.update({i[0]: list_names})
        # непонятно почему некорректно раотает закоментированная строка...
        #            workers_result.update({i[0]:workers_result.get(i[0]).append(i)})
        else:
            workers_result.setdefault(i[0], [i])
    print(workers_result)


workers_result = {}
workers_names = ["Иван", "Мария", "Петр", "Илья"]
workers_names.sort()
thesaurus(workers_names)
