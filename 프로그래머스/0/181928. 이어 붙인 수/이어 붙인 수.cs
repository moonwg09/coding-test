using System;
using System.Linq;

public class Solution {
    public int solution(int[] num_list) {
        string odd = string.Concat(num_list.Where(n => n % 2 != 0));
        string even = string.Concat(num_list.Where(n => n % 2 == 0));
        
        return int.Parse(odd) + int.Parse(even);
    }
}