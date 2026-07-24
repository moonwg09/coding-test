def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    current_health = health
    
    # 공격 정보를 딕셔너리로 변환하여 시간별로 빠르게 확인 (시간: 피해량)
    attack_dict = {attack[0]: attack[1] for attack in attacks}
    last_attack_time = attacks[-1][0]
    
    success_time = 0
    
    # 1초부터 마지막 공격 시간까지 반복
    for time in range(1, last_attack_time + 1):
        # 1. 몬스터의 공격이 있는 시간인 경우
        if time in attack_dict:
            current_health -= attack_dict[time]
            success_time = 0  # 연속 성공 초기화
            
            # 체력이 0 이하가 되면 사망
            if current_health <= 0:
                return -1
        
        # 2. 공격이 없는 시간인 경우 (회복)
        else:
            current_health += x
            success_time += 1
            
            # 시전 시간 t만큼 성공했을 경우
            if success_time == t:
                current_health += y
                success_time = 0
            
            # 최대 체력 제한
            if current_health > max_health:
                current_health = max_health
                
    return current_health