import sys
input = sys.stdin.readline

M = 1234567891
r = 31

L = int(input())
str = input().strip()

h = 0
for i,a in enumerate(str):
# a:1, b:2, ... ord(str[i]) - ord('a') + 1
# a값 * r ** i%M
    h += (ord(a) - ord('a') + 1) * r ** i

print(h % M)