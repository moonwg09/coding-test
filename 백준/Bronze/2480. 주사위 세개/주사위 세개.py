eye1, eye2, eye3 = map(int, input().split())

# 1. 세 숫자가 모두 같은 경우
if eye1 == eye2 == eye3:
    print(10000 + eye1 * 1000)

# 2. 두 숫자만 같은 경우 (세 숫자가 같지 않다는 전제가 깔림)
elif eye1 == eye2 or eye1 == eye3:
    print(1000 + eye1 * 100)
elif eye2 == eye3:
    print(1000 + eye2 * 100)

# 3. 모두 다른 경우
else:
    print(max(eye1, eye2, eye3) * 100)