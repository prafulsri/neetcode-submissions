class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
    
        for (int num : nums) {
            // If the number is already in the set, it's a duplicate
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}