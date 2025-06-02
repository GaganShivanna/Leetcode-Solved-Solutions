class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0 
        for stones in stones: 
            if stones in jewels:
                count += 1
        return count 