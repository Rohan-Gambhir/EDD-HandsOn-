import cv2
import mediapipe as mp
import time
import numpy as np

WHITE = np.array([224, 224, 224])
RED = np.array([0,0,225])
CAP = cv2.VideoCapture(0)

def getColorMask(img, plain_img):   #removes all but algorithm generated skeleton
    return img-plain_img




def main():
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
        print(results.multi_hand_landmarks)       #printslen(3) tuples for location
        if (results.multi_hand_landmarks):
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        maskedImg = getColorMask(img, plain_img)

        #find coords of all points on maskedImg, they needed to control robotic hand hinges






        cv2.imshow("Unprocessed Img", plainest_img)
        cv2.imshow("Masked Image", maskedImg)
        cv2.imshow("Process Img", img)
        cv2.waitKey(1)


if (__name__ == "__main__"):
    main()
    