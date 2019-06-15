from panorama import Panaroma
import imutils
import cv2

#Take picture from folder like: Hill1 & Hill2, scene1 & scene2, my1 & my2, taj1 & taj2, lotus1 & lotus2, beach1 & beach2, room1 & room2

print("Enter left part image name:")
filename1 = input()
print("Enter right part image name:")
filename2 = input()
imageA = cv2.imread(filename1)
imageB = cv2.imread(filename2)

height1,width1,channels1 = imageA.shape
height2,width2,channels2 = imageB.shape

#We need to modify the image resolution and keep our aspect ratio use the function imutils
imageA = imutils.resize(imageA,width=400)
imageB = imutils.resize(imageB,width=400)

imageA = imutils.resize(imageA,height=600)
imageB = imutils.resize(imageB,height=600)

panaroma = Panaroma()
(result, matched_points) = panaroma.image_stitch([imageA, imageB], match_status=True)

#to show the got panaroma image and valid matched points
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", matched_points)
cv2.imshow("Panorama", result)

#to write the images
cv2.imwrite("Matched_points.jpg",matched_points)
cv2.imwrite("Panorama_image.jpg",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
