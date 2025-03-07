n=[1,2,3,4]
def conversion(n):
    return n*2.54

z=[x for x in map(conversion,n)]
print(z)