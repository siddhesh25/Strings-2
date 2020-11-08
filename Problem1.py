class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0 
        if needle == haystack:
            return 0
        incr = len(needle)
        while i < len(haystack) - len(needle) + 1:
            if haystack[i:i+incr] == needle:
                return i
            i += 1
        return -1
        
