import pygame
import time
import random

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Snake properties
snake_block_size = 20
snake_speed = 15

# Snake body
def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_screen, black, [x[0], x[1], snake_block_size, snake_block_size])

# Game loop
def game_loop():
    game_over = False
    game_end = False

    # Initial position and movement of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    # Snake body list
    snake_list = []
    length_of_snake = 1

    # Generate random position for food
    food_x = round(random.randrange(0, screen_width - snake_block_size) / 20) * 20
    food_y = round(random.randrange(0, screen_height - snake_block_size) / 20) * 20

    # Main game loop
    while not game_over:
        while game_end:
            game_screen.fill(white)
            display_message("Oops! Press Q-Quit or C-Play Again", red)

            # Display score
            display_score(length_of_snake - 1)

            pygame.display.update()

            # Check for play again or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_end = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Control the snake movement using arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check for boundary collision
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_end = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        game_screen.fill(white)

        # Draw food
        pygame.draw.rect(game_screen, red, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Keep the snake length limited
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True

        # Display the snake
        snake(snake_block_size, snake_list)

        # Update screen
        pygame.display.update()

        # Check for food consumption
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block_size) / 20) * 20
            food_y = round(random.randrange(0, screen_height - snake_block_size) / 20) * 20
            length_of_snake += 1

        # Set game speed
        pygame.time.Clock().tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()


# Function to display messages on the screen
def display_message(message, color):
    font_style = pygame.font.SysFont(None, 50)
    message_render = font_style.render(message, True, color)
    game_screen.blit(message_render, [screen_width / 6, screen_height / 3])


# Function to display score
def display_score(score):
    font_style = pygame.font.SysFont(None, 30)
    value = font_style.render("Your Score: " + str(score), True, black)
    game_screen.blit(value, [0, 0])


# Start the game loop
game_loop()