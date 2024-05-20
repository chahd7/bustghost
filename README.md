I - Introduction:
Our third project consists of the implementation of the “Bust the ghost”
game, an interactive game that uses a grid-based environment. The goal is to
locate the ghost within the “grid” and bust it by using the sensory cues provided
within the game, combining logics and deduction reasoning alongside the usage
of probabilities. The player gets 10 attempts when it comes to the number of
cells it can click but only 2 attempts to bust one of the clicked cells to find the
ghost. The player can choose to showcase the probabilities of each one of the
squares, which gets updated after each click of the cells, using Bayesian
probabilistic inferencing. After each click, a color is displayed based on the
Manhattan distance between the clicked cells and the ghost’s position and by
sampling the appropriate color (and the appropriate direction in the case of the
bonus) from the conditional distribution table.
We developed this game using the python library Tkinter, as it allows us to
create a responsive interface for the game as well as implement the needed
elements and logic allowing the player to have a smooth experience. 

II - Bayesian Probabilistic Inferencing:
Bayesian Inference is a method used in statics which makes usage of Bayes’ theorem
to update the probability of a hypothesis as we get more information being made available.
Bayesian inference consists therefore of updating the probability estimates regarding certain
hypotheses/parameters based on prior knowledge as well as new acquired data. It therefore
differs from classical statistical inference which mainly focuses on frequency and likelihood
without taking prior consideration into consideration.
As it’s heart, we find the Bayes’ theorem which describes how to update the probabilities of
hypotheses when provided with further evidence. It states that posterior probabilities are
proportial to the likelihood times the prior probabilities.

![image](https://github.com/chahd7/bustghost/assets/125460075/80429166-e685-4505-9fe1-094943c89e62)

One of the strengths of Bayesian inference is how it gives the ability to quantify uncertainty
by working with probability distributions rather than single points estimates. 

III - Initial Set up of the Interface:
i. General Set up:
![image](https://github.com/chahd7/bustghost/assets/125460075/7025d7c8-7e0d-42e5-b977-9827257d1016)

Using python’s object-oriented properties, everything will be put within a
BustTheGhostGame class. Within the method __init__(self, master), we start by initializing
the class as well as all its attributes. The master here is used as a variable to store the main
Tkinter window that will be containing the game’s GUI. For the grid_size, we set it to be a
(9,12) grid as per the requirements given. The ghost_position returns contain the xg and yg
coordinates returned by the placeGhost() function, which places the ghost in a random cell
within a 7 x 13 domain, as precised in the requierements. In the ghost_remain variable, we
initially store how many ghosts we have (which is 1 here in our case) and we will be
decrementing it whenever a ghost is successfully busted. The bust_attempts variable stores
the number of busts that we can attempt (here, it is set to 2 as per the requierements) while
the credits variable stories the number of cells that we can click and as soon as we go over
that, we get a game over message and the game stops (here, we chose to set it to 10 in order
to give the player enough chances while also not making the game too long). The
selected_cell variable will be used to store the current selected cell and the probabilities
variable will come store the initial probabilities before one of the cells are clicked and we
update them, and the busted variable indicates whether the ghost was busted or not and
initially equal to a False. To decide if we show the probabilities or not using the Peep button,
we set a probabilities_visible variable initialized to False, and we also set a game_over
variable initialized to False as well. Finally, we have a variable that dictionary which will
come to store the color codes for all the needed colours.

![image](https://github.com/chahd7/bustghost/assets/125460075/2a5c87fe-c689-4615-b34f-38c87387294c)

Here, the setup_ui method is used to initialize the user interface of the game using the
Tkinter library. We create a 9 x 12 grid representing the game’s cells stores in a dictionary for
easy access, and each one of them is assigned the cell_clicked event handler. Additionally,
we have special control labels buttons:

• A “Bust” button which triggers an attempt to bust a cell to find the ghost
![image](https://github.com/chahd7/bustghost/assets/125460075/f85ec722-53e2-4543-b8a7-397676c6db22)
• A “Peep” button which allows that can be activated and deactivated by the player to
get hints about the position of the position of the ghost using the updated probabilities
displayed in each cell after each click
![image](https://github.com/chahd7/bustghost/assets/125460075/a4088436-c1c9-4140-9554-b87a22ba007a)
Additionally, we have label spaces:
• A label that displays the number of ghosts remaining, the credits (number of cells that
can still be clicked) and the remaining bust attempts
• A message label that gives the outcomes to the user for feedback


ii. Addition of the functionalities 
![image](https://github.com/chahd7/bustghost/assets/125460075/034ca3d1-1a3d-47ea-9671-f5aad15047cc)
In the placeGhost() function, we generate a random integer between 1 and 7 for the x
coordinates of the ghost and between 1 and 13 for the y coordinates of the ghost. We then
return the two variables which will be stored in the ghost_position variable when we did the
initiation of the class. 
![image](https://github.com/chahd7/bustghost/assets/125460075/bd71a9a6-552a-4676-bab4-8cc4a353c5bc)
Here, the computeInitialPriorProbabilities() function initializes a probability
distribution across the grid by assigning to each cell an equal probability of containing the
ghost. To do this, we divide 1.0 by the total of cells that we have (108 cells for a 9x12 grid).
This will make sure that the sum of the probabilities across all the cells equals to 1. Here, we
find 0.00926 for each cell but tkinter rounds it to 0.01 to make it more readable. We then
store this into a probabilities dictionary where each cell coordinate is linked with its
probability, and it is then returned.
![image](https://github.com/chahd7/bustghost/assets/125460075/33ea4686-aef1-46f0-8f91-036c2f257e67)
The cell_clicked() method handles the interactios within the grid. After each click of the
cells, the player’s credits are decremented. If the numbers of credits that are left is equal to
zero, then we end the game. Within this method, we call the DistanceSense method which
evaluates the clicked cell’s proximity to the ghost and returns the appropriate color based on
the conditional distribution table. The cell’s appearance is then updated to reflect the picked
color, helping guide the user. Additionally, it updates the probability distribution of the
ghost’s location based on the new provided information by calling the updatePosteriorGhostLocationProbabilities() method. Finally, we store the current clicked
cell into the selected_cell variable. 
![image](https://github.com/chahd7/bustghost/assets/125460075/f24c9fa3-d914-4e2c-9731-6adedad59dcb)
The end_game() method is used here to terminate the game. We start by setting the
game_over variable to True so that we have no further action. We then display to the player
either a “You Won!” message if the victory conditions have been met or “GAME OVER” one
otherwise. After this, we disable all the interactive elements of the interface (cell in grid,
control buttons..) so that we don’t have any further interaction and we freeze the game state
to show that the game has ended. 






