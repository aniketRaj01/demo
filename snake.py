import pygame as py
import random
import math

py.init()

#defining colors for game

white = (255,255,255)

green = (0, 255, 0)

black = (0,0,0)

gameWindow = py.display.set_mode((800,800))

py.display.set_caption("Snake Game")

#vars

exit_game = False
snake_x = 100 #x coord of innitial snake(upper left corner)
snake_y = 130
snake_size = 10 #size of our snake (we are taking length and bredth as same)
clock = py.time.Clock()
fps = 40
velocity_x = 4
velocity_y = 4
food_x = random.randint(40, 700)
food_y = random.randint(40,700)
definer = 0
score = 0
sub_snakes=[]
wagon_x = 60
wagon_y = 60
length = 0
font = py.font.SysFont(None, 55)
def score_print(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


while not exit_game:
    store = score # to inc difficulty level
    gameWindow.fill(white) # making background white
    strn = f"score is "+str(score)
    py.draw.rect(gameWindow, black, [80, 80, 600, 600], 30)
    py.draw.rect(gameWindow, (255,0,0), [snake_x, snake_y, 20, 20])

    
    score_print(strn, (0,255,0), 10,10) 
    py.draw.rect(gameWindow, black, [food_x, food_y, 10, 10])


    for lists in sub_snakes:
        py.draw.rect(gameWindow, (255, 0, 0), [lists[0], lists[1], 25, 20]) 
   
    py.display.update()  # must run this after making any change in display
    #event handeling
    for event in py.event.get():
        if event.type == py.QUIT:
            exit_game = True
        if event.type == py.KEYDOWN:
            
            if event.key == py.K_RIGHT and not (definer==2):
                definer = 1
                
            if event.key == py.K_LEFT and not (definer==1):
                definer = 2
                
            if event.key == py.K_UP and not (definer==4):
                definer = 3
                
            if event.key == py.K_DOWN and not (definer==3):
                definer = 4
                

            

    if definer == 1:
        snake_x = snake_x + velocity_x
    if definer == 2:
        snake_x = snake_x - velocity_x
    if definer == 3:
        snake_y = snake_y - velocity_y
    if definer == 4:
        snake_y = snake_y + velocity_y


    wagon = []
    wagon.append(snake_x)
    wagon.append(snake_y)
    sub_snakes.append(wagon) # continuously creating the drawing


    if len(sub_snakes)>length:
        del sub_snakes[0]


    

    

    if math.sqrt((food_x-snake_x)**2+(food_y-snake_y)**2)<=16:
        food_x = random.randint(120, 650)
        food_y = random.randint(120,655)
        score+=1
        length+=1
    
    for i in range(len(sub_snakes)-1):
        if (sub_snakes[-1][0] == sub_snakes[i][0]) and (sub_snakes[-1][1] == sub_snakes[i][1]):
            exit_game = True
    
    if snake_x>=665 or snake_y>=665 or snake_x<=85 or snake_y<=90:
        exit_game = True



        
    
        
        

    

    
    clock.tick(fps)


py.quit()
quit()
