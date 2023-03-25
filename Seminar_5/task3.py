result = (x for x in range(100) if int(sum(map(int, list(str(x))))) != 8 and x % 2 == 0)
print(*result)
