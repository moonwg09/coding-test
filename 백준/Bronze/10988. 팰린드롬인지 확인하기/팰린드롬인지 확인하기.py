charlist = list(input())
isPal = 1  # 처음부터 1(True)로 설정

# 단어의 절반까지만 확인하면 됩니다.
for i in range(len(charlist) // 2):
    # 양 끝에서부터 하나씩 안쪽으로 들어오며 비교
    if charlist[i] != charlist[-1 - i]:
        isPal = 0
        break  # 한 번이라도 다르면 팰린드롬이 아니므로 즉시 중단

print(isPal)