import pygame
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()

imgBg = pygame.image.load("../resources_game_dev/bg.jpeg").convert()
imgB = pygame.image.load('../resources_game_dev/balloon.png').convert_alpha()
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    window.fill((240, 143, 250))
    window.blit(imgBg,(0,0))
    window.blit(imgB,(200,200))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)