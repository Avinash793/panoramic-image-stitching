# Panoramic-Image-Stitching-using-invariant-features
I have implemented the Panoramic image stitching using invariant feature from scratch. Imlemented the David Lowe paper on Automatic Image stitching using Invariants features.

NOTE: You can experiment with any images (your own choices). I have experimented with many images. You can create two images like taj1.jpg and taj2.jpg from your desired images (taj.jpg).Make sure there will be some overlapping parts between both created images then only algorithm will find and match features and create panorama image of two images which you have provided. OR you can directly feed two images from camera with some overlapping parts between them. 

Please install Libraries:
1. Numpy
2. OpenCV
3. imutils

TO RUN CODE:
1. Run stitch.py code.
1. Provide left part of image name like taj1.jpg.
2. Provide right part of image name like taj2.jpg.
3. Then, you will get your panorama image and Matched points image as Panorama_image.jpg and Matched_points.jpg respectively in your current folder. 

- Used SIFT to detect feature and then RANSAC, compute Homography and matched points and warp prespective to get final panoramic image.

RESULTS:

Result of my1.jpg and my2.jpg
![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/my_report.JPG)

Result of taj1.jpg and taj2.jpg
![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/taj_report.JPG)

Result of room1.jpg and room2.jpg
![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/room_report.JPG)
