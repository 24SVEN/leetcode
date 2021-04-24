from typing import List
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.



# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
# Example 4:

# Input: coins = [1], amount = 1
# Output: 1
# Example 5:

# Input: coins = [1], amount = 2
# Output: 2
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


class Solution:

    def create_matrix(self,coins,amount):
        # mtx = [[amount + 1 for x in range(1,amount+1)] for c in range(len(coins) + 1)]
        # for i in range(0,len(mtx[0])):
        #     mtx[0][i] = i+1
        # return mtx
        matrix = [[0 for m in range(amount + 1)] for m in range(len(coins) + 1)]
        for i in range(amount + 1):
            matrix[0][i] = i
        return matrix

    def coinChange(self, coins: List[int], amount: int) -> int:
        temp_mtx = self.create_matrix(coins,amount)

        # for row in range(1,len(temp_mtx)):
        #     for col in range(1,amount):

        for row in range(1, len(coins) + 1):
            for col in range(1, amount + 1):

                #print(temp_mtx[row][col],row,col,coins[row-1])
                #print(temp_mtx)

                #if coin is equal to col, return 1
                if coins[row-1] == col:
                    temp_mtx[row][col] = 1

                #if coin is greater than col, retrieve previous row's value?
                elif coins[row-1] > col:
                    temp_mtx[row][col] = temp_mtx[row-1][col]
                    print('entered here',row,col)

                #otherwise get the min of the row above vs the current row's [column - coin] + 1
                else:
                    #print(min(temp_mtx[row-1][col],temp_mtx[row][col- coins[row-1]]+1))
                    temp_mtx[row][col] = min(temp_mtx[row-1][col],1 + temp_mtx[row][col - coins[row - 1]])
                print(temp_mtx[row][col],row,col)
        return temp_mtx


test = Solution()
print(test.coinChange([1,2,5],11))

# 5866
# 154


# # print(test.create_matrix([1,2,5],11))

# print(test.coinChange([1,2,5],11))





# class Solution(object):
#     def coinChange(self, coins, amount):
        


# #         #top down approach

#         t = amount
#         #print(coins)
#         coins.sort()
#         coins.reverse()
#         #print(coins)
#         answer = 999999

#         if amount == 0:
#             return 0
        
#         #s is steps
#         #t is temp amount
#         s = 0
#         def helper_func(coins,t,s,answer):
#             for c in coins:
#                 print(t,c,s)
#                 if t - c == 0:
#                     s = s+1
#                     answer = min(answer,s)
#                     return s
#                 elif t - c > 0:
#                     t =  t - c 
#                     s = s+1
#                     return helper_func(coins,t,s,answer)
#                 elif t - c < 0 and c == min(coins):
#                     #skip for now
#                     #return -1
#                     return -1
        

#         answer = min(answer,helper_func(coins,t,s,answer))
        
#         if answer == 999999:
#             return -1
#         else:
#             return answer

# test = Solution()
# print(test.coinChange([186,419,83,408],6249))
