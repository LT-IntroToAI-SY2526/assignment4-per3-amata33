# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?

The most difficult part of the program was making the self board, as the \ns took part of the syntax. Also, the new constructor method was pretty difficult to learn at first but then got the hang of it. This might have been because I sometimes confused it on how I would do it in java (using the this. method instead of self).

2. Explain how you would add a computer player to the game.

I would add an algorithm that would rival the player with "logical" strategies. Like covering a spot that the opponent would use to win. However, if it can't do that, I would implement the three corners strategy. Or it can also put in Xs or Os randomly by using the random function (this can be used to start the match).

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

Let's say the opponent has the board like this 
#* X * (# is being used to not make * a bullet point)
 O X *
 X * O
The computer will cover the bottom row center with an O to not let the player win. Also, as mentioned before, it could use the three corners method.
O * O
X * *
X X O
notice how the bot can win no matter what the opponent does. 
That's basically all I'm thiking of how I would do it.