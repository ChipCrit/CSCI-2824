#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class BitOperator(object):
    def bitOperator(self,bit1,bit2):
        x = int(bit1)
        y = int(bit2)
        i=int(0)
        for i in range(0,5):
            x[i]=x or y
            y[i]=x and y
        return x,y
#Start writing your code from here