import cv2
import csv
import os
import face_recognition
import datetime

known_face = []
known_name = []

for filename in os.listdir('image'):
    image = face_recognition.load_image_file(os.path.join('image', filename))
    encoding = face_recognition.face_encodings(image)[0]
    known_face.append(encoding)
    known_name.append(os.path.splitext(filename)[0])

video_capture = cv2.VideoCapture(0)

attendance_marked = False
- Implement face data loading and webcam capture