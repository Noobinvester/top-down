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
   current_timer = int(pygame.time.get_ticks() // 1000 - start_time)
   current_time_surf = fps_font.render(f"Time: {current_timer}", True, (fps_color))
   current_time_surf_rect = current_time_surf.get_rect(topright=(SCREEN_WIDTH - 10, 10))
   screen.blit(current_time_surf, current_time_surf_rect)

start_time = 0

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


#enemy spawn timer
enemy_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_spawn_timer, 2000)  # Spawn enemy every 2 seconds

enemy_list_rect = []

def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            # Calculate if player is in safe zone
            player_center_x = player_x + player.get_width() / 2
            player_center_y = player_y + player.get_height() / 2
            distance = ((player_center_x - safe_zone_center[0])**2 + (player_center_y - safe_zone_center[1])**2)**0.5
            player_radius = max(player.get_width(), player.get_height()) / 2

            # Only move if player is NOT in safe zone
            if distance + player_radius >= safe_zone_radius:
                if player_x > enemy_rect.x:
                    enemy_rect.x += 1
                if player_x < enemy_rect.x:
                    enemy_rect.x -= 1
                if player_y > enemy_rect.y:
                    enemy_rect.y += 1
                if player_y < enemy_rect.y:
                    enemy_rect.y -= 1
        return enemy_list
    else:
        return []


# Scoreboard
score_font = pygame.font.Font(None, 36)
score_text = score_font.render(f"Score: {score}  Lives: {lives}  Enemies Killed: {enemy_killed}", True, (255, 255, 255))
#safe zone (drawn in game loop)
# GAME LOOP
while RUNNING:
    for event in pygame.event.get():
           #enemy spawn timer event
        if event.type == enemy_spawn_timer:
            spawn_x = random.randint(0, SCREEN_WIDTH - enemy.get_width())
            spawn_y = random.randint(0, SCREEN_HEIGHT - enemy.get_height())
            new_enemy = enemy.get_rect(topleft=(spawn_x, spawn_y))
            enemy_list_rect.append(new_enemy)
            
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
    # if player_x > enemy_x:
    #     enemy_x += enemy_velocity_x
    # if player_x < enemy_x:
    #     enemy_x -= enemy_velocity_x
    # if player_y > enemy_y:
    #     enemy_y += enemy_velocity_y
    # if player_y < enemy_y:
    #     enemy_y -= enemy_velocity_y
    # if enemy_x < 0 - enemy.get_width():

    enemy_list_rect = enemy_movement(enemy_list_rect)

    # Update player rect position for collision check
    player_rect.x = player_x
    player_rect.y = player_y

    # Check collision with all spawned enemies
    for enemy_rect in enemy_list_rect:
        if player_rect.colliderect(enemy_rect):
            lives -= 1
            enemy_list_rect.remove(enemy_rect)
            break

    score_text = score_font.render(f"Score: {score}  Lives: {lives}  Enemies Killed: {enemy_killed}", True, (255, 255, 255))
   
     #end screen logic
    if lives <= 0:
        RUNNING = False
    while lives <= 0:
        screen.fill((0, 0, 0))
        screen.blit(end_screen_text, end_screen_rect)
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_text, restart_rect)
        player_scaled = pygame.transform.rotozoom(player, 0, 5)
        player_end_x = screen.get_width() // 2 - player_scaled.get_width() // 2
        player_end_y = end_screen_rect.top - player_scaled.get_height() - 50
        screen.blit(player_scaled, (player_end_x, player_end_y))
        enemy_list_rect = []  # Clear all enemies
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
                start_time = int(pygame.time.get_ticks() // 1000)
            
    
    # Draw everything
    #fps
    fps_text = fps_font.render(f"FPS: {int(clock.get_fps())}", True, (fps_color))
    screen.blit(surface, (0, 0))
    # Draw safe zone circle
    pygame.draw.circle(surface, ('green'), safe_zone_center, safe_zone_radius)
    screen.blit(player, (player_x, player_y))
    # Draw all spawned enemies
    for enemy_rect in enemy_list_rect:
        screen.blit(enemy, (enemy_rect.x, enemy_rect.y))
    score_text = score_font.render(f"Score: {score}  Lives: {lives}  Enemies Killed: {enemy_killed}", True, (255, 255, 255))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 10))
    screen.blit(fps_text, (10, 10))
    display_time()
    
    
    pygame.display.update()
    clock.tick(FPS)
