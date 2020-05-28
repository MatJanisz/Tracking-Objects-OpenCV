import cv2

capture = cv2.VideoCapture(0)

while True:
    success, image = capture.read()

    cv2.imshow("Tracking", image)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break