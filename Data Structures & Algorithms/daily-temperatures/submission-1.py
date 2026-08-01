class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = []

        # for i in range(len(temperatures)):
        #     found = False

        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             sub = j - i
        #             result.append(sub)
        #             found = True
        #             break

        #     if not found:
        #         result.append(0)

        # return result
        
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):

            
            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev_day = stack.pop()
                result[prev_day] = i - prev_day

            stack.append(i)

        return result
        