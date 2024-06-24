import pygame
import random
import math

# Initialize the pygame
pygame.init()
width = 960
height = 540
level = 1
if width + height < 2000:
    speed = level / 1.25
else:
    speed = level
# Create the screen
screen = pygame.display.set_mode((width, height))

# Background

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (width, height))

# Title and Icon
pygame.display.set_caption("Space Invader by @SZ")
icon = pygame.image.load("battleship.png")
pygame.display.set_icon(icon)

# Player
player_speed = speed
player_1 = pygame.image.load("player1.png")
player_1 = pygame.transform.scale(player_1, (int(width / 20), int(width / 20)))
player_1_X = random.randint(int(width / 2), int(width - 64))
player_1_Y = height - height / 6
player_1_dX = 0
player_1_dY = 0

player_2 = pygame.image.load("player2.png")
player_2 = pygame.transform.scale(player_2, (int(width / 20), int(width / 20)))
player_2_X = random.randint(1, int(width / 2))
player_2_Y = height - height / 6
player_2_dX = player_1_dX
player_2_dY = player_1_dY

# Weapon
weapon_1 = []
weapon_X = []
weapon_Y = []
weapon_dX = []
weapon_dY = []
num_weapon = 3
bullet_state = "ready"
for j in range(num_weapon):
    weapon_1.append(pygame.image.load("bullets.png"))
    weapon_1[j] = pygame.transform.scale(weapon_1[j], (int(width / 40), int(width / 40)))
    weapon_X.append(player_1_X + 15)
    weapon_Y.append(player_1_Y + 25)
    weapon_dX.append(player_1_dX)
    weapon_dY.append(2)


# Enemy
enemy_1 = []
enemy_X = []
enemy_Y = []
enemy_dX = []
enemy_dY = []
num_enemies = 6
hit = False
score = 0
for i in range(num_enemies):
    enemy_1.append(pygame.image.load("ufo.png"))
    enemy_1[i] = pygame.transform.scale(enemy_1[i], (int(width / 20), int(width / 20)))
    enemy_X.append(random.randint(1, int(width - 64)))
    enemy_Y.append(random.randint(1, int(height / 5)))
    enemy_dX.append(speed - speed / 3)
    enemy_dY.append(int(height / 18))

# Explosion
explosion_1 = pygame.image.load("blast.png")
explosion_1 = pygame.transform.scale(explosion_1, (int(width / 40), int(width / 40)))


def player1(x, y):
    screen.blit(player_1, (x, y))


def player2(x, y):
    screen.blit(player_2, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_1[i], (x, y))


def weapon(x, y, j):
    global bullet_state
    bullet_state = "fire"
    screen.blit(weapon_1[j], (x, y))


'''def weapon_2(x, y):
    screen.blit(weapon_c, (x, y))'''


def collision(enemy_X, enemy_Y, weapon_X, weapon_Y):
    D = math.sqrt(pow(enemy_X - weapon_X, 2) + pow(enemy_Y - weapon_Y, 2))
    if D < (int(width / 20)):
        return True
    else:
        return False


def explosion(x, y):
    screen.blit(explosion_1, (x, y))


# Game loop
running = True
Player1 = True
Player2 = False
while running:
    # RGB = Red, Green, Blue
    screen.fill((192, 192, 192))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            pass
        # keystrokes
        if event.type == pygame.KEYDOWN:
            if Player1:
                if event.key == pygame.K_LEFT:
                    player_1_dX = -player_speed
                elif event.key == pygame.K_RIGHT:
                    player_1_dX = player_speed
                elif event.key == pygame.K_UP:
                    player_1_dY = -player_speed
                elif event.key == pygame.K_DOWN:
                    player_1_dY = player_speed
                elif event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        '''bullet_count += 1'''
                        weapon_1_X = player_1_X + 15
                        weapon_1_Y = player_1_Y + 25
                        '''weapon_c_X = player_2_X + 15
                        weapon_c_Y = player_2_Y + 25'''
                        weapon(weapon_X[j], weapon_Y[j], j)
                        '''weapon_2(weapon_c_X, weapon_c_Y)'''

            if Player2:
                if event.key == pygame.K_a:
                    player_2_dX = -player_speed
                elif event.key == pygame.K_d:
                    player_2_dX = player_speed
                elif event.key == pygame.K_w:
                    player_2_dY = -player_speed
                elif event.key == pygame.K_s:
                    player_2_dY = player_speed
        if event.type == pygame.KEYUP:
            if Player1:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_1_dX = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_1_dY = 0
            if Player2:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player_2_dX = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    player_2_dY = 0

    # 5 = 5 + -0.1 -> 4.5
    # 5 = 5  + 0.1

    # Player Boundary
    if Player1:
        player_1_X += player_1_dX
        if player_1_X <= 1:
            player_1_X = 1
        elif player_1_X >= int(width - width / 20):
            player_1_X = int(width - width / 20)

        player_1_Y += player_1_dY
        if player_1_Y <= int(height / 4):
            player_1_Y = int(height / 4)
        elif player_1_Y >= int(height - width / 20):
            player_1_Y = int(height - width / 20)

    if Player2:
        player_2_X += player_2_dX
        if player_2_X <= 1:
            player_2_X = 1
        elif player_2_X >= int(width - width / 20):
            player_2_X = int(width - width / 20)

        player_2_Y += player_2_dY
        if player_2_Y <= int(height / 4):
            player_2_Y = int(height / 4)
        elif player_2_Y >= int(height - width / 20):
            player_2_Y = int(height - width / 20)

    # Enemy Boundary
    for i in range(num_enemies):
        enemy_X[i] += enemy_dX[i]

        if enemy_X[i] <= 1:
            enemy_dX[i] = speed - speed / 3
            enemy_Y[i] += enemy_dY[i]
        elif enemy_X[i] >= int(width - width / 20):
            enemy_Y[i] += enemy_dY[i]
            enemy_dX[i] = -(speed - speed / 3)

        # Collision
        Col_ = collision(enemy_X[i], enemy_Y[i], weapon_X[j], weapon_Y[j])
        if Col_:
            weapon_X[j] = player_1_X + 15
            weapon_Y[j] = player_1_Y + 25
            bullet_state = "ready"
            hit = True
            new = True
            explosion(enemy_X[i], enemy_Y[i])
            explosion_1_X = enemy_X[i]
            explosion_1_Y = enemy_Y[i]
            enemy_X[i] = random.randint(1, int(width - width / 20))
            enemy_Y[i] = random.randint(1, int(height / 5))
            score += 1

        enemy(enemy_X[i], enemy_Y[i], i)


    # Bullet Movement
    if weapon_Y[j] <= 1:
        weapon_X[j] = player_1_X + 15
        weapon_Y[j] = player_1_Y + 25
        bullet_state = "ready"
    '''if weapon_c_Y <= 1:
        weapon_c_X = player_2_X + 15
        weapon_c_Y = player_2_Y + 25
        bullet_state = "ready"'''
    if bullet_state == "fire":
        weapon(weapon_X[j], weapon_Y[j], j)
        '''weapon_2(weapon_c_X, weapon_c_Y)'''
        weapon_Y[j] -= weapon_dY[j]
        '''weapon_c_Y -= weapon_c_dY'''

    if Player1:
        player1(player_1_X, player_1_Y)
    if Player2:
        player2(player_2_X, player_2_Y)
    if hit:
        explosion(explosion_1_X, explosion_1_Y)

    pygame.display.update()
