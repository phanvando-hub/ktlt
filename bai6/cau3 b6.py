print('ho va ten:Phan Van Do')
print('MSSV:205752020710012')

class Nguoi(object):
 def getGender(self):
  return "Unknoun"

class Nam(Nguoi):
 def getGender(self):
     return "Nam"
class Nu(Nguoi):
 def getGender(self):
     return "Nu"

aNam = Nam()
aNu = Nu()
print (aNam.getGender())
print (aNu.getGender())
