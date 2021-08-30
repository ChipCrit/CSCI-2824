#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class BitOperator(object):
    def bitOperator(self,bit1,bit2):
        x=""
        y=""
        for i in range (5):
            if bit1[i]==bit2[i]and bit2[i]=="1":
                y+="1"
            else:
                y+="0"
            if bit1[i] == "1":
                x+="1"
            elif bit2[i] =="1":
                x+="1"
            else:
                x+="0"
        xf=int(x)
        yf=int(y)

        return xf,yf

        
#Start writing your code from here
