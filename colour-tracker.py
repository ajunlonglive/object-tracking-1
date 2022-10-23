from itertools import count
import numpy as np
import cv2

image = cv2.imread('circles.png')
original = image.copy()

literalcopy = image.copy()


image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


print(cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[370])


color_image = cv2.imread("circles.png", cv2.IMREAD_COLOR)

result = np.unique(color_image.reshape(-1, color_image.shape[2]), axis=0)

print(result)


lower = np.array([110,50,50])
upper = np.array([130,255,255])

mask = cv2.inRange(image, lower, upper)

# Find contours
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Extract contours depending on OpenCV version
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# Iterate through contours and filter by the number of vertices 
for c in cnts:
    perimeter = cv2.arcLength(c, True)
    print(perimeter)
    approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
    if len(approx) > 5:
        cv2.drawContours(original, [c], -1, (36, 255, 12), -1)

CountOfItems = len(cnts)

# print(cnts)

print("The count of items is : " + str(CountOfItems))

# print("The count is : " + str(count))

# adding counter to image
mask = cv2.putText(mask, "The count of items is : " + str(CountOfItems) , (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

# cv2.imshow('mask', mask)

cv2.imshow('real original?', literalcopy)

# cv2.imshow('original', original)

# cv2.imwrite('mask.png', mask)

# cv2.imwrite('original.png', original)

cv2.waitKey()