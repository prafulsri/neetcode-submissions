class Solution {
    public boolean isAnagram(String s, String t) {
        
        char[] sArray = s.toCharArray(); 
        char[] tArray = t.toCharArray(); 
        
        java.util.Arrays.sort(sArray);
        java.util.Arrays.sort(tArray);

        if (s.length() == t.length()) {
            for (int i = 0; i< sArray.length; i++) {
                if (sArray[i] != tArray[i]) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
}
