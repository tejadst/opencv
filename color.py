import numpy as a
import cv2
r=1
g=1
b=1
scale=1
np=a.zeros((4096,4096))
x=a.zeros((4096,4096,3),a.uint8)
for i in range(4096):
    for j in range(4096):
       if i==0 and j==0:
           continue
       elif j==0:
           p=i-1
           q=4095
       else:
           p=i
           q=j-1
       np[j][i] = np[q][p] +scale
print(a.shape(x));
for i in range(4096):
    for j in range(4096):
        for k in range(3):
            if k==0:
                x[i][j][k] = ((((np[i][j]) % 65536) % 256))
            elif k==1:
                x[i][j][k] =((((np[i][j]) % 65536) / 256) )
            else:
                x[i][j][k] =(((np[i][j]) / 65536))
print(x[511][511])
cv2.imshow('dk',x)
cv2.imwrite('G:\photos\ds.jpg',x)
cv2.waitKey(0)
