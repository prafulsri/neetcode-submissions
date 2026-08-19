class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        result = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])

            while (right-left+1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result           

        