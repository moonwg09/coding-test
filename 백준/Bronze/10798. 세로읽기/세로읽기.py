
strlist = []

for _ in range(5):
    strlist.append(list(input()))

for j in range(15):
    for i in range(5):
        if j < len(strlist[i]):
    
            print(strlist[i][j],end="")

