# N: 세로 크기, M: 가로 크기, K: 찾으려는 좌석 번호
n, m, k = map(int, input().split())

# 행(r)은 K를 가로 한 줄의 개수(M)로 나눈 몫
r = k // m
# 열(c)은 K를 가로 한 줄의 개수(M)로 나눈 나머지
c = k % m

print(r, c)