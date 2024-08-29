import pygame, sys
import random
import math
from pygame import mixer

# Initializing Pygame
pygame.init()
grey = (29, 29, 27)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("images/background.png")

# Background sound
mixer.music.load("images/music.ogg")
mixer.music.play(-1)

# Caption and icon
pygame.display.set_caption("<3 SPACE INVADERS <3")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load("images/rocket.png")
playerX = 370 
playerY = 480
playerX_change = 0

# Enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("images/alien.png"))
    enemyX.append(random.randint(0, 735)) # Updated to prevent enemy from spawning out of bounds
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletimg = pygame.image.load("images/bullet.png")
bulletX = 0 
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Start Menu text
start_font = pygame.font.Font("freesansbold.ttf", 64)

def showscore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text(x, y):
    over_text = over_font.render("<3GAME OVER<3", True, (255, 255, 255))
    screen.blit(over_text, (x, y))    
    
def player(x, y):
    screen.blit(playerimg, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))    

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + math.pow(enemyY - bulletY, 2))
    return distance < 27

def show_start_menu():
    menu_text = start_font.render("PRESS SPACE TO START", True, (255, 255, 255))
    screen.blit(menu_text, (10, 250))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

# Show start menu
show_start_menu()

# Game loop
while True:
    screen.fill(grey)
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # If keystroke is pressed, check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("images/laser.ogg")
                    bullet_sound.play()
                    # Getting the current coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)    
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(120, 250)
            break
        
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("images/explosion.ogg")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)   

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    showscore(textX, textY)
    pygame.display.update()
