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

screen=pygame.display.set_mode([400,400])
pygame.display.set_caption("Snake Xenia")
clock=pygame.time.Clock()
font=pygame.font.SysFont('comicsansms',20)
class Snake(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load('simg.png').convert_alpha()
        self.image=pygame.transform.scale(self.image,[20,20])
        self.right_image=pygame.transform.rotate(self.image,90)
        self.left_image=pygame.transform.rotate(self.image,-90)
        self.down_image=pygame.transform.rotate(self.image,180)
        self.top_image=self.image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vx=0
        self.vy=0
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
        if self.rect.right>=400:
            self.rect.right=400
        if self.rect.left<=0:
            self.rect.left=0
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=400:
            self.rect.bottom=400
class Food(pygame.sprite.Sprite):
    def __init__(self,x,y,snake,font):
        super().__init__()
        self.image=pygame.image.load("aimg.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,[30,30])
##        self.image.fill(Red)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.snake=snake
        self.score=0
        self.font=font
    def eat_food(self):
        if snake.rect.x>self.rect.x and snake.rect.x<self.rect.x+30 or snake.rect.x+20>self.rect.x and snake.rect.x+20<self.rect.x+30 :
            if snake.rect.y>self.rect.y and snake.rect.y<self.rect.y+30 or snake.rect.y+20>self.rect.y and snake.rect.y+20<self.rect.y+30: 
                 return True
        return False
    def Score(self):
        s=self.font.render("Score:"+str(self.score),True,Maroon)
        screen.blit(s,[0,0])
        
    def update(self):
        
        if self.eat_food():
            self.rect.x=random.randint(30,370)
            self.rect.y=random.randint(30,370)
            
            self.score+=1
            
        
        
        
all_sprites=pygame.sprite.Group()
foods=pygame.sprite.Group()
snake=Snake(200,200)
food=Food(100,100,snake,font)
foods.add(food)
all_sprites.add(food)
all_sprites.add(snake)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    clock.tick(60)
    all_sprites.update()
    screen.fill(White)
    all_sprites.draw(screen)
    food.Score()
    pygame.display.flip()
pygame.quit()
quit()

        
