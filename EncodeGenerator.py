#EncodeGenerator.py
import cv2
import face_recognition
import pickle #for dumping imgs
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facial-recognition-atten-53da8-default-rtdb.firebaseio.com/",
    'storageBucket': "facial-recognition-atten-53da8.appspot.com"
})

#importing the Student images to our list
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentRoll = []
image_extensions = ['.jpg', '.png', '.jpeg', '.bmp', '.gif']

for path in pathList:
    if any(path.lower().endswith(ext) for ext in image_extensions):
        img = cv2.imread(os.path.join(folderPath, path))
        if img is not None:
            imgList.append(img)
            studentRoll.append(os.path.splitext(path)[0])
            # print(os.path.splitext(path)[0])
            fileName = f'{folderPath}/{path}'
            bucket = storage.bucket()
            blob = bucket.blob(fileName)
            blob.upload_from_filename(fileName)

print(studentRoll)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)     #bgr to rgb opencv-bgr facerecg-rgb
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithRoll = [encodeListKnown, studentRoll]
print("Encoding Complete")

#now were saving in a pickle file
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithRoll, file)
file.close()
print("File Saved")