import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background_color = 'gray'
clock = pygame.time.Clock()
FPS = 60




player = pygame.image.load("assets/NinjaFrog/jump.png").convert_alpha()
player_speed = 5
player_x = (screen.get_width() - player.get_width()) // 2
player_y = (screen.get_height() + player.get_height())
floor = (screen.get_height)
gravity = 1
jump = -20
y_velocity = 0



RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            RUNNING = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
       player_x += player_speed
    # if keys[pygame.K_UP] or keys[pygame.K_w]:
    #     player_y -= player_speed
    # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    #     player_y += player_speed
    if keys[pygame.K_SPACE]:
        player_y -= jump
    

   

    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player.get_width():
        player_x = SCREEN_WIDTH - player.get_width()
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - player.get_height():
        player_y = SCREEN_HEIGHT - player.get_height()
    clock.tick(FPS)

    # Game logic and rendering code would go here
    screen.fill(background_color)
    screen.blit(player, (player_x, player_y))



    pygame.display.flip()