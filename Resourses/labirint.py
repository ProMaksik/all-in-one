from pygame import *
winback = (20,20,80)
window = display.set_mode(
    (500,500)
)
#window.fill(winback)
display.set_caption("Bombandito Gusito")
class GameSprite(sprite.Sprite):
    def __init__(self, x,y,w,h,imag,speed):
        super().__init__()
        self.image = transform.scale(image.load(imag), (w,h))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.x = x
        self.y = y
        self.rect.y = y
        self.rect.x = x
        self.color = color
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,x,y,w,h,img,speed):
        super().__init__(x,y,w,h,img,speed)
    def movement1(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 480:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
        if len(sprite.spritecollide(self, groupowalls, False)) != 0:
            if keys[K_a] and self.rect.x > 5:
                self.rect.x += self.speed + 1
            if keys[K_d] and self.rect.x < 480:
                self.rect.x -= self.speed + 1
            if keys[K_w] and self.rect.y > 5:
                self.rect.y += self.speed + 1
            if keys[K_s] and self.rect.y < 480:
                self.rect.y -= self.speed + 1
    
class Bulitr(GameSprite):
    def update(self):
        self.reset()
        self.rect.x += self.speed
        if self.rect.x > 500:
            self.kill()
class Bulitl(GameSprite):
    def update(self):
        self.reset()
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()
class Bulitu(GameSprite):
    def update(self):
        self.reset()
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.kill()
class Bulitd(GameSprite):
    def update(self):
        self.reset()
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    

class Enemyx(GameSprite):
    def update(self):
        self.reset()
        self.rect.x += self.speed
        if self.rect.x < self.x - 70 or self.rect.x > self.x + 50:
            self.speed *= -1
class Enemyy(GameSprite):       
    def update(self):
        self.reset()
        self.rect.y += self.speed
        if self.rect.y < self.y - 150 or self.rect.y > self.y + 150:
            self.speed *= -1 
walls = [GameSprite(90,100,310,20, 'brickwall.jpg', 0), GameSprite(200,200,15,300, 'brickwall.jpg', 0), GameSprite(400,10,40,300, 'brickwall.jpg', 0),GameSprite(70,70,20,300, 'brickwall.jpg', 0)]
groupowalls = sprite.Group()
for wall in walls:
    groupowalls.add(wall)
player = Player(30,40,40,40,'ывфаыаыпафывыа.PNG', 5)
enemyx1 = Enemyx(300,300,40,40, "500.png", 2)
enemyx2 = Enemyx(70,400,40,40, "500.png", 1)
enemyx3 = Enemyx(350,400,40,40, "500.png", 6)
enemyy = Enemyy(150,300,40,40, "500.png", 4)
enemyy2 = Enemyy(250,300,40,40, "500.png", 3)
enemyy3 = Enemyy(450,350,40,40, "500.png", 5)
group = sprite.Group()
bullets = sprite.Group()

group.add(enemyx1)
group.add(enemyx2)
group.add(enemyx3)
group.add(enemyy)
group.add(enemyy2)
group.add(enemyy3)
#player2 = Player(40,40,40,40,'2.jpg', 6)
windows = GameSprite(490,10,30,30,'500.png',0)
game = True
finish = True
img  = transform.scale(image.load('Bombandito Gusito.jpeg'), (500,500))
winimg = GameSprite(450,20,35,35,'giraffe mafiosi.jpeg',0)
win = transform.scale(image.load('1488.jpeg'), (500,500))
lose = transform.scale(image.load('lose.jpeg'), (500,500))
clock = time.Clock()
while game:
    clock.tick(100)
    if finish:
        window.blit(img, (0,0))
        winimg.reset()
        player.reset()
        player.movement1() 
        group.update()
        bullets.update()

    if sprite.collide_rect(player,winimg):
        window.blit(win, (0,0))
        finish = False
    if len(sprite.spritecollide(player, group, False)) != 0:
        window.blit(lose, (0,0))
        finish = False
    #player2.reset()
    #player2.movement2()
    groupowalls.draw(window)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_RIGHT:
            bullets.add(Bulitr(player.rect.x + 17, player.rect.y + 17, 10,10, "kakashka.PNG", 25))
        if e.type == KEYDOWN and e.key == K_LEFT:
            bullets.add(Bulitl(player.rect.x + 17, player.rect.y + 17, 10,10, "kakashka.PNG", 25))
        if e.type == KEYDOWN and e.key == K_UP:
            bullets.add(Bulitd(player.rect.x + 17, player.rect.y + 17, 10,10, "kakashka.PNG", 25))
        if e.type == KEYDOWN and e.key == K_DOWN:
            bullets.add(Bulitu(player.rect.x + 17, player.rect.y + 17, 10,10, "kakashka.PNG", 25))
    display.update()        
    