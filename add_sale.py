import sys
print(sys.argv)
with open('bakery.csv', 'a', encoding='utf-8') as _:
    _.writelines(sys.argv[1]+'\n')


