import pygame

pygame.init()

# SCREEN
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60
RUNNING = True
clock = pygame.time.Clock()
# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TEST")
surface = pygame.Surface((SCREEN_WIDTH, SCREEN_WIDTH))
surface.fill('gray')
#player
player = pygame.image.load("assets/NinjaFrog/jump.png").convert_alpha()
player_x = (screen.get_width() - player.get_width()) // 2
player_y = (screen.get_width() - player.get_height()) // 2
velocity_x = 5
velocity_y = 5

#enemy
enemy = pygame.image.load("C:/Users/guiza/Desktop/project py/top down/assets/MainCharacters/MaskDude/jump.png").convert_alpha()
enemy_x = (screen.get_width() - enemy.get_width()) // 2 - 200
enemy_y = (screen.get_width() - enemy.get_height()) // 2 - 200
enemy_velocity_x = 1
enemy_velocity_y = 1
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    key = pygame.key.get_pressed()


    velocity_x = 0
    velocity_y = 0

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        velocity_x = -5
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        velocity_x = 5
    if key[pygame.K_UP] or key[pygame.K_w]:
        velocity_y = -5
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        velocity_y = 5
    if key[pygame.K_LSHIFT]:
        velocity_x *= 2
        velocity_y *= 2
    if key[pygame.K_SPACE]:
        pass
        
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player.get_width():
        player_x = SCREEN_WIDTH - player.get_width()
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - player.get_height():
        player_y = SCREEN_HEIGHT - player.get_height()
    if velocity_x != 0 and velocity_y != 0:  # If moving diagonally
        velocity_x *= 0.7
        velocity_y *= 0.7
    player_x += velocity_x
    player_y += velocity_y
    if player_x > enemy_x:
        enemy_x += enemy_velocity_x
    if player_x < enemy_x:
        enemy_x -= enemy_velocity_x
    if player_y > enemy_y:
        enemy_y += enemy_velocity_y
    if player_y < enemy_y:
        enemy_y -= enemy_velocity_y
    if enemy_x < 0 - enemy.get_width():
        enemy_x = SCREEN_WIDTH

    screen.blit(surface, (0, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    pygame.display.update()
    clock.tick(FPS)
