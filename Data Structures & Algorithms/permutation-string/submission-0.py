class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
            
        s2_map = {}
        left = 0
        
        for right in range(len(s2)):
            current_char = s2[right]
            
            s2_map[current_char] = s2_map.get(current_char, 0) + 1
            
            
            if right - left + 1 > len(s1):
                left_char = s2[left]
                s2_map[left_char] -= 1
                if s2_map[left_char] == 0:
                    del s2_map[left_char]
                left += 1 
                
            
            if s2_map == s1_map:
                return True
                
        return False
            