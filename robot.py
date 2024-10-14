import random as rnd

class Robot:
    """
    Class object for machine learning agent, a theoretical robot.
    
    Attributes
    ----------
    alpha: float
        Learning rate, [0, 1]
    gamma: float
        Discount factor, [0, 1]
    epsilon: float
        Chance of doing exploration insted of exploitation [0, 1]
    min_epsilon: float
        Minimum value for epsilon [0, 1]
    decay_rate: float
        How fast epsilon decreases per epoch [0, 1]
    best_path: list of tuples
        Chronological list of states visited when using best found path.
    best_score: int
        Score achieved using best found path.

    Methods
    -------
    set_next_state(action: int) -> int:
        Updates robot position based on action (up, down, right, left)
        Checks if action is legal and returns the new states index.
    get_action_greedy(state: int) -> int:
        Returns the action with the highest Q-value for current state.
        If multiple actions have same value, selects one of them
        randomly.
    get_action_mc() -> int:
        Randomly selects and returns an action (0-3), simulating Monte
        Carlo policy.
    get_action_eg(state: int) -> int:
        Returns Monte Carlo or greedy action based on epsilon value.
    epsilon_update() -> None:
        Decreases epsilon by decay_rate towards min_epsilon.
    monte_carlo_exploration(epochs: int) -> None:
        Explores terrain with Monte Carlo policy. Starts in (0, 3),
        resets in (5, 0). Repeats for specified number of epochs, then
        prints best score achieved.
    one_step_q_learning() -> None:
        Executes one step of q-learning and updates the q-matrix.
    q_learning(epochs: int) -> None:
        Runs q_learning for specified number of epochs. Starts epoch in
        random state, ends epoch when reaching (5, 0). Reduces epsilon
        for each epoch.
    has_reached_goal() -> bool:
        Returns True if target state == (5, 0) is reached.
    reset_random() -> None:
        Resets robot position to random state.
    get_best_path() -> None:
        Finds best path and score using a greedy policy on the
        q-matrix.
    """

    def __init__(
            self, alpha: float, gamma: float, epsilon: float,
            min_epsilon: float, decay_rate: float
        ):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.min_epsilon = min_epsilon
        self.decay_rate = decay_rate
        self.best_path = []
        self.best_score = 0
        self.y = None
        self.x = None
            # Actions
            # Up  Down Right Left  # States
        self.r_matrix = [
            [-100, -15, -5, -100],  # (0,0)
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
            [-1, -100, -100, -15]   # (5,5)
        ]
        self.q_matrix = [[0] * 4 for _ in range(36)]

    def set_next_state(self, action: int) -> int:
        """
        Change and return position based on action, if action is legal.

        Parameters
        ----------
        action: int
            The action to perform, where:
            - 0: Move up (decrement y, if y > 0)
            - 1: Move down (increment y, if y < 5)
            - 2: Move right (increment x, if x < 5)
            - 3: Move left (decrement x, if x > 0)

        Returns
        -------
        int
            Row number in r/q-matrix.
        """
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
        return self.y * 6 + self.x

    def get_action_greedy(self, state: int) -> int:
        """
        Return best action for current state based on greedy policy.

        Parameters
        ----------
        state: int
            Row number in r/q-matrix.

        Returns
        -------
        int
            Highest rewarding action, between 0 and 3.
        """
        best_q = max(self.q_matrix[state])
        best_actions = ([
            index for index, value in 
            enumerate(self.q_matrix[state]) if value == best_q
        ])
        return rnd.choice(best_actions)
    
    def get_action_mc(self) -> int:
        """Return int representing action based on Monte Carlo policy."""

        return rnd.randint(0, 3)

    def get_action_eg(self, state: int) -> int:
        """
        Returns Monte Carlo or greedy action based on epsilon.

        Parameters
        ----------
        state: int
            Row number in r/q-matrix.

        Returns
        -------
        int
            Action between 0 and 3.
        """
        if rnd.uniform(0, 1) < self.epsilon:
            return self.get_action_mc()
        else:
            return self.get_action_greedy(state)
        
    def epsilon_update(self) -> None:
        """Changes epsilon by decay_rate until it is min_epsilon."""

        self.epsilon = max(self.min_epsilon, self.epsilon * self.decay_rate)
        return None

    def monte_carlo_exploration(self, epochs: int) -> None:
        """
        Prints the highest score achieved in given number of epochs.

        Parameters
        ----------
        epochs: int
            Number of simulation iterations to perform.

        Returns
        -------
        None
        """
        scores = []
        for _ in range(epochs):
            self.y = 0
            self.x = 3
            sum_reward = 0
            finished = False
            while not finished:
                action = self.get_action_mc()
                sum_reward += self.r_matrix[6 * self.y + self.x][action]
                self.set_next_state(action)
                finished = self.has_reached_goal()
            scores.append(sum_reward)
        print(max(scores))
        return None

    def one_step_q_learning(self) -> None:
        """Execute one step of q-learning."""

        current_state = self.y * 6 + self.x
        action = self.get_action_eg(current_state)
        next_state = self.set_next_state(action)
        reward = self.r_matrix[current_state][action]
        self.q_matrix[current_state][action] = (
            (1 - self.alpha) * self.q_matrix[current_state][action] + self.alpha
            * (reward + self.gamma * max(self.q_matrix[next_state]))
        )
        return None

    def q_learning(self, epochs: int) -> None:
        """Execute q-learning for given number of epochs."""

        for _ in range(epochs):
            self.reset_random()
            while not self.has_reached_goal():
                self.one_step_q_learning()
            self.epsilon_update()
        return None

    def has_reached_goal(self) -> bool:
        """Return True if Robot has reached target destination (5, 0)."""

        if self.y == 5 and self.x == 0:
            return True
        else:
            return False
        
    def reset_random(self) -> None:
        """Resets robot position to random state."""

        self.y = rnd.randint(0, 5)
        self.x = rnd.randint(0, 5)
        return None

    def get_best_path(self) -> None:
        """Finds and saves best path and its score."""

        self.y = 0
        self.x = 3
        self.best_path.append((self.y, self.x))
        while not self.has_reached_goal():
            current_state = self.y * 6 + self.x
            action = self.get_action_greedy(current_state)
            self.set_next_state(action)
            self.best_score += self.r_matrix[current_state][action]
            self.best_path.append((self.y, self.x))
        return None

#For testing monte carlo exploration
#robot = Robot()
#robot.monte_carlo_exploration(10000)