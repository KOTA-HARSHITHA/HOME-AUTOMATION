import cv2
import numpy as np
import face_recognition
import pandas as pd
from os import listdir
from os.path import isfile, join
import time as t

ef = pd.read_csv('F:/actors.csv')
# for cscv give the location of file above 
serialno = ef["Serial No"].tolist()
names = ef["Name"].tolist()
photolocation = ef["Photo Location"].tolist()
# for Photo Location change the locations of the images in csv file
n = len(serialno)
face = []
face_encod = []

for i in range(n):
    face.append(face_recognition.load_image_file(photolocation[i]))
    face_encod.append(face_recognition.face_encodings(face[i])[0])

names_upper = [name.upper() for name in names]

Training_Data, Labels = [], []

data_path = 'F:/faces/'
for f in listdir(data_path):
    image_path = join(data_path, f) 
    Labels.append(f[7:-4])
    if image_path.endswith(('.png', '.jpg', '.jpeg')): # you can add other formats
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))



Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")

face_classifier = cv2.CascadeClassifier('F:/face detection/faceDetection/haarcascade_frontalface_default.xml')

def face_detector(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return img,[]

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))
        cv2.rectangle(img, (x, (y+h) + 35), (x+w, y+h), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name, (x + 6, (y+h) + 30), font, 1.0, (0, 0, 0), 2)

    return img,roi

cap = cv2.VideoCapture(0)                                                                                        

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    
    
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(face_encod, face_encoding, tolerance=0.5)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(face_encod, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = names_upper[best_match_index]
                

            face_names.append(name)
    image, face = face_detector(frame)        

    process_this_frame = not process_this_frame    

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
        cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)


        if confidence > 77 and name != "Unknown":
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', image)
            
        else:
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)


    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image)
        pass

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
cap.release()
cv2.destroyAllWindows()