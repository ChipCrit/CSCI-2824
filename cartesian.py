class CartesianProduct:
    def get_cartesian_product(self,A,B,C):
        product = []
        temp = []
        for i in A:
            for j in B:
                for k in C:
                    temp.clear()
                    temp.append(i)
                    temp.append(j)
                    temp.append(k)
                    product.append(temp)
        return product