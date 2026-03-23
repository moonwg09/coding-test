
modlist = []

for _ in range(10):
    num = int(input())
    modlist.append(num % 42)
modlist.sort()  
count = 1
for i in range(1,10):
    if modlist[i-1] != modlist[i]:
        count+=1
    
print(count)
    

