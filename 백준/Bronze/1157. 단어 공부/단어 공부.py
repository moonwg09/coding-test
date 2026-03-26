# 1. 단어를 입력받자마자 모두 대문자로 바꿔줍니다. (예: "Mississipi" -> "MISSISSIPI")
word = input().upper()

# 2. set()을 사용해 중복을 제거하여 어떤 알파벳이 쓰였는지 후보를 리스트로 만듭니다.
# (예: "MISSISSIPI" -> ['M', 'I', 'S', 'P'])
unique_letters = list(set(word))

# 각 알파벳이 몇 번 쓰였는지 저장할 리스트
counts = []

# 3. 중복을 제거한 알파벳 후보들을 하나씩 꺼내서, 원래 단어(word)에서 몇 번 나오는지 셉니다.
for letter in unique_letters:
    counts.append(word.count(letter))

# 4. 가장 많이 나온 횟수(최댓값)를 찾습니다.
max_count = max(counts)

# 5. 만약 그 최댓값이 counts 리스트 안에 2개 이상 있다면 (동점자가 있다면)
if counts.count(max_count) > 1:
    print('?')
else:
    # 6. 동점자가 없다면 최댓값이 있는 위치(인덱스)를 찾아서, 
    # 알파벳 후보 리스트(unique_letters)의 같은 위치에 있는 글자를 출력합니다.
    max_index = counts.index(max_count)
    print(unique_letters[max_index])