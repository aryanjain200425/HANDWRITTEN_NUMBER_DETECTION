import os
import pygame
import sys
import tkinter as tk
from pygame.locals import *


#Color variables

black = (0,0,0)
white = (255,255,255)



# inital variable
isDrawing = False

drawColor = black

width = 50



root = tk.Tk()
root.geometry("800x600")  # Set the size of the Tkinter window

embed = tk.Frame(root, width=700, height=500)  # Set the size of the embedded Pygame window
embed.pack(side=tk.LEFT)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())  # Pass the window ID to Pygame
os.environ['SDL_VIDEODRIVER'] = 'windib'  # Set the Pygame video driver to windib

screen = pygame.display.set_mode((700, 500))  # Create a Pygame display surface within the embedded frame

screen.fill((255,255,255))


def handle_events():
    global isDrawing, drawColor, width

    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            root.quit()

        

        if event.type == pygame.KEYDOWN:

            print("DOWN DETECT")
            
            if event.key == pygame.K_a: #Drawing
                print("HIHI")
                isDrawing = True
                drawColor = black
                width = 50

            if event.key == pygame.K_0: #Clear the screen
                screen.fill((255,255,255))
            
            if event.key == pygame.K_c: #Erasing
                isDrawing = True
                drawColor = white
                width = 34

        if event.type == pygame.KEYUP: #Stopped drawing
            if event.key == pygame.K_a or event.key == pygame.K_c:
                isDrawing = False




def update_surface():
    global isDrawing, drawColor, width
    if isDrawing:
        print("NONON")
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.draw.circle(surface=screen, color=white, center=(mouse_x, mouse_y), radius=width)

    pygame.display.update()



def game_loop():
    handle_events()
    update_surface()
    root.after(10, game_loop)  # Repeat the loop after a delay (in milliseconds)

game_loop()


root.mainloop()

