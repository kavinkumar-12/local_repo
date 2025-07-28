
class prime:
    def __init__(self,n):
        self.n=n

    def calculate(self):
        for k in range(2,self.n+1):
            count=0
            for j in range(1,k+1):
                if k%j==0:
                    count+=1
            if count==2:
                print(k,end=" ")

a=int(input("enter a number to find primenumbers with in : "))
pri=prime(a)
pri.calculate()