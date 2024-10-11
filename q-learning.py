import pygame
from pygame.locals import *
from robot import Robot

# Add colors as needed.
GREEN_COLOR = pygame.Color(0, 255, 0)
BLACK_COLOR = pygame.Color(0, 0, 0)
WHITE_COLOR = pygame.Color(255, 255, 255)

if __name__ == "__main__":
    # Calls related to Q-learning.  
    robot = Robot(
        alpha=0.1, gamma=0.8, epsilon=1, min_epsilon=0.05, decay_rate=0.995
    )  # Create a new robot.
    robot.q_learning(epochs=1000)
    robot.get_best_path()

    # Result printing.
    print(f"Best Score: {robot.best_score}\nBest Path:" , end=" ")
    for state in robot.best_path:
        if state == (5, 0):
            print(state, end="")
        else:
            print(state, end=" -> ")

    pygame.init()
    fps_clock = pygame.time.Clock()

    play_surface = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Karaktersatt Oppgave 1 DTE2602')
    simulator_speed = 2  # Higher number == faster simulation.

    bg_image = pygame.image.load("grid.jpg")  # Loads simplified grid image.
    #bg_image = pygame.image.load("map.jpg")  # Loads terrain map image.

    # Visualize best path.
    running = True
    i = 0
    robot.y = 0
    robot.x = 3
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                break
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                    running = False
                    break

        play_surface.fill(WHITE_COLOR) # Fill the screen with white.
        play_surface.blit(bg_image, (0, 0)) # Render the background image.

        # Best path iteration
        if robot.has_reached_goal():
            pass
        else:
            robot.y = robot.best_path[i][0]
            robot.x = robot.best_path[i][1]
        i += 1

        # Render the robot over the image.
        pygame.draw.rect(
            play_surface, BLACK_COLOR,
            Rect(robot.x * 70 + 69,robot.y * 70 + 69, 22, 22)
        )  # A black outline around the robot.
        pygame.draw.rect(
            play_surface, GREEN_COLOR,
            Rect(robot.x * 70 + 70, robot.y * 70 + 70, 20, 20)
        )  # The robot is rendered in green.

        # Refresh the screen.
        pygame.display.flip()
        fps_clock.tick(simulator_speed)