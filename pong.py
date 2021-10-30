import sys
import pygame
import time

# Example #1
# from martin.engine.event import get
# some_result = get()
# print(some_result)

# Example #2
# from martin.engine import event
# some_result = event.get()
# print(some_result)

# Example #3
# from martin import engine
# some_result = engine.event.get()
# print(some_result)
"""
The main difference between pygame.display.flip and pygame.display.update is, that

display.flip() will update the contents of the entire display
display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
To tell PyGame which portions
"""
pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
SCREEN_CENTER_X = WINDOW_WIDTH / 2
SCREEN_CENTER_Y = WINDOW_HEIGHT / 2

screen: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
left_paddle_color = pygame.Color(33, 33, 11, 40)


RED = (255, 0, 0)
GOLDEN_ROD = (218, 165, 32)
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 80
BALL_SIZE = 50
BALL_SPEED_FACTOR = 20.53
ball_x = SCREEN_CENTER_X - (BALL_SIZE / 2)
ball_y = SCREEN_CENTER_Y - (BALL_SIZE / 2)
ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)
ball_color = (0, 0, 0)

pallet_x = 0
pallet_y = 0
ball_direction_x = 1
ball_direction_y = 1
ball_speed_x_axis = 3
ball_speed_y_axis = 7

while True:
    # Take input and handle events (keyboard/mouse)
    event_list = pygame.event.get()
    # print(event_list)
    for event in event_list:
        # if user clicks on "X"
        if event.type == pygame.QUIT:
            # what to do with with that event
            # sys.exit()
            pygame.quit()

    # Execute some game logic
    left_paddle = pygame.Rect(pallet_x, pallet_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    pallet_y += 1

    ball_x += ball_direction_x * ball_speed_x_axis * BALL_SPEED_FACTOR
    ball_y += ball_direction_y * ball_speed_y_axis * BALL_SPEED_FACTOR
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)

    # Check if ball touches wall on the right
    if ball_x >= WINDOW_WIDTH - BALL_SIZE:
        ball_direction_x = -1

    # Check if ball touches wall on the left
    if ball_x <= 0:
        ball_direction_x = 1

    # Check if ball touches wall on the bottom
    if ball_y >= WINDOW_HEIGHT - BALL_SIZE:
        ball_direction_y = -1
    
    # Check if ball touches wall on the top
    # TODO ball does not bounce when ball_speed is [-3, -7]
    # TODO we need to change sign and not hardcode it
    if ball_y <= 0:
        ball_direction_y = 1

    
    # Render objects to buffer
    screen.fill(GOLDEN_ROD)     
    pygame.draw.rect(screen, left_paddle_color, left_paddle)
    pygame.draw.rect(screen, ball_color, ball_rect)

    # Render to screen (update current frame)
    pygame.display.update()

    time.sleep(0.1)





