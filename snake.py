import pygame,time,random
pygame.init()
Aqua =( 0, 255, 255)
Black= ( 0, 0, 0)
Blue =( 0, 0, 255)
Fuchsia= (255, 0, 255)
Gray= (128, 128, 128)
Green= ( 0, 128, 0)
Lime= ( 0, 255, 0)
Maroon= (128, 0, 0)
NavyBlue= ( 0, 0, 128)
Olive =(128, 128, 0)
Purple =(128, 0, 128)
Red= (255, 0, 0)
Silver =(192, 192, 192)
Teal =( 0, 128, 128)
White= (255, 255, 255)
Yellow =(255, 255, 0)
def message(msg,size,color,x,y):
    font=pygame.font.SysFont("bold",size)
    text=font.render(msg,1,color)
    textrect=text.get_rect()
    textrect.center=x,y
    screen.blit(text,textrect)
class Snake(pygame.sprite.Sprite):
    def __init__(self,x,y,screen,font):
        super().__init__()
        self.image=pygame.image.load('simg.png')
        self.image.set_colorkey(Black)
        self.image=pygame.transform.scale(self.image,[20,20])
        self.right_image=pygame.transform.rotate(self.image,90)
        self.left_image=pygame.transform.rotate(self.image,-90)
        self.down_image=pygame.transform.rotate(self.image,180)
        self.top_image=self.image
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x=self.x
        self.rect.y=self.y
        self.vx=0
        self.vy=0
        self.screen=screen
        self.font=font
 
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx=-5
            self.vy=0
            self.image=self.right_image
        elif keys[pygame.K_RIGHT]:
            self.vx=5
            self.vy=0
            self.image=self.left_image
        elif keys[pygame.K_UP]:
            self.vy=-5
            self.vx=0
            self.image=self.top_image
        elif keys[pygame.K_DOWN]:
            self.vy=5
            self.vx=0
            self.image=self.down_image
        self.rect.x+=self.vx
        self.rect.y+=self.vy
class Food(pygame.sprite.Sprite):
    def __init__(self,x,y,snake,font):
        super().__init__()
        self.i1=pygame.image.load("aimg.png")
        self.i1=pygame.transform.scale(self.i1,[40,40])
        self.i2=pygame.image.load("sbonus.png")
        self.i2=pygame.transform.scale(self.i2,[40,40])
        self.i3=pygame.image.load("sbonus1.png")
        self.i3=pygame.transform.scale(self.i3,[40,40])
        self.slist=[self.i1,self.i2,self.i3]
        self.a=random.choice(self.slist)
        self.image=self.a.convert_alpha()
        self.image=pygame.transform.scale(self.image,[40,40])
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.snake=snake
        self.score=0
        self.font=font
        self.count=0
    def eat_food(self):
        if snake.rect.x>self.rect.x and snake.rect.x<self.rect.x+30 or snake.rect.x+20>self.rect.x and snake.rect.x+20<self.rect.x+30 :
            if snake.rect.y>self.rect.y and snake.rect.y<self.rect.y+30 or snake.rect.y+20>self.rect.y and snake.rect.y+20<self.rect.y+30: 
                 return True
        return False
    def Score(self):
        
        message("Score:"+str(self.score),30,Blue,50,10)
    
    def update(self):
        
        if self.eat_food():
                self.rect.x=random.randint(30,370)
                self.rect.y=random.randint(30,370)
           
                    
                if self.a==self.slist[0]:
                
                    self.score+=1
                elif self.a==self.slist[1]:
                    self.score+=2
                elif self.a==self.slist[2]:
                    self.score+=3
def pause():
    paused=1
    while paused:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    paused=0
        screen.fill(White)
        message('Paused',80,Red,200,100)
        message('Press Space to Continue',40,Red,200,300)
        pygame.display.update()
def start():
    screen.fill(Gray)
    message("Snake Xenia",60,Red,200,100)
    message("Use Arrow Keys To Move",30,Red,200,270)
    s1=pygame.image.load("s1.png").convert_alpha()
    s2=pygame.image.load("s2.png").convert_alpha()
    wait=1
    ci=1
    while wait:
        clock.tick(5)
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        c=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 70+65>c[0]>70 and 320+40>c[1]>320:
             pygame.draw.rect(screen,Aqua,[70,320,65,40])
             if click[0]==1:
                wait=0
        else:
            pygame.draw.rect(screen,Blue,[70,320,65,40])
        message("Start",30,Red,100,340)
        if 270+60>c[0]>270 and 320+40>c[1]>320:
             pygame.draw.rect(screen,Aqua,[270,320,60,40])
             if click[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen,Blue,[270,320,60,40])
    
        message("Exit",30,Red,300,340)
        if ci==1:    
             screen.blit(s1,[150,150])
        if ci==2:    
             screen.blit(s2,[150,150])
        if ci==2:    
             ci=1
        else:
            ci+=1
        pygame.display.flip()
            
                
screen=pygame.display.set_mode([400,400])
pygame.display.set_caption("Snake Xenia")
clock=pygame.time.Clock()
font=pygame.font.SysFont('comicsansms',20)

running=True
intro =True
gover=False

while running:
    for event in pygame.event.get():
      
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                           pause() 
    if intro :
        start()
        
        intro=False
        all_sprites=pygame.sprite.Group()
        foods=pygame.sprite.Group()
        snake=Snake(200,200,screen,font)
        food=Food(100,100,snake,font)
        foods.add(food)
        all_sprites.add(food)
        all_sprites.add(snake)
    if  gover:
        gover=False
        all_sprites=pygame.sprite.Group()
        foods=pygame.sprite.Group()
        snake=Snake(200,200,screen,font)
        food=Food(100,100,snake,font)
        foods.add(food)
        all_sprites.add(food)
        all_sprites.add(snake)
       
    clock.tick(fps)
    all_sprites.update()
    
    
    screen.fill(White)
    if snake.rect.right>=400 or snake.rect.left<=0 or snake.rect.top<=0 or snake.rect.bottom>=400:
            screen.fill(White)
            message("GameOver",60,Red,200,200)
            message("Press Enter to Continue",40,Blue,200,300)
            snake.kill()
            food.kill()
            for event in pygame.event.get():
                    
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                             gover=True
    
   
    
    food.Score()
    
    all_sprites.draw(screen)
    
    pygame.display.flip()
pygame.quit()
quit()
