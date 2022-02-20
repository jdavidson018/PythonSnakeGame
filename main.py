# Welcome to the wonderful world of programming

# Lines that start with '#' are comments. That means we can write anything we like on these lines and it will
# only be seen by future programmers.

# Below is the code to make the game snake. Throughout the code there will be comments starting with
#   P: {Instructions}
# These comments mean that there is a problem for you to solve or a spot where you can customize the game however you like.

# At the very bottom of the file, there are a few challenges to try and implement. See how many you are able to get.

from cgitb import text
from lib2to3.pgen2.pgen import generate_grammar
import time
import pygame
import random


def displayScore(score):
    mesg = score_style.render("Score: " + score, True, text_color)
    dis.blit(mesg, [10, 10])


def displayMessage(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [disp_width / 4, disp_height / 2])


def createRandomRect():
    return (
        random.randrange(0, round((disp_width / snake_dim))) * snake_dim,
        random.randrange(0, round((disp_height / snake_dim))) * snake_dim,
        snake_dim,
        snake_dim,
    )


def drawSnake(x, y, paused):
    if not paused:
        snake_list.append((x, y))

    if len(snake_list) - 1 > score:
        del snake_list[0]
    head = snake_list[len(snake_list) - 1]
    pygame.draw.rect(dis, head_color, [head[0], head[1], snake_dim, snake_dim])
    for block in snake_list[:-1]:
        pygame.draw.rect(dis, snake_color, [block[0], block[1], snake_dim, snake_dim])


def detectCollision(x, y):
    snake_head = snake_list[len(snake_list) - 1]
    for s in snake_list[:-1]:
        if s == snake_head:
            return True
    # End the game is you hit the boundary
    if x > disp_width - snake_dim or x < 0 or y > disp_height - snake_dim or y < 0:
        return True


# This initializes all of the important modules from pygame
pygame.init()

# Create the display the game will be played on
disp_width = 1000
disp_height = 800

# P: STEP 1: Pick a name for the game
game_name = "Snake Game Written by P & J"

# P: STEP 2: Pick out some of your favorite colors to represent the snake and it's food
snake_color = (0, 0, 255)
food_color = (0, 255, 0)
background_color = (255, 255, 255)
paused_background_color = (145, 145, 145)
text_color = (0, 0, 0)
head_color = (117, 255, 255)

# P: STEP 3: Pick where on the screen the snake will start
x = 400
y = 300

# P: STEP 4: Pick how big the Snake will be
snake_dim = 20

# P: STEP 4: Pick how fast the Snake will move
snake_speed = 8

# p: STEP 5: Pick what will show up when you lose the game
game_over_message = "You Lose: Better Luck Next Time"


# Other Variables needed to make the game work
game_over = False
paused = False
x_change = 0
y_change = 0
score = 0
font_style = pygame.font.SysFont(None, 50)
score_style = pygame.font.SysFont(None, 20)
food_rect = createRandomRect()
snake_list = [(x, y)]
clock = pygame.time.Clock()

dis = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption(game_name)


while not game_over:
    for event in pygame.event.get():
        # Handle all the possible actions that could be coming in
        # User clicks the red X to quick
        if event.type == pygame.QUIT:
            game_over = True

        # User Presses a key: Lets find out which key is it and react to it:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                paused = not paused
            if not paused:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    # Move the snake to the left
                    if len(snake_list) == 1 or x_change != snake_dim:
                        x_change = -snake_dim
                        y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # Move the snake to the right
                    if len(snake_list) == 1 or x_change != -snake_dim:
                        x_change = snake_dim
                        y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    # Move the snake up
                    if len(snake_list) == 1 or y_change != snake_dim:
                        x_change = 0
                        y_change = -snake_dim
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if len(snake_list) == 1 or y_change != -snake_dim:
                        x_change = 0
                        y_change = snake_dim
    if not paused:
        x += x_change
        y += y_change

    # Draw new food if you eat the current food
    if food_rect[0] == x and food_rect[1] == y:
        food_rect = createRandomRect()
        score += 1
        if score % 5 == 0:
            snake_speed += 3
    # Clear the snakes last location
    if paused:
        dis.fill(paused_background_color)
    else:
        dis.fill(background_color)

    # Draw the snake. (surface, color, rect=[x,y,w,h])
    drawSnake(x, y, paused)
    # End the game if any part of the snake is touching any other part
    game_over = detectCollision(x, y)
    pygame.draw.rect(dis, food_color, food_rect)
    displayScore(str(score))
    pygame.display.update()
    clock.tick(snake_speed)

displayMessage(game_over_message, text_color)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()

# Can you make the game restart when you hit the 'r' key?
# Can you make the snake change color when you hit the 'c' key?
# Can you disply options at the end of the game 'Try Again'?
# Can you make the snakes head a different color than its body?
# Can you make 2 snakes so it is a 2 player game?
# Can you make it so you aren't allowed to "Run over yourself"?
