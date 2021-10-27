class Recursive:
    counter = 0

    def get_item_at_n(self,n):
        self.counter += 1
        if (n==0):
            return 0
        elif (n==1):
            return 1
        elif (n==2):
            return 2
        else:
            if(n%2==0):
                return (2 * self.get_item_at_n(n-1))+self.get_item_at_n(n-2)
            else:
                return self.get_item_at_n(n-1) + (2 * self.get_item_at_n(n-2))