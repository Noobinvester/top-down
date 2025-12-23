import pygame

pygame.init()
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('My First Game')
mouse = pygame.mouse.get_pos()
mouse_font = pygame.font.SysFont('bold', 20)
mouse_rect = mouse_font.render(f"Mouse: {mouse}", True, "black")
#fps
fps_on_screen_font = pygame.font.SysFont('Arial', 10)
fps_on_screen_font_rect = fps_on_screen_font.render(f"FPS: {int(clock.get_fps())}", True, ('black'))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)

    #mouse
    mouse = pygame.mouse.get_pos()
    mouse_rect = mouse_font.render(f"x: {mouse[0]}, y: {mouse[1]}", True, "black")
    #fps 
    fps_on_screen_font_rect = fps_on_screen_font.render(f"FPS: {int(clock.get_fps())}", True, ('black'))
#draw everything here
    screen.fill("gray")
    
    
    screen.blit(fps_on_screen_font_rect, (10, 10))
    screen.blit(mouse_rect, (10,(fps_on_screen_font_rect.get_height() + 10)))
    
    pygame.display.update()
pygame.quit()