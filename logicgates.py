#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class LogicGates(object):
    def get_circuit_output(self, A, B, C):
        #Start writing your code from here
        a=bool(A)
        b=bool(B)
        c=bool(C)
        if c == True and b == True:
            return True
        elif c == False and a == False:
            if a == False and b == True:
                return True
        else:
            return False