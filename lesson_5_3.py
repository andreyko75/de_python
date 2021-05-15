tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]

tut_gen = ((tutors[_], None if _ > len(klasses) - 1 else klasses[_]) for _ in range(len(tutors)))

for _ in range(len(tutors)):
    print(next(tut_gen))
