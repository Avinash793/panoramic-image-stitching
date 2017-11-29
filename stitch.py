from panorama import Panaroma
import imutils
import cv2

#Take picture from folder like: 1Hill & 2Hill, S1 & S2, 1 & 2

imageA = cv2.imread('1.JPG')
imageB = cv2.imread('2.JPG')
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

panaroma = Panaroma()
(result, matched_points) = panaroma.image_stitch([imageA, imageB], match_status=True)

#to show the got panaroma image and valid matched points
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", matched_points)
cv2.imshow("Result", result)

#to write the images
cv2.imwrite("Matched_points.jpg",matched_points)
cv2.imwrite("Panorama_image.jpg",result)

cv2.waitKey(0)
cv2.destroyAllWindows()