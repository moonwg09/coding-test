using System;

public class Solution {
    public int solution(int a, int b) {
        // a ⊕ b 와 b ⊕ a를 문자열로 결합 후 정수로 변환
        int ab = int.Parse($"{a}{b}");
        int ba = int.Parse($"{b}{a}");
        
        // 둘 중 더 큰 값을 반환 (같을 경우 a ⊕ b인 ab를 반환)
        return ab >= ba ? ab : ba;
    }
}