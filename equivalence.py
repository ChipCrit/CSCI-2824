class EquivalenceRelation():
    def check_equivalence(self, relation_members):
        #checking for reflexive:
        zero = False
        one = False
        two = False
        three = False
        for x in range(len(relation_members)):
            if relation_members[x]==(0,0):
                zero = True
            if relation_members[x]==(1,1):
                one = True
            if relation_members[x]==(2,2):
                two = True
            if relation_members[x]==(3,3):
                three = True
        if zero == False or one == False or two == False or three == False:
            return False
        #checking for symmetry:
        symmetryArr = [(0,1),(0,2),(0,3),(1,0),(1,2),(1,3),(2,0),(2,1),(2,3),(3,0),(3,1),(3,2)]
        for x in range(len(relation_members)):
            if relation_members[x]!=(0,0) and relation_members[x]!=(1,1) and relation_members[x]!=(2,2) and relation_members[x]!=(3,3):
                symmetryArr.remove(relation_members[x])
        if len(symmetryArr)%2!=0:
            return False
        #checking for transitivity:
        for x in range(4):
            for y in range(4):
                if (x,y) in relation_members:
                    for z in range(4):
                        if (y,z) in relation_members and not (x,z) in relation_members:
                            return False
        return True