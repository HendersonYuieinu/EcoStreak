import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    # validacao, frame = webcam.read()
    while True:
        validacao, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("teste", frame)
        key = cv2.waitKey(30)
        if key == ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()