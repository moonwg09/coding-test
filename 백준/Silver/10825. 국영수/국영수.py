
# users = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Charlie', 'age': 25}
# ]

# # 'age' 키로 정렬하고 같으면 'name' 키로 정렬
# users.sort(key=itemgetter('age', 'name'))

from operator import itemgetter
n = int(input())

student_list = []

for _ in range(n):
    
    name, kor, eng, math = input().split()
    
    student_list.append([name, -int(kor), int(eng), -int(math)])

student_list.sort(key=itemgetter(1,2,3,0))

for s in student_list:
    print(s[0])



