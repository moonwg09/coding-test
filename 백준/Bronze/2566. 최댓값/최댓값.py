numlist = []

for _ in range(9):
    numlist.append(list(map(int, input().split())))

max = numlist[0][0]
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if numlist[i][j] > max:
            max = numlist[i][j]
            row = i
            col = j
print(max)
print(row+1,col+1)