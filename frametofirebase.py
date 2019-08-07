import dlib
from skimage import io
import numpy as np
import cv2
import math
import datetime
import pythontofirebase as ptf

detector = dlib.get_frontal_face_detector()# a detector to find the faces
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')#Training Set
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')#Training Set
#video capturing
v_cap= cv2.VideoCapture(0)#pass zero as parameter to use webcam
frame_rate=v_cap.get(5)#getting frame rate
count=1
suc=1
frames=[]
ts=[]
name=''
while suc:
    suc,frame = v_cap.read()#reading frames
    frame_id=v_cap.get(1)#getting frame number
    frames.append(frame)
    ts.append(count)
    count+=1
    dets = detector(frame, 1)# Ask the detector to find the bounding boxes of each face. The 1 in the second argument indicates that we should upsample the image 1 time. This will make everything bigger and allow us to detect more faces.
    print("Number of faces detected: {}".format(len(dets)))
    # Now process each face we found.
    for k, d in enumerate(dets):
        # Get the landmarks/parts for the face in box d.
        # Compute the 128D vector that describes the face in img identified by shape.
        shape = sp(frame, d)
        face_descriptor = facerec.compute_face_descriptor(frame, shape)
        ff=np.array(face_descriptor).tolist()
        ptf.insert(ff)
        #print(type(frame))
        #print(shape)
        #print(type(shape))
        now=datetime.datetime.now()
        name=str(now.strftime("%d_%m_%Y"))+' '+str(now.strftime("%H_%M_%S"))
        #print(name)
        dlib.save_face_chip(frame, shape, './face/face{0}.jpg'.format(name), size=150, padding=0.25)
v_cap.release()
