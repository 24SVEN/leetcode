
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


#BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        queue = []


        # if node is None:
        #     return []

        if not node:
            return node

        #enqueue
        queue.append(node)

        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        while len(queue)>0:
            
            current_node = queue.pop(0)

            #loop through neighbors
            for node_neighbor in current_node.neighbors:
                #check if in visited
                if node_neighbor in visited:
                    pass
                #if not visited, add to queue
                else:
                    visited[node_neighbor] = Node(node_neighbor.val,[])
                    queue.append(node_neighbor)

                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[current_node].neighbors.append(visited[node_neighbor])


        return visited[node]

            




        

#DFS
class Solution:
    def __init__:
        self.visited = {}


    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        #check if node is in visited
        if node in self.visited:
            #Returns the node if it is in the dictionary
            return self.visited[node]
        #copy node if it is not in visited
        else:
            clone_node = Node(node.val,[])

            self.visited[node] = clone_node

            if node.neighbors:
                #RECURSION ON LIST COMPREHENSION!!!
                clone_node.neighbors = [self.cloneGraph(node_neighbor) for node_neighbor in node.neighbors]

            return clone_node

