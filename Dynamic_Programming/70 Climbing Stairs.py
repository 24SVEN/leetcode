# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution:
    def climbStairs(self, n: int) -> int:
        
        #DP
        dp = [0] * (n+1)

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        #starting values
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2


        for i in range(3,n+1):
            
            dp[i] = dp[i-1] + dp[i-2]
            
        print(dp)
        return dp[-1]



if __name__ == "__main__":
    test = Solution()
    print(test.climbStairs(6))

    

            

