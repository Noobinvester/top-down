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
pygame.display.set_caption("TOP DOWN")


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        
        # Load sprite sheet (Ensure you have this file: "assets/NinjaFrog/jump.png")
        # If the file causes an error, replace the path with a simple placeholder like 'None' 
        # until you can fix the file path or use a built-in Pygame surface.
        try:
            self.image = pygame.image.load("assets/NinjaFrog/jump.png").convert_alpha()
        except pygame.error:
            # Fallback if image loading fails
            print("Warning: Could not load player image. Using a colored surface.")
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((255, 0, 0)) # Red square
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        # Update position based on velocity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Optional: Keep the player within the screen boundaries
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    def handle_input(self, keys):
        # Reset velocity to 0 before checking keys
        self.velocity_x = 0
        self.velocity_y = 0
        
        # --- Horizontal movement ---
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.speed
        
        # --- Vertical movement (THIS WAS MISSING) ---
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity_y = -self.speed # Negative Y moves up
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity_y = self.speed # Positive Y moves down

        # Optional: Normalize diagonal movement. If both x and y are set,
        # the player moves faster diagonally. To fix, you'd use vector math,
        # but for learning, keeping it simple is fine for now.

# Instantiate player
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # Spawn in the center

# --- Main Game Loop ---
while RUNNING:
    # 1. EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # 2. INPUT & UPDATE
    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    player.update() # <--- THIS WAS MISSING from the main loop
    
    # 3. DRAWING
    screen.fill('gray') # Changed to gray for better contrast
    
    player.draw(screen)

    # 4. FINALIZING
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()