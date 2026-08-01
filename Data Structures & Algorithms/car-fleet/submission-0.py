class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        stack = []

        for i in range(len(cars) - 1, -1, -1):

            position_i = cars[i][0]
            speed_i = cars[i][1]

            time = (target - position_i) / speed_i

            if not stack:
                stack.append(time)

            elif time > stack[-1]:
                stack.append(time)

        return len(stack)