print('ho va ten:Phan Van Do')
print('MSSV:205752020710012')

class daochuoi:
    def _init_(self,ch):
        self.chuoi=ch
    def dao(self):
        return ' '.join(reversed(self.chuoi.split()))
a='hello.py'
t=daochuoi(a)
print(t.dao())
