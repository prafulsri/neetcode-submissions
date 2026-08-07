class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        c = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                c.append(nums1[i])
                i += 1
            else:
                c.append(nums2[j])
                j += 1
                
        
        if i < m:
            c.extend(nums1[i:])
        if j < n:
            c.extend(nums2[j:])
            
        
        total_len = len(c)
        mid = total_len // 2
        
        if total_len % 2 == 0:
            return float(c[mid - 1] + c[mid]) / 2.0
        else:
            return float(c[mid])




        

        