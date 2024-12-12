print('ho va ten:Phan Van Do')
print('MSSV:205752020710012')
class Circle(object):
    def _init_(self, r):
      self.radius = r
############################
    def area(self):
      return self.radius**2*3.14
aCircle = Circle(3)
print (aCircle.area())
