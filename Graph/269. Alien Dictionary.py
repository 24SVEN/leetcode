# #HARD

# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. 
# If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.


# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

# Example 2:

# Input: words = ["z","x"]
# Output: "zx"

# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # alien_dict = {}
        
        # for ea_word in words:
        #     for ea_char in ea_word:
        #         if ea_char in alien_dict:
        #             pass
        #         else:
        #             alien_dict[len(alien_dict)] = ea_char

        # print(alien_dict)

        largest_word_char_count = len(max(words))
        #rltn_store = []
        rltn_store = {}

        for i in range(len(words)-1):
            j = 0
            while j != -1:
                if j > len(words[i]):
                    j = -1
                elif words[i][j] != words[i+1][j]:
                    #rltn_store.append([words[i][j],words[i+1][j]])
                    if words[i] in rltn_store:
                        rltn_store[words[i][j]].append(words[i+1][j])
                    else:
                        rltn_store[words[i][j]] = [words[i+1][j]]
                    j = -1
                else:
                    j+=1
    
        print(rltn_store)

        #check for cycles
        # for elemen in rltn_store:
        #     reveresed_elemen = [elemen[1],elemen[0]]
        #     if reveresed_elemen in rltn_store:
        #         print('entered here and this is a cycle!')
        #         return []
        for key in rltn_store:
            for val in rltn_store[key]:
                if val in rltn_store:
                    if key in rltn_store[val]:
                        print('this is a cycle!')
                        return []
            

        #BFS??
        bfs_queue = []

        first_key = list(rltn_store.keys())[0]
        bfs_queue.append(first_key)
        #print(bfs_queue)
        while bfs_queue:
            for val in rltn_store[bfs_queue[0]]:
                bfs_queue.append(val)
            





test_case = Solution()
test_case.alienOrder(["wrt","wrf","er","ett","rftt"])
#test_case.alienOrder(["z","x","z"])