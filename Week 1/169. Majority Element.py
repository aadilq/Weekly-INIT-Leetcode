from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
        Task:
        to find the number in the array which appears more than n // 2 times where n is the length of nums. 


        Important Observation:
        n // 2 is exactly half of the array so we want to find a number which occurs more than n // 2. There can only be one element which can satisfy this conditions

        Approach:
        - initialize a counter of nums, effectively counting the occurence of each number within nums.
        - we go through each number in the counter and see if the count of that number is bigger than n // 2.
        '''

        n = len(nums)
        count = Counter(nums)
        half = n // 2

        for val in count:
            if count[val] > half:
                return val
        
