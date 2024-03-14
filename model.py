#Now we will create a code for applications
import os
import cv2
import numpy as np
import mediapipe as mp
from time import time
mp_selfie_segmentation=mp.solutions.selfie_segmentation
segment=mp_selfie_segmentation.SelfieSegmentation(0)
def modifyBackground(image,b_i=255,blur=95,threshold=0.3,display=True,method='changeBackground'):
    image=cv2.resize(image,(640,640))
    RGB_img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result=segment.process(RGB_img)
    
    b_i=cv2.resize(b_i,(640,640))
    
    binary_mask=result.segmentation_mask>threshold
    binary_mask_3=np.dstack((binary_mask,binary_mask,binary_mask))
    
    if method=='changeBackground':
        background_image=cv2.resize(b_i,(image.shape[1],image.shape[0]))
        o_i=np.where(binary_mask_3,image,background_image)
    elif method=='blurBackground':
        blurred_image=cv2.GaussianBlur(image,(blur, blur),0)
        o_i=np.where(binary_mask_3,image,blurred_image)
    elif method=='desatureBackground':
        grayscale=cv2.cvtColor(src=image,code=cv2.COLOR_BGR2GRAY)
        grayscale_3=np.dstack((grayscale,grayscale,grayscale))
        o_i=np.where(binary_mask_3, image,grayscale_3)
    elif method=='transparentBackground':
        o_i=np.dstack((image,binary_mask*255))
    else: 
        print("Invalid")
        return
    if display:
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image);plt.title("original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(o_i);plt.title("modifed image");plt.axis('off');
    else:
        return o_i,(binary_mask_3*255).astype('uint8')
    
image3=cv2.imread('/DATA/atul_2221cs20/jitendra/MAMI_2022_images/training_images/11378.jpg')
bg_img2=cv2.imread('/DATA/atul_2221cs20/jitendra/MAMI_2022_images/training_images/11566.jpg')
modifyBackground(image3,bg_img2,threshold=0.55,method='changeBackground')
modifyBackground(image3,bg_img2,threshold=0.55,method='blurBackground')
modifyBackground(image3,bg_img2,threshold=0.55,method='desatureBackground')
modifyBackground(image3,bg_img2,threshold=0.55,method='transparentBackground')    
        
