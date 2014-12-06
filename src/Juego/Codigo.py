import pygame
import random
import sys

#Modulos
#Constantes 
WIDTH = 800    
HEIGHT = 480
RelojPantalla = pygame.time.Clock()
Rectangulo1 = pygame.Rect(1,1,1,1)
aRomper = 5
#Colores
Blanco = (255,255,255)
Rojo = (200,20,50)
Azul = (70,70,190)
Amarillo = (255,255,45)
#Clases
# ----------------------------------------------------+
#Funciones
#_-------------------------------------------
def main():
    
    pygame.init() #Inicializa los modulos 
    #imagenAbeja = pygame.image.load("Abeja.gif")
    background = pygame.image.load("Sprites/FondoPantalla.png")
    GameOver = pygame.image.load("Sprites/GAMEOVER.png")
    Ganaste = pygame.image.load("Sprites/GANASTE.png")
    pygame.mixer.music.load("Music/MusicaFondo.mp3")
    
    SegundosInt = 0
    flagCronometro = False
    ContadorRectangulosRotos = 0
    Sonido1 = pygame.mixer.Sound("Music/flecha.wav")
    fuente1 = pygame.font.Font(None,48)
    Ventana = pygame.display.set_mode((WIDTH, HEIGHT))
    Fuente1 = pygame.font.SysFont("Arial", 20, True, False)
    Info = Fuente1.render("A matar los cuadrados en 10 segundos",0,(255,255,255))
    pygame.display.set_caption("Seminario de Lenguajes") #Cambio el titulo de la Ventana
    salir = False
    Rectangulo1 = pygame.Rect(0,0,10,10) #Definimos el rectangulo
    # lista para los rectanuglos
    listarec = []
    for x in range(aRomper):
        w=random.randrange(25,30)
        h=random.randrange(25,30)
        x=random.randrange(800)
        y=random.randrange(480
                           )
        listarec.append(pygame.Rect(x,y,w,h))
    pygame.mixer.music.play(2)   
    while salir != True:   #Loop Principal
        for event in pygame.event.get(): #Buscamos los eventos
            
            if event.type == pygame.QUIT:
                salir = True
            #Si hago click dentro de un rectangulo, desaparece
            if event.type == pygame.MOUSEBUTTONDOWN:
                    for recs in listarec:
                        if flagCronometro == False:
                            if Rectangulo1.colliderect(recs):
                                Sonido1.play()
                                recs.width = 0
                                recs.height = 0
                                ContadorRectangulosRotos += 1
        
            #Colision con otro rectangulo
            (previousx,previousy) = (Rectangulo1.left, Rectangulo1.top)
            (Rectangulo1.left, Rectangulo1.top) = pygame.mouse.get_pos()
            Rectangulo1.left -= Rectangulo1.width/2
            Rectangulo1.top -= Rectangulo1.height/2
               
        RelojPantalla.tick(50)  #Reloj a 20fps (frames por segundo)
        Ventana.fill(Azul)  #Pintamos la pantalla de Blanco
        Ventana.blit(background,(0,0)) #Fondo de pantalla
        pygame.draw.rect(Ventana,Amarillo,Rectangulo1)  #Dibujamos el cuadrado
        #Dibuja los rectangulos al azar
        for recs in listarec:
            pygame.draw.rect(Ventana,Rojo,recs)
        Ventana.blit(Info,(5,5))
    
        if SegundosInt >= 10 and aRomper != ContadorRectangulosRotos:
            flagCronometro = True
            Ventana.blit(GameOver,(200,200))
        if aRomper == ContadorRectangulosRotos:
            Ventana.blit(Ganaste,(200,200))
            flagCronometro = True
        if flagCronometro == False:
            SegundosInt = pygame.time.get_ticks()/1000
            Segundos =  str(SegundosInt)
            Cronometro = Fuente1.render(Segundos,0, Amarillo)
        else:
            Cronometro = Fuente1.render(
                                        Segundos+"   Rectangulos rotos "+str(ContadorRectangulosRotos),0, Amarillo)
        Ventana.blit(Cronometro,(450,5))
        pygame.display.update()
    pygame.quit()
    
main()
