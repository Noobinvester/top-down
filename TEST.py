import pygame
import random
pygame.init()

# SCREEN
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60
RUNNING = True
clock = pygame.time.Clock()
# timer
def display_time():
    timer = pygame.time.get_ticks() // 1000
    
    return timer

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TEST")
surface = pygame.Surface((SCREEN_WIDTH, SCREEN_WIDTH))
surface.fill('gray')
#fps
fps_font = pygame.font.SysFont('bold', 36)
fps_color = "white"
fps_text = fps_font.render(f"FPS: {int(clock.get_fps())}", True,(fps_color))

#player
player = pygame.image.load("assets/NinjaFrog/jump.png").convert_alpha()
player_x = (screen.get_width() - player.get_width()) // 2
player_y = (screen.get_width() - player.get_height()) // 2
velocity_x = 5
velocity_y = 5
player_rect = player.get_rect()
# Safe zone center and radius
safe_zone_center = (100, 100)
safe_zone_radius = 100
#enemy
enemy = pygame.image.load("C:/Users/guiza/Desktop/project py/top down/assets/MainCharacters/MaskDude/jump.png").convert_alpha()
enemy_x = (screen.get_width() - enemy.get_width()) // 2 - 200
enemy_y = (screen.get_width() - enemy.get_height()) // 2 - 200
enemy_velocity_x = 1
enemy_velocity_y = 1
enemy_rect = enemy.get_rect()
#SCOREBOARD
score = 0
lives = 3
enemy_killed = 0
# end screen
end_screen_font = pygame.font.Font(None, 72)
end_screen_text = end_screen_font.render("Game Over", True, (255, 255, 255))
end_screen_rect = end_screen_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
restart_text = end_screen_font.render("Press Space to Restart", True, (255, 255, 255))
restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))

# Scoreboard
score_font = pygame.font.Font(None, 36)
score_text = score_font.render(f"Score: {score}  Lives: {lives}  Enemies Killed: {enemy_killed}", True, (255, 255, 255))
#safe zone (drawn in game loop)
# GAME LOOP
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    key = pygame.key.get_pressed()

    print(display_time())
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

    # Update rect positions before collision check
    player_rect.x = player_x
    player_rect.y = player_y
    enemy_rect.x = enemy_x
    enemy_rect.y = enemy_y
    if player_rect.colliderect(enemy_rect):
        lives -= 1
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy.get_width())
        enemy_y = random.randint(0, SCREEN_HEIGHT - enemy.get_height())
    score_text = score_font.render(f"Score: {score}  Lives: {lives}  Enemies Killed: {enemy_killed}", True, (255, 255, 255))
#safe zone (drawn in game loop)
    #safe zone logic - check if player is FULLY inside circle
    # Calculate player center point
    player_center_x = player_x + player.get_width() / 2
    player_center_y = player_y + player.get_height() / 2

    # Calculate distance from player center to safe zone center
    distance = ((player_center_x - safe_zone_center[0])**2 + (player_center_y - safe_zone_center[1])**2)**0.5

    # Player is fully inside if distance + player "radius" < safe zone radius
    # Using max dimension of player as diameter, so radius is half of that
    player_radius = max(player.get_width(), player.get_height()) / 2

    if distance + player_radius < safe_zone_radius:
        enemy_velocity_x = 0
        enemy_velocity_y = 0
    else:
        enemy_velocity_x = 1
        enemy_velocity_y = 1
   
     #end screen logic
    if lives <= 0:
        RUNNING = False
    while lives <= 0:
        screen.fill((0, 0, 0))
        screen.blit(end_screen_text, end_screen_rect)
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_text, restart_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                RUNNING = True
                lives = 3
                score = 0
                enemy_killed = 0
                enemy_x = random.randint(0, SCREEN_WIDTH - enemy.get_width())
                enemy_y = random.randint(0, SCREEN_HEIGHT - enemy.get_height())
            
    
    # Draw everything
    #fps
    fps_text = fps_font.render(f"FPS: {int(clock.get_fps())}", True, (fps_color))
    screen.blit(surface, (0, 0))
    # Draw safe zone circle
    pygame.draw.circle(surface, ('green'), safe_zone_center, safe_zone_radius)
    screen.blit(player, (player_x, player_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    score_text = score_font.render(f"Score: {score}  Lives: {lives}  Enemies Killed: {enemy_killed}", True, (255, 255, 255))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 10))
    screen.blit(fps_text, (10, 10))
    
    
    pygame.display.update()
    clock.tick(FPS)
