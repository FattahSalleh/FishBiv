import cv2, time

#1. Create an object. Zero for external camera.
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

a = 0

while True:

    a = a + 1

    #3. Create a frame object.
    check, frame = video.read()

    print (check)
    print (frame) #Representing image

    #6. Coverting to grayscale
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #4. Show the frame!
    cv2.imshow("Frame", frame) #'gray' on 'frame' if grayscale

    #5. For press any key to exit (miliseconds)
    #cv2.waitKey(0)

    #7. For playing
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#2. Shutdown the camera.
video.release()

cv2.destroyAllWindows