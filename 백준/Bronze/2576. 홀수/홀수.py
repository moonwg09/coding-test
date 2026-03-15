num = []
total = 0
min = 0

for i in range(7):

    num.append(int(input()))
    
    if num[i] % 2 == 1 :
        total += num[i]

if total == 0:
    print(-1)
else:
    print(total)

    min = 101

    for n in num:  #리스트의 값을 하나씩 순회
        if n % 2 == 1 and n < min:
            min = n

    print(min)