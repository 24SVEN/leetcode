# You are given an m x n integer matrix heights representing the height of each unit cell in a continent. 
# The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

# Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

# Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.


# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

#   1   2   2   3   5
#   3   2   3   4   4
#   2   4   5   3   1
#   6   7   1   4   5
#   5   1   1   2   4


# Example 2:

# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]

# Constraints:

#     m == heights.length
#     n == heights[i].length
#     1 <= m, n <= 200
#     1 <= heights[i][j] <= 105

from typing import List
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        pacific_coords =[]
        atlantic_coords = []

        height = len(matrix)
        width = len(matrix[0])
        
        for col in range(width):
            pacific_coords.append((0,col))
            atlantic_coords.append([height-1,col])
        
        for row in range(height):
            pacific_coords.append([row,0])
            atlantic_coords.append([row,width-1])
        
        # print(pacific_coords)
        # print(atlantic_coords)

        visited_pacific = set()
        visited_atlantic = set()

        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(row,col,visited):
            visited.add((row,col))
            for di,dj in dir:
                new_row = di+row
                new_col = dj+col

                if 0<=new_row<height and 0<=new_col<width and (new_row,new_col) not in visited and matrix[new_row][new_col] >= matrix[row][col]:
                    dfs(new_row,new_col,visited)

        for row,col in pacific_coords:
            dfs(row,col,visited_pacific)
        
        for row,col in atlantic_coords:
            dfs(row,col,visited_atlantic)
        


        # print(visited_pacific)
        # print(visited_atlantic)
        print(visited_pacific & visited_atlantic)
        return visited_pacific & visited_atlantic




        
    
test_instance = Solution()
test_instance.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])