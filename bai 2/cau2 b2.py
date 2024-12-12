print("Sinh vien: Phan Van Do")
print("MSSV:205752020710012")
import math;
x1=int(input("enter x1--->"))
yl=int(input("enter y1--->"))

x2=int(input("enter x2--->"))
y2=int(input("enter y2--->"))

d1 = (x2-x1)*(x2-x1);
d2 = (y2-yl)*(y2-yl);
res = math.sqrt(d1+d2)
print ("Distance betwen two points:",res);
