def palin(strlist, i, j):
    global count
    count += 1  # 함수가 호출될 때마다 카운트 1 증가
    
    # 1. Base condition: 인덱스 i가 j와 같거나 커지면 (가운데까지 무사히 검사 완료)
    if i >= j:
        return 1
    # 2. 양 끝의 문자가 다르다면 팰린드롬이 아님
    elif strlist[i] != strlist[j]:
        return 0
    # 3. 양 끝 문자가 같다면, 안쪽 문자를 검사하기 위해 재귀 호출
    else:
        return palin(strlist, i + 1, j - 1)

def isPalindrome(strlist):
    return palin(strlist, 0, len(strlist) - 1)

num = int(input())

for _ in range(num):
    count = 0  
    
    word = input() 
    
    # 팰린드롬 여부 결과와, 실행 횟수(count)를 함께 출력
    print(isPalindrome(word), count)