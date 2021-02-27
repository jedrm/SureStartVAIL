# SureStartVAIL

## Responses
#### February 8, 2021

- I hoped to get a lot of more project based experience when it comes to AI. I always watch videos about new research and some theory about deep neural networks, but I always wanted to have more projects so that I can be accustomed to technologies that are being used for neural networks used for everyday life. With that experience, I want to get into deep learning research in the future and strengthen my foundations in the field.


#### February 9, 2021

- The difference between supervised and unsupervised learning is supervised learning is labeled data and can be used to train models with a cost function that is used for predictions. Unsupervised learning is more for finding clusters and patterns in given unlabled data. Scikit-learn doesn't have the power to visualize data without other data analysis libraries since the library is more for developing and training models for data. Other data analysis libraries can interpret the data for visualization, hence why scikit-learn is usually used with Graphiviz, Pandas, and matplotlib.


#### February 10, 2021

- Tensors are multidimensional arrays and is usually represented by an array of 3R numbers in a 3-dimensional space. With its structure, it is able to do fast calculations simulataneously and update its values extremely fast. When doing the tensorflow calculations, it was faster than I thought since there were a lot of numbers that need to be computed, yet the runtime was still relatively fast.


#### February 11, 2021

- One real-world problem is credit card fraud detection. There are a lot of variables that are being kept track of when making purchases with a credit card and companies can use a deep neural network to detect possible fraudulent transactions through a classification problem. A dataset that I found can be found in [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud). One possible deep learning algorithm for it would be a feed-forward neural network as we can do a classification problem given a large enough dataset. The feed-forward neural network is also simple and has less chance of overfitting the dataset that was given for this particular problem.


#### February 16, 2021

- Machine Learning was utilized to automate the hiring process for a startup in Orange Valley. As there was bias and skewness in the dataset that was used to train the machine learning algorithm, the outputs for the model were also biased and was very problematic as it rejected a lot of blue candidates even if they were qualified enough for the position. A real world example of a biased machine learning model is the use for face verification for devices. Some people who look similar due to race can sometimes unlock the device. One way around this issue is to train the model on data that it gets incorrect to compensate for the examples that are being misclassified. Getting a larger dataset of the subgroup can also help reduce bias in the outputs of the models.


#### February 17, 2021

- One of the differences between convolutional neural network and a fully connected neural network is they are consisted of different layers. One of the layers in a convolutional neural network is a convolution layer. It is consisted of filters that passes over the image and the neurons are activated by certain features that show up in the image. The pooling layer reduces the amount of information from the convolution layer and downsamples while retaining the most important information. It also has a flatten layer which flattens the information into neurons that can be connected to a fully connected layer. Both the fully connected layer and the convolutional neural network have fully connected output layers, which provides the output for the model. Convolutional neural networks are better for images and computer vision as it greatly reduces the amount of weights needed to be trained and reduces overfitting certain images.


#### February 23, 2021

- The Rectified Linear Activation function is very useful in terms of backpropagation when training neural networks. The derivatives are very easy to calculate, which means the neural network can train more efficiently. The activation is also very simple in terms of calculating the activation, which takes less computing power than other activation functions. It also solves the vanishing gradient problem that a lot of very deep neural networks have. In convolutional neural networks, there are a lot of layers in networks that deals with higher quality images, and the gradients tend to vanish throughout the training process and slow down the optimizaiton of the loss function. Since a lot of the layers can use a ReLU activation function, it is easy to backpropagate and make the training process for the neural network more efficient. The ReLU also has variations that can make some networks more efficient, such as the Leaky ReLU and the ELU.


#### February 24, 2021

- When the loss functions were changed into regression based functions for the houses prices model, the loss converged slower and there was a larger difference between the training loss and the validation loss, which makes the model much less accurate for actual use. The accuracies for both the training and testing sets were way less accurate as the loss functions didn't fit the problem properly. 
