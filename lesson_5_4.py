src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
bigger_nums = [src[_ + 1] for _ in range(len(src) - 1) if src[_ + 1] > src[_]]
print(bigger_nums)
