#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class BitOperator(object):
    def bitOperator(self,bit1,bit2):
        x = int(bit1)
        y = int(bit2)
        sol1=x
        sol2=y
        if x[0] ==1 or y[0]==1:
            sol1[0]=1
        else:
            sol1[0]=0
        if x[1] ==1 or y[1]==1:
            sol1[1]=1
        else:
            sol1[1]=0
        if x[2] ==1 or y[2]==1:
            sol1[2]=1
        else:
            sol1[2]=0
        if x[3] ==1 or y[3]==1:
            sol1[3]=1
        else:
            sol1[3]=0
        if x[4] ==1 or y[4]==1:
            sol1[4]=1
        else:
            sol1[4]=0

        if x[0] ==1 and y[0]==1:
            sol2[0]=1
        else:
            sol2[0]=0
        if x[1] ==1 and y[1]==1:
            sol2[1]=1
        else:
            sol2[1]=0
        if x[2] ==1 and y[2]==1:
            sol2[2]=1
        else:
            sol2[2]=0
        if x[3] ==1 and y[3]==1:
            sol2[3]=1
        else:
            sol2[3]=0
        if x[4] ==1 and y[4]==1:
            sol2[4]=1
        else:
            sol2[4]=0
#Start writing your code from here
