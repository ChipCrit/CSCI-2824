class BaseConverter:
    def base_converter(self, num, from_base, to_base):
        baseTen = 0
        for x in range(0,len(num)):
            baseTen += (int(num[x])*pow(from_base,len(num)-1-x))
        power = 0
        while(pow(to_base,power)<baseTen):
            power+=1
        finalString=""
        finalNum=0
        y =1    
        power -=1
        while(power>-1):
            if(finalNum+pow(to_base,power)<=baseTen):
                while(finalNum+(y*pow(to_base,power))<=baseTen):
                    y+=1
                finalString+=str(y-1)
                finalNum += ((y-1)*pow(to_base,power))
            else:
                finalString+='0'
            y=1
            power-=1
        return finalString