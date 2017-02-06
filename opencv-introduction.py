#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/iwatch.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite('/images/iwatchgray.jpg', img)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([500, 1000], [800, 1000], 'c', linewidth=5)
plt.show()


