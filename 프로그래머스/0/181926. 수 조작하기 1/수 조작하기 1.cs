using System;

public class Solution {
    public int solution(int n, string control) {
        foreach (char c in control) {
            n += c switch {
                'w' => 1,
                's' => -1,
                'd' => 10,
                'a' => -10,
                _ => 0
            };
        }
        return n;
    }
}