l = [1, 2, 1, 1, 2, 3, 4, 4, 4, 4, 5, 3, 21, 21, 21, 233, 423, 432, 2344, 5, 677, 77, 6, 6, 6, 43, 34]
res = []

for i in l:
    if i not in res:
        res.append(i)

print(res)
