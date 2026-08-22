class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
           return ""
        
        t_count = Counter(t)      # Characters we need: {'x': 1, 'y': 1, 'z': 1}
        window_count = {}         # Characters currently inside our window
        
        required = len(t_count)   # Number of unique characters needed (3)
        have = 0                  # Number of unique characters matched so far
        
        left = 0
        min_len = float('inf')
        best_window = (-1, -1)
        
        # 'right' pointer expands the window
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
                
            # When the window contains all of 't' (This triggers at index 6: 'zodyx')
            while have == required:
                # Check if this window is smaller than our previous best
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    best_window = (left, right)
                    
                # SHRINK: Move 'left' forward to discard unnecessary characters
                left_char = s[left]
                window_count[left_char] -= 1
                
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1  # We broke the validity, loop stops expanding 'left'
                    
                left += 1
                
        start, end = best_window
        return s[start:end+1] if min_len != float('inf') else ""
        