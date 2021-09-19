# Step 1: Moving Custom Datasets Into Your Cloud VM
So now that you have your datasets properly formatted to be used for training and validation, we need to move them into this cloud VM so that when it comes the time we can actually train and validate our model.

# this is where my datasets are stored within my Google Drive (I created a yolov4 folder to store all important files for custom training) 
!ls /mydrive/Weapon_Detection/

# copy over both datasets into the root directory of the Colab VM (comment out test.zip if you are not using a validation dataset)
!cp /mydrive/Weapon_Detection/obj.zip ../
!cp /mydrive/Weapon_Detection/test.zip ../

# unzip the datasets and their contents so that they are now in /darknet/data/ folder
!unzip ../obj.zip -d data/
!unzip ../test.zip -d data/

# Step 2: Configuring Files for Training

# upload the custom .cfg back to cloud VM from Google Drive
!cp /mydrive/Weapon_Detection/yolov4-obj.cfg ./cfg


This backup path is where we will save the weights to of our model throughout training. Create a backup folder in your google drive and put its correct path in this file.
"""

# upload the obj.names and obj.data files to cloud VM from Google Drive
!cp /mydrive/Weapon_Detection/obj.names ./data
!cp /mydrive/Weapon_Detection/obj.data  ./data

"""## iii) Generating train.txt and test.txt
The last configuration files needed before we can begin to train our custom detector are the train.txt and test.txt files which hold the relative paths to all our training images and valdidation images.

Luckily I have created scripts that eaily generate these two files withe proper paths to all images.

The scripts can be accessed from the [Github Repo](https://github.com/theAIGuysCode/YOLOv4-Cloud-Tutorial)

Just download the two files to your local machine and upload them to your Google Drive so we can use them in the Colab Notebook.
"""

# upload the generate_train.py and generate_test.py script to cloud VM from Google Drive
!cp /mydrive/Weapon_Detection/generate_train.py ./
!cp /mydrive/Weapon_Detection/generate_test.py ./

"""Now simply run both scripts to do the work for you of generating the two txt files."""

!python generate_train.py
!python generate_test.py

# verify that the newly generated train.txt and test.txt can be seen in our darknet/data folder
!ls data/

)

It will contain one line for each training image path.

# Step 3: Download pre-trained weights for the convolutional layers.
This step downloads the weights for the convolutional layers of the YOLOv4 network. By using these weights it helps your custom object detector to be way more accurate and not have to train as long. You don't have to use these weights but trust me it will help your modle converge and be accurate way faster. USE IT!
"""

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137

# Step 4: Train Your Custom Object Detector!
# %%capture
!./darknet detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137 -dont_show -map


# Step 5: Run Your Custom Object Detector!!!
You have done it! You now have a custom object detector to make your very own detections. Time to test it out and have some fun!
"""

# Commented out IPython magic to ensure Python compatibility.
# need to set our custom cfg to test mode 
# %cd cfg
!sed -i 's/batch=64/batch=1/' yolov4-obj.cfg
!sed -i 's/subdivisions=16/subdivisions=1/' yolov4-obj.cfg
# %cd ..

# run your custom detector with this command (upload an image to your google drive to test, thresh flag sets accuracy that detection must be in order to show it)
!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/Weapon_Detection/backup/yolov4-obj_best.weights /content/gdrive/MyDrive/Weapon_Detection/test_images/test/4.jpg -thresh 0.1
imShow('predictions.jpg')


