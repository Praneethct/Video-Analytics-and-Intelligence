import dlib
from skimage import io
import numpy as np
import cv2
import pythontofirebase as ptf
import time

def cluster():
    s=time.time()
    query=''
    descriptors=[]
    dvec=dlib.vectors()
    date=input("enter a date in dd-mm-yyy format")
    from_time=input("enter start time in hh:mm format")
    to_time=input("enter end time in hh:mm format")
    data=ptf.retrive(date,from_time,to_time)
    for d in data:
        descriptors.append(dlib.vector(d))
    # Cluster the faces.
    labels = dlib.chinese_whispers_clustering(descriptors, 0.5)
    e=time.time()
    print(labels)
    print(len(descriptors))
    print(len(labels))
    labset=set(labels)
    print(labset)
    num_classes = len(set(labels))#total number of clusters
    print("Number of clusters: {}".format(num_classes))
    print(e-s)
    return num_classes

cluster()
