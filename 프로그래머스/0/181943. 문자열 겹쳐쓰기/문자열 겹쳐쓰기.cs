using System;

public class Solution {
    public string solution(string my_string, string overwrite_string, int s) {
        // 1. 인덱스 0부터 s 전까지 추출
        string head = my_string.Substring(0, s);
        
        // 2. overwrite_string이 끝난 위치부터 끝까지 추출
        string tail = my_string.Substring(s + overwrite_string.Length);
        
        // 3. 앞 + 덮어쓸 문자열 + 뒤 조합
        return head + overwrite_string + tail;
    }
}