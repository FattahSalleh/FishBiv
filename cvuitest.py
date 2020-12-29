import numpy as np
import cv2
import cvui

WINDOW_NAME = 'CVUI Test'

cvui.init(WINDOW_NAME)
frame = np.zeros((700, 1200, 3), np.uint8)

while True:
    frame[:] = (49, 52, 49)
    cvui.text(frame, 10, 15, 'Hello world!')

    # Show window content
    cvui.imshow(WINDOW_NAME, frame)

    # if cv2.waitKey(20) == 27:
    #     break

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break