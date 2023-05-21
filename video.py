import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #ссылка на библиотеку для выбора модели распознавания:https://github.com/opencv/opencv/tree/4.x/data/haarcascades

# img = cv2.imread('img1.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# faces = face_cascades.detectMultiScale(img_gray)

# for (x, y, w, h) in faces: # тоже самое, что и вложенный for
#     cv2.rectangle(img_gray, (x, y), (x + w, y + h), (255, 0, 0), 2)


# cv2.imshow('Result', img_gray)
# cv2.waitKey(0)

#cap = cv2.VideoCapture(0) #выбираем камеру 0..1..2..итд, если есть или:
# путь к файлу 
cap = cv2.VideoCapture('video.mp4')

while True:
    _, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
