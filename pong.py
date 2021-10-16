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
screen: pygame.Surface = pygame.display.set_mode((400, 400))
left_paddle_color = pygame.Color(33, 33, 11, 40)
right_paddle_color = pygame.Color(33, 33, 255, 0)
right_paddle = pygame.Rect(200, 200, 75, 125)


RED = (255, 0, 0)
GOLDEN_ROD = (218, 165, 32)
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 80
BALL = pygame.Rect(200, 200, 15, 15)
ball_color = (0, 0, 0)

# pygame.display.update()
# pygame.draw.rect(screen, left_paddle_color, right_paddle)

# should_quit_now = False
x = 0
y = 0
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
    left_paddle = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    x += 0.1
    y += 1
    
    # Render objects to buffer
    screen.fill(GOLDEN_ROD)     
    pygame.draw.rect(screen, left_paddle_color, left_paddle)
    pygame.draw.rect(screen, right_paddle_color, right_paddle)
    pygame.draw.rect(screen, ball_color, BALL)
    # Render to screen (update current frame)
    pygame.display.update()

    time.sleep(0.1)





