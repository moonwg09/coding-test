
# 단어 입력받기 (오른쪽 공백이나 줄바꿈 제거를 위해 strip() 사용)
word = input().strip()

# 'a'부터 'z'까지 모든 알파벳을 담은 문자열
alphabet = "abcdefghijklmnopqrstuvwxyz"

# 결과를 담을 리스트
result = []

for char in alphabet:
    # word 안에서 char(알파벳)가 처음 등장하는 위치를 찾아서 리스트에 추가
    # 없으면 알아서 -1이 추가됩니다.
    result.append(word.find(char))

# 리스트 괄호를 벗기고 공백으로 구분해 출력
print(*result)


