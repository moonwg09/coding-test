def to_seconds(time_str):
    """ 'mm:ss' 형식의 문자열을 초(second) 단위 정수로 변환 """
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def to_time_format(seconds):
    """ 초(second) 단위 정수를 'mm:ss' 형식 문자열로 변환 """
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    # 모든 시간 문자열을 '초' 단위로 변환
    v_len_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    op_start_sec = to_seconds(op_start)
    op_end_sec = to_seconds(op_end)
    
    # 1. 시작 전 오프닝 구간 체크
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
        
    # 2. 명령어 순차 처리
    for cmd in commands:
        if cmd == "prev":
            # 10초 전으로 이동 (0초 미만으로 내려가지 않도록 처리)
            pos_sec = max(0, pos_sec - 10)
        elif cmd == "next":
            # 10초 후로 이동 (비디오 길이를 초과하지 않도록 처리)
            pos_sec = min(v_len_sec, pos_sec + 10)
            
        # 명령어 이동 후 오프닝 구간 체크
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
    # 3. 결과를 "mm:ss" 포맷으로 반환
    return to_time_format(pos_sec)