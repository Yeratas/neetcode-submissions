class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for n in nums:
            if n not in hash_table:
                hash_table[n]=0
            else:
                hash_table[n]+=1
        
        for x in hash_table:
            if hash_table[x] >= 1:
                return True
        return False