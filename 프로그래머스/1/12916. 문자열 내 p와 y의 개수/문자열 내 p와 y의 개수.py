def solution(s):
    countp=0
    county=0
    for st in s:
        if st == 'p' or st == 'P':
            countp += 1
        elif st == 'y' or st == 'Y':
            county += 1
    
    if countp == county:
        return True
    else:
        return False