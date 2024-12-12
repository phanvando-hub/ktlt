print ('Ho va ten : Phan Van Do')
print('MSSV: 205752020710012')

import sys
import os
def file_read_from_tail (fname, lines):
    bufsize = 8192
    fsize = os.stat (fname).st_size
    iter = 0
    with open (fname) as f:
        if bufsize > fsize:
            bufsize = fsize-l
            data=[]
            while True:
                iter +=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(' '.join(data[-lines:]))
                    break
file_read_from_tail('D:/test.txt',3)
