
total = 0
total_n = 0

for _ in range(10):
    n = int(input())

    total += n

    if total == 100:
        print(100)
        break
    if total > 100:
        if (100-(total-n)) >= (total-100):
            print(total)
            break
        elif (100-(total-n)) < (total-100):
            print(total-n)
            break
        

else:
    print(total)

