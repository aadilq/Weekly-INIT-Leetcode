class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        '''
        Task: 
        Find a pair of duplicate numbers at indices i and j which satisfy the condition abs(i - j) <= k

        Approach:
        - keep a hashmap of seen numbers with their most recent index. 
        - if the current number is in our seen hashmap, check to see if the condition hold true
        - if the condition holds true, return True else add the current number with its appropriate index to the hashmap
        '''
        n = len(nums)
        seen = {}

        for i in range(n):
            if nums[i] in seen and abs(i - seen[nums[i]]) <= k:
                return True
            seen[nums[i]] = i
        return False
