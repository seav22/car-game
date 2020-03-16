'''Juego de carritos
Juego por Sebatian Avendano'''


#importo librerias
import pygame
import time
import random

pygame.init()

#cargar canciones
crash_sound = pygame.mixer.Sound("oof.wav")
pygame.mixer.music.load("oof-sports.wav")
pygame.mixer.music.play(-1)

#Size de la pantalla alto y ancho
width=800
height=600

#codigos RGB de colores que usare
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

#Pausar
pause = True

#creamos la ventana de juego
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Juego e' Carritos")
clock = pygame.time.Clock()

#size carro para borde
car_width = 55

#cargo imagenes que usare
carImage = pygame.image.load("carro.png")
backgroundImage = pygame.image.load("fondo.png")
truckImage = pygame.image.load("truck.png")
pygame.display.set_icon(carImage)


#contador puntaje
def trucks_dodged(count):
    font = pygame.font.SysFont(None,45)
    text = font.render("Puntos: "+str(count),True, black)
    gameDisplay.blit(text,(0,0))

#funcion para que se vea el carro
def car(x,y):
    gameDisplay.blit(carImage,(x,y))

#funcion para que se vea el fondo
def background(x,y):
    gameDisplay.blit(backgroundImage,(0,0))

#funcion para que se vea el camion
def truck(x,y):
    gameDisplay.blit(truckImage,(x,y))


#esta funcion renderiza el texto e identifica los limites del cuadro de texto
def text_objects(text,font):
    textSurface=font.render(text, True, white)
    return textSurface, textSurface.get_rect()

#esta funcion imprime texto cuando te sales de la via o chocas
def message_display(text,size):
    gameDisplay.fill(black)
    largeText = pygame.font.Font("ka1.ttf",size)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

#esto es lo pasa al chocar
def crash(msg):

    #para la musica y suena el choque
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #muestra el mensaje de choque del juego
        message_display(msg,40)
        
        #Llamado a funcion boton que genera botones
        button("Echarle Pichon",150,450,250,50,green,bright_green,game_loop)
        button("Salir",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(30)


def button(msg,x,y,w,h,ic,ac,action=None):
    #detectar posicion y clicks del mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #colorear cuadros mas brillantes al pasar por ellos
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("ka1.ttf",20)
    TextSurf, TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #muestra en pantalla titulo del juego
        gameDisplay.fill(black)
        largeText = pygame.font.Font("ka1.ttf",50)
        TextSurf, TextRect = text_objects("Juego e' Carritos",largeText)
        TextRect.center = ((width/2), int(height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        #Llamado a funcion boton que genera botones
        button("Dale!",150,450,100,50,green,bright_green,game_loop)
        button("Salir",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(30)


def unpause():
    
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #menu de pausa
        gameDisplay.fill(black)
        largeText = pygame.font.Font("ka1.ttf",50)
        TextSurf, TextRect = text_objects("Achantalo",largeText)
        TextRect.center = ((width/2),(height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        #Llamado a funcion boton que genera botones
        button("Dale Pues",150,450,150,50,green,bright_green,unpause)
        button("Salir",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(30)

      
#funcion de loop    
def game_loop():
    
    global pause

    pygame.mixer.music.play(-1)

    #dimensiones de carro
    x = (width*0.45)
    y = (height*0.8)

    #dimesiones de fondo
    x1 = width
    y1 = height

    #Variable que determina posicion de carrito en pantalla
    x_change = 0

    #camion
    truck_speed = 5
    truck_startx = random.randrange(150,500)
    truck_starty = -600
    truck_width = 50
    truck_height = 105

    #contador
    dodged = 0

    #Variable para terminar loop cuando choque
    gameExit = False

    #loop de juego
    while not gameExit:

        #Para cerrar juego con la X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            #Add funciones de teclas para mover carrito y pausar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        #Para actualizar posicion de carrito en cada frame            
        x += x_change
                    
        #mostrar el fondo de pantalla y carro
        background(x1,y1)
        truck(truck_startx,truck_starty)
        truck_starty += truck_speed
        car (x,y)
        trucks_dodged(dodged)
        
        #rango de colision en x
        if x>width-car_width-170 or x<170:
            crash("Te saliste mano que gafo!")

        #reinicio de posicion de camiones para respawn 
        if truck_starty > height:
            truck_starty = 0-150
            truck_startx = random.randrange(150,500)
            dodged += 1
            truck_speed += 1

        #rango de colision con camiones
        if y<truck_starty+truck_height:
            if x+car_width>truck_startx and x<truck_startx+truck_width:
                crash("Rolo e' choque mano!")
            
 
        #esto actualiza los frames
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
