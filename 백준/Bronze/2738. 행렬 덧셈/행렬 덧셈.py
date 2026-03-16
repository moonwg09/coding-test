row, col = map(int, input().split())


A = []
B = []
sum = 0

# row(줄) 수만큼 반복해서 한 줄씩 덩어리로 A에 추가합니다.
for _ in range(row):
    # 한 줄을 입력받아 정수 리스트로 만든 뒤 A에 쏙 넣습니다.
    A.append(list(map(int, input().split())))
for _ in range(row):
    # 한 줄을 입력받아 정수 리스트로 만든 뒤 A에 쏙 넣습니다.
    B.append(list(map(int, input().split())))

for i in range(row):

    for j in range(col):
        sum = A[i][j] + B[i][j]
        print(sum, end=" ")
    print()
