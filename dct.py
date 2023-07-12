import cv2
import numpy as np

# read input image as grayscale
img = cv2.imread('dip.png', 0)
#img2 = cv2.imread('1_long.png', 0)

# convert the grayscale to float32
imf = np.float32(img) # float conversion
#imf2 = np.float32(img2) # float conversion

# find discrete cosine transform
dst = cv2.dct(imf, cv2.DCT_INVERSE)
#dst2 = cv2.dct(imf2, cv2.DCT_INVERSE)

# apply inverse discrete cosine transform
img1 = cv2.idct(dst)
#img3 = cv2.idct(dst2)

# convert to uint8
img1 = np.uint8(img)
#img3 = np.uint8(img3)

# display the images
cv2.imshow("DCT", dst)
cv2.waitKey(0)
cv2.imshow("IDCT back image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()