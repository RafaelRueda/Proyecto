import pygame
import random


class Recs(object):
    def __init__(self,numeroinicial):
        self.lista=[]
        for x in range(numeroinicial):
            #Crear un rec random
            leftrandom=random.randrange(2,560)
            toprandom=random.randrange(-580,-10)
            width=random.randrange(10,30)
            height=random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))
    def reagregar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top>482:
                leftrandom=random.randrange(2,560)
                toprandom=random.randrange(-580,-10)
                width=random.randrange(10,30)
                height=random.randrange(15,30)
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
        
        #Si choca
        
        
        #MOvimiento normal
        
        self.imagenexplosion=pygame.image.load("Juegopython/Sprites/PNG/Sprite6.PNG").convert_alpha()
        self.imagen1=pygame.image.load("Juegopython/Sprites/PNG/Sprite3.PNG").convert_alpha()
        self.imagen2=pygame.image.load("Juegopython/Sprites/PNG/Sprite4.PNG").convert_alpha()
        self.imagenes=[self.imagen1,self.imagen2]
        self.imagenactual=0
        self.imagen=self.imagenes[self.imagenactual]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=280,0
        self.rect.height=100  #Altura
        self.rect.width=100   #Ancho
        #self.rect.left-=self.rect.width/2
        #self.rect.top-=self.rect.height/2
        self.estamoviendo=False
        self.choco=False
        
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie,vx,vy,t):
        
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
            
def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((640,480))
    salir=False
    reloj1= pygame.time.Clock()
    
    recs1=Recs(10)
    player1=Player()
    imagenfondo=pygame.image.load("Juegopython/Sprites/fondo3.jpg").convert_alpha()
    
    
    sonido1=pygame.mixer.Sound("C:\Users\userpc\desktop\juegopython\Sonidos\pounw.wav")
    
    
    
    #variables aux
    colisiono=False
    vx,vy=0,0
    velocidad=15
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    t=0
    
    
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True 
            if colisiono==False:        
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
            
        reloj1.tick(20) #Cuento el tiempo a si se mueve el tipo
        t+=1
        if t>1:
            t=0
        
        if colision(player1,recs1):
            player1.choco=True
            colisiono=True
            vx=0
            vy=0
            #sonido1.play()
        
       
        recs1.mover()
        pantalla.blit(imagenfondo,(0,0))
        recs1.pintar(pantalla)
       
        player1.update(pantalla,vx,vy,t)
        
        
            
        
        pygame.display.update()
        
        recs1.reagregar()
        
               
        
       
    pygame.quit()
    
main()