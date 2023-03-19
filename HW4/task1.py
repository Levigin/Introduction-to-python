def get_transposition(matrix: list) -> list:
    result = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            temp.append(matrix[j][i])
        result.append(temp)

    return result


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(get_transposition(m))
