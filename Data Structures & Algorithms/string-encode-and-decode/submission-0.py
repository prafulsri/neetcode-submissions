class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Find '#'
            j = i
            while s[j] != "#":
                j += 1

            # Length of the word
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the word
            word = s[j:j + length]
            result.append(word)

            # Move to the next encoded word
            i = j + length

        return result
