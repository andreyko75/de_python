n = int(input('Enter the int number: '))
odd_to_n = (_ for _ in range(1, n + 1, 2))
for _ in range(1, n + 1, 2):
    print(next(odd_to_n))
