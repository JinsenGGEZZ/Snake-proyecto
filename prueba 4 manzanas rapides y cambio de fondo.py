# -*- coding: utf-8 -*-
#importar
import pygame
import time
import os, pygame
import random


#funcion antes de inicializar juego para cargar imagenes
def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()
#iniciar pygame
pygame.init()
#al cargar icono del juego
icono = pygame.image.load("icon.ico")
pygame.display.set_icon(icono)


Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Morado = (255, 0, 255)
Azul = (0, 0, 255)
Verde = (0, 128, 0)
#VARIABLES TAMAÑO PANTALLA INICIO Y OBJETOS DENTRO
ancho = 920
altura = 700


superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('Serpiente')


background = load_image('29.jpg')

superficie.blit(background, [0, 0])

#para hacer mas simple el codigo
reloj = pygame.time.Clock()
#variable tamaño serpiente
serp_tamano = 20
#variable tiempo reloj
CPS = 10


#fondo letra y tamaño
font = pygame.font.SysFont("arial.ttf", 30)
      
#pausa
def pausa():
    pausado = True
   
    while pausado:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False

                elif event.key == pygame.K_x:
                    pygame.quit()
                    quit()
        background = load_image('25.jpg')
        superficie.blit(background, [0, 0])
        #superficie.fill(blanco)      
        message_to_screen("PAUSA", Blanco, -150)
        message_to_screen("-C- CONTINUAR   /   -X- SALIR ", Blanco, 200)
        pygame.display.update()
        reloj.tick(5)

#puntos
def puntos(score):
    text = font.render("PUNTAJE: "+str(score), True, Negro)
    superficie.blit(text, [0,0])
#rapidez
def rapidez(score):
    text = font.render("RAPIDEZ: "+str(score), True, Negro)
    superficie.blit(text, [0,30])      

#funcion introduccion pantalla inicio del juego mensajes etc
def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_x:
                    pygame.quit()
                    quit()

        background = load_image('FONDO jp-01.jpg')
        superficie.blit(background, [0, 0])
        message_to_screen("A JUGAR", Negro, -150)
        message_to_screen("OBJETIVO", Azul, -50)
        message_to_screen("USAR TECLAS DE DIRECCION PARA MOVERSE Y COMER MANZANAS", Azul, 0)
        message_to_screen("SI TOCAS EL BORDE O A TI MISMO PIERDES.", Negro, 50)
        message_to_screen("-P- PAUSA  / -C- CONTINUAR  / -X- TERMINAR Y SALIR DEL JUEGO.", Azul, 100)
        pygame.display.update()
        reloj.tick(15)

def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0],i[1],serp_tamano,serp_tamano])

def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()

#codigo video parametros msj y color/textsur textrect
def message_to_screen(msg, color, y_displace=0):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (ancho/2), (altura/2)+ y_displace
    superficie.blit(textSur, textRect)
    #pantalla_texto = font.render(msg, True, color)
    #superficie.blit(pantalla_texto,[display_ancho/2, display_altura/2])

 #gameloop para que se repitan variables   
    #siempre va al final
def gameLoop():
    gameExit = False
    gameOver = False

    mover_x = 300
    mover_y = 300

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1

    #manzanas tamaño
    #manzana roja
    azarManzanaX = round(random.randrange(0, 800 - 20)/20.0)*20.0
    azarManzanaY = round(random.randrange(0, 800 - 20)/20.0)*20.0
    #manzana verde
    azarManzana2X = round(random.randrange(0, 800 - 20)/20.0)*20.0
    azarManzana2Y = round(random.randrange(0, 800 - 20)/20.0)*20.0
    #manzana morada
    azarManzana3X = round(random.randrange(0, 800 - 20)/20.0)*20.0
    azarManzana3Y = round(random.randrange(0, 800 - 20)/20.0)*20.0

    #para llamar sonido dentr de gameloop crear variable pulsar_sonido
    pulsar_sonido = pygame.mixer.Sound("song.ogg")
    #set volume bajar y subir volumen dentro del parentesis
    pulsar_sonido.set_volume(0.50)
    #variable para definir cuantas veces se reproduce cancion
    pulsar_sonido.play(18)
    

    
    while not gameExit:

        while gameOver == True:


      
            ##superficie.fill(blanco)
            superficie.blit(background, [0, 0])
            pulsar_sonido.stop()
            message_to_screen("PERDISTE :C", Negro, -50)
            message_to_screen("-C- CONTINUA   /  -X- SALIR", Rojo, 50)
            pygame.display.update()
##ciclo for x salir(game exit) veradero o continuar (game over)= falso
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    


    #ciclo for serp controles
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover_x_cambio = -serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    mover_x_cambio = serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_UP:
                    mover_y_cambio = -serp_tamano
                    mover_x_cambio = 0
                elif event.key == pygame.K_DOWN:
                    mover_y_cambio = serp_tamano
                    mover_x_cambio = 0   
                elif event.key == pygame.K_p:
                    pulsar_sonido.set_volume(0.0)
                    pausa()
                    pulsar_sonido.set_volume(0.50)


                     
                
        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
            gameOver = True


        mover_x += mover_x_cambio
        mover_y += mover_y_cambio
        ##superficie.fill(blanco)
        superficie.blit(background, [0, 0])
        #tamaño dibujo manzana
        pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 20, 20])
        pygame.draw.rect(superficie, Verde, [azarManzana2X, azarManzana2Y, 20, 20])
        pygame.draw.rect(superficie, Morado, [azarManzana3X, azarManzana3Y, 20, 20])

        #se crea variable 
        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        
        #si la cola de la serpiente (lista) toca el cuerpo se pierde partida
        listaSerpiente.append(cabezaSerpiente)
        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        for eachSegment in listaSerpiente[:-1]:
            if eachSegment == cabezaSerpiente:
                gameOver = True
     
            
        
        serpiente(serp_tamano,listaSerpiente)
        puntos(largoSerpiente -1)
        rapidez (CPS)
        pygame.display.update()
         #llamar sonido manzana
        #manzana roja
       
        if mover_x == azarManzanaX and mover_y == azarManzanaY: 
            pygame.mixer.music.load("manzanaroja.ogg")
            azarManzanaX = round(random.randrange(0, 800-20)/20.0)*20.0
            azarManzanaY = round(random.randrange(0, 800-20)/20.0)*20.0
            largoSerpiente += 1
            
            #reproduce musica manzana roja
            pygame.mixer.music.play(0)
            
        #manzana verde
        if mover_x == azarManzana2X and mover_y == azarManzana2Y:
            pygame.mixer.music.load("manzanaverde.ogg")
            azarManzana2X = round(random.randrange(0, 800-20)/20.0)*20.0
            azarManzana2Y = round(random.randrange(0, 800-20)/20.0)*20.0
            largoSerpiente += 1
         
            

            #reproduce sonido verde
            pygame.mixer.music.play(0)

         #manzana morada   
        if mover_x == azarManzana3X and mover_y == azarManzana3Y  :
            pygame.mixer.music.load("manzanamorada.ogg")
            azarManzana3X = round(random.randrange(0, 800-20)/20.0)*20.0
            azarManzana3Y = round(random.randrange(0, 800-20)/20.0)*20.0
            largoSerpiente += 10
            
            
            
            

        #reproduce sonido morada
            pygame.mixer.music.play(0)
            
        reloj.tick(CPS)


    pygame.quit()
    quit()

intro_juego()
gameLoop()
