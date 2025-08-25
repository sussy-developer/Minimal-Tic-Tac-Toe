import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((905, 905))
clock = pygame.time.Clock() #this clock obj is called for the fps settings
screen.fill('black')

# music
pygame.mixer.init()
winning_music = pygame.mixer.Sound('sounds/mixkit-winning-chimes-2015.wav')
click = pygame.mixer.Sound('sounds/sharp-pop-328170.mp3')
# font
fontt= pygame.font.Font('fonts/Pixeltype.ttf',110)
win_o= fontt.render("'o' win !!", False,'black') 
win_x= fontt.render("'X' win !!", False,'black') 
tie = fontt.render("tie !!",False,"black")
w = 0
# box for menu


# 1strow
box1 = pygame.Surface((300,300))
onerec = box1.get_rect(midleft = (1,151))
box1.fill('light blue')

box2 = pygame.Surface((300,300))
tworec =box2.get_rect(midleft = (302,151))
box2.fill('light yellow')

box3 = pygame.Surface((300,300))
threerec =box3.get_rect(midleft = (603,151))
box3.fill('light pink')

# # 2nd row
box4 = pygame.Surface((300,300))
fourrec =box4.get_rect(midleft = (1,452))
box4.fill('light blue')

box5 = pygame.Surface((300,300))
fiverec =box5.get_rect(midleft = (302,452))
box5.fill('light yellow')

box6 = pygame.Surface((300,300))
sixrec =box6.get_rect(midleft = (603,452))
box6.fill('light pink')

# # 3rd row
box7 = pygame.Surface((300,300))
sevenrec =box7.get_rect(midleft = (1,753))
box7.fill('light blue')

box8 = pygame.Surface((300,300))
eightrec =box8.get_rect(midleft = (302,753))
box8.fill('light yellow')

box9 = pygame.Surface((300,300))
ninerec =box9.get_rect(midleft = (603,753))
box9.fill('light pink')

board = [
    [ {"surface": box1, "rect": onerec, "state": None}, 
      {"surface": box2, "rect": tworec, "state": None}, 
      {"surface": box3, "rect": threerec, "state": None} ],

    [ {"surface": box4, "rect": fourrec, "state": None}, 
      {"surface": box5, "rect": fiverec, "state": None}, 
      {"surface": box6, "rect": sixrec, "state": None} ],

    [ {"surface": box7, "rect": sevenrec, "state": None}, 
      {"surface": box8, "rect": eightrec, "state": None}, 
      {"surface": box9, "rect": ninerec, "state": None} ]
]


tic = pygame.image.load('pics/tic.png')
tic = pygame.transform.scale(tic,(300,300))

toe = pygame.image.load('pics/toe.png')
toe = pygame.transform.scale(toe,(300,300))

sound=False              
x=400
count = 0
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
 
    screen.blit(box1,onerec)
    screen.blit(box2,tworec)
    screen.blit(box3,threerec)
    screen.blit(box4,fourrec)
    screen.blit(box5,fiverec)
    screen.blit(box6,sixrec)
    screen.blit(box7,sevenrec)
    screen.blit(box8,eightrec)
    screen.blit(box9,ninerec)

#     horizontal
    pygame.draw.line(screen,'black',(1,600),(905,600),10)  
    pygame.draw.line(screen,'black',(1,300),(905,300),10)

#     virtical
    pygame.draw.line(screen,'black',(300,1),(300,905),10)    
    pygame.draw.line(screen,'black',(600,1),(600,905),10)
    


    if event.type == pygame.MOUSEBUTTONDOWN:
       for row in board :
            for ele in row:
                if ele["rect"].collidepoint(event.pos):
                   if(count%2 == 0):
                       if ele["state"] == None:
                           ele["state"] = "o"
                           count += 1
                           click.play()
                           print(count)
                           print("state of the rect is :",ele["state"])
                   else :
                        if ele["state"] == None:
                            ele["state"] = "x"
                            count += 1
                            click.play()
                            print(count)
                            print("state of the rect is :",ele["state"])
    for row in board :
        for ele in row:
            if ele["state"] == "x":
                tic_rect = tic.get_rect(center = ele["rect"].center)
                screen.blit(tic,tic_rect)
                

            elif ele["state"] == "o":
                teo_rect = toe.get_rect(center = ele["rect"].center)
                screen.blit(toe,teo_rect)
                
                    
        
# 1st row check
    if (board[0][0]["state"] == "o")and(board[0][1]["state"] == "o")and(board[0][2]["state"] == "o") :
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True
        
    elif (board[0][0]["state"] == "x")and(board[0][1]["state"] == "x")and(board[0][2]["state"] == "x") :
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True



# 2nd row check
    elif (board[1][0]["state"] == "x")and(board[1][1]["state"] == "x")and(board[1][2]["state"] == "x") :
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True
    elif (board[1][0]["state"] == "o")and(board[1][1]["state"] == "o")and(board[1][2]["state"] == "o") :
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True



# 3rd row check
    elif (board[2][0]["state"] == "x")and(board[2][1]["state"] == "x")and(board[2][2]["state"] == "x") :
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True

    elif (board[2][0]["state"] == "o")and(board[2][1]["state"] == "o")and(board[2][2]["state"] == "o") :
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True



#right dai check
    elif (board[0][2]["state"]=="x")and(board[1][1]["state"]=="x")and(board[2][0]["state"]=="x"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True

    elif (board[0][2]["state"]=="o")and(board[1][1]["state"]=="o")and(board[2][0]["state"]=="o"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True


#left dai check
    elif (board[0][0]["state"]=="x")and(board[1][1]["state"]=="x")and(board[2][2]["state"]=="x"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True

    elif (board[0][0]["state"]=="o")and(board[1][1]["state"]=="o")and(board[2][2]["state"]=="o"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True


#1st col check
    elif (board[0][0]["state"]=="x")and(board[1][0]["state"]=="x")and(board[2][0]["state"]=="x"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True

    elif (board[0][0]["state"]=="o")and(board[1][0]["state"]=="o")and(board[2][0]["state"]=="o"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True

# 2nd col check
    elif (board[0][1]["state"]=="x")and(board[1][1]["state"]=="x")and(board[2][1]["state"]=="x"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True

    elif (board[0][1]["state"]=="o")and(board[1][1]["state"]=="o")and(board[2][1]["state"]=="o"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True


# 3rd col check
    elif (board[0][2]["state"]=="x")and(board[1][2]["state"]=="x")and(board[2][2]["state"]=="x"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_x,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True

    elif (board[0][2]["state"]=="o")and(board[1][2]["state"]=="o")and(board[2][2]["state"]=="o"):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(win_o,(x,100))
        w=1
        if not sound:   # ✅ only once
            winning_music.play()
            sound = True


# draw factor    
    elif (((board[0][2]["state"]!=None)and(board[1][2]["state"]!=None)and(board[2][2]["state"]!=None))and((board[0][1]["state"]!=None)and(board[1][1]["state"]!=None)and(board[2][1]["state"]!=None))and((board[0][0]["state"]!=None)and(board[1][0]["state"]!=None)and(board[2][0]["state"]!=None))and((board[0][0]["state"]!=None)and(board[1][0]["state"]!=None)and(board[2][0]["state"]!=None))and((board[0][0]["state"]!=None)and(board[1][1]["state"]!=None)and(board[2][2]["state"]!=None))and((board[0][2]["state"]!=None)and(board[1][1]["state"]!=None)and(board[2][0]["state"]!=None))and((board[2][0]["state"] != None)and(board[2][1]["state"] != None)and(board[2][2]["state"] != None))and((board[1][0]["state"] != None)and(board[1][1]["state"] != None)and(board[1][2]["state"] != None))and((board[0][0]["state"] != None)and(board[0][1]["state"] != None)and(board[0][2]["state"] != None))and(w !=1)):
        pygame.draw.rect(screen,'gray',(240,50,500,300),border_radius=34)
        screen.blit(tie,(400,100))

    pygame.display.update()
    clock.tick(90)
    pygame.display.set_caption("tic tac toe")
