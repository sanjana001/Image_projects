#image cartoonizer
import cv2
#reading an image
img = cv2.imread(r"C:\Users\HP\Pictures\camera pictures\DSC01029.JPG")
#resize the image
image = cv2.resize(img,(800,800))
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
colors = cv2.bilateralFilter(image,9,300,300)
cartoon = cv2.bitwise_and(colors,colors,mask=edges)
cv2.imshow("image",image)
cv2.imshow("cartoon",cartoon)
cv2.imshow("color",colors)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()