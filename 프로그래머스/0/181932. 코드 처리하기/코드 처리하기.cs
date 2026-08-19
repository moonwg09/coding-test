using System.Text;

public class Solution {
    public string solution(string code) {
        StringBuilder ret = new StringBuilder();
        int mode = 0;
        
        for (int idx = 0; idx < code.Length; idx++) {
            if (code[idx] == '1') {
                mode = 1 - mode; // 0은 1로, 1은 0으로 변경
            } else {
                if (mode == 0 && idx % 2 == 0) {
                    ret.Append(code[idx]);
                } else if (mode == 1 && idx % 2 == 1) {
                    ret.Append(code[idx]);
                }
            }
        }
        
        string result = ret.ToString();
        return string.IsNullOrEmpty(result) ? "EMPTY" : result;
    }
}