# covid_classification
Project Goals: Imagine you are a researcher in a hospital lab and are given the task to develop a learning model that supports doctors with diagnosing 
illnesses that affect patients’ lungs. At your disposal, you have a set X-ray lung scans with examples of patients who had either 
pneumonia, Covid-19, or no illness. Using the Keras module, you will create a classification model that outputs a 
diagnosis based on a patient’s X-ray scan. You hope this model can help doctors with the challenge of deciphering X-ray scans 
and open a dialogue between your research team and the medical staff to create learning models that are as effective and interpretable as possible.


1.
If you take a look at Covid19 dataset, you’ll see that there are two different folders inside. Take some time to look around these directories and familiarize yourself with the images inside. As you peruse through them, think about the following:

What types of images are we working with?
How are they organized? How will this affect preprocessing?
Will this be binary classification or multi-class classification?
After you do this, you will be ready to get started on preprocessing! Click the hint below if you want to see some insights on the image data.

2.
Load in your image data and get it ready for the journey through a neural network. One possible way to do this is to use an ImageGenerator object; however, feel free to try other methods you may have experienced before this project.

When creating the object, remember that neural networks struggle with large integer values. Think about how you might want to get your image data ready for your neural network and get the best results.

3.
Now that you have set up your ImageDataGenerator object, it is time to actually load in your image data.

You will want to create two different iterable objects from this ImageDataGenerator: a train set and a test/validation set.

When you are creating these sets of images consider the following:

The directory the images come from
The types of images you are working with
The target size of the images
Click the hint below if you need any other guidance.

4.
Now that your image data is loaded and ready for analysis, create a classification neural network model to perform on the medical data.

With image data, there are a ton of directions to go in. To get you grounded, we recommend you start by creating your input layer and output layer and compile it before diving into creating a more complex model.

When starting your neural network, consider the following:

The shape of your input
The shape of your output
Using any activation functions for your output
Your gradient descent optimizer
Your learning rate
Your loss functions and metrics
Flattening the image data before the output layer

5.
It’s time to test out the model you created!

Fit your model with your training set and test it out with your validation/test set.

Since you have not added many layers yet or played around with hyperparameters, it may not be very accurate yet. Do not fret! Your next adventure will be to play with your model and mold it until you see more ideal results.

6.
You have created a model and tested it out. Now it is time for the real fun! Start playing around with some hidden layers and hyperparameters.

When adding hidden layers, consider the type of hidden layers you add (remember this is image data).

As you add in layers, you should also adjust your model’s hyperparameters. You have a lot of choices to make. You can choose:

the number of epochs
The size of your batch_size
to add more hidden layers
your type of optimizer and/or activation functions
the size of your learning rate
Have fun in the hyperparameter playground. Test things out and see what works and what does not work. See what makes your model optimized between speed and accuracy. You have complete creative power!
