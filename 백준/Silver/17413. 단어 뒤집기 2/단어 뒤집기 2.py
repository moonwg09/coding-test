str = input()
i = 0
length = len(str)
stack=[]

while i < length:

    if str[i] not in [' ', '<']:     # in 안에 있으면 
        stack.append(str[i])

    else:
        while stack:  #stack에 뭐가 있는 동안
            print(stack.pop(), end = '')
        
        if str[i] == '<':
            while str[i] != '>':
                print(str[i], end = '')
                i += 1
        print(str[i], end = '')
    i += 1

while stack:
    print(stack.pop(), end = '')
        