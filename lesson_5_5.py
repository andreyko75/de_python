src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [23, 1, 3, 10, 4, 11]
result=[src[_] for _ in range(len(src)) if src.count(src[_])==1]
print(result)
