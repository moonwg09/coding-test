using System;

public class Solution {
    public int[] solution(int[] arr, int[,] queries) {
        int queryCount = queries.GetLength(0);
        int[] answer = new int[queryCount];

        for (int q = 0; q < queryCount; q++) {
            int s = queries[q, 0];
            int e = queries[q, 1];
            int k = queries[q, 2];

            int minVal = int.MaxValue;

            // s부터 e까지 순회하며 k보다 크면서 가장 작은 값 탐색
            for (int i = s; i <= e; i++) {
                if (arr[i] > k && arr[i] < minVal) {
                    minVal = arr[i];
                }
            }

            // 조건을 만족하는 값이 없으면 -1, 있으면 최솟값 저장
            answer[q] = (minVal == int.MaxValue) ? -1 : minVal;
        }

        return answer;
    }
}