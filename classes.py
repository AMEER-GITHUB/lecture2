# magic method '__init__'auto called when point is created & self is object notation like 'this'

class Point():
    def __init__(self, input1, input2):
        self.x=input1
        self.y=input2

p=Point(2,8)
print(p.x)
print(p.y)