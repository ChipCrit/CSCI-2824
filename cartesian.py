import itertools
class CartesianProduct:
    def get_cartesian_product(self,A,B,C):
        lists = [
            [A],
            [B],
            [C]
        ]
        for element in itertools.product([A],[B],[C]):
            print(element)
