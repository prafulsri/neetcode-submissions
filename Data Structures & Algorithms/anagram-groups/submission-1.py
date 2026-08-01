class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs.sort()
        
        # result = []
        # matched = [False] * len(strs)

        # for i in range(len(strs)):

        #     if matched[i]:
        #         continue

        #     current_group = [strs[i]]
        #     matched[i] = True     


        #     for j in range(i+1, len(strs)):

                
        #         if sorted(strs[i]) == sorted(strs[j]):
                    
        #             current_group.append(strs[j])
        #             matched[j] = True
            
        #     result.append(current_group)
        # return result 

        seen = {}
        for word in strs:
            sorted_word = sorted(word) 
            key = tuple(sorted_word)   

            if key not in seen:
                seen[key] = []
            seen[key].append(word)
        return list(seen.values())                           