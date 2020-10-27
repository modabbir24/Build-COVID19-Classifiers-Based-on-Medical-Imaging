covid_from_ctscan
Model which can predict COVID-19 positive case from axial lung CT-scan images.The model may not detect COVID-19 affected patients who are yet to develop pneumonia symptoms.It can only predict COVID-19 pneumonia cases from normal healthy images. This work in any way does not claim any perfect method of detection.

Hypothesis
Researchers have noticed white patches in the boundary of lung CT scans in COVID affected patients.This is the motivation to develop a model which can detect the probablity of a CT scan,affected with COVID-19.The videos(Video-1 and Video-2) attached explains the hypothesis in a better way.

Data
Three public data sources:- 1.Kaggle 2.Github 3.Github

No data sample is repeated while modelling.But still the data collected must represent the data from a larger group of people,which may be available later.

Link to the custom dataset generated is found here.

sample image

The above sample image has plentiful noise and it varies from one image to other.

sampled image

The images may have taken at different axial cross sections of different people or repeated images taken at different cross sections of the same person.So as per the labelling above the part between the lungs can be considered as noise.

Bayesian Neural Network with variational inference for Out Of Distribution Detection
Resnet-18 architecture is used as a feature detector and the fully connected layer as bayesian architecture with prior normal distributions to every parameter in the FC layer. So by giving the same input again and again to the model OOD samples can be separated. Every layer is trained.KL divergence loss is also optimized along with cross entropy to approximate the posterior distributions of the FC layer.

Approach
Batch size is altered as a large batch size may reduce generalization ability of the model.VGG-19(smaller architecture) didn't come out to be better.Directly modelling with all the given images(raw data) the best results obtained are given below(different techniques to remove under or overfitting were used,resnet-50 architecture was better performing)-

initial model

Blurring the images and then masking them would rather reduce the noise in the images.

image transformation

Now the model has more meaningful information to learn(the portion I like it to capture).So different transformations are applied on both classes.In the testing of the model,both these transformations would be applied(done in app.py,similar to TTA) and more certain results are chosen.This need to be done during my validation as labels are known beforehand.

Now a best model on all images was found.Another model trained was initializing the model on all images and trained on the 232 refined images.(let us call it Model-a)

halved

Now each image was cut into two halves vertically(this was done so that my model can understand more texture based information than spatial information) and then augmented to 1000 images,500 in each class.Resnet-18 model(trained from scratch with no pretrained initializations)on these 1000 images was the best performing one.Now visualizing the layers of the above both models was done.(let us call it Model-b).

Upon Visualization the best model is the model trained on halved images as expected though it had lesser accuracy(model b).

Insights generated
The best model(Model-b) is shown below.It has an accuracy score of 95%(190 correctly predicted out of 200 in validation set).

best_model

This model shown above could detect ALL COVID positive images in validation image set and most importantly it actually learns and generalizes COVID-19 "white spots".The only drawback is that it misdetects some non-covid images as COVID-19 affected images.

Adding weight_decay to an SGD optimizer just adds an L2-regularizer like term during your optimizer step.(So that was added to reduce the overfit).Dropout layer was introduced in the final fully connected layer as another way to tacckle overfit.The reason why Model-a is not considered best is explained below-

Wrong fit

Not only accuracy and recall score,making sure our model does learn the excpected thing is ncessary.The above image explains the beforesaid line,the model overfits to the noise(Gradients show up near the black portion,which is unnecessary) though it's validation scores are better.

Local Host Deployment
A local host is created,more details in the local host folder.

Files Uploaded
A local host website solely for the COVID-19 prediction and the files are uploaded(with app.py as the major file,but the model file cannot be uploaded due to storage issues).

The link to the custom dataset generated in the process is already mentioned above(can be accessed here).

The four commented code files(two for momdelling and one for layer visualization and one for bayesian NN) are also uploaded.
