class Sequence():
    def next_in_sequence(self, input_sequence):
        difference = 0
        difference = input_sequence[1]-input_sequence[0]
        round(difference,2)
        if((input_sequence[2]-input_sequence[1]==difference)):
            num=input_sequence[-1]+difference
            round(num,2)
            return num
        else:
            r=input_sequence[1]/input_sequence[0]
            round(r,2)
            difference=input_sequence[-1]*r
            round(difference,2)
            return difference