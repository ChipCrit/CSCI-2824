#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class BitOperator(object):
    def bitOperator(self,bit1,bit2):
        x=str(bit1)
        y=str(bit2)
        for i in range (5):
            if bit1[i]==bit2[i]:
                y[i]=1
            else:
                y[i]=0
            if bit1[i] == 1:
                x[i]=1
            elif bit2[i] ==1:
                x[i]=1
            else:
                x[i]=0
        xf=int(x)
        yf=int(y)

        
#Start writing your code from here
