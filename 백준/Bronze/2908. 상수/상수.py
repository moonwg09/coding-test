

num1,num2 = map(str,input().split())

num1=list(num1)
num2=list(num2)

num1[0],num1[-1] = num1[-1],num1[0]
num2[0],num2[-1] = num2[-1],num2[0]

i = 0
while True:

    if num1[i] < num2[i]:
        print("".join(num2))
        break
    elif num1[i] == num2[i]:
        i += 1
    elif num1[i] > num2[i]:
        print("".join(num1))
        break


