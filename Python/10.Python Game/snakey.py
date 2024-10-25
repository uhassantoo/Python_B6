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
green = pygame.Color(0,255,0)


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

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               change_to = 'UP'
           if event.key == pygame.K_DOWN:
               change_to = 'DOWN'
           if event.key == pygame.K_LEFT:
               change_to = 'LEFT'
           if event.key == pygame.K_RIGHT:
               change_to = 'RIGHT'
    #Validate direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
                
    # MOVE SNAKE
    if direction == 'UP':
        snake_pos[1] -=10
    if direction == 'DOWN':
        snake_pos[1] +=10
    if direction == 'LEFT':
        snake_pos[0] -=10
    if direction == 'RIGHT':
        snake_pos[0] +=10
        
    # Snake growing
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == eat_pos[0] and snake_pos[1] == eat_pos[1]:
        score += 10
        eat_spawn = False
    else:
      snake_body.pop()
      
    #new fruit to eat
    if not eat_spawn:
        eat_pos = [random.randrange(1, (window_x // 10 )) * 10,
                   random.randrange(1, (window_y // 10 )) * 10]
    eat_spawn = True
        
    #RENDER
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10 , 20))
    pygame.draw.rect(game_window, white, pygame.Rect(eat_pos[0], eat_pos[1], 10, 20 ))
    
    #Wall
    
    if (snake_pos[0]< 0 or snake_pos[0] > window_x - 10 or
        snake_pos[1] < 0 or snake_pos [1]> window_y - 10):
        end_game()
        
    for block in snake_body[1:]:
        if snake_pos[0] == block [0] and snake_pos[1] == block[1]:
            end_game()

    #Display the score
    pygame.display.update()
    fps.tick(snake_speed)
