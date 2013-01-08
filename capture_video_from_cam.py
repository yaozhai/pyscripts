#!/usr/bin/python2.7.3
# -*-  coding: utf-8 -*-

import cv
import sys
import time

path = 'c:\\Python27\\data\\haarcascades\\'
capture = cv.CaptureFromCAM(0)

cv.NamedWindow('image')
hc = cv.Load(path + "haarcascade_frontalface_alt2.xml")
time_pre = 0
count = 0
time_delta_total = 0


while True:
    time_now = time.clock()
    time_delta = time_now - time_pre
    time_pre = time_now
    time_delta_total = time_delta_total + time_delta
    count = count + 1

    frame = cv.QueryFrame(capture)
    if frame == None:
        break

    image_size = cv.GetSize(frame)

    #cv.Flip(frame, None, 1)

    storage = cv.CreateMemStorage()

    faces = cv.HaarDetectObjects(frame, hc, storage, 1.2, 5, 0, (50, 50))

    if faces:
        for (x,y,w,h),n in faces:
            cv.Rectangle(frame, (x,y), (x+w,y+h), 255, 2)

    cv.ShowImage('image', frame)

    k = cv.WaitKey(10)

    # ESC
    if k % 256 == 27:
        print("Average frame time: {0} seconds".format(time_delta_total/count))
        break

cv.DestroyWindow('image')