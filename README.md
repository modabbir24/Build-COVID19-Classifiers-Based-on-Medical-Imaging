# Detecting Presence of COVID19 in Patients from Chest X-Ray Images Using CNN-Deep Learning.
### Abstract
<b>In this project, we were asked to experiment with a real-world dataset, and develop an advanced ML based Classifier that can scan chest XRays and COVID19 cases. After performing the required tasks on a dataset of my choice, herein lies my final report.</b>
*Keywords*: Machine Learning | Classification | Artificial Intelligence | CNN
### Introduction
Corona virus disease (COVID-19) is an infectious disease caused by a newly discovered corona virus.Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment. Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.
The best way to prevent and slow down transmission is be well informed about the COVID- 19 virus, the disease it causes and how it spreads. Protect our self and others from infection by washing hands or using an alcohol based rub frequently and not touching your face. The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that we also practice respiratory etiquette (for example, by coughing into a flexed elbow). At this time, there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments.
Artificial intelligence applied to the medical domain can have very real consequences.
### Dataset
We have gathered all the images from the positive COVID images.We ended up with 140 images of positive COVID X rays with view-‘PA’ out of 350 total images and same 140 number of images were taken from the Kaggle chest X rays for negative COVID images. Total number of images in each folder before training are as shownin table 1.
### Algorithm
Some Important terminologies which are used in algorithm:
**CNN**: A convolutional neural network (CNN) is a type of artificial neural network used in image recognition and processing that is specifically designed to process pixel data.
**Relu**: The output of ReLu is the maximum value between zero and the input value. An output is equal to zero when theinput value is negative and the input value when the input is positive.
**Max pooling layer**: Max pooling is a pooling operation that selects the maximum element from the region of the feature map covered by the filter. 
**Convolutional layer**: a convolutional neural network is  a class of deep neural networks, most commonly applied to 
analyzing visual imagery. 
Binary Cross-Entropy Loss: It is a Sigmoid activation 
plus a Cross-Entropy loss. Unlike Softmax loss it is inde- 
pendent for each vector component (class), meaning that the 
loss computed for every CNN output vector component is not 
affected by other component values. 
**Adam optimizer**: Adam is an optimization algorithm 
that can be used instead of the classical stochastic gradient 
descent procedure to update network weights iterative based 
in training data. 
**Keras Fit Generator**: It in python can be used to train 
our machine learning and deep learning models. 
**Confusion Matrix**: A confusion matrix is a table that 
is often used to describe the performance of a classification 
model (or "classifier") on a set of test data for which the true 
values are known. 
Steps involved in Algorithm: 
* Pre-process the given input X ray images and convert 
them to RGB channel ordering to make them ready for 
our CNN. 
* Initialize data augmentation generator object where each 
image is first normalized by dividing each image by 255 
so that its pixels are now between 0 and 1. After that, 
rotation of image is done. 
* We instantiate the CNN model with nodes of size 
32,64,64,128,128 in each CNN layer respectively. Filters 
of size (3*3) are used to detect the patterns in images. 
* First, apply Relu then add the Max pooling layer 
after each convolutional layer and a drop-out of 0.25. 
To compile the network, use the Binary cross-entropy 
loss and Adam optimizer. 
* To start CNN training process, we make a call to Keras 
fit generator method, while passing in chest X-ray 
data via data augmentation object. 
* For evaluation, first make predictions on the testing set 
and grab the prediction indices, then generate and print 
out a confusion matrix report and save it to disk.

