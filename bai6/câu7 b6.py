class Circle(object):
    def _init_ (self,r ):
        self.bankinh =r
    def dientich (self):
        return self.bankinh**2*3.14
    def chuvi (self):
        return self.bankinh*2*3.14
r = int (input("Nhập bán kính: "))
aCircle = Circle(r)
print("Diện tích hình tròn là: ",aCircle.dientich())
print("Chu vi hình tròn là: ", aCircle.chuvi())
