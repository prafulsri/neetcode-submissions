class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
    
        for (int i : nums) {
            // If the number is already in the set, it's a duplicate
            if (seen.contains(i)) {
                return true;
            }
            seen.add(i);
        }
        return false;
    }
}