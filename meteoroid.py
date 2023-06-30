
import pygame , time , random
#---------
pygame.init()

crash_sound = pygame.mixer.Sound("./public/lose-m.wav")
pygame.mixer.music.load("./public/world-m.ogg")

display_width = 800
display_height = 600

bg = pygame.image.load('./public/bg.png')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


display = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption('./public/Meteoroid v-1.6.9')
icon = pygame.image.load('./public/icon1.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


space_craft = pygame.image.load('./public/space_craft.png')
craft_width = 48
meteor_obj = pygame.image.load('./public/meteor.png')

    
def button(msg,x,y,w,h,inac,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(display , ac , (x,y,w,h))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display , inac , (x,y,w,h))
        if click[0] == True and action != None:
            if action == "play":
                game_loop()
            elif action == "Quit":
                pygame.quit()
                
            
    button_text = pygame.font.Font("./public/FreeSansBold.ttf" , 20)
    textsurf , textrect =  text_object(msg , button_text)
    textrect.center = ((x + (w/2)) , (y + (h/2)))
    display.blit(textsurf , textrect)

def start():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largetext = pygame.font.SysFont(None , 60)
        textsurf , textrect = text_object("lets go explore space!" , largetext)
        textrect.center = ((display_width/2),(150))
        display.blit(bg, (0, 0))
        display.blit(textsurf , textrect)


        button("GO!" , 150 , 450 , 100 , 50 , (250,100,100) , (100,250,0) , "play")
        button("Quit" , 550 , 450 , 100 , 50 , (100,250,100) , (200,50,0) , "Quit")


        pygame.display.update()


def score(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("dodged meteors:" +str(count) , True , (100,100,255))
    display.blit(text , (0,0))

def meteor(meteorx , meteory , meteorw , meteorh):
    display.blit(meteor_obj , [meteorx,meteory,meteorw,meteorh])

def craft(x,y):
    display.blit(space_craft , (x,y))

def text_object(text , font):
    textsurface = font.render(text , True , red)
    return textsurface , textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf' , 60)
    textsurf , textrect = text_object(text , largetext)
    textrect.center = ((display_width/2),(display_height/2))
    display.blit(textsurf , textrect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    largetext = pygame.font.Font('freesansbold.ttf' , 60)
    textsurf , textrect = text_object("space craft exploded!" , largetext)
    textrect.center = ((display_width/2),(display_height/2))
    display.blit(textsurf , textrect)

    while 1:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
               pygame.quit()
               quit()
        button("try again:)" , 150 , 450 , 100 , 50 , (250,100,100) , (100,250,0) , "play")
        button("back" , 550 , 450 , 100 , 50 , (100,250,100) , (200,50,0) , "Quit")

        pygame.display.update()

    

def game_loop():

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_ch = 0

    meteor_sx = random.randrange(0,display_width)
    meteor_sy = -600
    meteor_speed = 7
    meteor_width = 100
    meteor_height = 100

    score_count = 0

    game_exit = False

    while not game_exit:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
               pygame.quit()
            
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    x_ch = -5
                elif events.key == pygame.K_RIGHT:
                    x_ch = 5

            if events.type == pygame.KEYUP:
                if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                    x_ch = 0

        x += x_ch

        display.blit(bg, (0, 0))
        
        meteor(meteor_sx , meteor_sy , meteor_width , meteor_height)
        meteor_sy += meteor_speed
        
        score(score_count)

        craft(x,y)     
        if x > display_width - craft_width or x < 0:
            crash()
        
        if meteor_sy > display_height:
            meteor_sy = 0 - meteor_height
            meteor_sx = random.randrange(0 , display_width)
            score_count += 1
            
            if (score_count % 7 == 0 ):
                meteor_speed += 1

        
        if y < meteor_sy + meteor_height:
            if x > meteor_sx and x < meteor_sx + meteor_height or x + craft_width > meteor_sx and x + craft_width < meteor_sx + meteor_width:
                crash()


        pygame.display.update()
        clock.tick(60)
    
   
start()
game_loop()
pygame.quit()
quit() 
