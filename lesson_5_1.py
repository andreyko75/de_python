def odd_nums(n):
    for _ in range(1, n + 1, 2):
        yield _


n = int(input('Enter the int number: '))
odd_to_n = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(odd_to_n))
