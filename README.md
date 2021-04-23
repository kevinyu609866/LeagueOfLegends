# PersonalizedTierListByPlayer

This program uses Riot Developer API for data. 

It takes the generated statistics from the last 100 games of a player. 
We then record the champions in each of the 100 games, and further, record the result of the game for each set of 5 champions as follows:

![image](https://user-images.githubusercontent.com/34112687/115303267-07b58600-a129-11eb-9cc7-e8d7a7f85687.png)

Such that each storage of 100 games gives us a dataset of 200 by 6 as follows:
![image](https://user-images.githubusercontent.com/34112687/115303285-0edc9400-a129-11eb-8cd0-b16cb2609fab.png)

Since champions are encoded with an ID, the decoding was used done using the following json file:
http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json

Each champion is then encoded by index, such that the values are between Champions 1 and Champion 155. 
Further, since the numerical magnitude of the champion does not matter, and champions are categorical variables, one-hot-encoding is applied.

We then divide the dataset into training and testing splits and utilize different models to generate a prediction based on team champion composition.

The model structure for the learning is as follows:
![image](https://user-images.githubusercontent.com/34112687/115801123-9f250e00-a3a1-11eb-8777-6ab500e20d82.png)

where we apply softmax to the first dense layer, followed by sigmoid on the output node to give us a value between 0-1, which can be interpretted as the likelihood of victory. 
The higher the predicted value the more likely that composition is going to win.

The program further takes in 5 champion values and predicts a win percentage, based on the match results of the original summoner used to train the model.

