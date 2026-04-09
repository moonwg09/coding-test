import sys
input = sys.stdin.readline

def recursive_story(depth, n):
    # 언더바(____) 개수 설정
    underbar = "____" * depth
    
    # 1. 공통 질문
    print(f'{underbar}"재귀함수가 뭔가요?"')
    
    # 2. 재귀의 끝 (Base Case)
    if depth == n:
        print(f'{underbar}"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(f'{underbar}라고 답변하였지.')
        return

    # 3. 재귀가 계속될 때의 답변
    print(f'{underbar}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f'{underbar}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(f'{underbar}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    
    # 4. 자기 자신을 호출 (더 깊이 들어감)
    recursive_story(depth + 1, n)
    
    # 5. 재귀에서 빠져나올 때 출력되는 부분
    # (recursive_story 함수가 끝나고 돌아왔을 때 실행됨)
    print(f'{underbar}라고 답변하였지.')

n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursive_story(0, n)