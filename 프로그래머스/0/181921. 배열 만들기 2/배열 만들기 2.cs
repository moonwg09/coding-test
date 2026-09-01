using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int l, int r) {
        List<int> result = new List<int>();

        // 1부터 63(111111_2)까지 이진수로 변환 후 5를 곱해 숫자 생성
        for (int i = 1; i < 64; i++) {
            int num = int.Parse(Convert.ToString(i, 2)) * 5;
            if (num >= l && num <= r) {
                result.Add(num);
            }
        }

        return result.Count > 0 ? result.ToArray() : new int[] { -1 };
    }
}