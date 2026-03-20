
def getJum(N):
    if N == 1:
        return 3
    k = getJum(N-1) + (getJum(N-1)-1)
    return k

num = int(input())

total = getJum(num)

print(total * total)


