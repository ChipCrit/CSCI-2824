from itertools import chain, combinations
class PowerSet:
    def powerset(self, input_set):
        i_s = list(input_set)
        return chain.from_iterable(combinations(i_s,x)for x in range (len(input_set)+1))