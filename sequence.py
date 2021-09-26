class Sequence():
    def next_in_sequence(self, input_sequence):
        difference = 0
        difference = input_sequence[1]-input_sequence[0]
        if((input_sequence[2]-input_sequence[1]==difference)):
            num=input_sequence[-1]+difference
            return num
        else:
            r=input_sequence[1]/input_sequence[0]
            difference=input_sequence[-1]*r
            return round(difference,2)