a, b, v = map(int, input().split())

# 나누어 떨어지면 (나머지가 0이면) 몫이 곧 정답입니다.
if (v - b) % (a - b) == 0:
    print((v - b) // (a - b))
# 나머지가 남으면 하루가 더 필요한 것이므로 몫에 1을 더해줍니다.
else:
    print((v - b) // (a - b) + 1)