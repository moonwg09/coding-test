
basket, line = map(int,input().split())
basketlist=[]
for i in range(basket):
    basketlist.append(i+1)

for _ in range(line):
    i , j = map(int, input().split())
    if j-i <= 1:
        basketlist[i-1], basketlist[j-1] = basketlist[j-1], basketlist[i-1]
    else:
        while i<j:
            basketlist[i-1], basketlist[j-1] = basketlist[j-1], basketlist[i-1]
            i+=1 
            j-=1
    
print(*basketlist)
