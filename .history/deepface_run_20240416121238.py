import os
import numpy as numpy
import cv2
from deepface import DeepFace 


class Detect_verify:
    def capture_live_faces(self):
        model_names = ["opencv", "ssd", "dlib", "mtcnn"]
        # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)
        while True:
            ret, self.frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # using "SSD(single shot detector)" for its faster performance
            try:
                detected_face = DeepFace.extract_faces(frame, detector_backend = "ssd")
            
            except:
                continue

            faces = detected_face[0]["facial_area"]
            
            cv2.rectangle(frame, (faces["x"],faces["y"]), (faces["x"]+faces["w"], faces["y"]+faces["h"]), (255, 0, 0), 2)

            cv2.imshow("Detect Faces", frame)


            if cv2.waitKey(1) & 0xFF == ord("v"):
                break


        cap.release()
        cv2.destroyAllWindows()    


    def verify_faces(self):
        models = ['VGG-Face', 'Facenet', 'OpenFace', 'DeepFace', 'DeepID', 'Dlib']
        model = DeepFace.build(models)
        DeepFace.verify_faces(frame, "dataset/Photo on 16-04-24 at 11.50 AM.jpg")








capture_live_faces()
