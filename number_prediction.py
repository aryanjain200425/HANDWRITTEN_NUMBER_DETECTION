import os
import pygame
import sys
import tkinter as tk
import keras
from PIL import Image
from keras.datasets import mnist
import numpy as np



#Color variables
black = (0,0,0)
white = (255,255,255)



# inital variable
isDrawing = False

drawColor = black

width = 50

screenWidth, screenHeight = 700, 700




root = tk.Tk()
root.geometry("800x800")  # Set the size of the Tkinter window

embed = tk.Frame(root, width= screenWidth, height=screenHeight)  # Set the size of the embedded Pygame window
embed.pack(side=tk.LEFT)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())  # Pass the window ID to Pygame
os.environ['SDL_VIDEODRIVER'] = 'windib'  # Set the Pygame video driver to windib

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))  # Create a Pygame display surface within the embedded frame





def handle_events():
    
    global isDrawing, drawColor, width

    
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            
            pygame.quit()
            root.quit()


        if event.type == pygame.MOUSEBUTTONDOWN: #Drawing
            isDrawing = True
            drawColor = black
            width = 50

        if event.type == pygame.MOUSEBUTTONUP: #Stopped drawing
            isDrawing = False

        if event.type == pygame.MOUSEWHEEL:
            screen.fill(white)
            drawColor = black





def update_surface():
    
    global isDrawing, drawColor, width
    
    if isDrawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(surface=screen, color=drawColor, center=(mouse_x, mouse_y), radius=width)

    pygame.display.update()



def game_loop():
    pygame.event.pump()
    handle_events()
    update_surface()
    root.after(10, game_loop)  # Repeat the loop after a delay (in milliseconds)


def predictNum():
    pygame.image.save(screen,"predict_image.jpeg")

    model = keras.models.load_model("model.h5")

    image = Image.open("predict_image.jpeg")

    
    new_image = image.resize((28,28)).convert("L") #Resizing to 28X28 and converting to BW

    (_, _), (test_data, _) = mnist.load_data()

    inverted_image = Image.eval(new_image, lambda px: 255 - px)

    new_test_data = np.insert(test_data, 0, inverted_image, axis=0)

    predictions = model.predict(new_test_data)

    print(np.argmax(predictions[0]))





button = tk.Button(text="Predict", command=predictNum)

button.pack(side='left', fill="x", padx=10, pady=10)



game_loop()



root.mainloop()

