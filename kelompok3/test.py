import cv2 as cv

img = cv.imread('img/hand2.jpg', cv.IMREAD_GRAYSCALE)
rows,cols = img.shape

M = cv.getRotationMatrix2D(((cols)/2.0, (rows)/2.0), 45, 1)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('Original Photo', img)
cv.imshow('Rotation Photo', dst)

cv.waitKey(0)
cv.destroyAllWindows()
