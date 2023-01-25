import pygame as py
import random as r

def draw_player(x):
    screen.blit(x, p_rect)
def draw_coin():
    screen.blit(coin, coin_rect)
def update_coin():
    coin_rect.centerx = r.randint(50,1000)
def draw_score():
    score_text = font.render(str(score), False, (255,255,255))
    score_text_rect = score_text.get_rect(center = (500,100))
    screen.blit(score_text, score_text_rect)


py.init()

width, height = 1000, 500
screen = py.display.set_mode((width, height))
py.display.set_caption('Side Scroller')
clock = py.time.Clock()

# Player

player_right = py.transform.scale(py.image.load('sprite_0.png').convert(), (50,50))
player_left = py.transform.scale(py.image.load('sprite_1.png').convert(), (50,50))
p_rect = player_right.get_rect(center = (500,285))
player_direction = True

movement = 0

# background

background = py.transform.scale(py.image.load('background.png').convert(), (1000,500))

# coin

coin = py.transform.scale(py.image.load('coin.png').convert(), (30,30))
coin_rect = coin.get_rect(center = (700, 275))

# text

font = py.font.Font('ARCADECLASSIC.TTF', 200)


# score

score = 0

while True:
    screen.blit(background, (0,0))
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                player_direction = True
                movement = 0
                movement += 5
            if event.key == py.K_LEFT:
                player_direction = False
                movement = 0
                movement -= 5
        if event.type == py.KEYUP:
            movement = 0

    if p_rect.centerx < coin_rect.centerx:
        movement = 0
        movement += 20
    else:
        movement = 0
        movement -= 20

    p_rect.centerx += movement
    
    if player_direction:
        draw_player(player_right)
    else:
        draw_player(player_left)

    if p_rect.colliderect(coin_rect):
        score += 1
        update_coin()
        
    draw_coin()
    draw_score()
    


    py.display.update()
    clock.tick(120)
