def solution(strings, n):
    sorted_words = sorted(strings, key=lambda x: (x[n],x))
    return sorted_words
    