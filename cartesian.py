class CartesianProduct:
    def get_cartesian_product(self,A,B,C):
        product = []
        temp = []
        for i in A:
            for j in B:
                for k in C:
                    temp = [i,j,k]
                    product.append(temp)
        return product