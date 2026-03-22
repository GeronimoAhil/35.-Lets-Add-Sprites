import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

display_surface = pygame.display.set_mode((500, 400))
rect_width = 50
rect_height = 50
rect_x = SCREEN_WIDTH // 2 - rect_width // 2
rect_y = SCREEN_HEIGHT // 2 - rect_height // 2
player_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
rect_speed = 5
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= rect_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += rect_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += rect_speed
    if keys[pygame.K_UP]:
        player_rect.y -= rect_speed
        pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
pygame.quit()
    