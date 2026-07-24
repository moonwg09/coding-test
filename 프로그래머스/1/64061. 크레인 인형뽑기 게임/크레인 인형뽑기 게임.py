def solution(board, moves):
    stack = []
    result = 0
    for n in moves:
        for i in range(len(board)):
            if board[i][n-1] != 0:
                pick = board[i][n-1]
                board[i][n-1] = 0
                if stack and stack[-1] == pick:
                    stack.pop()
                    result += 2
                else:
                    stack.append(pick)
                break
    return result