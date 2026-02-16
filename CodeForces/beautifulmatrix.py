
matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)


r, c = -1, -1
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r, c = i, j
            break
    if r != -1:
        break


target_r = 2
target_c = 2


moves = abs(r - target_r) + abs(c - target_c)

print(moves)