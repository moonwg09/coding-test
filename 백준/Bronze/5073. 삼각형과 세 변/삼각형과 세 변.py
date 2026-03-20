
import sys
input = sys.stdin.readline

while True:
    number = list(map(int,input().split()))
    if number[0] == number[1] == number[2] == 0:
        break
    else:
        number.sort()
        if number[2] >= number[0] + number[1]:
            print("Invalid")
        elif number[0]== number[1] == number[2]:
            print("Equilateral")
        elif number[0]== number[1] or number[0]== number[2] or number[2]== number[1]:
            print("Isosceles")
        else:
            print("Scalene")




