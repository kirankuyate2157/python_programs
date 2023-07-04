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
    yellow,pink,green = (253,235,8),(253,8,200),(58,223,117)
    pygame.draw.polygon(window,yellow,((491, 100), (788, 100), (937, 357),(788, 614), (491, 614), (342, 357)))
    pygame.draw.circle(window, green, (640, 360), 200)
    pygame.draw.line(window, pink, (468, 392), (812, 392), 10)
    pygame.draw.rect(window, pink, (468, 307, 345, 70), border_radius=5)


    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)