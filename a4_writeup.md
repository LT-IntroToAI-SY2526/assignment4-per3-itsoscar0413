# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?

# Because AI helped me with the code, function wise, I did learn about object and classes but I still wanted to do some work, so I wanted to make my own assert, thus the most difficult part of tic-tac-toe was the assert itself. It was a bit difficult to not only try to format the assert to match the other asserts, but also make sure it passes. Especially when it came to using the functions written previously, and making it make sense both logically and also with the code. But in the end, I did manage to make it work and I learned how each method within the class function relies on each other in order to make it work.

2. Explain how you would add a computer player to the game.

# If it's just an AI without difficulty, you could have it choose a spot randomly, like choose a number randomly through a list of available spots. Assign each spot on the board with a number, and have it use that list. Every time a spot gets filled with 'X' or 'O', the number associated to that spot is removed from the generator

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

# I'm not sure how to actually make the code itself but I know it exists. Every time it loses, it takes in the information why it loss, and how the player won, and it can try to train itself to not only spot and prevent that type of win, but also try to mimic it. Bascailly after every game, it learns from its mistakes and how the player plays, and adjusts itself. If it notices the player is doing really well, it will learn from the player and adjust to it. However, if the player is playing poorly, the Ai could inspect what actions it is doing which is causing it to win, and repeat it or learn from it.