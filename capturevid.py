import cv2
import numpy as np
import cvui

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("facevid.mp4")

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for(x, y, w, h) in faces:
        frame = cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame', gray)

    key = cv2.waitKey(1)

    # Press Q on keyboard to  exit
    if cv2.waitKey(100) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
