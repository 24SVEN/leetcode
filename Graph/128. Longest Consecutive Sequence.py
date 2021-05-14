# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #The solution I initially solved is incorrect as it's time complexity is O(n log n) due to the sort.
        # if len(nums) == 0:
        #     return 0


        # temp_nums = nums.sort()

        # longest_int = 1
        # temp_int = 1

        # for i in range(len(nums)):
        #     if i == 0:
        #         pass
            
        #     if nums[i] == nums[i-1]:
        #         pass
        #     elif nums[i] == (nums[i-1] + 1):
        #         temp_int = temp_int + 1

        #         if temp_int > longest_int:
        #             longest_int = temp_int
        #     else:
        #         temp_int = 1

        # print(longest_int)
        # return longest_int

    # O(N) Time complexity solution:
        if len(nums) == 0:
            return 0
        test_set = set(nums)

        
        longest_int = 1
        for x in test_set:
            if (x-1) not in nums:

                temp_int = 1
                while (x+1) in nums:
                    temp_int +=1
                    longest_int = max(temp_int,longest_int)
                    x += 1
        print(longest_int)
        return longest_int



test = Solution()
test.longestConsecutive([100,4,200,1,3,2])

