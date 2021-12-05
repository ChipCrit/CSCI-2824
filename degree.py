class Graph():
    def get_degrees(self, A):
        ''' A here is the adjacency matrix '''
        x = len(A)
        inD = [0 for y in range(x)]
        outD = [0 for z in range(x)]
        for i in range(x):
            for j in range(x):
                if A[i][j]==1:
                    outD[i]+=1
                    inD[j]+=1
        return [(inD[k], outD[k]) for k in range(x)]