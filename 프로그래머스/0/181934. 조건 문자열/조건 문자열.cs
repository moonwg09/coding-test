using System;

public class Solution {
    public int solution(string ineq, string eq, int n, int m) {
        if (ineq == ">" && eq == "="){
            if (n >= m){
                return 1;
            }
            else {
                return 0;
            }
        }
        else if(ineq == "<" && eq == "="){
            if(n<=m){
                return 1;
            }
            else{
                return 0;
            }
        }
        
        else if(ineq == ">" && eq == "!"){
            if(n > m){
                return 1;
            }
            else{
                return 0;
            }
        }
        
        else if(ineq == "<" && eq == "!"){
            if(n<m){
                return 1;
            }
            else{
                return 0;
            }
        }
        return 0; // 모든 조건에 해당하지 않을 경우를 대비한 기본 리턴
    }
}