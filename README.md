\documentclass[9pt,twocolumn,twoside,lineno]{pnas-new}
% Use the lineno option to display guide line numbers if required.

\templatetype{briefreport} % Choose template 
% {pnasresearcharticle} = Template for a two-column research article
% {pnasmathematics} %= Template for a one-column mathematics article
% {pnasinvited} %= Template for a PNAS invited submission

\title{Detecting Presence of COVID19 in Patients from Chest X-Ray Images Using CNN-Deep Learning.}

% Use letters for affiliations, numbers to show equal authorship (if applicable) and to indicate the corresponding author
\author{Modabbir Tarique}

\affil{Department of Chemical Engineering, IIT Guwahati}

% Please give the surname of the lead author for the running footer
\leadauthor{Tarique} 

% At least three keywords are required at submission. Please provide three to five keywords, separated by the pipe symbol
\keywords{Machine Learning $|$ Classification $|$ Artificial Intelligence $|$ CNN} 

\begin{abstract}
In this project, we were asked to experiment with a real-world dataset, and develop an advanced ML  based  Classifier  that  can  scan  chest  X-Rays  and  COVID19  cases.  After  performing  the required tasks on a dataset of my choice, herein lies my final report.
\end{abstract}

\dates{This manuscript was compiled on \today}

\begin{document}

\maketitle
\thispagestyle{firststyle}
\ifthenelse{\boolean{shortarticle}}{\ifthenelse{\boolean{singlecolumn}}{\abscontentformatted}{\abscontent}}{}

% If your first paragraph (i.e. with the \dropcap) contains a list environment (quote, quotation, theorem, definition, enumerate, itemize...), the line after the list may have some extra indentation. If this is the case, add \parshape=0 to the end of the list environment.
\dropcap{C}orona virus disease (COVID-19) is an infectious disease caused by a newly
discovered corona virus.Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment. Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.\par
The best way to prevent and slow down transmission is be well informed
about the COVID- 19 virus, the disease it causes and how it spreads.
Protect our self and others from infection by washing hands or using an alcohol based rub frequently and not touching your face.
The COVID-19 virus spreads primarily through droplets of saliva or
discharge from the nose when an infected person coughs or sneezes, so it’s
important that we also practice respiratory etiquette (for example, by
coughing into a flexed elbow).
At this time, there are no specific vaccines or treatments for COVID-19.
However, there are many ongoing clinical trials evaluating potential
treatments. \par
Artificial intelligence applied to the medical domain can have very real
consequences.
 

\section{Dataset}
We have gathered all the images from the positive COVID images.We ended up with 140 images of positive COVID X-rays with view-'PA' out of 350 total images and same 140 number of images were taken from the Kaggle chest X rays for negative COVID images. Total number of images in each folder before training are as shown in table 1.\par
The data set is available at:
\begin{itemize}
\item \href{https://github.com/ieee8023/covid-chestxraydataset/tree/master/images}{GitHub}
\item \href{https://www.mohfw.gov.in/}{Ministry of Health and Family Welfare}
\end{itemize}
\section{Algorithm}
Some Important terminologies which are used in algorithm:\par
\textbf{CNN}: A convolutional neural network (CNN) is a type of artificial neural network used in image recognition and processing that is specifically designed to process pixel data.\par
\textbf{Relu}: The output of ReLu is the maximum value between zero and the input value. An output is equal to zero when the input value is negative and the input value when the input is positive.\par
\textbf{Max pooling layer}: Max pooling is a pooling operation that selects the maximum element from the region of the feature map covered by the filter.\par
\textbf{Convolutional layer}: a convolutional neural network is a class of deep neural networks, most commonly applied to analyzing visual imagery. \par
\textbf{Binary Cross-Entropy Loss}: It is a Sigmoid activation plus a Cross-Entropy loss. Unlike Softmax loss it is independent for each vector component (class), meaning that the loss computed for every CNN output vector component is not affected by other component values.\par
\textbf{Adam optimizer}: Adam is an optimization algorithm that can be used instead of the classical stochastic gradient descent procedure to update network weights iterative based in training data.\par
\textbf{Keras Fit Generator}: It in python can be used to train our machine learning and deep learning models. \par
\textbf{Confusion Matrix}: A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known.\par
Steps involved in Algorithm:
\begin{itemize}
  \item Pre-process the given input X ray images and convert them to RGB channel ordering to make them ready for our \textbf{CNN}.
  \item Initialize data augmentation generator object where each image is first normalized by dividing each image by 255 so that its pixels are now between 0 and 1. After that, rotation of image is done.
  \item We  instantiate  the  CNN model  with  nodes  of  size  32,64,64,128,128  in  each  CNN  layer respectively. Filters of size (3*3) are used to detect the patterns in images.
  \item First, apply \textbf{Relu} then add the \textbf{Max pooling layer} after each \textbf{convolutional layer} and a drop-out of 0.25. To compile the network, use the \textbf{Binary cross-entropy loss} and \textbf{Adam optimizer}.
  \item To start CNN training process, we make a call to \textbf{Keras fit generator method}, while passing in chest X-ray data via data augmentation object.
  \item For  evaluation,  first  make  predictions  on  the  testing  set  and  grab  the  prediction  indices, then generate and print out a \textbf{confusion matrix} report and save it to disk.
\end{itemize}

\section{Results}
From Figure \ref{fig:Fig2_new}. We have found that COVID-19 detector is obtaining approximately 96\%\ accuracy  on  our  test  data set,  along with  100\%\  sensitivity  and  98\%\  specificity  implying that:
\begin{itemize}
  \item Of  patients  that  do  have  COVID-19  (i.e.,  true  positives),  we  could  accurately identify them 100\%\ of time.
  \item Of patients that do not have COVID-19 (i.e., true negatives), we could accurately identify them only 98\%\ of the time. 
\end{itemize}
Refer Table 2. \par
On testing Model on real life data, we have found that it predicting the same level which was shown by actual level. Refer figure \ref{fig:Fig2} to check the result.

\section{Discussion}
COVID-19 tests are currently hard to come by —there are simply not enough of them and they  cannot  be  manufactured  fast  enough,  which  is  causing  panic.  Given  that  there  are  limited COVID-19 testing kits, we need to rely on other diagnosis measures. Since COVID-19 attacks the epithelial cells that line our respiratory tract, we can use X-rays to analyze the health of a patient’s lungs. It could be possible to use X-rays to test for COVID-19 without the dedicated test kits. A drawback is that X-ray analysis requires a radiology expert and takes significant time —which is precious when people are sick around the world. Therefore, this CNN based automated model will be helpful that time.
\section{Reference}
We have taken references from \cite{das2020prediction},\cite{hill_2016}, and \cite{Chinazzi395} respectively for this project.
\begin{figure}%[tbhp]
	\centering
	\includegraphics[scale=0.25]{Fig2_new.png}
	\caption{Result after 10 epochs of validation steps of 2 and batch size of 32.}
	\label{fig:Fig2_new}
\end{figure}
\begin{figure}%[tbhp]
	\centering
	\includegraphics[scale=0.3]{Fig2.png}
	\caption{Prediction by Model.}
	\label{fig:Fig2}
\end{figure}

\begin{table}%[tbhp]
\centering
\caption{Number of images in each folder before training }
\begin{tabular}{lrrr}
Image type & Count \\
\midrule
1. True-Positive Images & 115 \\
2. True-Negative Images & 115 \\
3. Validation-Positive Images & 25 \\
4. Validation-Negative Images & 25 \\
\bottomrule
\end{tabular}
\end{table}
\begin{table}%[tbhp]
\centering
\caption{Accuracy of Model}
\begin{tabular}{lrrr}
Data Category & Accuracy in \%\ \\
\midrule
1. Training Accuracy (CNN) & 95.22 \\
2. Test Accuracy (CNN) & 96.00 \\
\bottomrule
\end{tabular}
\end{table}
\section*{Mathematical Equations}
\subsection{Convolution}
It is a process where we take a small matrix of numbers, we pass it over our image and transform it based on the values from filter.Subsequent feature map values are calculated according to the following formula, where the input image is denoted by \emph{f} and our kernel by \emph{h}. The indexes of rows and columns of the result matrix are marked with \emph{m} and \emph{n} respectively.
\begin{equation}
G[m,n]=(f*g)[m,n]
=\sum\sum h[j,k]f[m-j,n-k]
\end{equation}
\subsection{Convolutional Layer Back propagation}
\emph{dW[l]} and \emph{db[l]} -which are derivatives associated with parameters of current layer, as well as the value of \emph{dA[ l -1]}-which will be passed to the previous layer. \emph{dA[l]} is input.The first step is to obtain the intermediate valued \emph{Z[l]} by applying a derivative of our activation function to our input tensor.
\begin{equation}
dZ[l]=dA[l]*g'(z[l])
\end{equation}
This operation can be described by the following formula, where the filter is denoted by \emph{W}, and \emph{dZ[m,n]} is a scalar that belongs to a partial derivative obtained from the previous layer.
\begin{equation}
dA+=\sum \sum W.dZ[m,n]    
\end{equation}
\section*{}
\vspace*{-0.4cm}
% References
\section*{References}
\bibliography{Bib_database}
\end{document}
