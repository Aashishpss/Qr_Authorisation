import cv2
import numpy as np
from pyzbar.pyzbar import decode
#image = cv2.imread("../Images/MultipleQR_Bar_code.PNG")
cap=cv2.VideoCapture(0)
with open("../Resources//myData.txt") as f:
    datalist = f.read().splitlines()
    print("My Approved Data", datalist)
while True:
    ret,frame=cap.read()
    if ret:
        frame=cv2.resize(frame,(0,0),None,0.6,0.6)
        for code in decode(frame):
            mydata= code.data.decode('utf-8')
            if mydata in datalist:
                output="Authorized"
                my_color=(0,255,0)
            else:
                output="Unauthorized"
                my_color=(0,0,255)
            pts = np.array([code.polygon], np.int32)
            pts.reshape((-1,1,2))
            cv2.polylines(frame,[pts],True,(255,0,0),3)
            pts1=code.rect
            cv2.putText(frame, output, (pts1[0], pts1[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, my_color,2)
        cv2.imshow("Input_info",frame)
        if cv2.waitKey(1) & 0xFF==ord('1'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows


    
