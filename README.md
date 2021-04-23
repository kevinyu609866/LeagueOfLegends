This program uses Riot Developer API for data. 

Since champions are encoded with an ID, the decoding was used done using the following json file:
http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json

It takes the generated statistics from the last 100 games per player. 
v1: Records the champions in every game for 100 games. 
The model was given the result of the game, for every set of five champions: Win or Loss. 

![image](https://user-images.githubusercontent.com/34112687/115303267-07b58600-a129-11eb-9cc7-e8d7a7f85687.png)

Such that each storage of 100 games gives us a dataset of 200 by 6 as follows:
![image](https://user-images.githubusercontent.com/34112687/115303285-0edc9400-a129-11eb-8cd0-b16cb2609fab.png)

where [A,B,C,D,E] is the encoding of some champion. 
The model then learns on the stored data for the player[s] and calculates the strength, measured by probability of 'winning' based on those games used to train. 

More details on the model is below:

![image](https://user-images.githubusercontent.com/34112687/115831242-f396b080-a3d6-11eb-87bc-d6ae12c3506f.png)

where we apply softmax to the first and second dense layer, followed by sigmoid on the last dense layer: the result node to give us a value between 0-1, which can be interpretted as the likelihood of victory. 
The higher the predicted value the more likely that composition is going to win.

The program further takes in 5 NEW champion values and predicts a win percentage.

