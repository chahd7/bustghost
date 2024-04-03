import tkinter as tk
import numpy as np

class BustTheGhostGame:
    def __init__(self, master):
        self.master = master
        self.grid_size = (9, 12)
        self.ghost_position = self.placeGhost()
        self.ghost_remain = 1
        self.bust_attempts = 2
        self.credits = 10 
        self.selected_cell = None
        self.busted = False
        self.probabilities = self.computeInitialPriorProbabilities()
        self.probabilities_visible = False
        self.game_over = False
        self.color_mapping = {
    'Red': '#FF0000',  # Red
    'Orange': '#FFA500',  # Orange
    'Yellow': '#FFFF00',  # Yellow
    'Green': '#008000'  # Green
}

        self.setup_ui()

#conditional probabilities table 
    S = {
    0: {'Red': 0.80, 'Orange': 0.15, 'Yellow': 0.04, 'Green': 0.01},
    1: {'Red': 0.30, 'Orange': 0.60, 'Yellow': 0.07, 'Green': 0.03},
    2: {'Red': 0.30, 'Orange': 0.60, 'Yellow': 0.07, 'Green': 0.03},
    3: {'Red': 0.03, 'Orange': 0.07, 'Yellow': 0.60, 'Green': 0.30},
    4: {'Red': 0.03, 'Orange': 0.07, 'Yellow': 0.60, 'Green': 0.30},
    '>5': {'Red': 0.03, 'Orange': 0.07, 'Yellow': 0.30, 'Green': 0.60}
}

    def placeGhost(self):
        # Randomly place the ghost in the grid
        xg = np.random.randint(0, 9)
        yg = np.random.randint(0, 12)
        print(f"Ghost placed at: ({xg}, {yg})")
        return (xg, yg)

    def computeInitialPriorProbabilities(self):
        # Compute the initial probabilities uniformly for all locations
        initial_prob = 1.0 / (self.grid_size[0] * self.grid_size[1])
        probabilities = {loc: initial_prob for loc in np.ndindex(self.grid_size)}
        return probabilities

    def setup_ui(self):
        self.cells = {}
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                cell = tk.Button(self.master, text='', command=lambda i=i, j=j: self.cell_clicked(i, j), width=5, height=2)
                cell.grid(row=i, column=j, sticky='nsew')
                self.cells[(i, j)] = cell

        self.bust_button = tk.Button(self.master, text='BUST', bg='blue', fg='white', command=self.bust_ghost)
        self.bust_button.grid(row=0, column=self.grid_size[1], rowspan=2, sticky='nsew')

        self.ghosts_remaining_label = tk.Label(self.master, text=f'GHOSTS REMAINING: {self.ghost_remain}')
        self.ghosts_remaining_label.grid(row=2, column=self.grid_size[1], sticky='nsew')

        self.busts_remaining_label = tk.Label(self.master, text=f'BUSTS REMAINING: {self.bust_attempts}')
        self.busts_remaining_label.grid(row=3, column=self.grid_size[1], sticky='nsew')

        self.credits_label = tk.Label(self.master, text=f'CREDITS: {self.credits}')
        self.credits_label.grid(row=4, column=self.grid_size[1], sticky='nsew')

        self.messages_label = tk.Label(self.master, text='MESSAGES:')
        self.messages_label.grid(row=5, column=self.grid_size[1], rowspan=4, sticky='nsew')

        self.peep_button = tk.Button(self.master, text='PEEP', bg='red', fg='white', command=self.toggle_peep)
        self.peep_button.grid(row=9, column=self.grid_size[1], sticky='nsew')

    def toggle_peep(self):
        self.probabilities_visible = not self.probabilities_visible
        for (i, j), cell in self.cells.items():
            if self.probabilities_visible:
                probability_text = f'{self.probabilities[(i, j)]:.2f}'
                cell.config(text=probability_text)
            else:
                cell.config(text='')

    def cell_clicked(self, i, j):
     if not self.game_over:
        self.credits -= 1  # decrement credits
        self.credits_label.config(text=f'CREDITS: {self.credits}')
        if self.credits <= 0:
            self.end_game()
            return
        
        # Use the DistanceSense function to get a color based on the distance to the ghost
        sensed_color = self.DistanceSense(i, j, *self.ghost_position)
        # Update cell color based on the sensor reading
        self.cells[(i, j)].config(bg=self.color_mapping[sensed_color])
        print(f"Cell clicked at: ({i}, {j}), sensed color: {sensed_color}")
        
        # Update the probabilities based on the sensed color
        self.updatePosteriorGhostLocationProbabilities(sensed_color, i, j)
        
        # Refresh the probability display if the peep mode is active
        if self.probabilities_visible:
            self.toggle_peep()
        
        if not self.game_over:
            self.selected_cell = (i, j)
            
    def bust_ghost(self):
     if not self.game_over and self.selected_cell:  # Ensure there's a selected cell and game is not over
        self.bust_attempts -= 1
        self.busts_remaining_label.config(text=f'BUSTS REMAINING: {self.bust_attempts}')
        # Check if the selected cell matches the ghost's position
        if self.busted :
            
            self.ghost_remain -= 1
            self.ghosts_remaining_label.config(text=f'GHOSTS REMAINING : {self.ghost_remain}')
            
            if self.ghost_remain > 0:
                message = f'You busted a ghost! {self.ghost_remain} ghosts remaining.'
                self.messages_label.config(text=message)
                
            else:
                # No ghosts remaining, win the game
                message = 'You busted the last ghost! Congratulations, you win!'
                self.messages_label.config(text=message)
                self.end_game(won=True)
        else:
            # Ghost is not found in the selected cell
            message = 'MESSAGE : The ghost is not on this cell.'
            self.messages_label.config(text=message)
            if self.bust_attempts <= 0:
                self.end_game(won=False)

        # Deselect the cell after attempting a bust
        self.selected_cell = None




                
    
    def distance_key(self, distance):
     if distance > 4:  # If the distance is greater than 4, use the key '>5'
        return '>5'
     else:
        return distance  # Otherwise, use the distance as the key directly
     
    

    def DistanceSense(self, xclk, yclk, gx, gy):
        
     # Calculate the Manhattan distance
     distance = abs(xclk - gx) + abs(yclk - gy)
    
     # Convert the Manhattan distance to a key for accessing the probability table
     distance_key = self.distance_key(round(distance))
    
     # Get the probability distribution for the given distance from the table
     color_prob = self.S[distance_key]
    
     # Sample a color based on the probability distribution
     colors, probabilities = zip(*color_prob.items())
     chosen_color = np.random.choice(colors, p=probabilities)

     print(f"Ghost placed at: ({self.ghost_position[0], self.ghost_position[1]})")

     if (xclk == gx and yclk == gy):
        self.busted = True; 
     

     return chosen_color


    

    def updatePosteriorGhostLocationProbabilities(self, sensed_color, xclk, yclk):
     for (i, j) in np.ndindex(self.grid_size):
        distance = abs(i - xclk) + abs(j - yclk)
        distance_key = self.distance_key(distance)  
        likelihood = self.S[distance_key][sensed_color]
        # Update the probability for the cell being the ghost's location
        self.probabilities[(i, j)] *= likelihood

     # Normalize the probabilities to sum to 1
     total_prob = sum(self.probabilities.values())
     for key in self.probabilities:
        self.probabilities[key] /= total_prob




                
    

    def end_game(self, won=False):
     self.game_over = True
     message = 'You won!' if won else 'GAME OVER'
     self.messages_label.config(text=message)
     for (i, j), cell in self.cells.items():
        cell.config(state='disabled')
     self.bust_button.config(state='disabled')
     self.peep_button.config(state='disabled')


def main():
    root = tk.Tk()
    root.title("Bust the Ghost Game")
    game = BustTheGhostGame(root)
    root.geometry('800x400') 
    root.mainloop()

if __name__ == "__main__":
    main()

