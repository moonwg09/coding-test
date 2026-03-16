list = []
num1, num2 = map(int,input().split())

list = [0] * num1   #리스트의 크기를 정하는 방법

for _ in range(num2) :
    
    i , j , k = map(int,input().split())

    for index in range(i-1,j):
        list[index] = k

print(*list, end=" ")  # 대괄호는 벗기고 안에 있는 값만 출력한다.