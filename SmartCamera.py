import cv2
import numpy as np
import time
import threading
from tkinter import *
from PIL import Image


def Launch():

    #defining both cascade files
    face_cascade = cv2.CascadeClassifier('face.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    #text font
    myfont = cv2.FONT_HERSHEY_COMPLEX

    def Timer():
    
        time = 30 #timer in seconds*10
        
        while time >= 10:
            _, canvas = video_capture.read()

            if time%10 == 0:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(canvas,str(time//10),(250,250), font, 7,(255,255,255),10,cv2.LINE_AA)

            cv2.imshow('MagicBooth',canvas)
            cv2.waitKey(125)
            time = time-1

        else:
            _, canvas = video_capture.read()
            cv2.imshow('MagicBooth',canvas)
            cv2.waitKey(2000)
            
            # Save the frame
            cv2.imwrite(r'PATH_TO_SAVE_PICTURE\capture.jpg',canvas)



    def detect(gray, frame):

        f_count = 0 #face count
        s_count = 0 #smile count
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        #loop to check for faces
        for (x, y, w, h) in faces:
            f_count=f_count+1
            f_count_str = str(f_count)
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
            cv2.putText(frame, 'FACE'+f_count_str, (x, y), myfont, 1, (0,0,255), 2, cv2.LINE_8 )
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
            
            #loop to check for smile
            for (sx, sy, sw, sh) in smiles:
                s_count=s_count+1
                s_count_str = str(s_count)
                
                #draws a rectangle and label "smile" around the smile (could be removed)
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 2)
                cv2.putText(frame, 'SMILE'+s_count_str, ((sx + sw), (sy + sh)), myfont, 1, (0,0,255), 2, cv2.LINE_8 )
                
                #starts timer
                Timer()
                
                #opens the picture captured to view
                im = Image.open(r'PATH_TO_SAVE_PICTURE\capture.jpg')
                im.show()                 
  
# This method will show image in any image viewer  

                break
            
        return frame


#setting video capture to be live camera 
video_capture = cv2.VideoCapture(0)

#loop to capture the frames
while True:
    _, frame = video_capture.read()
    k = cv2.waitKey(125)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canvas = detect(gray, frame)

    cv2.imshow('MagicBooth',canvas)

    if k == 27:
        break

    video_capture.release()
    cv2.destroyAllWindows()

#A simple tkinter gui with a single button to launch the script
Window = Tk()
Window.geometry('250x50')
Window.title('Magic Camera')
Window.configure(bg='grey')
Window.resizable(0, 0)

Launch_bt = Button(Window, text='Launch', bg='white', fg='black', command=Launch,  height = 2, width = 5)
Launch_bt.pack()

Window.mainloop()
