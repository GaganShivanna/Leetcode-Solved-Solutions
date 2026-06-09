class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l=0
        total = 0
        res = 0
        for r in range(len(fruits)):
            c = fruits[r]
            count[c] = 1 + count.get(c,0)
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f]-= 1
                total -= 1
                l+= 1

                if not count[f]:
                    count.pop(f)
            res = max(res, total)
        return res