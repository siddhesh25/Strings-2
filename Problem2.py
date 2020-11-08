class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result
        hmap = collections.Counter()
        for c in p:
            hmap[c] += 1
        counter = len(hmap)
        begin, end = 0, 0
        
        while end < len(s):
            c = s[end]
            if c in hmap: 
                hmap[c] -= 1
                if hmap[c] == 0: counter -= 1
            while counter == 0:
                temp = s[begin]
                if temp in hmap:
                    hmap[temp] += 1
                    if hmap[temp] > 0:
                        counter+=1
                if end - begin + 1 == len(p):
                    result.append(begin)
                begin+=1
            end+=1
        return result
