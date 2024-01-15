# Panoramic Image Stitching

Create panorama image from given set of overlapping images.


## Requirements
* numpy >= 1.24.3 
* opencv-python >= 4.9.0 (latest as of 2024)
* opencv-contrib-python >= 4.9.0 (latest as of 2024)
* imutils >= 0.5.4


## Description
We have implemented the **panoramic image stitching algorithm** using invariant features from scratch.
We have Implemented the David Lowe research paper on "Panoramic Image Stitching using Invariant Features".
Used SIFT to detect features, RANSAC, Homography and Warp Prespective concepts.


## About Data
**NOTE:** You can experiment with any images (of your own choice). We have experimented with many which you can find in 
`data/` folder. Please check the results below.
#### Sample Images
* Repo already provides sample images present in `data/` folder. Copy images from `data/` folder
and put it into `inputs/` folder. 
* **Default**: you will find `data/tajm` folder images in `inputs/` folder.
#### Custom Images
You can create your own images as well and put it into `inputs/` folder.
* Make sure your images must be in sequence and have overlapping parts between consecutive images.
* Minimum width and height for all images should be 400.


## How To Run
1. Put images in `inputs/` folder from which you want to create panorama image.
2. Run:
    ```shell
    python3 stitch.py
    ```
3. Enter the number of images you want to concatenate 
   (i.e number of images present in `inputs/` folder):
    ```shell
    Enter the number of images you want to concatenate: 4
    ```
4. Keep entering the images name along with path and extension. For Ex:
    ```shell
    Enter the image names with extension in order of left to right in the way you want to concatenate: 
    Enter the 1 image name along with path and extension: inputs/tajm1.jpg
    Enter the 2 image name along with path and extension: inputs/tajm2.jpg
    Enter the 3 image name along with path and extension: inputs/tajm3.jpg
    Enter the 4 image name along with path and extension: inputs/tajm4.jpg
    ```
5.  `panorama_image.jpg` and `matched_points.jpg` will be created in `output/` folder.


## RESULTS

#### Result of Images from data/tajm folder
tajm1.jpg, tajm2.jpg, tajm3.jpg, tajm4.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/result/tajm_result.jpg)

#### Result of Images from data/nature folder
nature1.jpg, nature2.jpg, nature3.jpg, nature4.jpg, nature5.jpg, nature6.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/result/nature_result.jpg)

#### Result of Images from data/my folder
my1.jpg and my2.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/result/my_result.jpg)

#### Result of Images from data/taj folder
taj1.jpg and taj2.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/result/taj_result.jpg)

#### Result of Images from data/room folder
room1.jpg and room2.jpg

![alt text](https://github.com/AVINASH793/Panoramic-Image-Stitching-using-invariant-features/blob/master/result/room_result.jpg)
