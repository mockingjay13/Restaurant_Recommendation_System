# Restaurants Recommendation System 


This repository contains the code for a Recommendation System for Lucknow Restaurants. It is developed using Flask and Python.


### Folder Structure

The directory contains web sub directories and a sub directory for hosting model and other scripts:

1. [app.py](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/app.py) Contains all the main backend operations of the website and used to run the flask server locally on a local server.

2. [requirements.txt](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/requirements.txt) Contains all the dependencies.

3. [templates](https://github.com/mockingjay13/Restaurant_Recommendation_System/tree/main/templates) contains the html file.

      |- - - [home.html](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/templates/home.html) Contains the home page.
      
      |- - - [search.html](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/templates/search.html) Contains the search results page.

4. [static](https://github.com/mockingjay13/Restaurant_Recommendation_System/tree/main/static) Contains the css files and images.

      |- - - [home.css](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/static/home.css) Contains formatting of home page.
      
      |- - - [search.css](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/static/search.css) Contains formatting of search results page.
      
      |- - - [backgrund.jpg](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/static/background.jpg) Contains the background image of web pages.

5. [restaurants.csv](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/restaurants.csv) Contains Lucknow restaurants' data.
  

The entire code has been developed using Python programming language. The analysis and model is developed using ScikitLearn library. The website is developed using Flask. 

### How to run the project:

  1. Open `Terminal`.
  2. Clone the repository by entering `$ git clone https://github.com/shsarv/Restaurant-Recommendation-System.git`.
  3. Ensure that `Python3` and `pip` are installed on the system.
  4. Change the current working directory to repository name using  `$ cd [Repository name]`.
  4. Create a `virtualenv` by executing the following command: `virtualenv env`.
  5. Activate the `env` virtual environment by executing the follwing command: `source env/bin/activate`.
  6. Enter the cloned repository directory and execute `pip install -r requirements.txt`.
  7. Now execute the following command: `flask run` and it will point to the `localhost` server with the port `5000`.
  8. Enter the `IP Address: http://localhost:5000` on a web browser and use the application.
  

The following dependencies can be found in [requirements.txt](https://github.com/mockingjay13/Restaurant_Recommendation_System/blob/main/requirements.txt):

  1. [scikit-learn](https://scikit-learn.org/)
  2. [Flask](https://palletsprojects.com/p/flask/)
  3. [pandas](https://pandas.pydata.org/)
  4. [numpy](http://www.numpy.org/)
  5. [scikit-learn](https://scikit-learn.org/stable/index.html)
  6. [gunicorn](https://gunicorn.org/)
  
### Cosine Similirity is used for recommendation purpose using Scikit-learn library.


<center><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRa3ATcSqTT8I671rT7KAjWSDoAq70w6nDStA&usqp=CAU"></center>


### References 
#### For Building machine learning model and deployment:
1. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
2. https://www.machinelearningplus.com/nlp/cosine-similarity/
3. https://towardsdatascience.com/cosine-similarity-how-does-it-measure-the-similarity-maths-behind-and-usage-in-python-50ad30aad7db
4. https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
5. Machine Learning course- https://www.coursera.org/learn/machine-learning/



<h3> Thank You! <h3>

<hr> 