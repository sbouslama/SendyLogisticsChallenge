# SendyLogisticsChallenge
this is a git repositry for the Sendy logistics challenge holded on Zindi. This challenge aims to predict the estimated time of delivery of orders, from the point of driver pickup to the point of arrival at final destination. 

## Motivation
The solution will help Sendy enhance customer communication and improve the reliability of its service; which will ultimately improve customer experience. In addition, the solution will enable Sendy to realise cost savings, and ultimately reduce the cost of doing business, through improved resource management and planning for order scheduling.

## Data
you can download the data via the [ZindiPlateform](https://zindi.africa/competitions/sendy-logistics-challenge/data)

## business questions
you can find answers for some business questions related to Sendy's logistics plateform on this [medium](https://medium.com/@s.bouslama/challenges-of-transporting-goods-in-east-africa-ee66d3897b0b?sk=9d117404beee5cd97c3ac76537b76824) blog post

## librairies
You should have the anaconda distribution to run the code. Here are some extra librairies used in this repository:
- sklearn
- lightgbm
you can install them by running the following command: pip install -r requirements.txt

## File Descriptions
In this repository, you will find 4 folders: 
- data: contains all the datasets needed for the challenge
- features: contains the notebooks about the exporatory data analysis
- model: contains the different models used for this task
- submissions: contains the submissions of each model

## Models
this git repositry contains multiple folders. In the one callded models, you can find all the models tested in this challenge.

### lightGBM with base features
this is the base lightGBM model for this challenge without feature engineering.
The cv score: 743.78
The leaderbord score: 724.47

timeConstraints features with the same model: 
the cv score: 735.216
the leaderboard score: 717.76

## Acknowledgements
Must give credit to Sendy and Zindi for the data. feel free to use the code here as you would like!