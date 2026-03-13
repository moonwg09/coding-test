#import sys
#count = int(input())
#sum = 0

#for _ in range(count):
#    a, b = map(int, input(sys.stdin.readline).split())
#    sum = a + b
#    print(sum)
import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
# 맨 처음에 테스트 케이스 개수를 받습니다.
count_str = sys.stdin.readline().rstrip()
if count_str:
    count = int(count_str)

    for _ in range(count):
        # 각 줄에서 a와 b를 읽어와 더한 뒤 바로 출력
        line = sys.stdin.readline().split()
        if len(line) == 2:
            a, b = map(int, line)
            print(a + b)