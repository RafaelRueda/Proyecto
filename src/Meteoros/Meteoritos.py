import pygame
import random
import sys


WIDTH = 800    
HEIGHT = 480
fondoPrincipal = pygame.image.load("Juegopython/Sprites/FondoMenu.jpg")
fondoJuego = pygame.image.load("Juegopython/Sprites/FondoJuego.jpg")

#Colores
Blanco = (255,255,255)
Rojo = (200,20,50)
Azul = (70,70,190)
Amarillo = (255,255,45)


class Recs(object):
    def __init__(self,numeroinicial):
        self.lista=[]
        for x in range(numeroinicial):
            #Creamos los rectangulos en random
            leftrandom=random.randrange(2,770)
            toprandom=random.randrange(-440,-10)
            width=random.randrange(10,30)
            height=random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))
    def reagregar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top>482:
                leftrandom=random.randrange(2,770)
                toprandom=random.randrange(-440,-10)
                width=random.randrange(10,20)
                height=random.randrange(10,25)
                self.lista[x]=(pygame.Rect(leftrandom,toprandom,width,height))
    def agregarotro(self):
        pass
    def mover(self):
        for rectangulo in self.lista:
            rectangulo.move_ip(0,5)
    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(200,0,0),rectangulo)

class Player(pygame.sprite.Sprite):
    def __init__(self):     
       
        #Movimiento normal
        self.imagenexplosion=pygame.image.load("Juegopython/Sprites/PNG/Sprite6.PNG").convert_alpha()
        self.imagen1=pygame.image.load("Juegopython/Sprites/PNG/Sprite3.PNG").convert_alpha()
        self.imagen2=pygame.image.load("Juegopython/Sprites/PNG/Sprite4.PNG").convert_alpha()
        self.imagenes=[self.imagen1,self.imagen2]
        self.imagenactual=0
        self.imagen=self.imagenes[self.imagenactual]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=280,0
        self.rect.height=50  #Altura
        self.rect.width=50   #Ancho
        #self.rect.left-=self.rect.width/2
        #self.rect.top-=self.rect.height/2
        self.estamoviendo=False
        self.choco=False
        
    def mover(self,vx,vy):
        
        self.rect.move_ip(vx,vy)
        
    def update(self,superficie,vx,vy,t):
        
        #Si choca
        if self.choco==True:
            self.imagenes=[self.imagenexplosion]
            self.imagen=self.imagenes[0]
            self.imagenactual=0
        
        if (vx,vy)==(0,0):self.estamoviendo=False
        else: 
            self.estamoviendo=True
        
            if t==1:
                self.imagenactual+=1
       
                if self.imagenactual>(len(self.imagenes)-1):
             
                    self.imagenactual=0    
            
          
        self.mover(vx,vy)
        self.imagen=self.imagenes[self.imagenactual]
        superficie.blit(self.imagen,self.rect)
        
        if self.estamoviendo==False:
            self.imagenactual=0
            self.imagen=self.imagenes[0]
              
def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
        
def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.mixer.music.load("Juegopython/Sonidos/SonidoFondo.mp3")
    pygame.mixer.music.play(2) 
    reloj1= pygame.time.Clock()
    reloj2= pygame.time.Clock()
    #Instancias de objetos:
    recs1=Recs(10)
    player1=Player()
    cursor1=Cursor()
    #Fondo de pantalla
    imagenfondo=pygame.image.load("Juegopython/Sprites/fondo3.jpg").convert_alpha()
    imagenBoton1=pygame.image.load("Juegopython/Sprites/PNG/start1.PNG").convert_alpha()
    imagenBoton2=pygame.image.load("Juegopython/Sprites/PNG/start2.PNG").convert_alpha()
    imagenBoton3=pygame.image.load("Juegopython/Sprites/PNG/exit1.PNG").convert_alpha()
    imagenBoton4=pygame.image.load("Juegopython/Sprites/PNG/exit2.PNG").convert_alpha()
    boton1=Boton(imagenBoton1,imagenBoton2,260,100)
    boton2=Boton(imagenBoton3,imagenBoton4,260,200)
    #Sonidos
    sonido1=pygame.mixer.Sound("juegopython\Sonidos\die1.wav")
    SegundosInt = 0
    flagCronometro = False
    Fuente1 = pygame.font.SysFont("Arial", 20, True, False)
    #variables aux
    #------------------------------------------------------------------------------------------
    colisiono=False
    vx,vy=0,0
    velocidad=15
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    t=0
    menuPrincipal=True
    salirMenuPrincipal=False
    salirJuego=False
    #------------------------------------------------------------------------------------------
    
    #---------------MENU PRINCIPAL---------------
    
    if menuPrincipal==True:
        while menuPrincipal==True and salirMenuPrincipal==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salirMenuPrincipal=True
                    salirJuego=True 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                        menuPrincipal=False
                        score_start = pygame.time.get_ticks()/1000
                    if cursor1.colliderect(boton2.rect):
                        menuPrincipal=False
                        salirMenuPrincipal=True
                        salirJuego=True
            pantalla.blit(fondoPrincipal,(0,0))
            pygame.display.set_caption("Seminario de Lenguajes") #Nombre de la ventana
            #pantalla.fill((0,0,0))
            cursor1.update()
            boton1.update(pantalla,cursor1)
            boton2.update(pantalla,cursor1)
            pygame.display.update()
            reloj2.tick(20)
        #pygame.quit()
    #pygame.init()
    
    #---------------JUEGO EN SI---------------
    while salirJuego!=True | salirMenuPrincipal!=False:#LOOP PRINCIPAL
        for event in pygame.event.get():
            #Para salir del juego
            if event.type == pygame.QUIT:
                salirJuego=True 
            #Movimientos
            if colisiono==False:    
                #Manteniendo la tecla apretada    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=True
                        vx=-velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=True
                        vx=velocidad
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy=-velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=True
                        vy=velocidad
                #Si suelto la tecla
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=velocidad
                        else:vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-velocidad
                        else:vx=0
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=velocidad
                        else:vy=-0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-velocidad
                        else:vy=0         
                  
            score = pygame.time.get_ticks()/1000 - score_start
        reloj1.tick(20)
        pygame.display.set_caption("Meteoro ") #Nombre de la ventana
        Info = Fuente1.render("Trata de esquivar los cuadrados",0,(255,255,255))
        pantalla.blit(fondoJuego,(0,0))
        pantalla.blit(Info,(5,5))
        t+=1
        if t>1:
            t=0
        if colision(player1,recs1):
            player1.choco=True
            colisiono=True
            vx=0
            vy=0
            sonido1.play()
        if menuPrincipal == False:
                
            if flagCronometro == False:
                SegundosInt = pygame.time.get_ticks()/1000
                Segundos =  str(score_start - SegundosInt)
                Cronometro = Fuente1.render(Segundos,0, Amarillo)
            else:
                Cronometro = Fuente1.render(
                                        Segundos+str,0, Amarillo)
        
        recs1.mover()
        recs1.pintar(pantalla)
        player1.update(pantalla,vx,vy,t)
        pantalla.blit(Cronometro,(450,5))
        pygame.display.update()
        
        recs1.reagregar()

    pygame.quit()
    
main()