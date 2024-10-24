import pygame
import time
import random

#Game Setting
snake_speed = 15
window_x = 720
window_y = 480

#Define colors
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
red = pygame.Color (255, 0, 0)
green = pygame.Color(0,128,0)


# Game Initialize
pygame.init()
game_window = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption('Snake Game')
fps = pygame.time.Clock()

#Snake & EAT
snake_pos = [100 , 50]
snake_body = [[100 , 50], [90,50], [80,50],[70,50]]
eat_pos = [random.randrange(1, (window_x//10))* 10,
           random.randrange(1 ,(window_y//10))* 10]
eat_spawn = True

# Set initial Direction and Score
direction = 'RIGHT'
change_to = direction
score = 0

#Function to display score
def display_score():
    score_font = pygame.font.SysFont('times new roman', 20)
    score_surface = score_font.render('Score: '+ str(score), True, white)
    game_window.blit(score_surface, (10 , 10))
    
# End game Function
def end_game():
    font = pygame.font.SysFont('times new roman',50)
    message_surface = font.render('Your Score:'+ str(score), True, red)
    message_rect = message_surface.get_rect()
    message_rect.midtop = (window_x /2, window_y /4)
    game_window.blit(message_surface, message_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()