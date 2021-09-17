class CartesianProduct:
    def get_cartesian_product(self,A,B,C):
        '''
        input: A,B,C are three input sets
        output: A * B * C
        '''
        lists = [[A],
                 [B],
                 [C]]
        final = []
        for i in range (0,len(A)):
            for j in range (0,len(B)):
                for k in range (0,len(C)):
                    if type(A[i]) != list:
                        A[i] = lists[i]


                    temp = [num for num in A[i]]
                    temp.append(B[j])
                    final.append(temp)
        return final