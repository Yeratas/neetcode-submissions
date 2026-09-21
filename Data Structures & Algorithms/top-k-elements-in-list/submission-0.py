class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for n in nums:
            freq_table[n] = freq_table.get(n,0) + 1
        ordered_freq_table = sorted(
            freq_table,
            key = freq_table.get,
            reverse = True
        )
        return ordered_freq_table[:k]