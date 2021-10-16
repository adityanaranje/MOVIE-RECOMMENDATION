<p align="center" >
    PERSONAL PROJECT
  </p>

# Project Title : MOVIE RECOMMENDATION USING CONTENT BASED FILTERING.
# Technologies : Machine Learning Technology
# Domain : Sales And Marketing


## What actually is Recommendation System?
### A recommendation engine is a class of machine learning which offers relevant suggestions to the customer.  Before the recommendation system, the major tendency to buy was to take a suggestion from friends. But Now Google knows what news you will read, Youtube knows what type of videos you will watch based on your search history, watch history, or purchase history. A recommendation system helps an organization to create loyal customers and build trust by them desired products and services for which they came on your site. The recommendation system today are so powerful that they can handle the new customer too who has visited the site for the first time. They recommend the products which are currently trending or highly rated and they can also recommend the products which bring maximum profit to the company. For this particular project we have used collabrotive filtering.

## What is content based filtering?

### The algorithm recommends a product that is similar to those which used as watched. In simple words, In this algorithm, we try to find finding item look alike. For example, a person likes to watch Sachin Tendulkar shots, so he may like watching Ricky Ponting shots too because the two videos have similar tags and similar categories. Only it looks similar between the content and does not focus more on the person who is watching this. Only it recommends the product which has the highest score based on past preferences. :- Analytics Vidhya


## Problem Statement:
### -> Just like Netflix many other apps are all about connecting people to the movies they love. For that it is must to provide user's what they need. So for that it necessary to know what the user need and that can be possible using recommendation systems. This gives a better user experience.

## Aim/Goal :
## To make a basic end to end web application for movie recommendation using content based filtering.

## Approach
### -> The classical machine learning tasks like Data collection, Data Cleaning, Feature Selection, Feature Engineering, Model Deployment. Created the vectores for each movie which will be used for recommendation of movie for corresponding selected movie.

## Dataset
### The dataset is taken from kaggle.
### Link :- https://www.kaggle.com/tmdb/tmdb-movie-metadata
### It consists of two csv files one contains movies data while other containts credits related to that movie.






## Tools Used:
### 1. Python 
### 2. Pandas
### 3. Streamlit
### 4. Sklearn
### 5. NLTK
### 7. Pickle
### 8. Requests
### 9. Heroku




## Platforms Used:
### Jupyter Notebook, Spyder, Github, Heroku 



## Operations Performes:
### 1. Data Collection: 
#### -> Data is taken from kaggle which is a TMDB 5000 Movie Dataset.

### 2. Data Cleaning:
#### -> Dataset may consists of some missing values and duplicate values so we will remove these impurities.

### 3. Feature Selection:
#### -> We will not take all of the feature columns . We will only choose which we think can help us to make recommendations.

### 4. Feature Engineering: 
#### -> For recommendation system we requires some tags which we are gonig to extract from some of the selected features.

### 5. Stemming 
#### -> Performing stemming operations on the tags column using PorterStemming. For that we use python's nltk module. Stemming is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words known as a lemma. For example a stemming algorithm reduces the words “chocolates”, “chocolatey”, “choco” to  ### the root word, “chocolate” and “retrieval”, “retrieved”, “retrieves” reduce to the stem “retrieve”.

### 6. Creating Vectors:
#### -> Based on the tags column we formed the vectors for corresponding movies and then calculate the cosine distance i.e. using Cosine-similarity. Cosine similarity is a  metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.  

### 7. Performing Recommendations: 
#### -> Based on the top five closest vectors by cosine-similarity we recommend the five movies for the corresponding selected movie.

### 8. Model Deployment:
#### -> Using streamlit module and github the model is deployed on heroku.






## Model Deployment Link:
#### -> Heroku Link: https://movie-recommendation-system-an.herokuapp.com/
##### Have a patience it will take a little bit to load.



## User Interface:
![](https://github.com/adityanaranje/MOVIE-RECOMMENDATION/blob/master/static/movie_recommend.jpg)




# Thank You
