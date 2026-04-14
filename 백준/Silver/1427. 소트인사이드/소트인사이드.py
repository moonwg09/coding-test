
str = input()

num_list = list(str)

num_list.sort(reverse=True)

for num in num_list:
    print(num,end="")