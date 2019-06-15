from panorama import Panaroma
import imutils
import cv2

#Take picture from folder like: Hill1 & Hill2, scene1 & scene2, my1 & my2, taj1 & taj2, lotus1 & lotus2, beach1 & beach2, room1 & room2

print("Enter the number of images you want to concantenate:")
no_of_images = int(input())
print("Enter the image name in order of left to right in way of concantenation:")
#like taj1.jpg, taj2.jpg, taj3.jpg .... tajn.jpg
filename = []

for i in range(no_of_images):
    print("Enter the %d image:" %(i+1))
    filename.append(input())

images = []

for i in range(no_of_images):
    images.append(cv2.imread(filename[i]))

#We need to modify the image resolution and keep our aspect ratio use the function imutils

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], width=400)

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], height=400)


panaroma = Panaroma()
if no_of_images==2:
    (result, matched_points) = panaroma.image_stitch([images[0], images[1]], match_status=True)
else:
    (result, matched_points) = panaroma.image_stitch([images[no_of_images-2], images[no_of_images-1]], match_status=True)
    for i in range(no_of_images - 2):
        (result, matched_points) = panaroma.image_stitch([images[no_of_images-i-3],result], match_status=True)

#to show the got panaroma image and valid matched points
for i in range(no_of_images):
    cv2.imshow("Image {k}".format(k=i+1), images[i])

cv2.imshow("Keypoint Matches", matched_points)
cv2.imshow("Panorama", result)

#to write the images
cv2.imwrite("Matched_points.jpg",matched_points)
cv2.imwrite("Panorama_image.jpg",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
