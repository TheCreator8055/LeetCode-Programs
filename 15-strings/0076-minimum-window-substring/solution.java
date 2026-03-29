class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        int[] target = new int[128], window = new int[128];
        for (char c : t.toCharArray()) target[c]++;
        
        int left = 0, right = 0, count = 0, minLen = Integer.MAX_VALUE;
        String res = "";
        
        while (right < s.length()) {
            char rChar = s.charAt(right);
            if (target[rChar] > 0 && ++window[rChar] <= target[rChar]) count++;
            
            while (count == t.length()) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    res = s.substring(left, right + 1);
                }
                char lChar = s.charAt(left);
                if (target[lChar] > 0 && --window[lChar] < target[lChar]) count--;
                left++;
            }
            right++;
        }
        return res;
    }
}

