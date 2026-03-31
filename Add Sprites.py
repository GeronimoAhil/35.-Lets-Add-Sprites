import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

display_surface = pygame.display.set_mode((500, 400))
rect1_width = 50
rect1_height = 50
rect1_x = SCREEN_WIDTH // 2 - rect1_width // 2
rect1_y = SCREEN_HEIGHT // 2 - rect1_height // 2
player_rect = pygame.Rect(rect1_x, rect1_y, rect1_width, rect1_height)
rect_speed = 5

rect2_width = 50
rect2_height = 50
rect2_x = SCREEN_WIDTH // 2 - rect2_width // 3
rect2_y = SCREEN_HEIGHT // 2 - rect2_height // 3
player_rect = pygame.Rect(rect2_x, rect2_y, rect2_width, rect2_height)
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
    