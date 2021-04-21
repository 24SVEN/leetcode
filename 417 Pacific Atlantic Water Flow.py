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
