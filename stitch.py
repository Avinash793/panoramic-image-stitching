from panorama import Panaroma
import imutils
import cv2


no_of_images = int(input("Enter the number of images you want to concatenate: "))
print("Enter the image names with extension in order of left to right in the way you want to concatenate: ")
# like tajm1.jpg, tajm2.jpg, tajm3.jpg .... tajmn.jpg

filename = []
for i in range(no_of_images):
    filename.append(input("Enter the %d image name along with path and extension: " % (i + 1)))

images = []
for i in range(no_of_images):
    images.append(cv2.imread(filename[i]))

# We need to modify the images width and height to keep our aspect ratio same across images
for i in range(no_of_images):
    images[i] = imutils.resize(images[i], width=400)

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], height=400)


panorama = Panaroma()
if no_of_images == 2:
    (result, matched_points) = panorama.image_stitch([images[0], images[1]], match_status=True)
else:
    (result, matched_points) = panorama.image_stitch([images[no_of_images - 2], images[no_of_images - 1]], match_status=True)
    for i in range(no_of_images - 2):
        (result, matched_points) = panorama.image_stitch([images[no_of_images - i - 3], result], match_status=True)

# show input images
# for i in range(no_of_images):
#     cv2.imshow("Image {k}".format(k=i + 1), images[i])

# show the panorama image and valid matched points
cv2.imshow("Keypoint Matches", matched_points)
cv2.imshow("Panorama", result)

# save panorama and matched_points images in output folder
cv2.imwrite("output/matched_points.jpg", matched_points)
cv2.imwrite("output/panorama_image.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
