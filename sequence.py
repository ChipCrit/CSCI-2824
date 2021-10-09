class Sequence():
    def next_in_sequence(self, input_sequence):
        difference = input_sequence[1]-input_sequence[0]
        difference = round(difference,2)
        if((round(input_sequence[2]-input_sequence[1],2) == difference)):
            num=(input_sequence[-1]+difference)
            return num
        else:
            r=round((input_sequence[1]/input_sequence[0]),2)
            difference=input_sequence[-1]*r
            return difference