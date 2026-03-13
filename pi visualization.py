
import pygame
import time
import numpy as np
#np.gcd()
TARGET = 6/((np.pi)**2)

#abcd = [2,2000,2,1000]
abcd = []
x = 1
pygame.font.init()
font = pygame.font.SysFont("Arial",20)
while len(abcd)<4:
    try:
        abcd.append(int(input(f"Input a integer greater than 1 ({x}/4): ")))
        if(abcd[x-1]<1):
            abcd.pop(x-1)
            raise Exception()
        x+=1
    except:
        print("Invalid value, try an integer greater than 1 (prefearbly >1000)")
if(abcd[0] > abcd[1]):
    abcd[1],abcd[0] = abcd[0:2]
if(abcd[2] > abcd[3]):
    abcd[3],abcd[2] = abcd[2:4]
x = []
y= []
color = []
coprime = 0
notcoprime = 0  
for i in range(abcd[0],1+abcd[1]):
    for j in range(abcd[2],1+abcd[3]):
        x.append(i)
        y.append(j)
        if(np.gcd(i,j) == 1):
            color.append((0,0,0,0.5))
            coprime+=1
        else:
            color.append((1,1,1,0.5))
            notcoprime+=1
pygame.init()
screen = pygame.display.set_mode((100,100),flags=pygame.RESIZABLE)
screen.fill((255,255,255))

def render():
    startDrawing = time.time()
    #screen.lock()
    for i in range(len(x)):
        screen.set_at([x[i],y[i]],(color[i][0]*255,color[i][1]*255,color[i][2]*255))
    #screen.unlock()
    #print(time.time()-startDrawing)
print(f"The ratio of coprime to not coprime is: {coprime/(coprime+notcoprime)}")
print(f"The target (6/pi^2) is {TARGET}")
print(f"The diffrence is {abs(TARGET-(coprime/(coprime+notcoprime)))}")
render()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            quit()
        elif event.type == pygame.WINDOWRESIZED:
            render()
            pygame.display.flip()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_SPACE):
                cursor = pygame.mouse.get_pos()
                toBlit = font.render(f"({cursor[0]},{cursor[1]},{color[cursor[0]]})",True,(0,0,0))
                render()
                screen.blit(toBlit,cursor)
                pygame.display.flip()