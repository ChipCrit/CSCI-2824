#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class LogicGates(object):
    def get_circuit_output(self, A, B, C):
        #Start writing your code from here
        bool(A, B, C)
        if C == True and B == True:
            return True
        elif C == False and A == False:
            if A == False and B == True:
                return True
        else:
            return False