#Example
'''
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l
        if k > 0:
            nums[0:l] = nums[-k:] +nums[:-k]
        
        
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            
            numReverse(0, n - 1) #[7, 6, 5, 4, 3, 2, 1]
            numReverse(0, k - 1) #[5, 6, 7, 4, 3, 2, 1]
            numReverse(k, n - 1) #[5, 6, 7, 1, 2, 3, 4]
