import numpy as np
import pandas as pd
import pygame
import random
import sys
import time

pygame.init()

#setting up form
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
Display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Welcome')
clock = pygame.time.Clock()
crashed = False

#making colors
BLACK = (0, 0, 0)
GREEN = (0,195,0)
GREY = (170,170,170)
LIGHT_BLACK = (150,150,150)
LIGHT_GREEN =  (0,235,0)
LIGHT_RED = (255,0,0)
ORCHID = (218,112,214)
RED =  (205,0,0)
TEAL = (0,128,128)
WHITE = (255, 255, 255)

#global variables
counter = 1
x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.8)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
temp = 0
returned = 0
counterone = 0
countertwo = 1
score = 0
guessed_label = ""
clear = False
random_number = 0
info  = False

#loading images
paper_img = pygame.image.load('assets/img/mixed_paper.gif')
stem_img = pygame.image.load('assets/img/stem.png')
green_arrow_img = pygame.image.load("assets/img/Green_Arrows.png")
dark_green_arrow_img = pygame.image.load("assets/img/Dark_Green_Arrows.png")
products_img = pygame.image.load("assets/img/products2.PNG")
conveyor_img = pygame.image.load("assets/img/Conveyor.png")
conveyor_img_2 = pygame.image.load("assets/img/Conveyor2.png")
strands_img = pygame.image.load("assets/img/Strands.png")
filter_img = pygame.image.load("assets/img/Filter.PNG")
filter_block_img = pygame.image.load("assets/img/FilterBlock.PNG")
icon_img = pygame.image.load("assets/img/icon.png")
flames_img = pygame.image.load("assets/img/flames.PNG")
shredding_img = pygame.image.load("assets/img/Shredding.PNG")
rotate_img_1 = pygame.image.load("assets/img/Rotat1.PNG")
rotate_img_2 = pygame.image.load("assets/img/Rotat2.PNG")
rotate_img_3 = pygame.image.load("assets/img/Rotat3.PNG")
rotate_img_4 = pygame.image.load("assets/img/Rotat4.PNG")
deink_img_1 = pygame.image.load("assets/img/Deink1.PNG")
deink_img_2 = pygame.image.load("assets/img/Deink2.PNG")
deink_img_3 = pygame.image.load("assets/img/Deink3.PNG")
deink_img_4 = pygame.image.load("assets/img/Deink4.PNG")
line_img = pygame.image.load("assets/img/line.PNG")
pulp_img= pygame.image.load("assets/img/pulp.PNG")
vat_img = pygame.image.load("assets/img/Vat.PNG")
water_filter_img = pygame.image.load("assets/img/waterfilter.PNG")
bleached_pulp_img = pygame.image.load("assets/img/bleachedpulp.PNG")
bleach_block_img = pygame.image.load("assets/img/bleachblock.PNG")
spray_img_1= pygame.image.load("assets/img/Spray1.PNG")
spray_img_2= pygame.image.load("assets/img/Spray2.PNG")
spray_img_3= pygame.image.load("assets/img/Spray3PNG.PNG")
spray_img_4= pygame.image.load("assets/img/Spray4.PNG")
spray_img_5= pygame.image.load("assets/img/Spray5.PNG")
spray_img_6= pygame.image.load("assets/img/Spray6.PNG")
spray_img_7= pygame.image.load("assets/img/Spray7.PNG")
spray_img_8= pygame.image.load("assets/img/Spray8.PNG")
spray_img_9= pygame.image.load("assets/img/Spray9.PNG")
spray_img_10 = pygame.image.load("assets/img/Spray10.PNG")
roller_img_1 = pygame.image.load("assets/img/Roller1.PNG")
roller_img_2 = pygame.image.load("assets/img/Roller2.PNG")
final_paper_img = pygame.image.load("assets/img/FinalPaper.jpg")

pygame.display.set_icon(icon_img)

#class for conveyor objects
class GameItems:
    def __init__(self,name,directory,classification):
        self.name = name
        self.directory = directory
        self.classification = classification
        
    #function capable of displaying images given the self argument, and the object's attributes 
    def display(self,x,y):
        Display.blit(pygame.image.load(self.directory),(x,y))
        

        
        
        
banana = GameItems("banana","assets/img/banana.png","Landfill")
newspaper = GameItems("newspaper","assets/img/newspaper.png","Mixed")
carton =  GameItems("carton", "assets/img/Carton.png", "Mixed")
bottle = GameItems("bottle","assets/img/bottle.png","Plastics")
boxes = GameItems("Cardboard Box", "assets/img/boxes.png","Mixed")

object_list = [banana,newspaper,carton,bottle,boxes]

# class for page descriptions
class Pages:
    def __init__(self,name,description):
        
        self.name = name
        self.description = description
        
        
    def displaytext(self):
        message_display(self.description,400,75,'assets/font/TIMESBD.ttf',20)

page1 = Pages("page1","The intro page")
page2 = Pages("page2","This page is a game-like format of the waster sorting step.")
page3 = Pages("page3","This page demonstrates the paper being shREDded, then heated, and finally filteRED")
page4 = Pages("page4","The pulp is being cleaned extensively by spinning in a centrifuge.")
page5 = Pages("page5","The pulp is deinked, and ink, glue, and residue of adhesives are chemically separated")
page6= Pages("page6","This page shows the processs of paper pulp being rinsed with water")
page7 = Pages("page7","This page shows bleaching of the pulp, resulting in a WHITE color")
page8 = Pages("page8","This page shows paper pulp being sprayed on metal sheets, serving as a platform for the paper")
page9 = Pages("page9","This page shows the rolling out of paper, draining excess water and bonding paper pulp together")
page10 = Pages("page10","The Conclusion Page.")
page_list = [page1,page2,page3,page4,page5,page6,page7,page8,page9,page10]



'''
all functions
'''

#functions that each display different images
def paper(x, y):
    Display.blit(paper_img, (x, y) )
def stem(x, y):
    Display.blit(stem_img, (x, y))
def arrow(x,y):
    Display.blit(green_arrow_img,(x,y))
def arrow2(x,y):
    Display.blit(dark_green_arrow_img,(x,y))
def products(x,y):
    Display.blit(products_img,(x,y)) 
def conveyor(x,y):
    Display.blit(conveyor_img,(x,y))
def conveyor2(x,y):
    Display.blit(conveyor_img_2,(x,y))
def shredder(x,y):
    Display.blit(shredding_img,(x,y))
def Strands(x,y):
    Display.blit(strands_img,(x,y))
def flames(x,y):
    Display.blit(flames_img,(x,y))
def Filter(x,y):
    Display.blit(filter_img,(x,y))
def FilterBlock(x,y):
    Display.blit(filter_block_img,(x,y))
def line(x,y):
    Display.blit(line_img,(x,y))
def pulp(x, y):
    Display.blit(pulp_img, (x, y))
def Vat(x, y):
    Display.blit(vat_img, (x, y))
def WaterFilter(x, y):
    Display.blit(water_filter_img, (x, y))
def bleachedpulp(x, y):
    Display.blit(bleached_pulp_img, (x, y))
def bleachblock(x,y):
    Display.blit(bleach_block_img,(x,y))
def Roller1(x,y):
    Display.blit(roller_img_1,(x,y))
def Roller2(x,y):
    Display.blit(roller_img_2,(x,y))
def FinalPaper(x,y):
    Display.blit(final_paper_img,(x,y))
def Rotat(number,x,y):
    if number == 1:
        Display.blit(rotate_img_1,(x,y))

    if number == 2:
        Display.blit(rotate_img_2,(x-2,y-4))

    if number == 3:
        Display.blit(rotate_img_3,(x+4,y-2))

    if number == 4:
        Display.blit(rotate_img_4,(x-2,y+2))
        
def Deink(number,x,y):
    if number == 1:
        Display.blit(deink_img_1,(x,y))

    if number == 2:
        Display.blit(deink_img_2,(x-2,y-4))

    if number == 3:
        Display.blit(deink_img_3,(x-5,y))

    if number == 4:
        Display.blit(deink_img_4,(x-6,y-2))
        
def Spray(number,x,y):
    if number == 1:
        Display.blit(spray_img_1,(x,y))
    if number == 2:
        Display.blit(spray_img_2,(x,y+1))
    if number == 3:
        Display.blit(spray_img_3,(x-3,y))
    if number == 4:
        Display.blit(spray_img_4,(x-6,y-2))
    if number == 5:
        Display.blit(spray_img_5,(x-26,y-2))
    if number == 6:
        Display.blit(spray_img_6,(x-6,y-2))
    if number == 7:
        Display.blit(spray_img_7,(x-6,y-2))
    if number == 8:
        Display.blit(spray_img_8,(x-6,y-2))
    if number == 9:
        Display.blit(spray_img_9,(x-6,y-2))
    if number == 10:
        Display.blit(spray_img_10,(x-6,y-2))
    
    
    
    
    
#displays message in (parameter 1) in specific coordinate (paramater 2 and 3) 
def message_display(text,x,y,font,size):
    largeText = pygame.font.Font(font,size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    Display.blit(TextSurf, TextRect)
    pygame.display.update()
    

#function that alerts during when object exceeds boubdaries
def boundar():
    message_display('You Crashed',400,400,'assets/font/PAPYRUS.ttf',115)
    
#function that helps with message displaying
def text_objects(text,font):
    TextSurface = font.render(text,True,BLACK)
    return TextSurface, TextSurface.get_rect()

    
#animation logic for each and every page
def page():
    
    global x
    global x1
    global x2
    global y
    global y1
    global y2
    global counter
    global returned
    global counterone
    global countertwo
    global clear
    global random_number
    global guessed_label
    global score
    
    if info == True:
        
        if back() == False:
            
            Display.fill(WHITE)
            back()
            page_list[counter-1].displaytext()
        else:
            pass
        
        
        pygame.display.update()
        
    else:
        
        if counter == 1: 
            counterone += 1

            if counterone == 25:
                counterone -=25
                countertwo += 1

            if countertwo > 2:
                countertwo = 1

            returned = 0       
            Display.fill(WHITE)
            returned = buttons()
            stem(70,160)


            if countertwo == 1:
                arrow(-100,-25)
            if countertwo == 2:
                arrow2(-100,-25)

            message_display("Welcome to the Recycling Stream of Mixed Paper!",400,75,'assets/font/TIMESBD.ttf',37)


            pygame.display.update()

            
            
            if returned == 1:
                clear =True
            if returned == -1:
                returned = 0
                
            counter += returned
            pygame.display.update()

        


        elif counter == 2: 
            if clear == True:
                Display.fill(WHITE)
                clear = False
                random_number = random.randint(0,4)
                x = 0 
                y = 109
                y2 = 0 
                points = 0


            returned = 0 

            returned = buttons()



            y+= y2

            if y<150 and y >80:
                x += 1.5
            if x > 475:
                x = 475

            points = 0
            if x>20 and x < 110:
                if y>275:
                    guessed_label = "Landfill"

                    if object_list[random_number].classification == guessed_label:
                        clear = True
                        score += 1
                    else:
                        message_display("Sorry, incorrect. The correct classification is " + object_list[random_number].classification+ ". " + "restarting in 5 seconds",400,550, "assets/font/PlayfairDisplay-Black.otf",15)
                        time.sleep(5)
                        clear = True
                        gameloop()

            elif x>111 and x<235:
                if y>275:
                    guessed_label = "Mixed"
                    if object_list[random_number].classification == guessed_label:
                        clear = True
                        score += 1
                    else:
                        message_display("Sorry, incorrect. The correct classification is " + object_list[random_number].classification+ ". " + "restarting in 5 seconds",400,550, "assets/font/PlayfairDisplay-Black.otf",15)
                        time.sleep(5)
                        clear = True
                        gameloop()

            elif x > 234 and x < 400:
                if y>275:
                    guessed_label = "Plastics"
                    if object_list[random_number].classification == guessed_label:
                        clear = True
                        score += 1
                    else:
                        message_display("Sorry, incorrect. The correct classification is " + object_list[random_number].classification+ ". " + "restarting in 5 seconds",400,550, "assets/font/PlayfairDisplay-Black.otf",15)
                        time.sleep(5)
                        clear = True
                        gameloop()

            else: 
                pass

            conveyor(-50,100)
            object_list[random_number].display(x,y)
            message_display("Conveyor Game",400,75,'assets/font/PlayfairDisplay-Regular.otf',37)
            message_display("Current Object: " + object_list[random_number].name,660,175,'assets/font/PlayfairDisplay-Regular.otf',19)
            pygame.display.update()
            message_display("Score: " + str(score),600,275,'assets/font/PlayfairDisplay-Regular.otf',27)





            pygame.display.update()

            pygame.display.update()
            if returned == 1:
                counterone = -1
                x = 0
                y = 200
                clear = True
            counter += returned


        elif counter == 3:

            if clear == True:
                counterone += 1
                clear = False
                Display.fill(WHITE)
            conveyor2(-150,100)


            returned = buttons()
            paper_objects = []
            for objects in object_list:
                if objects.classification == "Mixed":
                    paper_objects.append(objects)

            if counterone == len(paper_objects):
                counterone = 0

            if y > 175 and y <275:
                x += 2


            if x<50: 
                paper_objects[counterone].display(x,y)


            elif x > 50 and x < 550:
                Strands(x,y-10)

            if x > 550:

                Filter(x,y-15)
                
            if x> 550 and x<700:
                FilterBlock(550,175)

            if x>350 and x<600:
                flames(350,295)
                message_display("Heating",450,400,"assets/font/PlayfairDisplay-Regular.otf",25)

            

            if x > 50 and x <150:
                shredder(50,175)



            if x> 800:
                clear = True
                x = 0


            message_display("Step 2: Paper Shredding, Heating & Filtering",400,75,'assets/font/PlayfairDisplay-Regular.otf',34)



            
            pygame.display.update()

            pygame.display.update()
            if returned ==  1 or returned == -1:
                Display.fill(WHITE)
                if returned == -1:
                    y = 109
                if returned == 1:
                    counterone =0 
                    countertwo = 1
                    Display.fill(WHITE)
            counter += returned

        elif counter == 4:
            returned = buttons()
            message_display("Step 3: Centrifuging",400,75,'assets/font/PlayfairDisplay-Regular.otf',37)
            counterone += 1
            if counterone == 5:
                counterone = 0
                countertwo += 1
            if countertwo == 5:
                countertwo = 1
            Rotat(countertwo,280,160)

            if returned == 1 or returned == -1:
                Display.fill(WHITE)
                clear = True
                x =0 
                if returned == -1:
                    y = 200
                counterone = 0
                countertwo = 0

            pygame.display.update()
            counter += returned
            
            
        elif counter == 5:
            returned = buttons()
            message_display("Step 4: Deinking",400,75,'assets/font/PlayfairDisplay-Regular.otf',37)
            counterone += 1
            
            if counterone == 5:
                counterone = 0
                countertwo += 1
            if countertwo == 5:
                countertwo = 1
            Deink(countertwo,280,160)

            if returned == 1 or returned == -1:
                Display.fill(WHITE)
                clear = True
                counterone = 0
                countertwo = 0 
                if returned == 1:
                    x= 0
                    y= 175

            pygame.display.update()
            counter += returned
            
        elif counter == 6:
            if clear ==  True:
                Display.fill(WHITE)
                clear = False
            
            returned = buttons()
            message_display("Step 5: Water Rinsing",400,75,'assets/font/PlayfairDisplay-Regular.otf',37)
            line(0,150)
            pulp(x,y)
            Vat(650,270)
            
            
            if x < 700:
                x +=2
                
            if x > 120 and x <350:
                WaterFilter(200,169)
                
            if x >665:
                
                y+=5
                if y > 250:
                    clear = True
                    x = 0
                    y = 175
                
                
            
            
            pygame.display.update()
            
            if returned == 1 or returned == -1:
                Display.fill(WHITE)
                clear = True
                counterone = 0
                if returned == 1:
                    x = 0
                    y = 200
                

            pygame.display.update()
            counter += returned
            
        elif counter == 7:
            if clear == True:
                counterone += 1
                clear = False
                Display.fill(WHITE)
                
            conveyor2(-150,100)


            returned = buttons()
            
            y = 200
            

            if x > -1 and y <320:
                x += 2
                
            if x>319:
                x+=3


            if x<250: 
                pulp(x,y-18)


            elif x > 250 and x < 800:
                bleachedpulp(x,y-10)

            
            if x > 150 and x <370:
                bleachblock(250,180)



            if x> 800:
                clear = True
                x = 0
                


            message_display("Step 6: Paper Bleaching & Whitening",400,75,'assets/font/PlayfairDisplay-Regular.otf',34)



            
            pygame.display.update()
            if returned ==  1 or returned == -1:
                Display.fill(WHITE)
                if returned == -1:
                    y = 175
                    x = 0
                if returned == 1:
                    counterone =0 
                    countertwo = 1
                    Display.fill(WHITE)
                    
            counter += returned
            
        elif counter == 8:
        
            
                
                
            
            
            
            
            counterone += 1
            if counterone == 10:
                
                counterone = 0
                countertwo += 1
            if countertwo == 11:
                countertwo = 1
            Display.fill(WHITE)
            Spray(countertwo,200,150)
            returned = buttons()
            message_display("Step 7: Paper Spraying",400,75,'assets/font/PlayfairDisplay-Regular.otf',34)
            pygame.display.update()
            if returned ==  1 or returned == -1:
                Display.fill(WHITE)
                if returned == -1:
                    y = 109
                if returned == 1:
                    counterone =0 
                    countertwo = 1
                    Display.fill(WHITE)
                    
            counter += returned
            
        elif counter == 9: 
            
            message_display("Step 8: Paper Rolling",400,75,'assets/font/PlayfairDisplay-Regular.otf',34)
            returned = buttons()
            
            counterone += 1
            if counterone == 6:
                counterone = 1
                countertwo+=1
                
            if countertwo == 3:
                countertwo =1
            
            if countertwo ==1:
                Roller1(0,200)
                
            if countertwo ==2:
                
                Roller2(0,200)
            
            if returned == 1 or returned == -1:
                Display.fill(WHITE)
            counter += returned
            
        elif counter == 10:
            
            message_display("All Done!",400,75,'assets/font/PlayfairDisplay-Regular.otf',34)
            FinalPaper(200,200)
            returned = buttons()
            pygame.display.update()
            if returned == 1:
                returned = 0
            if returned == -1:
                Display.fill(WHITE)
            counter += returned

            

#function responsible for display buttons and checking for the cursor position and clicks




def buttons():
    global temp
    global returned
    global info
    temp = 0
   
    mouse = pygame.mouse.get_pos()
    
    click = pygame.mouse.get_pressed()
    
    # The Red Back Button
    if  150 + 100 > mouse[0] > 150 and 450 + 50  > mouse[1] > 450:
        
        pygame.draw.rect(Display,LIGHT_RED,(150,450,100,50))
        if click[0] == 1:
            time.sleep(.5)
            
            pygame.draw.rect(Display,RED,(150,450,100,50))
            temp =   -1
            
    else:
        pygame.draw.rect(Display,RED,(150,450,100,50))
        
        
    #The GREEN Next button
    
    if 550 + 100 > mouse[0] > 550 and 450 + 50  > mouse[1] > 450:
        pygame.draw.rect(Display,LIGHT_GREEN,(550,450,100,50))
        
        if click[0] == 1:
            time.sleep(.5)
            pygame.draw.rect(Display,GREEN,(550,450,100,50))
            
            temp =  1
            
            
    else:
        pygame.draw.rect(Display,GREEN,(550,450,100,50))
        
    #The Grey Info button
        
    if  350 + 100 > mouse[0] > 350 and 450 + 50  > mouse[1] > 450:
        
        pygame.draw.rect(Display,GREY,(350,450,100,50))
        if click[0] == 1:
            time.sleep(.5)
            
            pygame.draw.rect(Display,LIGHT_BLACK,(350,450,100,50))
            
            info = True
            
    else:
        pygame.draw.rect(Display,LIGHT_BLACK,(350,450,100,50))
    
    smallText = pygame.font.Font("assets/font/PAPYRUS.ttf",20)
    textSurf, textRect = text_objects("Back",smallText)
    textRect.center= ((150+(100/2)),(450+(50/2)))
    Display.blit(textSurf,textRect)
    
    smallText = pygame.font.Font("assets/font/PAPYRUS.ttf",20)
    textSurf, textRect = text_objects("Next",smallText)
    textRect.center= ((550+(100/2)),(450+(50/2)))
    Display.blit(textSurf,textRect)
    
    smallText = pygame.font.Font("assets/font/PAPYRUS.ttf",20)
    textSurf, textRect = text_objects("Info",smallText)
    textRect.center= ((350+(100/2)),(450+(50/2)))
    Display.blit(textSurf,textRect)
    
    return temp

def back():
    global info
    global clear
    global temp
    temp = False
    mouse = pygame.mouse.get_pos()
    
    click = pygame.mouse.get_pressed()
    if  350 + 100 > mouse[0] > 350 and 450 + 50  > mouse[1] > 450:
        
        pygame.draw.rect(Display,GREY,(350,450,100,50))
        if click[0] == 1:
            time.sleep(.5)
            Display.fill(WHITE)
            info = False
            Display.fill(WHITE)
            pygame.draw.rect(Display,LIGHT_BLACK,(350,450,100,50))
            clear = True
            Display.fill(WHITE)
            temp = True
            
    
            
    else:
        pygame.draw.rect(Display,LIGHT_BLACK,(350,450,100,50))

    smallText = pygame.font.Font("assets/font/PAPYRUS.ttf",10)
    textSurf, textRect = text_objects("Back To Simulation",smallText)
    textRect.center= ((350+(100/2)),(450+(50/2)))
    Display.blit(textSurf,textRect)
    return temp
    

    

#the game loop sequence, checks constantly for events.

def gameloop():
    global x
    global y 
    global x1
    global x2 
    global y1
    global y2
    global counter
    crashed = False
    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x1 = 0
                if event.key == pygame.K_RIGHT:
                    x2 = 0
                if event.key == pygame.K_UP:
                    y1 = 0
                if event.key == pygame.K_DOWN:
                    y2 = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1 = -5
                if event.key == pygame.K_RIGHT:
                    x2 = 5
                if event.key == pygame.K_UP:
                    y1 = -5
                if event.key == pygame.K_DOWN:
                    y2 = 5

       ######################
       

        page()
        clock.tick(60)
        

        

gameloop()


# 

# In[ ]:




