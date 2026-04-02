
N = int(input())
paper = []
color_list = []

for _ in range(N):
    paper.append(list(map(int,input().split())))

def makePaper(row,col,size):
    # 현재 영역이 모두 같은 색인지 확인
    color = paper[row][col]
    for i in range(row, row+size):
        for j in range(col, col+size):
            # 같은 색이 아니면, 영역을 나누어 정복한다
            if paper[i][j] != color:
                new_size = size//2
                # row, col, new_size
                makePaper(row,col,new_size)
                makePaper(row,col+new_size,new_size)
                makePaper(row + new_size, col,new_size)
                makePaper(row + new_size, col+new_size, new_size)
                return
    # 모두 같은 색이면, 현재 색을 color_list에 추가
    color_list.append(color)

makePaper(0,0,N)
print(color_list.count(0))
print(color_list.count(1))