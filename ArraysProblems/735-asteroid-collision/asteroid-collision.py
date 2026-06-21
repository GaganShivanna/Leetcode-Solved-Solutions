class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []
        for cur in ast:
            alive = True

            while alive and stack and stack[-1] > 0 and cur < 0 :
                top = stack[-1]
                if abs(cur) > top:
                    stack.pop()
                elif abs(cur) == top:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(cur)
        return stack