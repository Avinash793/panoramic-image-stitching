import numpy as np
import cv2


class Panaroma:
    def image_stitch(self, images, lowe_ratio=0.75, max_Threshold=4.0, match_status=False):
        # detect the features and keypoints from SIFT
        (imageB, imageA) = images
        (key_points_A, features_of_A) = self.detect_feature_and_keypoints(imageA)
        (key_points_B, features_of_B) = self.detect_feature_and_keypoints(imageB)

        # get the valid matched points
        Values = self.match_keypoints(key_points_A, key_points_B, features_of_A, features_of_B, lowe_ratio, max_Threshold)
        if Values is None:
            return None

        # get wrap perspective of image using computed homography
        (matches, Homography, status) = Values
        result_image = self.get_warp_perspective(imageA, imageB, Homography)
        result_image[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

        # check to see if the keypoint matches should be visualized
        if match_status:
            vis = self.draw_matches(imageA, imageB, key_points_A, key_points_B, matches, status)
            return result_image, vis

        return result_image


    def get_warp_perspective(self, imageA, imageB, Homography):
        val = imageA.shape[1] + imageB.shape[1]
        result_image = cv2.warpPerspective(imageA, Homography, (val, imageA.shape[0]))
        return result_image


    def detect_feature_and_keypoints(self, image):
        # detect and extract features from the image
        descriptors = cv2.SIFT_create()
        (keypoints, features) = descriptors.detectAndCompute(image, None)
        keypoints = np.float32([i.pt for i in keypoints])
        return keypoints, features


    def get_all_possible_matches(self, featuresA, featuresB):
        # compute the all matches using Euclidean distance. Opencv provide DescriptorMatcher_create() function for that
        match_instance = cv2.DescriptorMatcher_create("BruteForce")
        All_Matches = match_instance.knnMatch(featuresA, featuresB, 2)
        return All_Matches


    def get_all_valid_matches(self, AllMatches, lowe_ratio):
        # to get all valid matches according to lowe concept..
        valid_matches = []
        for val in AllMatches:
            if len(val) == 2 and val[0].distance < val[1].distance * lowe_ratio:
                valid_matches.append((val[0].trainIdx, val[0].queryIdx))
        return valid_matches


    def compute_homography(self, pointsA, pointsB, max_Threshold):
        return cv2.findHomography(pointsA, pointsB, cv2.RANSAC, max_Threshold)


    def match_keypoints(self, KeypointsA, KeypointsB, featuresA, featuresB, lowe_ratio, max_Threshold):
        all_matches = self.get_all_possible_matches(featuresA, featuresB)
        valid_matches = self.get_all_valid_matches(all_matches, lowe_ratio)

        if len(valid_matches) <= 4:
            return None

        # construct the two sets of points
        points_A = np.float32([KeypointsA[i] for (_, i) in valid_matches])
        points_B = np.float32([KeypointsB[i] for (i, _) in valid_matches])
        (homograpgy, status) = self.compute_homography(points_A, points_B, max_Threshold)
        return valid_matches, homograpgy, status


    def get_image_dimension(self, image):
        return image.shape[:2]


    def get_points(self, imageA, imageB):
        (hA, wA) = self.get_image_dimension(imageA)
        (hB, wB) = self.get_image_dimension(imageB)
        vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
        vis[0:hA, 0:wA] = imageA
        vis[0:hB, wA:] = imageB
        return vis


    def draw_matches(self, imageA, imageB, KeypointsA, KeypointsB, matches, status):
        (hA, wA) = self.get_image_dimension(imageA)
        vis = self.get_points(imageA, imageB)

        # loop over the matches
        for ((trainIdx, queryIdx), s) in zip(matches, status):
            if s == 1:
                ptA = (int(KeypointsA[queryIdx][0]), int(KeypointsA[queryIdx][1]))
                ptB = (int(KeypointsB[trainIdx][0]) + wA, int(KeypointsB[trainIdx][1]))
                cv2.line(vis, ptA, ptB, (0, 255, 0), 1)
        return vis
