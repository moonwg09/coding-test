using System.Collections.Generic;

public class Solution {
    public int[] solution(int n) {
        List<int> sequence = new List<int>();
        sequence.Add(n);

        while (n > 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
            sequence.Add(n);
        }

        return sequence.ToArray();
    }
}