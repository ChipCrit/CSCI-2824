#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class BitOperator(object):
    def bitOperator(self,bit1,bit2):
        x = bin(bit1)
        y = bin(bit2)
        sol1 = x|y
        sol2= x&y
        return sol1,sol2
#Start writing your code from here