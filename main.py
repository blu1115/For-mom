import cv2 as cv

img = cv.imread('images/mom.jpeg')
name = input("Enter your name: ")
name2 = str(name)

if name2 == "Thya" or "thya":
    cv.imshow('cat', img)
else:
    print("Not for you!!")

cv.waitKey(0)