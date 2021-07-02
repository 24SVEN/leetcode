# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.



from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #visited = []
        num_islands = 0

        for j in range(len(grid)):
            for i in range(len(grid[0])):
                #if visited, skip
                #print(j,i)
                # if (j,i) in visited:
                #     pass
                #if 0, add to visited and move to next square
                # elif grid[j][i] == "0":
                #     visited.append((j,i))
                #This is a part of an island. Perform BFS and add all coord of island to visited.
                if grid[j][i] == '1':

                    bfs_visited = self.bfs(grid,(j,i))

                    #add all island values to visited
                    #visited = visited + bfs_visited
                    num_islands += 1

        return num_islands

    #This bfs function returns all coordinates for the current island
    def bfs(self,grid,start_coord):
        #up, down, right, left
        possible_directions = [(1,0),(-1,0),(0,1),(0,-1)]

        queue = [start_coord]
        #bfs_visited = []


        while queue:
            start_pos = queue.pop()
            grid[start_pos[0]][start_pos[1]] = '#'
            for ea_dir in possible_directions:
                
                #adding direction to starting coordinate
                new_coord = tuple(map(sum, zip(start_pos, ea_dir)))
                #if the new coordinate is a valid coord (not out of bounds)
                if new_coord[0]>=0 and new_coord[0] < len(grid) and new_coord[1] < len(grid[0]) and new_coord[1] >= 0:
                    # if new_coord in visited:
                    #     pass
                    #if the coord hasn't been visited yet and it is an island, add it to queue
                    if grid[new_coord[0]][new_coord[1]] == '1': 
                        queue.append(new_coord)
                        #bfs_visited.append(new_coord)
   
        return None

            

#Test cases
test_case = Solution()
# #expecting 1 island returned for 1st test
# if test_case.numIslands([
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]) == 1:
#     print('passed first test')

# #expecting 3 islands returned for 2nd test
# if test_case.numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]) == 3:
#     print('passed second test')

