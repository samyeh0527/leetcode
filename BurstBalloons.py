"""
nums = [3,1,5,8]


output :167
Explanation: nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
             coins = 3*1*5      +  3*5*8   + 1*3*8  +1*8*1 =167


"""

class BurstBalloons():
    def __init__(self) -> None:
        self.nums = [3,1,5,8]


    def solution(self):
        nums_length = len(self.nums)
        self.nums.insert(0,1)
        self.nums.append(1)
        dp = [[0] * (nums_length + 2 ) for _ in range (nums_length + 2)]
        print(dp)
        for len_ in range (1,nums_length + 1 ):
            for left in range(1, nums_length - len_ +2):
                right = left + len_ -1
                for k in range(left,right +1 ):
                    dp [left][right] = max(dp[left][right], dp[left][k -1 ] + self.nums[left - 1] * self.nums[k] * self.nums[right +1] + dp[k+1][right])
                                                   
        return dp[1][nums_length]

ANS = BurstBalloons().solution()
print(ANS)