class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #ok so binary search, dfs,bfs all dont work here, sliding window lowk didnt study enough but that def dont work here. gotta be hash i guess. what if i sort and append everything to a hash set and then check like if set 1 == set 2 then return true? this is me attempting without looking at solution

        if sorted(s) == sorted(t):
            return True
        else:
            return False
