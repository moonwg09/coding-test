import sys
input = sys.stdin.readline

backet, line = map(int, input().split())

backetlist = []

for i in range(1, backet+1):
    backetlist.append(i)

for _ in range(line):
    i, j = map(int, input().split())
    # 로직은 아주 좋습니다!
    backetlist[i-1], backetlist[j-1] = backetlist[j-1], backetlist[i-1]
    
# 반복문 밖에서 최종 결과만 한 번, 언패킹(*)을 사용해서 출력
print(*backetlist)