import cv2
import numpy as np
import cvui

#Initialize cascades
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

#1. Create an object. Zero for external camera.
# video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
video = cv2.VideoCapture("testface.mp4")

a = 0 #Frame counter

while True:

    a = a + 1

    #3. Create a frame object.
    check, frame = video.read()

    #Image Matrix Details
    #print (check)
    #print(a)
    #print (frame) #Representing image

    #6. Coverting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #EYES DETECTION
        # roi_gray = gray[y:y+h, x:x+w]
        # roi_colour = frame[y:h, x:x+w]

        # eyes = eye_cascade.detectMultiScale(roi_gray)

        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_colour, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        #SMILE DETECTION
        # rois_gray = gray[y:y+h, x:x+w]
        # rois_colour = frame[y:h, x:x+w]

        # smiles = smile_cascade.detectMultiScale(rois_gray)

        # for (sx, sy, sw, sh) in smiles:
        #     cv2.rectangle(rois_colour, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
    

    #4. Show the frame!
    cv2.imshow("Frame", frame) #'gray' on 'frame' if grayscale

    #5. For press any key to exit (miliseconds)
    #cv2.waitKey(0)

    #7. For playing
    key = cv2.waitKey(1)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

#2. Shutdown the camera.
video.release()

cv2.destroyAllWindows