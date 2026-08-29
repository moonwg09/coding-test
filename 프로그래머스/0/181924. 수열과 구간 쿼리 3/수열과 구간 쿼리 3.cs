using System;

public class Solution {
    public int[] solution(int[] arr, int[,] queries) {
        int queryCount = queries.GetLength(0);

        for (int q = 0; q < queryCount; q++) {
            int i = queries[q, 0];
            int j = queries[q, 1];

            // 튜플 분해(Tuple Deconstruction)를 사용한 스왑
            (arr[i], arr[j]) = (arr[j], arr[i]);
        }

        return arr;
    }
}