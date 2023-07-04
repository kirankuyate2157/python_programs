import pygame
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()

imgBg = pygame.image.load("../resources_game_dev/bg.jpeg").convert()
imgB = pygame.image.load('../resources_game_dev/balloon.png').convert_alpha()
rectB = imgB.get_rect()
rectN = pygame.Rect(500,0,200,200)
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    print(rectB.colliderect(rectN))
    rectB.x += 5
    # rectN.y += 5

    window.fill((240, 143, 250))

    window.blit(imgBg,(0,0))
    # pygame.draw.rect(window, (0, 255, 0), rectB)
    pygame.draw.rect(window, (200, 255, 34), rectN)
    window.blit(imgB,rectB)


    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)