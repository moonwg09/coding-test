n = int(input())
count = 0

while True:
    # 1. 현재 남은 설탕이 5로 딱 나누어 떨어지면 가장 베스트!
    if n % 5 == 0:
        count += (n // 5)
        print(count)
        break
    
    # 2. 5로 안 나누어 떨어지는데, 남은 설탕이 3보다 작아서 더 뺄 수도 없다면? (실패)
    if n < 3:
        print(-1)
        break
        
    # 3. 5로 나누어 떨어질 때까지 3kg 봉지에 하나씩 담아봅니다.
    n -= 3
    count += 1