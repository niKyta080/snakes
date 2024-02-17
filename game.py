
import pygame
from os import path
import time
import random
pygame.init()
WIDTH = 800
HEIGHT = 800
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
img_dir = path.join(path.dirname(__file__),'img')
music_dir = path.join(path.dirname(__file__),'music')
pygame.mixer.music.load(path.join(music_dir,'Intense.mp3'))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
am = pygame.mixer.Sound(path.join(music_dir, 'apple_bite.ogg'))
bg = pygame.image.load(path.join(img_dir, 'Grass.jpg')).convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_rect= bg.get_rect()
clock = pygame.time.Clock()
snake_speed = 15
font_style = pygame.font.SysFont(None, 32)
score_font = pygame.font.SysFont('comicsansms',25)
def score_for_snake(score):
    value = score_font.render('Ваш счёт:'+str(score),True, RED)
    screen.blit(value, [0, 0])
def message(msg, color):
    mes = font_style.render(msg, True, color)
    screen.blit(mes, [WIDTH/16, HEIGHT/2])
def new_block(snake_body):
    for x in snake_body:
        pygame.draw.rect(screen,BLACK,[x[0],x[1],10,10])
def game():
    x = 0
    y = 0
    xcor = WIDTH/2
    ycor = HEIGHT/2
    snake_body = []
    length = 1
    foodx = round(random.randrange(0,WIDTH -10)/10)*10
    foody = round(random.randrange(0,HEIGHT -10)/10)*10
    food_img = [pygame.image.load(path.join(img_dir,'f_1.png')).convert(),pygame.image.load(path.join(img_dir,'f_5.png')).convert(),pygame.image.load(path.join(img_dir,'banana.png')).convert(),pygame.image.load(path.join(img_dir,'lemon.png')).convert(),pygame.image.load(path.join(img_dir,'red-apple.png')).convert(),pygame.image.load(path.join(img_dir,'watermelon.png')).convert()]
    food = pygame.transform.scale(random.choice(food_img),(10,10))
    food.set_colorkey(WHITE)
    food_rect = food.get_rect(x = foodx, y = foody)
    run = True
    end = False
    while run:
        while end == True:
            screen.fill(BLUE)
            message("Tы проиграл! Нажми 'C' для продолжения или 'Q' для выхода",RED)
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        end = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -10
                    y = 0
                elif event.key == pygame.K_RIGHT:
                    x = 10
                    y = 0
                elif event.key == pygame.K_UP: 
                    y = -10 
                    x = 0 
                elif event.key == pygame.K_DOWN: 
                    y = 10
                    x = 0
        if xcor >= WIDTH or xcor < 0 or ycor >=HEIGHT or ycor < 0:
            end = True
        xcor+=x
        ycor+=y

        screen.fill(BLUE)
        screen.blit(bg,bg_rect)
        screen.blit(food,food_rect)
        #pygame.draw.rect(screen,BLUE,(xcor,ycor,10,10))
        snake_head = []
        snake_head.append(xcor)
        snake_head.append(ycor)
        snake_body.append(snake_head)
        if len(snake_body)>length:
            del snake_body[0]
        for z in snake_body[:-1]:
            if z == snake_head:
                end = True
        new_block(snake_body)
        score_for_snake(length-1)
        pygame.display.update()
        if xcor == foodx and ycor == foody:
            foodx = round(random.randrange(0,WIDTH -10)/10)*10 
            foody = round(random.randrange(0,HEIGHT -10)/10)*10
            food_img = [pygame.image.load(path.join(img_dir,'f_1.png')).convert(),pygame.image.load(path.join(img_dir,'f_5.png')).convert(),pygame.image.load(path.join(img_dir,'banana.png')).convert(),pygame.image.load(path.join(img_dir,'lemon.png')).convert(),pygame.image.load(path.join(img_dir,'red-apple.png')).convert(),pygame.image.load(path.join(img_dir,'watermelon.png')).convert()]
            food = pygame.transform.scale(random.choice(food_img),(10,10))
            food.set_colorkey(WHITE)
            food_rect = food.get_rect(x = foodx, y = foody)
            length += 1
            am.play()
        
        pygame.display.flip()
        clock.tick(snake_speed)
    #message("ТЫ ПРОИГРАЛ",RED)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
game()