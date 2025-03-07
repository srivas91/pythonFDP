class Student:
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.course=c
    def __str__(self):  #toString() in java
        return f'{self.id}-{self.name}-{self.course}'
s1=Student(1001,'mani','python')
print(s1)