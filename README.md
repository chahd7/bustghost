I - Introduction:

Our third project consists of the implementation of the “Bust the ghost” game, an interactive game that uses a grid-based environment. The goal is to locate the ghost within the “grid” and bust it by using the sensory cues provided within the game, combining logics and deduction reasoning alongside the usage of probabilities. The player gets 10 attempts when it comes to the number of cells it can click but only 2 attempts to bust one of the clicked cells to find the ghost. The player can choose to showcase the probabilities of each one of the squares, which gets updated after each click of the cells, using Bayesian probabilistic inferencing. After each click, a color is displayed based on the Manhattan distance between the clicked cells and the ghost’s position and by sampling the appropriate color (and the appropriate direction in the case of the bonus) from the conditional distribution table. We developed this game using the python library Tkinter, as it allows us to create a responsive interface for the game as well as implement the needed elements and logic allowing the player to have a smooth experience. 

II - Bayesian Probabilistic Inferencing:

Bayesian Inference is a method used in statics which makes usage of Bayes’ theorem to update the probability of a hypothesis as we get more information being made available. Bayesian inference consists therefore of updating the probability estimates regarding certain hypotheses/parameters based on prior knowledge as well as new acquired data. It therefore differs from classical statistical inference which mainly focuses on frequency and likelihood without taking prior consideration into consideration. As it’s heart, we find the Bayes’ theorem which describes how to update the probabilities of hypotheses when provided with further evidence. It states that posterior probabilities are proportial to the likelihood times the prior probabilities.

![image](https://github.com/chahd7/bustghost/assets/125460075/80429166-e685-4505-9fe1-094943c89e62)

One of the strengths of Bayesian inference is how it gives the ability to quantify uncertainty by working with probability distributions rather than single points estimates. 

III - Initial Set up of the Interface:

i. General Set up:

![image](https://github.com/chahd7/bustghost/assets/125460075/7025d7c8-7e0d-42e5-b977-9827257d1016)

Using python’s object-oriented properties, everything will be put within a BustTheGhostGame class. Within the method __init__(self, master), we start by initializing the class as well as all its attributes. The master here is used as a variable to store the main Tkinter window that will be containing the game’s GUI. For the grid_size, we set it to be a (9,12) grid as per the requirements given. The ghost_position returns contain the xg and yg coordinates returned by the placeGhost() function, which places the ghost in a random cell within a 7 x 13 domain, as precised in the requierements. In the ghost_remain variable, we initially store how many ghosts we have (which is 1 here in our case) and we will be decrementing it whenever a ghost is successfully busted. The bust_attempts variable stores the number of busts that we can attempt (here, it is set to 2 as per the requierements) while the credits variable stories the number of cells that we can click and as soon as we go over that, we get a game over message and the game stops (here, we chose to set it to 10 in order to give the player enough chances while also not making the game too long). The selected_cell variable will be used to store the current selected cell and the probabilities variable will come store the initial probabilities before one of the cells are clicked and we update them, and the busted variable indicates whether the ghost was busted or not and initially equal to a False. To decide if we show the probabilities or not using the Peep button, we set a probabilities_visible variable initialized to False, and we also set a game_over variable initialized to False as well. Finally, we have a variable that dictionary which will come to store the color codes for all the needed colours.

![image](https://github.com/chahd7/bustghost/assets/125460075/2a5c87fe-c689-4615-b34f-38c87387294c)

Here, the setup_ui method is used to initialize the user interface of the game using the Tkinter library. We create a 9 x 12 grid representing the game’s cells stores in a dictionary for easy access, and each one of them is assigned the cell_clicked event handler. Additionally, we have special control labels buttons:

• A “Bust” button which triggers an attempt to bust a cell to find the ghost

![image](https://github.com/chahd7/bustghost/assets/125460075/f85ec722-53e2-4543-b8a7-397676c6db22)

• A “Peep” button which allows that can be activated and deactivated by the player to get hints about the position of the position of the ghost using the updated probabilities displayed in each cell after each click

![image](https://github.com/chahd7/bustghost/assets/125460075/a4088436-c1c9-4140-9554-b87a22ba007a)

Additionally, we have label spaces:
• A label that displays the number of ghosts remaining, the credits (number of cells that can still be clicked) and the remaining bust attempts
• A message label that gives the outcomes to the user for feedback


ii. Addition of the functionalities 

![image](https://github.com/chahd7/bustghost/assets/125460075/034ca3d1-1a3d-47ea-9671-f5aad15047cc) 

In the placeGhost() function, we generate a random integer between 1 and 7 for the x coordinates of the ghost and between 1 and 13 for the y coordinates of the ghost. We then return the two variables which will be stored in the ghost_position variable when we did the initiation of the class. 

![image](https://github.com/chahd7/bustghost/assets/125460075/bd71a9a6-552a-4676-bab4-8cc4a353c5bc)

Here, the computeInitialPriorProbabilities() function initializes a probability distribution across the grid by assigning to each cell an equal probability of containing the ghost. To do this, we divide 1.0 by the total of cells that we have (108 cells for a 9x12 grid). This will make sure that the sum of the probabilities across all the cells equals to 1. Here, we find 0.00926 for each cell but tkinter rounds it to 0.01 to make it more readable. We then store this into a probabilities dictionary where each cell coordinate is linked with its probability, and it is then returned.

![image](https://github.com/chahd7/bustghost/assets/125460075/33ea4686-aef1-46f0-8f91-036c2f257e67)

The cell_clicked() method handles the interactios within the grid. After each click of the cells, the player’s credits are decremented. If the numbers of credits that are left is equal to zero, then we end the game. Within this method, we call the DistanceSense method which evaluates the clicked cell’s proximity to the ghost and returns the appropriate color based on the conditional distribution table. The cell’s appearance is then updated to reflect the picked color, helping guide the user. Additionally, it updates the probability distribution of the ghost’s location based on the new provided information by calling the updatePosteriorGhostLocationProbabilities() method. Finally, we store the current clicked cell into the selected_cell variable. 

![image](https://github.com/chahd7/bustghost/assets/125460075/f24c9fa3-d914-4e2c-9731-6adedad59dcb)

The end_game() method is used here to terminate the game. We start by setting the game_over variable to True so that we have no further action. We then display to the player either a “You Won!” message if the victory conditions have been met or “GAME OVER” one otherwise. After this, we disable all the interactive elements of the interface (cell in grid, control buttons..) so that we don’t have any further interaction and we freeze the game state to show that the game has ended. 

IV. Implementation of the Distance Sensors:

The equation P(Ghost) = P(Ghost/Colour) = P(Ghost(t-1)) * P (Colour/Distance from Ghost) exemplifies the application of Bayesian inference to revise the likelihood of the ghost being in a particular cell. Initially, the prior probability P(Ghost) indicates the baseline probability of the ghost's presence in each cell before any sensor data is considered. Following a player's selection of a cell, a sensor reading is conducted, yielding a colour determined by the conditional probability distribution P (Colour/Distance from Ghost). This distribution signifies the probability of observing a specific colour given the ghost's distance from the selected cell. Subsequently, this distribution informs the update of the posterior probability regarding the ghost's presence in that cell based on the latest sensor data.

In this game, probabilistic inference plays a crucial role in estimating the likelihood of the ghost's presence in specific locations based on observed tile colours and their respective distances from the ghost. This process relies on probability theory principles and the information contained within the joint probability table. Here's how it operates within the context of the game:
Joint probability table: This table encompasses joint probability values for each color and distance combination, indicating the likelihood of observing a particular color at a given distance from the ghost.
For the distance sensors, this is the conditional probability table that has been used:

![image](https://github.com/chahd7/bustghost/assets/125460075/a3689bcf-9b0b-4fe9-aaf3-ad2d92ef95b7)

For distance = 0 : 

![image](https://github.com/chahd7/bustghost/assets/125460075/7b08bf5a-efd1-4d96-abde-d63523471347)

For distance = 1 or distance = 2 :

![image](https://github.com/chahd7/bustghost/assets/125460075/c21d0f7b-0aed-421c-bb3a-884b0c579852)

For distance = 3 or distance = 4 : 

![image](https://github.com/chahd7/bustghost/assets/125460075/5ebeedf9-b598-4c7b-89bd-084567ad4065)

For distance >= 5 : 

![image](https://github.com/chahd7/bustghost/assets/125460075/0ec1c698-cac1-4c60-9eca-07d5411ab9cb)

Which reflects on the rules given by the game stating that:
On the ghost: red
1 or 2 cells away: orange
3 or 4 cells away: yellow
5+ cells away: green
We then converted into a dictionary where the key is the distance which we will be using later: 

![image](https://github.com/chahd7/bustghost/assets/125460075/77031a9a-1e74-47cf-ae38-95153403ea0f)

Observation: When the player selects a tile, they observe its colour. This observation serves as evidence regarding the ghost's potential location, with different colours carrying different probabilities depending on their distances from the ghost.

![image](https://github.com/chahd7/bustghost/assets/125460075/4c30cd87-ba75-4a3c-80b8-951bf66f0958)

The DistanceSense() method helps the players see how close they are to the hidden ghost within the grid. We start by calculating the distance between the ghost (gx and gy) and the selected cell (xclk and yclk) by using the Manhattan distance, which is more suited for grid environments. The distance is then rounded and used to access the specific distribution from the previously defined table S using color_prob = self.S[distance_key], where we have an association of the different distances with their probabilities for each color. We then conduct a sampling from the retrieved distribution using colors, probabilities =zip(*color_prob.items()) which extracts the color names alongside their associated probabilities from the distribution into lists. Then, using chosen_color = np.random.choice(colors, p=probabilities), we randomly selected one of the colours, with a selection weight by the probabilities. We therefore provide a color-coded indication about how close we are to the ghost to the player. If the clicked cell corresponds to the cell where the ghost is located, the busted variable is set to true. This will make it able for us to use in the bust_ghost() function while ensuring that the location of the ghost is only used in the distanceSense() function. Finally, the chosen color is returned.
Inference: After determining the likelihood based on the sensed color, the method updates the probabilities for each cell using the updatePosteriorGhostLocationProbabilities method. In this method, the likelihood obtained from the joint probability table is used to update the probability for each cell, multiplying the current probability by the likelihood. Here, we make usage of the Bayesian inference as follows: Pt(G=Li) = Pt(G=Li/ S=Color at location Li)= P(S=Color at location Li/ / G=Li) * Pt1 (G=Lj)
With P0 (G=Lj) is a uniform distribution (Initial prior probability) And P(S=Color at location Li/ / G=Li) = P(S=Color/ distance=0).

![image](https://github.com/chahd7/bustghost/assets/125460075/f75dce23-ba17-44d6-aa62-10a3ba105843)

We loop through the grid cells by using np.ndindex(self.grid_size) which generates a pair of (i,j) for each cell. After that, we calculate the distance between the location and the cell where the color was sensed and using this distance, the function retreaves a distance_key and then looks up for the likelihood of observing the sensed_color we generated from that distance using the conditional table S we have defined previously. The probability of the ghost being in each cell is then updated by multiplying the probabilities we have in self.probabilities[(i, j)] by the like likelihood of observing the sensed color at that distance, applying therefore Bayesian Inferance and updating the belief about where the ghost is depending on the new evidence. Finally, we normalize the entire probability distribution to make sure that their sum equals to one. We do this by dividing each cell’s updated probability by the sum of all updated probabilities. 














