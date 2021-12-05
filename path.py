class Graph():
    def is_path(self, A, start_node, end_node):
        x = len(A)
        visited = [False]*x
        
        dfs_queue = []
        dfs_queue.append(start_node)
        visited[start_node] = True
        
        while(dfs_queue):
            current = dfs_queue.pop(0)
            
            if current == end_node :
                return True
            index = 0
            for i in A[current]:
                if visited[index] == False and i != 0:
                    dfs_queue.append(index)
                    visited[index] = True
                index +=1
        return False