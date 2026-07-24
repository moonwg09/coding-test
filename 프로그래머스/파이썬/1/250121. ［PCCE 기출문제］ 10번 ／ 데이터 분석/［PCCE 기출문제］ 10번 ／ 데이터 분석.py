from operator import itemgetter
def solution(data, ext, val_ext, sort_by):
    # 1. 각 컬럼 명칭에 대응하는 인덱스 번호를 매핑합니다.
    col_name = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    # 2. 필터링: ext 값이 val_ext보다 작은 데이터만 추출
    # ext_idx를 찾아 해당 인덱스의 값을 비교합니다.
    ext_idx = col_name[ext]
    filtered_data = [d for d in data if d[ext_idx] < val_ext]
    
    # 3. 정렬: itemgetter를 사용하여 sort_by 인덱스를 기준으로 오름차순 정렬
    sort_idx = col_name[sort_by]
    # itemgetter(sort_idx)는 데이터를 받아서 d[sort_idx]를 반환하는 함수 역할을 합니다.
    filtered_data.sort(key=itemgetter(sort_idx))
    
    return filtered_data