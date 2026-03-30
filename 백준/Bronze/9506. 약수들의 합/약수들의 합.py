
import sys
input = sys.stdin.readline


def divisor(num):
    div_list=[]
    for i in range(1,num):
        if num % i == 0:
            div_list.append(i)
    return div_list
        


while True:
    n = int(input())
    
    # 3. -1이 들어오면 여기서 바로 반복문을 탈출하여 프로그램을 완전히 끝냅니다!
    if n == -1:
        break
        
    # 함수를 호출해서 약수 리스트를 받아옵니다.
    div_list = divisor(n)
    
    # 4. 파이썬 내장 함수 sum()을 사용하면 for문으로 직접 더할 필요가 없습니다.
    total = sum(div_list)
    
    # 5. 완전수 판별 및 출력
    if total == n:
        div_str = " + ".join(map(str, div_list))
        print(f"{n} = {div_str}")
    else:
        print(f"{n} is NOT perfect.")


    
    


