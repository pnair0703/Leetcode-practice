class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # so what the hash map is gonna look like, ik its key:value, so the key will be coutn of characters which will mean the key will hold an array like [a:2, b:3, d:2] and then the value will be all strings that fit

        #so lets set hash map first?
        hashhh = defaultdict(list)

        for s in strs:
            #lets set the array that will be the key?
            count = [0] * 26 # 26 zeros
            #now for char in string
            for c in s:
                #here i add one for every character for the count. but i gotta find value first
                count[ord(c) - ord("a")] +=1
            hashhh[tuple(count)].append(s)
        return list(hashhh.values())
