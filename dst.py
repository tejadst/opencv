from cv2 import *
from numpy import *
import color2.py
import matplotlib.pyplot as plt
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
while 1:
    s, img = cam.read()
    if s:    # frame captured without any errors
        for i in range(420):
            for j in range(640):
                if img[i][j][1]<50 and img[i][j][2]<50 and img[i][j][0]<50:
                    img[i][j][1]=200
        img=img.astype(uint8)
        imshow("cam-test",img)
        if waitKey(1) == ord('q'):
            break
print()
cam.release()
destroyAllWindows()
