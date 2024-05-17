from cv2 import CascadeClassifier, COLOR_BGR2GRAY, cvtColor, flip, VideoCapture, CAP_DSHOW


class Face:
    __faceCascade = CascadeClassifier('D:/Python Project/keep_screen_on/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


    def preprocessFace(self, face):
        face = flip(face, 1)
        grayFace = cvtColor(face, COLOR_BGR2GRAY)
        return grayFace


    def captureCamera(self):
        cap = VideoCapture(0, CAP_DSHOW)
        if not cap.isOpened():
            print("Cannot open camera")
            return -1
        _, face = cap.read()
        cap.release()
        return self.preprocessFace(face)


    def detectFace(self):
        face = self.captureCamera()
        if face == -1:
            return -1
        faceCoordinates = self.__faceCascade.detectMultiScale(
            face,
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20)
        )

        # for (x,y,w,h) in faces:
        #     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #     roi_gray = gray[y:y+h, x:x+w]
        #     roi_color = img[y:y+h, x:x+w]
            
        # cv2.imshow('video',img)

        return type(faceCoordinates) != tuple
