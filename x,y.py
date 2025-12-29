import pygame
pygame.init()
width,height=640,470
screen= pygame.display.set_mode((width,height))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            print(f"{x},{y}")                                    