#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class BitOperator(object):
    def bitOperator(self,bit1,bit2):
        x = int(bit1,2) | (bit2,2)
        y = int(bit1,2) & (bit2,2)
        binarysol1 = bin(x)
        binarysol2= bin(y)
        sol1 = binarysol1[2,7]
        sol2 = binarysol2[2,7]
        return sol1,sol2
#Start writing your code from here