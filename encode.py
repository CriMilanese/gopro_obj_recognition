import os
import cv2 as cv
import urllib
import requests as req
import numpy as np
import sys
import time
import math
from scaling_temp import seek

def alreadyPlayed(new_img):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    global last_computed
    prevImg = cv.imread("newPage/"+last_computed+".jpg")
    urllib.urlretrieve("http://10.5.5.9:8080/videos/DCIM/105GOPRO/GOPR" + new_img + ".JPG", "newPage/"+ new_img + ".jpg")
    lastImg = cv.imread("newPage/"+new_img+".jpg")
    err = np.sum((lastImg.astype("float") - prevImg.astype("float")) ** 2)
    err /= float(lastImg.shape[0] * prevImg.shape[1])

    prevImg = None
    lastImg = None

    # the smaller the error the more similar the images are
    err = math.sqrt(err)
    print(err)

    if err < 25:
        print("images are fairly equal")
        return True
    print("images are clearly different")
    return False

# when a new shot has been taken I want to remove the latest_image for
# the new one in order to keep always up-to-date photos
def removeOld(new_img):
    old_img = str(int(new_img)-1)
    os.remove("target/"+old_img+".jpg")
    print("the old image has been deleted")

def findAll(p, s):
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

def Updated():
    print("...")
    file_list = req.get("http://10.5.5.9:8080/"+root).text
    content = str(file_list)
    index = findAll(root, content)
    myList = list(index)
    new_img_names = []
    isPhoto = ''
    for i in myList:
        isPhoto = content[i+len(root):i+len(root)+8]
        if(isPhoto[7]=='G'):
            new_img_names.append(isPhoto)

    max_img = max(new_img_names)
    print("max_img value in Updated: " + max_img)
    max_img = max_img[0:4]
    global latest_image
    global last_computed
    if(max_img == latest_image):
        last_computed = max_img
        return None
    else:
        latest_image = max_img
        print("max_img: " + str(max_img))
        return latest_image

def Sampler():
    print("sampler function")
    while True:
        time.sleep(1.5)
        new_img = Updated()
        if new_img == None:
            print("no new file added")
            continue
        else:
            # I am wondering how many problems I can have with this
            urllib.urlretrieve("http://10.5.5.9:8080/videos/DCIM/105GOPRO/GOPR" + new_img + ".JPG", "template/"+ new_img + ".jpg")
            image = cv.imread("template/"+ new_img + ".jpg")
            h, w, c = image.shape

            # !!! try to retrieve template, tune this values !!!
######################################################################################################################################
            image = image[(h/4):(h*3/4), (w/4):(w*3/4)]
            #image = image[ y-from : y-to, x-from : x-to ]
######################################################################################################################################
            cv.imwrite("template/"+new_img+".jpg", image)


def Play(root):
    print("play function")
    global last_computed
    new_img = Updated(root)
    urllib.urlretrieve("http://10.5.5.9:8080" + root + new_img + ".JPG", "newPage/"+ new_img + ".jpg")
    last_computed = new_img
    counter = 0
    while True:
        time.sleep(1)

        if counter == 10:
            exit(0)

        # returns the last taken image, none if last was the same as previous
        new_img = Updated(root)
        if new_img == None:
            counter += 1
            continue
        counter = 0
        # compare new image with latest one to check if they are the same
        # I do not want to reprocess old images
        if not alreadyPlayed(new_img):
            removeOld(new_img)
            continue

        print("the value of new_img if new picture is different than previous: "+new_img)


latest_image = ""
last_computed = ""
while True:
    try:
        photo_folder = ''
        case = raw_input("select mode: [sampler, play]")
        if case == "sampler":
            Sampler()
        elif case == "play":
            photo_folder = raw_input("insert address of web folder containing photos: http://10.5.5.9:8080/")
            Play(photo_folder)
        else:
            print(" argument not valid")
            exit(0)
    except:
        raise
