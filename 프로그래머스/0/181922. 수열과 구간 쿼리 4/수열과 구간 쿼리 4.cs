using System;

public class Solution {
    public int[] solution(int[] arr, int[,] queries) {
        int queryCount = queries.GetLength(0);

        for (int q = 0; q < queryCount; q++) {
            int s = queries[q, 0];
            int e = queries[q, 1];
            int k = queries[q, 2];

            for (int i = s; i <= e; i++) {
                if (k == 0) {
                    if (i == 0) arr[i]++;
                } else if (i % k == 0) {
                    arr[i]++;
                }
            }
        }
        return arr;
    }
}