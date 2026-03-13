import sys
input = sys.stdin.readline
pactorial = 1

num = int(input())

for i in range(1,num+1):
    pactorial *= i

print(pactorial)