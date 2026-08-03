using System;
using System.Text;

public class Solution {
    public string solution(string str1, string str2) {
        StringBuilder sb = new StringBuilder();
        
        // 두 문자열의 길이가 같으므로 str1의 길이만큼 반복합니다.
        for (int i = 0; i < str1.Length; i++) {
            sb.Append(str1[i]); // str1의 i번째 문자 추가
            sb.Append(str2[i]); // str2의 i번째 문자 추가
        }
        
        return sb.ToString();
    }
}