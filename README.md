# MLS Player Recommendation Capstone Documentation

<img src="https://github.com/misterrustia/MLS_clustering_Captsone/blob/main/data/images/Jullian_tackle.jpg" width="400" height="325">

## Problem Statement 
  The average MLS roster guaranteed salary for 2021 is $13,381,000, with some teams spending north of 20 Million dollars a year. For some teams below the average salary, finding talent that is not already in the limelight is a must. With 85 different countries represented in the league in 2021 there is a large and diverse pool of players. Having the best defenders is the underpinning of any winning team. Through exploratory data analysis I will profile defenders who are the most progressive in the play and then create a player  recommendation system to identify players in the league that have similar stats to the players profiled in the exploratory data analysis. 


## 1 - Data 
[data wrangling notebook](MLS_clustering_Captsone/notebooks/1_Data_Wrangling/)
2021 MLS season is collected from FBREF data by Sports Reference , “Football Stats and History Statistics, scores and history for 100+ men's and women's club and national team competitions.”. The referenced data source for the FBREF website is Statsbomb collected event data. Tables from multiple pages on the site are collected and cleaned to be formatted for ingestion into Google Big Query. Once these initial tables are in Big Query they are joined together on player_id.


## 2 - Feature Engineering 
[Feature Engineering notebook](MLS_clustering_Captsone/notebooks/3_feature_engineering.ipynb)
To be able to compare players to find progressive defenders, features that exemplify this kind of player have to be created from the original dataset. Among other sources of inspiration The 10 Commandments of football analytics was a great starting place for feature design. Through feature engineering the following questions were addressed.   

- Problem: Data has season totals for all stats and comparisons need to be done at per 90 values. No true player comparisons can be done without scaling to per 90 on all non percentage based stats. 

- Problem: Different team styles will cause some players to be playing without the ball more than others. Players without the ball are going to inevitably be in situations to rack up defensive stats more than players on teams that keep more possession. With the goal of having a balanced field to make comparisons on defensive features , key features are scaled to an industry standard of per 1000 opposing touches to create possession adjusted features. 

- Problem : Basic defensive features do not give a descriptive picture of progressive play. Key features associated with progressive defenders had to be engineered to allow for the model to give a more detailed picture of a players style and impact on a match. Two of those features are as follows.
1) Attacking touches = _touches in the attacking third + touches in attacking box+ number of players dribbled past + carries in the attacking third + carries in the attacking box_.

To evaluate effective progression of the ball up the field Progressive play is measured 
 2) Progressive play is measured by  = _progressive carries + completed long balls + Crosses_.
 
 
 

## 3 - Exploratory Data Analysis 
[Exploratory Data Analysis notebook](MLS_clustering_Captsone/notebooks/2_exploratory_data_analysis.ipynb)
As John Tukey said 
> Exploratory data Analysis can never be the whole story, but nothing else can serve as a foundation stone, the first step.
In my EDA there are some key questions that drive the exploration of the player features. The main questions are phrased below. 

### Key Question- Who are the most progressive ball playing defenders in the league? 

The first step in answering this question is to define a progressive defender. This player is sound defensively as well as being able to get involved in the attack through their dribbling, passing or a combination of the both. Specifically their play progresses the attack forward instead of simply distributing to low lying midfielders to do most of the progression. In the modern game players such as Alexander Arnold  come to mind. His ability to use wide space to progress the ball as well as put crosses in have been a staple of the Liverpool attack for years.  To start illuminating players in the MLS that fit this mold, Key features for progressive defenders were visualised.

### images of scatter plots 
![[true_tackle_pct|width=100px]](/data/images/true_tackle_pct.png)
![[Attacking_touches_vs_key_passes|width=100px]](/data/images/Attacking_touches_vs_key_passes.png)


### EDA final player list 
Nathan Cordoso, Julian Gressel, Hector Jimenez, Kai Wagner and Graham Zusi  were identified through the EDA process as progressive defenders involved in the attack. The output matrix from the NMF will be used to find the closest players to these players of interest. 



## 4 - Algorithm and Machine Learning 
[Preprocessing notebook](MLS_clustering_Captsone/notebooks/4_preprocessing_tuning.ipynb)
NMF or Non Negative Matrix Factorization is widely used for topic modeling and document clustering. NMF classifies the MLS 2021 data set by "topic" or ,group of player stats, called a "skill set group". Similar players will have similar scores for the NMF generated skill set group features. To be able to compare players skill set group scores the cosine similarity between the normalized NMF output W(weight) matrix allows for a distance between a target players identified in EDA and the rest of the league to be calculated. 
The clusters below show the leauge classified into 9 different skill set groups by the final NMF model. 
![[test image|width=100px]](/data/images/NMF_clusters_PCA.jpeg)

## 5 - Predictions  
Objective - Take target players from EDA and use the NMF model as a recommendation system for similar players.
[Modeling Notebook with all player recomendations](MLS_clustering_Captsone/notebooks/5_modeling.ipynb)

Example of the comparison between Julian Gressel and the models closest match Guðmundur Þórarinsson below 

<img src="https://github.com/misterrustia/MLS_clustering_Captsone/blob/main/data/images/Julian_radar.png" width="300" height="300">
- need breakdown of comparison here
<img src="https://github.com/misterrustia/MLS_clustering_Captsone/blob/main/data/images/Jullian_bar.png" width="400" height="225">
 
<img src="https://github.com/misterrustia/MLS_clustering_Captsone/blob/main/data/images/Def_player_heatmap.png" width="300" height="300">

## 6 -  Future Improvements 

There are multiple options to expand this project to allow for more impact to be made.
1 - the first extension would be to model attacking KPI’s and attacking players.
2 - create more granular KPIs such as forward pass completion rate, from Second Spectrum data provided to all MLS clubs to build NMF recommendations on.  
3 - Scaling the model to connect with statsbombs data from other leagues to look for players similar to target players around the world. This expanded database would allow for scouting of key markets or for searches driven by key features. This Technique could allow teams with smaller pockets to find gems that could make the difference in winning a MLS cup.
4 - package the model into a user interface with Bokeh for stakeholders to access freely.  

## 9 - Credits 
Thanks to Charlie Tuley, Ramzi Bensaid and Jeff Ota for the support working with MLS player data, Upom Malik for being an amazing Springboard mentor. 


