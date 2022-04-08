# MLS_Clustering_Captsone
Clustering on 2021 player stats

# MLS Player Recommendation Capstone Documentation
By Robet D. Rustia 

## Problem Statement 
  The average MLS roster guaranteed salary for 2021 is $13,381,000, with some teams spending north of 20 Million dollars a year. For some teams below the average salary, finding talent that is not already in the limelight is a must. With 85 different countries represented in the league in 2021 there is a large and diverse pool of players. Having the best defenders is the underpinning of any winning team. Through exploratory data analysis I will profile defenders who are the most progressive in the play and then create a player  recommendation system to identify players in the league that have similar stats to the players profiled in the exploratory data analysis. 


## 1 - Data 
2021 MLS season is collected from FBREF data by Sports Reference , “Football Stats and History Statistics, scores and history for 100+ men's and women's club and national team competitions.”. The referenced data source for the FBREF website is Statsbomb collected event data. Tables from multiple pages on the site are collected and cleaned to be formatted for ingestion into Google Big Query. Once these initial tables are in Big Query they are joined together on player_id.


## 2 - Feature Engineering 
To be able to compare players to find progressive defenders, features that exemplify this kind of player have to be created from the original dataset. Among other sources of inspiration The 10 Commandments of football analytics was a great starting place for feature design. Through feature engineering the following questions were addressed.   

- Problem: Data has season totals for all stats and comparisons need to be done at per 90 values. No true player comparisons can be done without scaling to per 90 on all non percentage based stats. 

- Problem: Different team styles will cause some players to be playing without the ball more than others. Players without the ball are going to inevitably be in situations to rack up defensive stats more than players on teams that keep more possession. With the goal of having a balanced field to make comparisons on defensive features , key features are scaled to an industry standard of per 1000 opposing touches to create possession adjusted features. 

- Problem : Basic defensive features do not give a descriptive picture of progressive play. Key features associated with progressive defenders had to be engineered to allow for the model to give a more detailed picture of a players style and impact on a match. Two of those features are as follows.
1) Attacking touches = _touches in the attacking third + touches in attacking box+ number of players dribbled past + carries in the attacking third + carries in the attacking box_.

To evaluate effective progression of the ball up the field Progressive play is measured 
 2) Progressive play is measured by  = _progressive carries + completed long balls + Crosses_.
 
 
 

## 3 - Exploratory Data Analysis  
As John Tukey said 
> Exploratory data Analysis can never be the whole story, but nothing else can serve as a foundation stone, the first step.
In my EDA there are some key questions that drive the exploration of the player features. The main questions are phrased below. 

### Key Question- Who are the most progressive ball playing defenders in the league? 

The first step in answering this question is to define a progressive defender. This player is sound defensively as well as being able to get involved in the attack through their dribbling, passing or a combination of the both. Specifically their play progresses the attack forward instead of simply distributing to low lying midfielders to do most of the progression. In the modern game players such as Alexander Arnold  come to mind. His ability to use wide space to progress the ball as well as put crosses in have been a staple of the Liverpool attack for years.  To start illuminating players in the MLS that fit this mold, Key features for progressive defenders were visualised.

### images of scatter plots 
![[true_tackle_pct|width=100px]](/data/images/true_tackle_pct.png)
![[Attacking_touches_vs_key_passes|width=100px]](/data/images/Attacking_touches_vs_key_passes.png)


### EDA final player list 
Nathan Cordoso, Julian Gressel, Hector Jimenez, Kai Wagner and Graham Zusi  were identified through the EDA process as progressive defenders involved in the attack. 



## 4 - Algorithm and Machine Learning 

NMF or Non Negative Matrix Factorization is widely used for topic modeling and document clustering. I used NMF to classify my MLS 2021 data set by the "topic" or ,grouping of player stats,that I will call a "skill set group". Similar players will have similar scores for the NMF generated skill set group features. To be able to compare players skill set group scores the cosine similarity between the normalized NMF output matrix allows for a distance between the target players identified in EDA and the rest of the league to be calculated. 
The clusters 
![[test image|width=100px]](/data/images/NMF_clusters_PCA.jpeg)
## 5 - Predictions  
Objective - Take target players from EDA and use the NMF model as a recommendation system for similar players.

- Nathan Cordoso 
One of the players profiled in the EDA is Nathan Cordoso who stood out as a dependable and efficient Defender for the San Jose Earthquakes in 2021 after coming over from FC Zurich mid season Unfortunately with Nathan having undergone surgery to repair a torn meniscus in his left knee suffered in the opening game of the 2022 season he is expected to be sidelined for up to two months. The player identified to be the closest from the W matrix is Andres Reyes -- 
![[Nathan|width=100px]](/data/images/Nathan.png| width=100)
![[Andres_Reyes|width=100px]](/data/images/Andres_Reyes.png| width=100)
![[Nathan_radar|width=100px]](/data/images/Nathan_radar.png| width=100)
- Julian Gressel
![[Jullian-Gressel|width=100px]](/data/images/Jullian-Gressel.png| width=100) 
![[Gumundur_porarinsson|width=100px]](/data/images/Gumundur_porarinsson .png| width=100)
![[Julian_radar|width=100px]](/data/images/Julian_radar.png| width=100)
![[Jullian_bar|width=100px]](/data/images/Jullian_bar.png)
 Guðmundur Þórarinsson who now plays for AALBORG BKin the SUPERLIGAEN  after leaving NYC and their successful total campaign is closest to Julian Gressle. Both players are highlighted for their Progressive play on the ball, number of players dribbled past and recoveries. 

![[Player_rank_heat_map|width=100px]](/data/images/Def_player_heatmap.png)


