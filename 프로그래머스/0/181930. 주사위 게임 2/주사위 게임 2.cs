using System;

public class Solution {
    public int solution(int a, int b, int c) {
        // 1. 세 숫자가 모두 같은 경우
        if (a == b && b == c) {
            return (a + b + c) 
                 * (a * a + b * b + c * c) 
                 * (a * a * a + b * b * b + c * c * c);
        }
        // 2. 세 숫자 중 어느 두 개만 같은 경우
        else if (a == b || b == c || a == c) {
            return (a + b + c) 
                 * (a * a + b * b + c * c);
        }
        // 3. 세 숫자가 모두 다른 경우
        else {
            return a + b + c;
        }
    }
}