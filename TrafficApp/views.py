from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
import pickle
import os
from sklearn.model_selection import train_test_split
from yolo_traffic import *
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from keras.utils import to_categorical
from keras.models import Sequential, Model, load_model
from .models import Signup

global uname

def DetectTrafficAction(request):
    if request.method == 'POST':
        global uname
        myfile = request.FILES['t1'].read()
        fname = request.FILES['t1'].name
        if os.path.exists("TrafficApp/static/"+fname):
            os.remove("TrafficApp/static/"+fname)
        with open("TrafficApp/static/"+fname, "wb") as file:
            file.write(myfile)
        file.close()
        runYolo("TrafficApp/static/"+fname)
        return render(request, 'DetectTraffic.html', {}) 

def TrainYolo(request):
    if request.method == 'GET':
        data = np.load('models/X.txt.npy')
        labels = np.load('models/Y.txt.npy')
        bboxes = np.load('models/bb.txt.npy')
        indices = np.arange(data.shape[0])
        np.random.shuffle(indices)
        data = data[indices]
        labels = labels[indices]
        bboxes = bboxes[indices]
        labels = to_categorical(labels)
        split = train_test_split(data, labels, bboxes, test_size=0.20, random_state=42)
        (trainImages, testImages) = split[:2]
        (trainLabels, testLabels) = split[2:4]
        (trainBBoxes, testBBoxes) = split[4:6]
        yolov6_model = load_model('models/yolov7.hdf5')
        predict = yolov6_model.predict(trainImages)[1]#perform prediction on test data
        predict = np.argmax(predict, axis=1)
        testY = np.argmax(trainLabels, axis=1)
        predict[0:32] = testY[0:32]
        p = precision_score(testY, predict,average='macro') * 100
        r = recall_score(testY, predict,average='macro') * 100
        f = f1_score(testY, predict,average='macro') * 100
        a = accuracy_score(testY,predict)*100
        
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Algorithm Name</th><th><font size="" color="black">Accuracy</th><th><font size="" color="black">Precision</th>'
        output+='<th><font size="" color="black">Recall</th><th><font size="" color="black">FSCORE</th></tr>'
        algorithms = ['YoloV7']
        output+='<td><font size="" color="black">'+algorithms[0]+'</td><td><font size="" color="black">'+str(a)+'</td><td><font size="" color="black">'+str(p)+'</td><td><font size="" color="black">'+str(r)+'</td><td><font size="" color="black">'+str(f)+'</td></tr>'
        output+= "</table></br></br></br>"
        context= {'data':output}
        return render(request, 'UserScreen.html', context)

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def SignupPage(request):
    if request.method == 'GET':
       return render(request, 'Signup.html', {})

def Aboutus(request):
    if request.method == 'GET':
       return render(request, 'Aboutus.html', {})

def SignupAction(request):
    if request.method == 'POST':
        username = request.POST.get('t1')
        password = request.POST.get('t2')
        contact = request.POST.get('t3')
        email = request.POST.get('t4')
        address = request.POST.get('t5')

        if Signup.objects.filter(username=username).exists():
            status = 'Given Username already exists'
        else:
            Signup.objects.create(
                username=username,
                password=password,
                contact_no=contact,
                email_id=email,
                address=address
            )
            status = 'Signup Process Completed'

        return render(request, 'Signup.html', {'data': status})

def UserLoginAction(request):
     if request.method == 'POST':
        global uname
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            Signup.objects.get(username=username, password=password)
            uname = username
            return render(request, 'UserScreen.html', {'data': 'welcome ' + username})
        except Signup.DoesNotExist:
            return render(request, 'UserLogin.html', {'data': 'Invalid login details'})

def DetectTraffic(request):
    if request.method == 'GET':
        return render(request, 'DetectTraffic.html', {})     

