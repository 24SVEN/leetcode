# You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

# Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

# Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.


# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# Example 2:

# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]

# Constraints:

#     m == heights.length
#     n == heights[i].length
#     1 <= m, n <= 200
#     1 <= heights[i][j] <= 105

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        #BFS

        max_right = len(matrix[0])
        max_left = 0
        max_top = 0
        max_bot = len(matrix)

        queue = []

        #first in first out

        queue.append(matrix[0])

        #queue
        visited = []

        #final list of coord
        answer = []

        #need some way to identify if it's in atlantic or pacific
        #think list of coordinates is easiest. Can also say if x is 0 then pacific and when x is N (max), then Atlantic. Same logic for vertical
        pacific_list =[]
        atlantic_list = []
        
        #let's generate a mtrix? or loop through..
        for hor_lists in matrix:
            for vert_lists in hor_lists:
                if [x,y] in visited:
                    pass
                else:
                    if bfs(x,y,matrix,visited):
                        answer.append([x,y])
                    



    #This function will return True if it there is path to pacific and atlantic
    def bfs(self,x,y,matrix,visited):
        #if the coord has been visited
        if [x,y] in visited:
            #return True if it already in the answer list
            if [x,y] in answer:
                return True
            else:
                return False
        
        #if the coord is not in visited
        


    def check_move_right(self,matrix,row,x,max_right):
        if x + 1 < max_right:
            if matrix[row][x] <= matrix[row][x+1]:
                return True
        
        return False

    def check_move_bottom(self,matrix,col,y,max_bottom):
        if y + 1 < max_bottom:
            if matrix[col][y] <= matrix[col][y+1]:
                return True
        
        return False

    def check_move_left(self,matrix,row,x,max_left):
        if x - 1 > max_left:
            if matrix[row][x] <= matrix[row][x-1]:
                return True
        
        return False

    def check_move_top(self,matrix,col,y,max_top):
        if y - 1> max_top:
            if matrix[col][y] <= matrix[col][y-1]:
                return True

        return False
    

    
test_instance = Solution()
