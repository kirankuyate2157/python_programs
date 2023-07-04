import pygame
import cv2
import numpy as np
pygame.init()
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")
fps = 30
clock = pygame.time.Clock()
cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    success,img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgRGB = cv2.resize(imgRGB,(1280,720))
    imgRGB = np.rot90(imgRGB)

    imgF = pygame.surfarray.make_surface(imgRGB).convert()
    # imgF = pygame.transform.flip(imgF,True,False)
    window.blit(imgF,(0,0))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)