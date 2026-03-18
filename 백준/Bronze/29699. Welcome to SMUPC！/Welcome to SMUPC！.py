import sys
input =sys.stdin.readline

strlist = ["WelcomeToSMUPC"]

list = list(strlist[0])  # 문자로 쪼개기

num = int(input().strip())

index = (num - 1) % 14

# 4. 출력
print(list[index])


