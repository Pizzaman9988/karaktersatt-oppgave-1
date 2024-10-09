import random as rnd

class Robot:

    def __init__(self):
        self.y = None
        self.x = None
        # Define R- and Q-matrices here.
                        #Actions
                        #  Up  Down Right Left  # States
        self.r_matrix = [[-100, -15, -5, -100], # (0,0)
                        [-100, -15, -5, -15],   # (0,1)
                        [-100, -1, -1, -5],     # (0,2)
                        [-100, -5, -1, -5],     # (0,3)
                        [-100, -1, -15, -1],    # (0,4)
                        [-100, -1, -100, -1],   # (0,5)
                        [-15, -5, -15, -100],   # (1,0)
                        [-5, -1, -1, -15],      # (1,1)
                        [-5, -1, -5, -15],      # (1,2)
                        [-1, -5, -1, -1],       # (1,3)
                        [-1, -1, -1, -5],       # (1,4)
                        [-15, -5, -100, -1],    # (1,5)
                        [-15, -5, -1, -100],    # (2,0)
                        [-15, -1, -1, -5],      # (2,1)
                        [-1, -1, -5, -1],       # (2,2)
                        [-5, -1, -1, -1],       # (2,3)
                        [-1, -1, -5, -5],       # (2,4)
                        [-1, -1, -100, -1],     # (2,5)
                        [-5, -5, -1, -100],     # (3,0)
                        [-1, -1, -1, -5],       # (3,1)
                        [-1, -5, -1, -1],       # (3,2)
                        [-5, -1, -1, -1],       # (3,3)
                        [-1, -5, -1, -1],       # (3,4)
                        [-5, -1, -100, -1],     # (3,5)
                        [-5, 50, -1, -100],     # (4,0)
                        [-1, -15, -5, -5],      # (4,1)
                        [-1, -15, -1, -1],      # (4,2)
                        [-1, -15, -5, -5],      # (4,3)
                        [-1, -15, -1, -1],      # (4,4)
                        [-1, -15, -100, -5],    # (4,5)
                        [-5, -100, -15, -100],  # (5,0)
                        [-1, -100, -15, 50],    # (5,1)
                        [-5, -100, -15, -15],   # (5,2)
                        [-1, -100, -15, -15],   # (5,3)
                        [-5, -100, -15, -15],   # (5,4)
                        [-1, -100, -100, -15]]  # (5,5)
        self.q_matrix = [[0] * 4 for _ in range(36)]

    def get_action_mc(self):
        return rnd.randint(0, 3)

    def set_next_state_mc(self, action):
        # Return the next state based on Monte Carlo.
        match action:
            case 0:
                if self.y != 0:
                    self.y -= 1
            case 1:
                if self.y != 5:
                    self.y += 1
            case 2:
                if self.x != 5:
                    self.x += 1
            case 3:
                if self.x != 0:
                    self.x -= 1
        return

    def get_next_state_eg(self):
        # Return the next state based on Epsilon-greedy.
        pass

    def monte_carlo_exploration(self, epochs):
        score = []
        for _ in range(epochs):
            self.y = 0
            self.x = 3
            sum_reward = 0
            finished = False
            while not finished:
                action = self.get_action_mc()
                sum_reward += self.r_matrix[6 * self.y + self.x][action]
                self.set_next_state_mc(action)
                finished = self.has_reached_goal()
            score.append(sum_reward)
        print(max(score))


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
        if self.y == 5 and self.x == 0:
            return True
        else:
            return False
        
    def reset_random(self):
        self.y = rnd.randint(0, 5)
        self.x = rnd.randint(0, 5)
        return

    def greedy_path(self):
        pass

robot = Robot()

robot.monte_carlo_exploration(10000)