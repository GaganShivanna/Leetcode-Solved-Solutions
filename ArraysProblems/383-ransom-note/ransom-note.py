class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for char in r:
            if r[char] > m[char]:
                return False
        return True