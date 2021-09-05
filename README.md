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

<p align="center">
<img src = "https://user-images.githubusercontent.com/51092051/132125266-f227768b-e0bf-48f3-82b3-5d70f0696030.png" width = "700" height = "550">
</p>

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

## 2. Intruder and Weapon detection

Once we were able to process low light, next it was time to move on to detecting the intruders and their weapons. 

### Intruder detection

In this case, we utilized the pre-trained YOLOv4-tiny weights for person detection and were able to achieve some great results. 
Using our [intruder detection script](https://github.com/AmanGoyal99/Low-light-intrusion-detection/blob/main/Intruder-detection/intruder_detection.py), we were able to achieve results which are as follows:
                                                
<img src = "/assets/person_1.png" width = '400' height = '300' > <img src = "/assets/person_2.png" width = '400' height = '300' >

Finally, this is how intruder detection perfrormed on our video :

<p align="center">
<img src = "/assets/out_intruder_detection.gif">
</p>

### Weapon detection

For this part, we had to train our own model using the [YOLOv4 architecture](https://arxiv.org/abs/2004.10934). The dataset was collected from [here](https://dasci.es/transferencia/open-data/24705/). Coming back to the model, as per various useful suggestions mentioned in the [official implementation](https://github.com/AlexeyAB/darknet), we accordingly formulated a pipeline consisting of various necessary files as shown in our [weapon detection folder](https://github.com/AmanGoyal99/Low-light-intrusion-detection/tree/main/Weapon-detection).

It's quantitative results are as follows:

| Class | AP | TP | FP |
| --- | --- | --- | --- |
| Knife | 86.57% | 65 | 18 |
| Handgun | 88.10% | 21 | 9 |

The mAP curve of our trained model can be found below :

<p align="center">
<img src = "/assets/weapon_detection_mAP_curve.png" width = '400' height = '300'>
</p>

It's qualitative results are as followed:

<img src = "/assets/weapon_detection_1.png" width = '450' height = '350' > <img src = "/assets/weapon_detection_2.png" width = '450' height = '350' >

## 3. Pose estimation

This step in our pipeline is quite crucial as pose information of any criminal can play a major role in the vigilantes capturing the criminal. We utilized [HRNet](https://arxiv.org/abs/1902.09212) for achieving intruder pose estimation.

Initially, we tested out our pose estimation module on some youtube videos :

<img src = "/assets/pose_estimation_1.gif" width = '450' height = '350' >  <img src = "/assets/pose_estimation_2.gif" width = '450' height = '350' >

Once, we were satisfied with the results, we finally applied it on our own video :

<p align="center">
<img src = "/assets/out_intruder_pose_estimation.gif">
</p>

## 4. Face detection

Once intruder, it's weapon and it's pose has been estimated, the next crucial task is that of face detection as we would be requiring it to extract intruder's face and scan it in the database of existing wanted criminals and terrorists.

In order to achieve this, we utilize the [Viola Jones algorithm](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework). However, the default parameters did not work for us well and we had to finetune the parameters to get optimal performance for our use-case.
After running some test images over our [face detection script](https://github.com/AmanGoyal99/Low-light-intrusion-detection/blob/main/Face-detection/face_detect_img.py), we were able to obtain the following results:

<img src = "/assets/face_detection_1.jpg" width = '350' height = '350' >  <img src = "/assets/face_detection_2.jpg" width = '500' height = '350' >

The qualitative results obtained on our video are as follows:

<p align="center">
<img src = "/assets/face_output.gif">
</p>

## 5. Final Output

After all the above steps were achieved as mentioned in the pipeline as well, we were able to obtain the following result on our video :

<p align="center">
<img src = "/assets/final_output.gif">
</p>

## Next steps and Conclusion

After having spent a decent amount of time on developing this solution, we have just gathered more and more awareness about the benefits of Deep Learning not just to the AI Community but in fact to the entire humanity by solving some of the most important problems of the mankind. 

Like every other AI based system, our system has also few flaws which are listed below :

- It has difficulty in detecting the weapon when it is quite close to the person and merges with his/her clothing. The model tends to be confused and this could be improved by gathering more such dataset.
- Pose estimation of multiple intruders from a given image is an intensive task and was not achieved in this project. In case of multiple persons in a given frame, an additional network for object detection would be used and this just adds to the already computationally intensive system. Our system is meant to be used in real-time and hence alternatives would have to be looked at.


We look to work and fix the above issues mentioned in the future to build a more robust solution which can hopefully be added as an extra layer of protection for military purposes and therefore curb terrorism.






