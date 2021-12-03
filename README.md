# tensorflow-deployment

Here are the several demo for TensorFlow Deployment using TFX (TensorFlow Serving) with Docker.

This project contains the Container Based Deployment:
- Flask + Docker deployment and test locally
- TFX + Docker deployment and test locally
- TFX + Docker + Heroku deployment and test hosted 

## Want to try it on your machine?

1. Install Library
    Make sure you have install python 3.7 and using tensorflow 2.2.0. You can use pyenv to use python version differently. Note that tensorflow 2.2.0 until 2.5.0 was only supported by python 3.7.

    ```
    pip install jupyterlab
    pip install tensorflow==2.2.0
    pip install matplotlib
    pip install flask
    ```
    
    Note: You can create the separate virtual environment to install the library.

2. Run the notebook

    If you are using Visual Studio Code for code development and run notebook, you can install and use Jupyter Notebook extension. Otherwise, you can install jupyter notebook on your machine by running:
    
    ```
    pip install jupyterlab
    ```
    
    Then, you can go running all the command on the notebook
    
3. Run Flask Deployment
    Make sure to go the `flask-deploy` directory to run the app. Then export the flask app to run it locally.
    ```
    cd flask-deploy
    export FLASK_APP=app.py
    ```
    After exporting complete, you can run the app and predict using notebook at the section `Consume Flask Model`.
    ```
    flask run
    ```
    
    You can try to predict using docker if you are planning to deploy it as a containerized application. Make sure docker has installed on your machine. Run this command to build the docker image.
    ```
    docker build -t fashion-mnist-flask . 
    ```
    After you build the image, run the image as containerized application and test it locally.
    ```
    docker run -p 5000:5000 fashion-mnist-flask 
    ```
    Docker image will expose the port at the same port you build the application with flask run. Now you can predict the model using notebook.
    
4. Run TF Serving Deployment
    First, build the docker image as you do in the flask development using docker by running this command.
    ```
    docker build -t fashion-mnist-tf-serving 
    ```
    Then run the image and expose the port. Note that TensorFlow Serving is using port 8501 in the container.
    ```
    docker run -p 8080:8501 fashion-mnist-tf-serving
    ```
    After running the container, test it using notebook to predict the data.
    
5. Run TF Serving and Deploy to Heroku
    Now you have run the TF Serving on local. Now you want to deploy it using Heroku. Make sure you have heroku CLI installed on your machine, and log in to the account you have in heroku.
    
    If you have completing setup the account, now you have to create the project on our heroku.
    ```
    heroku create fashion-mnist-demo 
    ```
    After create the project push the container to Heroku
    ```
    heroku container:push web -a fashion-mnist-demo
    ```
    Then release the web app.
    ```
    heroku container:release web -a fashion-mnist-demo
    ```
    You can enable the logging of your model on your terminal by using this command.
    ```
    heroku logs --tail -a fashion-mnist-demo
    ```
    As you know machine learning need some resource, so we need to scale the dyno on heroku. (Don't worry this is free)
    ```
    heroku ps:scale web=1 -a fashion-mnist-demo
    ```
    
---

Happy coding!
