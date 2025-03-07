num=[10,20,-30,40,-50]
def mydata(n):
    if n<0:
        return True
    else:
        return False
z=[x for x in filter(mydata,num)]
print(z)