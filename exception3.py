num=[10,20,30]
try:
    print(num[50])
except IndexError as ie:
    print(ie)
else:
    print('no error')
finally:
    print('always executed')



