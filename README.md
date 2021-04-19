# PersonalizedTierListByPlayer

This program uses Riot Developer API for data. 

It takes the generated statistics from the last 100 games of a player. 
We then record the champions in each of the 100 games, and further, record the result of the game for each set of 5 champions as follows:

![image](https://user-images.githubusercontent.com/34112687/115303267-07b58600-a129-11eb-9cc7-e8d7a7f85687.png)

Such that each storage of 100 games gives us a dataset of 200 by 6 as follows:
![image](https://user-images.githubusercontent.com/34112687/115303285-0edc9400-a129-11eb-8cd0-b16cb2609fab.png)

We then divide the dataset into training and testing splits and utilize different models to generate a tier list of champions and their expected result. 
