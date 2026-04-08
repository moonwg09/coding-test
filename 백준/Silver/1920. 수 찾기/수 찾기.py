
import sys
input = sys.stdin.readline

n = int(input())

num_list = set(map(int,input().split()))

m = int(input())

m_list = map(int,input().split())

for number in m_list:
    if number in num_list:
        print(1)
    else:
        print(0)
