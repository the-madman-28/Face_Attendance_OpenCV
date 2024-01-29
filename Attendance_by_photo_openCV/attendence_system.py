import cv2
import face_recognition as face_rec
import os
import pyttsx3 as textSpeach
from datetime import datetime
import numpy as np

engine = textSpeach.init()

path = 'student_images'
studentImg = []
studentName = []
myList = os.listdir(path)

for cl in myList:
    curimg = cv2.imread(f'{path}/{cl}')
    studentImg.append(curimg)
    studentName.append(os.path.splitext(cl)[0])

def findEncoding(images):
    imgEncodings = []
    for img in images:
        img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeimg = face_rec.face_encodings(img)[0]
        imgEncodings.append(encodeimg)
    return imgEncodings

def MarkAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDatalist = f.readlines()
        nameList = [entry.split(',')[0] for entry in myDatalist]

        if name not in nameList:
            now = datetime.now()
            date_str = now.strftime('%Y-%m-%d')
            time_str = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{date_str},{time_str}')
            statement = f'Welcome to class {name}'
            engine.say(statement)
            engine.runAndWait()

EncodeList = findEncoding(studentImg)

vid = cv2.VideoCapture(0)

while True:
    success, frame = vid.read()
    smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

    faces_in_frame = face_rec.face_locations(smaller_frames)
    encode_faces_in_frame = face_rec.face_encodings(smaller_frames, faces_in_frame)

    for encode_face, face_loc in zip(encode_faces_in_frame, faces_in_frame):
        face_dis = face_rec.face_distance(EncodeList, encode_face)
        match_index = np.argmin(face_dis)

        if face_dis[match_index] < 0.6:  # Added a threshold for face recognition
            name = studentName[match_index].upper()
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 0, 255))
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_ITALIC, 1, (0, 200, 200), 2)
            MarkAttendance(name)

    cv2.imshow('video', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

# Release the VideoCapture object to close the camera
vid.release()
cv2.destroyAllWindows()
