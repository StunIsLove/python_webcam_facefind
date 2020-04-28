import cv2
from cv2 import CascadeClassifier
import sys

print("Укажите ID камеры:")
id = int(input())

print("Для завершения программы нажмите ESC")

faceCascade = CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(id)

while True:
	count = 0

	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		count += 1
		cv2.putText(img,str(count),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,0,255),2)

	cv2.imshow("OpenCV window", img)
	if cv2.waitKey(10) == 27:
		break

cap.release()
cv2.destroyAllWindows()