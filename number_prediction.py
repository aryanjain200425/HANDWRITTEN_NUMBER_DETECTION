import pygame
import sys

# inital screen setup
pygame.init()

screen = pygame.display.set_mode((800,800))

pygame.display.set_caption("AI Number Detection")



# inital variable
isDrawing = False

screen.fill((255,255,255))

drawColor = (0,0,0)

running = True

width = 50




while running:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a: #Drawing
                isDrawing = True
                drawColor = (0,0,0)
                width = 50

            if event.key == pygame.K_0: #Clear the screen
                screen.fill((255,255,255))
            
            if event.key == pygame.K_c: #Erasing
                isDrawing = True
                drawColor = (255,255,255)
                width = 34

        if event.type == pygame.KEYUP: #Stopped drawing
            if event.key == pygame.K_a or event.key == pygame.K_c:
                isDrawing = False


    if isDrawing:

        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(surface=screen, color=drawColor, center=(mouse_x, mouse_y), radius=width)

    pygame.display.update()




pygame.quit()
sys.exit()

