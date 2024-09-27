import random as rnd

class Robot:

    def __init__(self):
        # Define R- and Q-matrices here.
                   #Actions
                   #  Up   Down Right Left  # States
        r_matrix = [[-100, -1, -100, -5],   # (0,0)
                    [-100, -5, -1, -5],     # (0,1)
                    [-100, 0, 0, -1],       # (0,2)
                    [-100, -1, 0, -1],      # (0,3)
                    [-100, 0, -5, 0],       # (0,4)
                    [-100, 0, -100, 0],     # (0,5)
                    [-5, -1, -5, -100],     # (1,0)
                    [-1, 0, 0, -5],         # (1,1)
                    [-1, 0, -1, -5],        # (1,2)
                    [0, -1, 0, 0],          # (1,3)
                    [0, 0, 0, -1],          # (1,4)
                    [-5, -1, -100, 0],      # (1,5)
                    [-5, -1, 0, -100],      # (2,0)
                    [-5, 0, 0, -1],         # (2,1)
                    [0, 0, -1, 0],          # (2,2)
                    [-5, 0, 0, 0],          # (2,3)
                    [0, 0, -1, -1],         # (2,4)
                    [0, 0, -100, 0],        # (2,5)
                    [-1, -1, 0, -100],      # (3,0)
                    [0, 0, 0, -1],          # (3,1)
                    [0, -1, 0, 0],          # (3,2)
                    [-1, 0, 0, 0],          # (3,3)
                    [0, -1, 0, 0],          # (3,4)
                    [-1, 0, -100, 0],       # (3,5)
                    [-1, 10, 0, -100],      # (4,0)
                    [0, -5, -1, -1],        # (4,1)
                    [0, -5, 0, 0],          # (4,2)
                    [0, -5, -1, -1],        # (4,3)
                    [0, -5, 0, 0],          # (4,4)
                    [0, -5, -100, -1],      # (4,5)
                    [-1, -100, -5, -100],   # (5,0)
                    [0, -100, -5, 10],      # (5,1)
                    [-1, -100, -5, -5],     # (5,2)
                    [0, -100, -5, -5],      # (5,3)
                    [-1, -100, -5, -5],     # (5,4)
                    [0, -100, -100, -5],    # (5,5)
                    ]
        q_matrix = [[0] * 4 for _ in range(36)]

    def get_x(self):
        # Return the current column of the robot, should be in the range 0-5.
        return 3

    def get_y(self):
        # Return the current row of the robot, should be in the range 0-5.
        return 0

    def get_next_state_mc(self):
        # Return the next state based on Monte Carlo.
        pass

    def get_next_state_eg(self):
        # Return the next state based on Epsilon-greedy.
        pass

    def monte_carlo_exploration(self):
        pass

    def q_learning(self):
        pass
        
    def one_step_q_learning(self):
        # Get action based on policy
        # Get the next state based on the action
        # Get the reward for going to this state
        # Update the Q-matrix
        # Go to the next state
        pass
    
    def has_reached_goal(self):
        # Return 'True' if the robot is in the goal state.
        pass
        
    def reset_random(self):
        # Place the robot in a new random state.
        pass

    def greedy_path(self):
        pass

# Feel free to add additional classes / methods / functions to solve the assignment...