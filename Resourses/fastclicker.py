import pygame
from time import time
from random import randint
pygame.init()
back = (80, 80, 255) 
window = pygame.display.set_mode(
   (1000, 500)
)
#negr = pygame.image.load("funny.jpeg")
window.fill(back)
clock = pygame.time.Clock()
class Area():
    def __init__(self, x,y,width,height,color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.colorf = color 
        self.set_text()
    def set_text(self, text=':)', fsize=35, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def paint(self):
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, (0,0,0), self.rect,3) 
    def drawe(self):
        self.paint()
        window.blit(self.image, (self.rect.x + 5, self.rect.y + 75))
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y) 
print('Белый - правильно\nЧёрный - неправильно')
rects = [Area(100,110,80,180,(255, 0, 0)), Area(250,110,80,180,(255, 123, 0)), Area(400,110,80,180,(255, 255, 0)), Area(550,110,80,180,(0, 255, 51)), Area(700,110,80,180,(80, 80, 255)), Area(850,110,80,180,(0, 0, 255)), Area(1000,110,80,180,(139, 0, 255))]
game = True
start = time()
start_time = time()

counter = 0

score = Area(50,55,40,90,(255, 0, 0))
score.set_text('Счёт:'+str(counter),35,(0,0,0))
timer = Area(1000,110,80,180,(139, 0, 255))
timer.set_text('Время:'+str(int(time()-start_time)),35,(0,0,0))

while game:
    #window.blit(negr,(randint(0,1000), randint(0,500)))
    clock.tick(240)
    if time() - start > 0.5:
        r = randint(0,len(rects))
        for i in range(len(rects)):
            rects[i].color = rects[i].colorf
            if i == r:
                rects[i].drawe()
            else:
                rects[i].paint()
        start = time()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            for i in range(len(rects)):
                if rects[i].collidepoint(x,y):
                    if r == i:
                        rects[i].color = (255, 255, 255)
                    else:
                        rects[i].color = (0, 0, 0)
                    rects[i].paint()
    if game:
        if counter >= 5: 
            win = pygame.font.SysFont('verdana', 35).render('WIN',True,(0,0,0))
            window.blit(win, (150,150))
            game = False
        if time() - start_time >= 10:
            lose = pygame.font.SysFont('verdana', 35).render('LOSE',True,(0,0,0))
            window.blit(lose, (150,150))
            game = False
        score.set_text('Счёт:'+str(counter),True,(0,0,0))
        timer.set_text('Время:'+str(time() - start_time),True,(0,0,0))
        score.drawe()
        timer.drawe()
    
    
    pygame.display.update()