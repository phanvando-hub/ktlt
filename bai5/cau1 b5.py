print('Ho va ten:Phan Van Do')
print('MSSV:205752020710012')

import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2024-10-23T13:25:45', format)
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))
#Xac dinh ngay gio hom nay
t2 = dt.datetime.now()
diff = t2 - t1
print('chenh lech bao nhieu ngay:'+ str(diff.days))
