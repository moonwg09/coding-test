import sys
input = sys.stdin.readline

size_A, size_B = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

merged_list = []
pA = pB = 0

# 1. 두 배열을 비교하며 작은 값부터 차례대로 넣습니다.
while pA < size_A and pB < size_B:
    if A[pA] < B[pB]:
        merged_list.append(A[pA])
        pA += 1
    else:
        merged_list.append(B[pB])
        pB += 1

# 2. 한쪽 배열이 먼저 끝났을 때, 남은 요소들을 뒤에 찰싹 붙여줍니다.
if pA < size_A:
    merged_list.extend(A[pA:])
if pB < size_B:
    merged_list.extend(B[pB:])

# 3. 공백을 두고 출력합니다.
print(*(merged_list)) # print(" ".join(map(str, merged_list)))와 같습니다.