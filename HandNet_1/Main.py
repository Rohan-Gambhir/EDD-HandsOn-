import cv2
import mediapipe as mp
import time
import numpy as np

#my libs
import SpaceCalculator as SC


WHITE = np.array([224, 224, 224])
RED = np.array([0,0,225])
CAP = cv2.VideoCapture(1)

def getColorMask(img, plain_img):   #removes all but algorithm generated skeleton
    return img-plain_img




def live_feed():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    while (1):
        success, img = CAP.read()
        plain_img = img.copy()
        plainest_img = img.copy()
        #Convolutional neural net init+act here
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   #mpHands.process() only takes RGB images
        results = hands.process(imgRGB)
        if (results.multi_hand_landmarks):
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        maskedImg = getColorMask(img, plain_img)




        # cv2.imshow("Unprocessed Img", plainest_img)
        cv2.imshow("Masked Image", maskedImg)
        # cv2.imshow("Process Img", img)
        cv2.waitKey(1)
    cv2.destroyWindow("Masked Image")

def cap_single_frame():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    success, img = CAP.read()
    plain_img = img.copy()
    plainest_img = img.copy()
    #Convolutional neural net init+act here
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   #mpHands.process() only takes RGB images
    results = hands.process(imgRGB)
    if (results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            print(handLms)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    maskedImg = getColorMask(img, plain_img)
    #landmarks (in order of x values)

    #image of hand with corresponding index for each point
    
    #need hand image with landmark indexes to choose angles needed to calculate

    use_ind = [()]
    for i in use_ind:
        pass
    vectors = []
    hand_angles = {
        "thumb_middle": 0,
        "thumb": 0,
        "pointer_top" : 0,
        "pointer_bottom": 0,
        "pointer": 0,
        "middle_top": 0,
        "middle_bottom": 0,
        "middle": 0,
        "top_ring": 0,
        "bottom_ring": 0,
        "ring": 0,
        "top_pinky": 0,
        "bottom_pinky": 0,
        "pinky": 0
    }

    #when creating vectors, make sure the p2 in constructors are consisted for each vector pair (will be used as origin to simplify calculations)
    
    for key in hand_angles.keys():
        #vec1: Vector = Vector(p1, p2)
        #vec2: Vector = Vector(p1, p2)
        #hand_angles[key] = (SC.calcAngle(vec1, vec2, int_point))  #int point is for validation
        pass
    
    #add safety net for maximum degrees of movement requested to hand



    # cv2.imshow("Unprocessed Img", plainest_img)
    cv2.imshow("Masked Image", maskedImg)
    # cv2.imshow("Process Img", img)
    cv2.waitKey(1)
    time.sleep(10)


def cap_SOMEFRAMES():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    max_frames = 10
    i = 0
    while (i<max_frames):
        success, img = CAP.read()
        plain_img = img.copy()
        plainest_img = img.copy()
        #Convolutional neural net init+act here
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   #mpHands.process() only takes RGB images
        results = hands.process(imgRGB)
        if (results.multi_hand_landmarks):
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                print(handLms)
        maskedImg = getColorMask(img, plain_img)



        # cv2.imshow("Unprocessed Img", plainest_img)
        cv2.imshow("Masked Image", maskedImg)
        # cv2.imshow("Process Img", img)
        cv2.waitKey(1)
        time.sleep(1)
        i+=1
    cv2.destroyWindow("Masked Image")

def cap_img():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    img = cv2.imread("Desktop/PLTW/Test_img.png")
    plain_img = img
    plainest_img = img
    #Convolutional neural net init+act here
    results = hands.process(img)
    if (results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            print(handLms)
    maskedImg = getColorMask(img, plain_img)
    # cv2.imshow("Unprocessed Img", plainest_img)
    cv2.imshow("Masked Image", maskedImg)
    # cv2.imshow("Process Img", img)
    cv2.waitKey(1)
    time.sleep(10)
    cv2.destroyWindow("Masked Image")



if (__name__ == "__main__"):
    live_feed()
    # # cap_single_frame()
    # # cap_SOMEFRAMES()
    # cap_img()



