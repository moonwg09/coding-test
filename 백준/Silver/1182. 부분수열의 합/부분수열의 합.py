

n, m = map(int,input().split())

num_list = list(map(int,input().split()))

count = 0

def fuc (num, sum):
    global count

    if num == n:
        
        if sum == m:
            count += 1
        return


    fuc(num+1, sum+num_list[num])

    fuc(num+1, sum)

fuc(0,0)

if m == 0:
    count -= 1
    print(count)
else:
    print(count)




    
    
