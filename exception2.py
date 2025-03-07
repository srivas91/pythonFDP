d={'stid':1001,'stname':'rajesh'}
try:
    print(d['location'])
except KeyError as ke:
    print(ke)
else:
    print('no error')



