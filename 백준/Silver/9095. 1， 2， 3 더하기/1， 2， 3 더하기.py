# if n>=4:
# m(n) = m(n-1) + m(n-2) + m(n-3)

n = int(input())


for _ in range(n):
    table = [1,2,4] + [0] * 8
    for i in range(3,11):
        table[i] = table[i-1] + table[i-2] + table[i-3]
    m = int(input())
    print(table[m-1])

    


