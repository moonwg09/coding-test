# 1. 처음부터 대괄호 []를 사용해 리스트로 만들어 줍니다.
strlist = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]

num = int(input())

# 해킹 당했는지(이상한 문장이 있는지) 기록해 둘 변수
is_hacked = False 

# 2. num 번만큼 반복하면서 문장을 하나씩 입력받고 바로바로 검사합니다.
for _ in range(num):
    pledge = input() # 쪼개지 않고 문장 통째로 받기!
    
    # 3. 입력받은 문장이 strlist 안에 '없다면(not in)' 해킹된 것!
    if pledge not in strlist:
        is_hacked = True

# 4. 모든 검사가 끝난 후, 최종 결과 딱 한 번만 출력
if is_hacked == True:
    print('Yes')
else:
    print('No')