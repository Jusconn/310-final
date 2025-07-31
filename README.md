This application is a Flask API and GUI that allows users to upload images of clothing and get them classified by the model. Works best with images of clothing with white background.
The application can be started by running the start_app.sh script.
Model training code with some analysis can be found here: [Link](https://colab.research.google.com/drive/1xGy-gFNZEGjP1jiifN-yM6C4Y_bXUmFB)


***
**Overview**

This model was trained using the [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset. This is a dataset of 60,000 black and white images of clothing on white background with no hanger!

![Fashion MNIST Sprite](imgs/fashion-mnist-sprite.png)

The model works best with smaller images that have white backgrounds as this fits the training data best. The imgs folder contains some sample images and their results.

This project was inspired by some work at a previous internship in which I helped create a model that classified furniture category and quality. 