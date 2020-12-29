import numpy as np
import cv2
import cvui

WINDOW_NAME = 'CVUI Test'

cvui.init(WINDOW_NAME)
frame = np.zeros((700, 1200, 3), np.uint8)

while True:
    frame[:] = (49, 52, 49) #BG Colour
    cvui.text(frame, 100, 150, 'Hello world!')

    cvui.rect(frame, 60, 10, 130, 90, 0xff0000, 0x00ff00)

    cvui.window(frame, 200, 300, 300, 300, "Video1")

    # Show window content
    cvui.imshow(WINDOW_NAME, frame)

    # if cv2.waitKey(20) == 27:
    #     break

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break