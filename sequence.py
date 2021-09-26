class Sequence():
    def next_in_sequence(self, input_sequence):
        difference = 0
        difference = input_sequence[1]-input_sequence[0]
        if((input_sequence[2]-input_sequence[1]==difference)):
            num=input_sequence[-1]+difference
            return float(round(num,2))
        else:
            r=input_sequence[1]/input_sequence[0]
            difference=input_sequence[-1]*r
            return float(round(difference,2))