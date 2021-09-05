# Low-light-intrusion-detection

## Introduction

Terrorism has been rising exponentially in all parts of the world. One of the major starting points of terrorism in most countries is the trespassing of terrorists through borders.
In this project, we present a Deep Learning and Computer Vision based solution for tracking intrusions across the border. With the advent in AI over past few years and rising intrusions across national border, it becomes a need of the hour to develop a system which can help curb terrorism.
In general, current surveillance techniques are majorly restricted to bright light images and do not benchmark their models on low light images as the model performance drastically reduces in them.
Apart from this, many current techniques are also majorly restricted to just criminal detection.
In our approach, we work on 5 major use cases which include both low light image processing and intruder pose estimation.
The 5 use cases proposed are 
- Intruder Detection
- Weapon Detection
- Intruder Pose Estimation
- Intruder Face Recognition 
- Low Light image processing. 

In the project, we demonstrate results of all the 5 use cases mentioned which are tested on various images. 
By working on these 5 use cases, we hope to detect and track the intruder. These pieces of information provided to the vigilantes could help them a great deal to search and get hold of the intruder.  

<p align="center">
<img src = "/assets/final_output.gif">
</p>

The above illustration demonstrates all the various techniques being performed on a low light clip. A step-by-step explanation of our approach has been mentioned below.

Before moving on to the approaches, following is the architecture of our proposed system :

![Level 2 DFD](https://user-images.githubusercontent.com/51092051/132125266-f227768b-e0bf-48f3-82b3-5d70f0696030.png)


## Collecting low light videos

The first step for any deep learning based project is collection of relevant data. After intensively searching for hours, we collected few clips which contained the components over which we wanted to run our models. We chose the following video clip to be our input video.

<p align="center">
<img src = "/assets/input.gif">
</p>

## 1. Low light image processing

This is the most crucial part of this project as without this part, other modules which are to be applied will not work. In order to achieve this we are following a technique known as **stacking and averaging**. 

Here we are taking a video stream from a CCTV camera or any camera for the matter and then extracting individual frames then we use these frames to create a long exposure of the camera stream. This then leads to us getting an image or a frame with a duration of more than one frame. This additional input data that we have acquired can be used to apply filters that give an impression of a wideband filter leading to a high dynamic ranges.

This may introduce some noise and ghosting in the image to tackle we use a weighted average filter that will improve the quality of the image.

After processing input video over our [low light image processing script](https://github.com/AmanGoyal99/Low-light-intrusion-detection/blob/main/Low_Light_processing/low_light_image_processing.py), we were able to achieve the following output:

<p align="center">
<img src = "/assets/low_light_output.gif">
</p>

It can be clearly noticed that the video has become much visible as compared to the low light input video.

## 2. Intruder detection

Once we were able to process low light, next it was time to move on to 


