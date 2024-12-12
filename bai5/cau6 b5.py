print('Ho va ten:Phan Van Do')
print('MSSV:205752020710012')

A=[3,6,9,12,34,64]
max = A[0]
for i in range (len(A)):
    if A[i] > max:
        max = A[i]
        i = i+1
for k in range (len(A)):
    if A[k] == max:
        print('gia tri lon nhat la:',max,"vi tri thu:", k)

min = A[0]
for i in range (len(A)):
    if A[i] < min:
        min = A[i]
        i = i+1
for k in range (len(A)):
    if A[k] == min:
        print('gia tri nho nhat la:',min,"vi tri thu:",k)
    
