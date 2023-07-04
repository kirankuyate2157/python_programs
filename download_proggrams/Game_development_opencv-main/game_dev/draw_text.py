import pygame
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    window.fill((240, 143, 250))
    font2 = pygame.font.Font(None, 100)
    font = pygame.font.Font('../resources_game_dev/Parisienne-Regular.ttf', 100)
    text2 = font2.render("My Awesome Game", True, (245,247,7))
    text = font.render("My Awesome Game", True, (149,7,247))
    window.blit(text2, (350, 400))
    window.blit(text, (350, 200))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)