
num1, num2 = map(int,input().split())
jin = []

       # 0~9 숫자와 A~Z 알파벳을 모두 합친 '36진법 표'를 만듭니다.
# index 0은 '0', index 10은 'A', index 35는 'Z'와 완벽히 일치하게 됩니다.
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"          

# num1이 0보다 클 때까지만 반복합니다.
while num1 > 0:
    # 1. 현재 숫자를 B(num2)로 나눈 나머지를 구합니다.
    remainder = num1 % num2
    
    # 2. 나머지에 해당하는 문자(숫자 or 알파벳)를 진법 표에서 찾아 리스트에 넣습니다.
    jin.append(system[remainder])
    
    # 3. 숫자를 B로 나눈 몫으로 갱신해 줍니다. (그래야 다음 자리를 계산하니까요!)
    num1 = num1 // num2

# 4. 저장된 문자들은 역순이므로 뒤집어주고([::-1]), 하나의 문자열로 찰싹 붙여서(join) 출력합니다.
print("".join(jin[::-1]))
    