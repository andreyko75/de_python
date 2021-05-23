import sys


def default_args(_, first_num=0, end_num=-1):
    return int(first_num), int(end_num)


first_num, end_num = default_args(*sys.argv)
count_lines = end_num - first_num if end_num != -1 else 0
with open('bakery.csv', 'r', encoding='utf-8') as _:
    n_pos = 0
    while first_num > n_pos:
        line = _.readline()
        n_pos += 1
    count_lines += n_pos
    while line:
        if (end_num == -1 or n_pos <= count_lines):
            print(line.strip())
        n_pos += 1
        line = _.readline()
