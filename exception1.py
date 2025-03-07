a,b=10,2
try:
    print(a//b)
except ArithmeticError as ae:
    print(ae)

