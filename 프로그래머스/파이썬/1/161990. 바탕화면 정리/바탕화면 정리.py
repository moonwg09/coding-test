def solution(wallpaper):
    # 최솟값을 찾기 위해 시작점은 무한대(inf)로, 끝점은 0으로 초기화
    lux, luy = float('inf'), float('inf')
    rdx, rdy = 0, 0
    
    # 바탕화면을 순회하며 파일('#')의 위치를 확인
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                # 가장 위, 가장 왼쪽 좌표 갱신
                lux = min(lux, i)
                luy = min(luy, j)
                
                # 가장 아래, 가장 오른쪽 좌표 갱신 (+1을 해주는 이유는 격자칸 자체를 포함해야 하므로)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)
                
    return [lux, luy, rdx, rdy]