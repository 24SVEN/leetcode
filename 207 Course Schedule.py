from typing import List
#https://www.youtube.com/watch?v=yPldqMtg-So&ab_channel=TimothyHChang
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #key is course | values is prereq
        rules = {}

        #generate dictionary [Adjacency list]
        for pre_req in prerequisites:
            #pre_req[0] = Course
            #pre_req[1] = Pre-Requisite
            course = pre_req[0]

            #if the course already exists in dictionary 'rules', append otherwise create a new entry
            if course in rules:
                rules[course].append(pre_req[1])
            else:
                rules[course] = [pre_req[1]]

        print(rules)

        tracking = {}
        for x in range(numCourses):
            check_list = {}
            if x in rules:
                if x not in tracking and self.check_if_cycle(x,rules,check_list,tracking):
                    return False
        
        return True
        

    def check_if_cycle(self,course_num,rules,check_list,tracking):
        check_list[course_num] = True
        tracking[course_num] = True

        if course_num in rules:
            for x in rules[course_num]:
                if x not in tracking and self.check_if_cycle(x,rules,check_list,tracking):
                    return True
                elif x in check_list:
                    return True
        
        #We are popping the dictionary keys because these prerequisite courses shouldn't be marked as viisted (TRUE value) for the next x (the next course)
        check_list.pop(course_num)
        return False

        
        #return False


test = Solution()

# print(test.canFinish(20,[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
# print(test.canFinish(3,[[1,0],[0,2],[2,1]]))



#Expected Answer: True
#print(test.canFinish(2,[[0, 1]]))
#print(test.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))

#Expected Answer: False
#print(test.canFinish(8,[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
#print(test.canFinish(4,[[0,1],[1,2],[0,3],[3,0]]))
print(test.canFinish(2,[[1,0],[0,1]]))









        





        # #Returns True if there is a loop
        # #Currently function is only checking if there is one level loop. Loop could be [0 -> 1 -> 2 -> 0].
        # #Basically function needs to have a key start input and recurse until no more or loop.
        # def check_loop(key,rules_dict,storage):
        #     print('entered here!','key is :',key, ' and storage is :',storage)
        #     if key in storage:
                
        #         return True
        #     else:
        #         storage[key] = []
        #         pre_req = rules_dict[key]

        #         #If they key itself is in pre_req, return True
        #         if key in pre_req:
        #             return True


        #         for pr in pre_req:
        #             storage[key].append(pr)
        #             if pr in rules_dict:
        #                 if check_loop(pr,rules_dict,storage):
        #                     return True

        #     return False
        

        # original_rules = rules.copy()
        
        # #Loop through adj. list
        # while len(rules) > 0:
        #     keys = list(rules.keys())
        #     #vals = list(rules.values())
        #     storage = {}
        #     #pass function check here
        #     print('main loop')
        #     if check_loop(keys[0],original_rules,storage):
        #         return False

        #     rules.pop(keys[0])

        # return True

        # # #print(check_loop(rules))
        # # if check_loop(rules):
        # #     return False
        # # else:
        # #     return True



