import copy
class Mat:
    def __init__(self,A):
        self.nr=len(A)
        self.nc=len(A[0])
        self.data=copy.deepcopy(A)

    def mul(self,b):
        if self.nc==b.nr:
            A=[]
            for i in range(self.nr):
                ci=[]
                for j in range(b.nc):
                    sum=0
                    for k in range(self.nc):
                        sum+=self.data[i][k]*b.data[k][j]
                    ci.append(sum)
                A.append(ci)
            return(Mat(A))
        else:
            print("cant multiply")
            return -1
        


A=[[0,1,2],[3,-1,4]]
a=Mat(A)
B=[[0,1,2,3],[9,2,5,7],[8,6,5,4]]
b=Mat(B)
c=a.mul(b)
print(c.data)
# d=a.add(b)

    # def mul(self,A):
    #     print("enter")
    #     for i in range(self.row):
    #         row=[]
    #         for j in range(self.col):


