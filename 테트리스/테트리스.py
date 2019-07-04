from tkinter import *
from tkinter import messagebox
import tkinter.font
import time
import random
import threading
import os
import numpy as np
root = Tk()
root.title('테트리스')
root.geometry('480x750')
root.resizable(width = FALSE, height = FALSE)

rock_placex = [29,67,105,143,181,219,257,295,333,371,409]
rock_placey = [0, 38, 76, 114, 152, 190, 228, 266, 304, 342, 380, 418, 456, 494, 532, 570, 608, 646, 684]


#global
wall = PhotoImage(file = "wallrock.PNG")
wall1 = PhotoImage(file = "wallrock1.PNG")
wall2 = PhotoImage(file = "wallrock2.PNG")
wall3 = PhotoImage(file = "wallrock3.PNG")
wall4 = PhotoImage(file = "wallrock4.PNG")

wallc = [wall1,wall2,wall3,wall4]
color = 0
shape = 0
sub_shape = 0
usr_x =random.randint(0,8)
usr_y = 0

walllabelL = []
walllabelR = []
walllabelU = []

#테두리 생성
for i in range(28):
    walllabelL.append(Label(root,image = wall))
    walllabelL[i].place(x=0,y=i*27)
for i in range(28):
    walllabelR.append(Label(root,image = wall))
    walllabelR[i].place(x=453,y=i*27)
for i in range(18) :
    walllabelU.append(Label(root,image = wall))
    walllabelU[i].place(x=i*27,y=723)
                  
for i in range(18) :
    walllabelU.append(Label(root,image = wall))
    walllabelU[i].place(x=i*27,y=723)


def makeusr_rock():
    global color,shape
    color = random.randint(0,len(wallc)-1)
    shape = random.randint(0,7)
    rock_shape()
    

usr_rock = [Label(root,image = wallc[0]),Label(root,image = wallc[1]),Label(root,image = wallc[2]),Label(root,image = wallc[3])]
def rock_shape():
    #shape 0 ㄱ_
    #shape 1 _l-
    #shape 2 l
    #shape 3 ㄱ
    #shape 4 ㅗ
    #shape 5 ㅁ
    #shape 6 l-
    global usr_rock
    global color,shape
    global usr_x,usr_y
    usr_wall = wallc[color]
    

    for i in range(4):
        usr_rock[i].configure(image = usr_wall)
    
    if shape == 0 :
        if sub_shape %2 == 0:
            usr_rock[0].place(x= rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y+1])
        elif sub_shape %2 == 1:
            usr_rock[0].place(x= rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x],y=rock_placey[usr_y+2])
            
        
    elif shape == 1 :
        if sub_shape %2 == 0 :
            usr_rock[0].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
        elif sub_shape %2 == 1 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+2])
            
    elif shape == 2 :
        if sub_shape %2 == 0 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y])
            usr_rock[3].place(x=rock_placex[usr_x+3],y=rock_placey[usr_y])
        elif sub_shape %2 == 1 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x],y=rock_placey[usr_y+2])
            usr_rock[3].place(x=rock_placex[usr_x],y=rock_placey[usr_y+3])
            
    elif shape == 3 :
        if sub_shape == 0:
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+2])
        elif sub_shape ==1 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y])
        elif sub_shape == 2:
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x],y=rock_placey[usr_y+2])
            usr_rock[3].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+2])
        elif sub_shape == 3:
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y])
            usr_rock[3].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            
    elif shape == 4 :
        if sub_shape == 0:
            usr_rock[0].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y+1])
        elif sub_shape == 1 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x],y=rock_placey[usr_y+2])
            usr_rock[3].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
        elif sub_shape == 2 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y])
            usr_rock[3].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
        elif sub_shape == 3 :
            usr_rock[0].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+2])
            usr_rock[3].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])            
        
            
            
    elif shape == 5 :
        usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
        usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
        usr_rock[2].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
        usr_rock[3].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
    elif shape == 6 :
        if sub_shape ==0 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x],y=rock_placey[usr_y+2])
        elif sub_shape == 1:
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[2].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y])
            usr_rock[3].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y+1])
        elif sub_shape == 2 :
            usr_rock[0].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+2])
            usr_rock[3].place(x=rock_placex[usr_x],y=rock_placey[usr_y+2])
        elif sub_shape == 3 :
            usr_rock[0].place(x=rock_placex[usr_x],y=rock_placey[usr_y])
            usr_rock[1].place(x=rock_placex[usr_x],y=rock_placey[usr_y+1])
            usr_rock[2].place(x=rock_placex[usr_x+1],y=rock_placey[usr_y+1])
            usr_rock[3].place(x=rock_placex[usr_x+2],y=rock_placey[usr_y+1])
def check_shape():

    global color,shape
    global usr_x,usr_y
    
    if sub_shape+1 == 4:
        fake_sub_shape = 0
    else :
        fake_sub_shape = sub_shape + 1
        
    if shape == 0 :
        if fake_sub_shape %2 == 0:
            if usr_x+2>10 or usr_y+1>18 :
                return False

        elif fake_sub_shape %2 == 1:
            if usr_x+1>10 or usr_y+2>18 :
                return False
            
        
    elif shape == 1 :
        if fake_sub_shape %2 == 0 :
            if usr_x+2>10 or usr_y+1>18 :
                return False
            
        elif fake_sub_shape %2 == 1 :
            if usr_x+1>10 or usr_y+2>18 :
                return False
            
    elif shape == 2 :
        if fake_sub_shape %2 == 0 :
            if usr_x+3>10 or usr_y>18 :
                return False
        elif fake_sub_shape %2 == 1 :
            if usr_x>10 or usr_y+3>18 :
                return False
            
    elif shape == 3 :
        if fake_sub_shape == 0:
            if usr_x+1>10 or usr_y+2>18 :
                return False
        elif fake_sub_shape ==1 :
            if usr_x+2>10 or usr_y+1>18 :
                return False
        elif fake_sub_shape == 2:
            if usr_x+1>10 or usr_y+2>18 :
                return False
        elif fake_sub_shape == 3:
            if usr_x+2>10 or usr_y+1>18 :
                return False
            
    elif shape == 4 :
        if fake_sub_shape == 0:
            if usr_x+2>10 or usr_y+1>18 :
                return False
        elif fake_sub_shape == 1 :
            if usr_x+1>10 or usr_y+2>18 :
                return False
        elif fake_sub_shape == 2 :
            if usr_x+2>10 or usr_y+1>18 :
                return False
        elif fake_sub_shape == 3 :
            if usr_x+1>10 or usr_y+2>18 :
                return False               
    elif shape == 5 :
        return True
    elif shape == 6 :
        if fake_sub_shape ==0 :
            if usr_x+1>10 or usr_y+2>18 :
                return False
        elif fake_sub_shape == 1:
            if usr_x+2>10 or usr_y+1>18 :
                return False
        elif fake_sub_shape == 2 :
            if usr_x+1>10 or usr_y+2>18 :
                return False
        elif fake_sub_shape == 3 :
            if usr_x+2>10 or usr_y+1>18 :
                return False
    return True


#key input func
def Left_input(event) :
    global usr_x
    if check_x('L') == 0:
        return
    else :
        usr_x -=1
        rock_shape()
    
def Up_input(event) :
    global sub_shape
    if check_shape() == True :
        if sub_shape+1 == 4:
            sub_shape = 0
            rock_shape()
        else :
            sub_shape+= 1
            rock_shape()
    else :
        return
    
def Down_input(event) :
    global usr_y
    if not usr_y> 15:
        usr_y = 15
        rock_shape()
def Right_input(event) :
    global usr_x
    if check_x('R') == 0:
        return
    else :
        usr_x +=1
        rock_shape()

root.bind('<Left>',Left_input)
root.bind('<Right>',Right_input)
root.bind('<Up>',Up_input)
root.bind('<Down>',Down_input)

def buttonc() :
    global usr_x,usr_y
    #usr_y = 0
    #makeusr_rock()
    a = list(usr_rock)
    print(usr_rock)
    print(a)
    #for i in range(4):
    #    print(usr_rock[i].place_info())
    #    print(a[i].place_info())
    
button1 = Button(root,text = 'make wall',command = buttonc)
button1.place(x = 20, y = 20)

def check_floor():
    global usr_y
    global usr_x

    for i in range(4):
        if int(usr_rock[i].place_info()['y']) == rock_placey[18]:
            usr_y = 0
            usr_x = random.randint(0,7)
            makeusr_rock()
            break
        
def check_x(LR):
    global usr_x
    for i in range(4) :
        if LR == 'L' and int(usr_rock[i].place_info()['x']) == rock_placex[0] :
            return 0
        if LR == 'R' and int(usr_rock[i].place_info()['x']) == rock_placex[10] :
            return 0
    return 1

def drop_rock():
    global usr_x,usr_y
    usr_y += 1
    rock_shape()
drop_rock()
def timerwall() :
    check_floor()
    drop_rock()
    timer = threading.Timer(1,timerwall)
    timer.start()
timerwall()


root.mainloop()

