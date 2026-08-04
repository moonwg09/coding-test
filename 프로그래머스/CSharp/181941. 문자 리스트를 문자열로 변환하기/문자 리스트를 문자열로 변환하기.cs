using System;

public class Solution {
    public string solution(string[] arr) {
        // 방법 1: string.Concat을 사용해 배열의 모든 문자열을 이어 붙이기
        return string.Concat(arr);
        
        // 방법 2: string.Join을 사용해 구분자 없이 이어 붙이기
        // return string.Join("", arr);
    }
}