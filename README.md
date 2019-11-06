# Panoramic-Image-Stitching-using-invariant-features
I have implemented the Panoramic image stitching using invariant feature from scratch. Implemented the David Lowe paper on Image stitching using Invariants features.

NOTE: You can experiment with any images (your own choices). I have experimented with many images. You can check result below. You can find many images in "Image_Data" folder.

CREATE DATA:
- You can create multiple images like tajm1.jpg, tajm2.jpg, tajm3.jpg and tajm4.jpg (shown below) from your desired images (taj.jpg).Make sure there will be some overlapping parts between two consecutive created images in a sequence. then only algorithm will find and match features and create panorama image of all images which you have provided. 
- OR you can directly feed multiple images from camera in a sequence with some overlapping parts between two consecutive images. 

Please install Libraries:
1. Numpy
2. OpenCV (version 3.3.0)
3. imutils

TO RUN CODE:
1. Put images in your current folder where your code is present.
2. Run stitch.py code.
3. Provide the number of images you want to concantenate as input. Like: 2,5,6,10 etc.
4. Enter the image name in order of left to right in way of concantenation. Like:
    Enter the 1 image: tajm1.jpg
    Enter the 2 image: tajm2.jpg
    Enter the 3 image: tajm3.jpg
    Enter the 4 image: tajm4.jpg   (See below example).
5. Then, you will get your panorama image as Panorama_image.jpg in your current folder. 

- Used SIFT to detect feature and then RANSAC, compute Homography and matched points and warp prespective to get final panoramic image.

RESULTS:

Result of tajm1.jpg, tajm2.jpg, tajm3.jpg, tajm4.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/tajm_report.JPG)

Result of nature1.jpg, nature2.jpg, nature3.jpg, nature4.jpg, nature5.jpg, nature6.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/nature_report.JPG)

Result of my1.jpg and my2.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/my_report.JPG)

Result of taj1.jpg and taj2.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/taj_report.JPG)

Result of room1.jpg and room2.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/Result/room_report.JPG)
