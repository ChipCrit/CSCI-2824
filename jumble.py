import math
class Jumble():
    def get_total_distinct_combinations(self,input_string):
        max_chars=26
        length = len(input_string)
        occurances = [0] * max_chars
        for i in range(0, length):
            if(input_string[i] >= 'a' and input_string[i] <= 'z'):
                occurances[(ord)(input_string[i])-97] = occurances[(ord)(input_string[i])-97]+1
            elif(input_string[i]>='A' and input_string[i] <= 'Z'):
                occurances[(ord)(input_string[i])-65] = occurances[(ord)(input_string[i])-65]+1
        dividingFactorials = 1
        for i in range (0,max_chars):
            dividingFactorials = dividingFactorials * math.factorial(occurances[i])
        return math.factorial(len(input_string)) / dividingFactorials