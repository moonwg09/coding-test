#import sys
#input = sys.stdin.readline

#while True:
   # number = list(map(int,input().split()))
   # if number[0] == number[1] == number[2] == 0:
    #    break
   # else:
       # number.sort()
      #  if number[2] >= number[0] + number[1]:
     #       print("Invalid")
    #    elif number[0]== number[1] == number[2]:
    #        print("Equilateral")
   #    elif number[0]== number[1] or number[0]== number[2] or number[2]== number[1]:
  #          print("Isosceles")
 #       else:
#            print("Scalene")

import sys
input = sys.stdin.readline

while True:
    # 1. 입력받으면서 바로 정렬하고 a, b, c에 담습니다.
    a, b, c = sorted(map(int, input().split()))
    
    # 2. 종료 조건 (정렬되었으므로 가장 큰 c가 0이면 모두 0입니다)
    if c == 0:
        break
        
    # 3. 삼각형 조건 판별
    if c >= a + b:
        print("Invalid")
    elif a == c:  # 정렬되어 있으므로 가장 작은 값과 큰 값이 같으면 세 변이 모두 같습니다.
        print("Equilateral")
    elif a == b or b == c:  # 정렬되어 있으므로 a==c는 위에서 걸러졌고, 인접한 두 변만 비교하면 됩니다.
        print("Isosceles")
    else:
        print("Scalene")


