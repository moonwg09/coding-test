all_students = []
attlist = []

# 1. 전체 명단과 제출자 명단 만들기
for i in range(1, 31):
    all_students.append(i)

for _ in range(28):
    attlist.append(int(input()))

# 2. 리스트를 집합(set)으로 바꿔서 빼기 연산 후, 다시 리스트로 만들기
# 이게 바로 원하셨던 "전체 - 제출자 = 미제출자" 입니다!
nonlist = list(set(all_students) - set(attlist))

# 3. 정렬 후 출력
nonlist.sort()
print(nonlist[0])
print(nonlist[1])