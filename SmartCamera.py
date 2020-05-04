import cv2
import numpy as np
import time
import threading
from tkinter import *


def starttheshit():
    face_cascade = cv2.CascadeClassifier('face.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    myfont = cv2.FONT_HERSHEY_COMPLEX


    def Timer():
        j = 30
        while j>=10:
            _, canvas = video_capture.read()

            if j%10 == 0:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(canvas,str(j//10),(250,250), font, 7,(255,255,255),10,cv2.LINE_AA)
            cv2.imshow('a',canvas)
            cv2.waitKey(125)
            j = j-1
        else:
            _, canvas = video_capture.read()
            cv2.imshow('a',canvas)
            cv2.waitKey(2000)
            # Save the frame
            cv2.imwrite('C:/*path*/capture.jpg',canvas)



    def detect(gray, frame):
        f_count = 0
        s_count = 0
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            f_count=f_count+1
            f_count_str = str(f_count)
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
            cv2.putText(frame, 'FACE'+f_count_str, (x, y), myfont, 1, (0,0,255), 2, cv2.LINE_8 )
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

            for (sx, sy, sw, sh) in smiles:
                s_count=s_count+1
                s_count_str = str(s_count)
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 2)
                cv2.putText(frame, 'SMILE'+s_count_str, ((sx + sw), (sy + sh)), myfont, 1, (0,0,255), 2, cv2.LINE_8 )
                Timer()
                break
        return frame



    video_capture = cv2.VideoCapture(0)
    while True:
        _, frame = video_capture.read()
        k = cv2.waitKey(125)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        canvas = detect(gray, frame)

        cv2.imshow('a',canvas)

        if k == 27:
            break

    video_capture.release()
    cv2.destroyAllWindows()


root = Tk()
root.geometry('550x290')
root.title('Magic Camera')
root.configure(bg='grey')
root.resizable(0, 0)

fp = Button(root, text='START', bg='white', fg='black', command=starttheshit,  height = 5, width = 10)
fp.pack()
root.mainloop()
# s = float(k)

# for cast in (int, float):
#     k = cast(e_interest.get())
#     break
#
#
# s = float(k)
