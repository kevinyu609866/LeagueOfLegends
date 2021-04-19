# PersonalizedTierListByPlayer

This program uses Riot Developer API for data. 

It takes the generated statistics from the last 100 games of a player. 
We then record the champions in each of the 100 games, and further, record the result of the game for each set of 5 champions as follows:
[A,B,C,D,E,WIN]
[F,G,H,I,J,LOSS]

Such that each storage of 100 games gives us a dataset of 200 by 6 as follows:
        Champ1 Champ2 Champ3 Champ4 Champ5 Result
Game 1      A       B      C      D      E    WIN
Game 1      F       G      I      K      L   LOSS
......
Game 100    A       G      C      K      E    WIN
Game 100    F       B      I      D      L   LOSS

We then divide the dataset into training and testing splits and utilize different models to generate a tier list of champions and their expected result. 
