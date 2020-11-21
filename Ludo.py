"""Yet To Do
-Need to worry about the inside like how the token behaves somewhere it is incrementing
-Tabel->Almost done need to update the table with some function and it is printing many time
    You know there are some edge cases like the whne the token is inside the strip. Need to itroduce new bool for inside strip
    and also need to add home and points
-CPU->Yet to start
-Need to write for deth home and some error cases


+++++-Need to think of the if case x.case>35 in the mover ot vhanger function because without that the code will work same
---> Should call death function
+++++++++++++++++Dnt Forget TO add+++++++++++++++++++++
-One move per person and click need 2 create a new boolean varialbeand use it at mouse click event handler
-More than the 54 it should not move 
"""

from tkinter import *
from tkinter.ttk import *
import pygame,random,time
class Token:
    hori,veri = True,True;#For movement if false then negitive true then positive
    home,inside = False,True#home means it is going inside th estrip, Inside meanseif it is playing or not
    move = True#True is for hori, false is for vertical movement
    x_pos,y_pos=0,0
    b_x,b_y=0,0
    count = 0
    number=0
    def __init__(self,color,number):
        self.number=number
        if(color  == 1):#Red
            self.veri = False
        elif (color == 4):#Blue
            self.veri=self.hori = False
            self.move = False
        elif (color == 3):#Green
            self.hori = False
            self.move = False
        else:#Yellow
            self.hori = False
            self.move = True
    def printer(self,board,color):
        pygame.draw.circle(board,(0,0,0),(self.x_pos,self.y_pos),15,3)
        pygame.draw.circle(board,color,(self.x_pos,self.y_pos),8)#(244,81,30) Mana color
    def red_changer(self,col):
        temp=0
        if(col==3):#Green
            temp = self.count+13
            if(temp>52):
                return(temp-52)
            return(temp)
        if(col == 2):
            temp=self.count+26
            if(temp>52):
                return(temp-52)
            return(temp)
        if(col == 4):
            temp = self.count+39
            if(temp>52):
                return(temp-52)
            return(temp)
        else:
            return(self.count)
             
        
    def changer(self,col):
        if(self.count>52):
            return
        #print("It is in changer. The values are",self.count)
        if(self.count==52):
            ##print("Now the count is 53")
            self.h_inside=True
            if(col == 3):
                self.y_pos-=40
                self.x_pos+=24
                self.veri =True
                self.move=False
                return
            if(col==4):
                self.veri =False
                self.move=False
                self.x_pos-=25
                self.y_pos+=40
                return True
            if(col==1):
                self.hori=True
                self.move=True
                self.y_pos-=25
                self.x_pos-=40
                return True
            if(col==2):
                #time.sleep(1)
                #exit()
                self.hori=False
                self.move=True
                self.y_pos+=30
                self.x_pos+=39
                ##print("It is in Yello case:(Later)",self.x_pos,self.y_pos)
                
                return True

        if(self.count!=52):    
            t_count = self.red_changer(col)
        ##print(t_count,"THe valu",self.count,"(",self.x_pos,self.y_pos,")")  
        
        if(t_count==1):
            ##print("After Entering:",self.x_pos,self.y_pos)
            self.y_pos-=28
            self.x_pos-=40
            self.hori = True
            self.move = True
            ##print("After Entering:",self.x_pos,self.y_pos)
            return True
        if(t_count==7):
            self.hori=False
            self.veri=False
            self.move=False
            self.x_pos+=35
            self.y_pos+=5
            return True
        if(t_count==13):#This br
            self.move=True
            self.hori=True
            self.veri = False
            
            self.x_pos-=15
            #print("in the 13")
            return True
        if(t_count ==14):
            ##print("Befor Entering:",self.x_pos,self.y_pos)
            self.move=False
            self.veri=True
            self.y_pos-=40
            self.x_pos+=25
            ##print("After Entering:",self.x_pos,self.y_pos)
            return True
        if(t_count==20):#Working
            self.move=True
            self.hori=True
            self.y_pos +=33
            self.x_pos-=5
            return True
        if(t_count == 26):
            self.move=False
            self.veri =True
            self.y_pos-=10
            return True
        if(t_count== 27):
            #print("Befor Entering:",self.x_pos,self.y_pos)
            self.move=True
            self.hori= False
            #self.vertical=False
            self.y_pos+=25
            self.x_pos+=40
            #print("After Entering:",self.x_pos,self.y_pos)
            
            return True
            
        if(t_count==33):
            self.x_pos-=35
            self.y_pos-=7
            self.move = False
            self.veri = True
            
            return True
        if(t_count==39):
            self.move = True
            self.hori = False
            self.x_pos+=15
            return True
        if(t_count==40):
            
            ##print("Befor Entering:",self.x_pos,self.y_pos)
            self.move=False
            self.veri=False
            self.x_pos-=27
            self.y_pos+=39
            ##print("After Entering:",self.x_pos,self.y_pos)
            
            return True
        if(t_count==46):
            self.move=True
            self.hori=False
            
            self.y_pos-=32
            self.x_pos+=9
            return True
        if(t_count==52):
            self.move=False
            self.veri=False
            self.y_pos+=15
            self.x_pos-=2
            ##print("After Leaving:",self.x_pos,self.y_pos)
               
            #self.y_pos-=15
            return True
            
            
            
            
            
            
class Player:
    valid=False
    
    current=0#Maintains the current token which the player is using
    def __init__(self,code,board,p_n):
        self.main=[]
        self.color = 0
        self.name=p_n
        self.points = 0
        self.outside=[]
        self.computer=False
        self.board,self.code=board,code
        x,y=0,0
        j=0
        #print(self.name)
        if(code == 1 ):#red
            x,y=140,130#old values 120,110
            self.color = (255,0,0)
            ###print("in REd") 
        elif(code == 4):#Yello    
            #print("It is printing in blue")
            x,y = 140,460
            self.color = (0,0,255)
        elif (code == 3):#Green
            x,y = 465,130
            self.color = (0,255,0)
        else:#Bliue
            x,y = 465,460
            self.color = (255,255,0)
        for i in range(0,4):
            j = Token(code,i)
            if(i==0):
                j.x_pos,j.y_pos,j.b_x,j.b_y = x,y,x,y
            if(i == 1):
                j.x_pos,j.y_pos,j.b_x,j.b_y = x+65,y,x+65,y
            if(i==2):
                j.x_pos,j.y_pos,j.b_x,j.b_y = x,y+60,x,y+60
            if(i==3):
                j.x_pos,j.y_pos,j.b_x,j.b_y = x+65,y+60,x+65,y+60
            self.main.append(j)
            j=0
    def coin(self):
        for x in self.main:
            x.printer(self.board,self.color)
    def clicked(self,m_po,dice):
        m_x,m_y = m_po
        self.current=0;
        for x in self.main:
            if(0<= abs(x.x_pos- m_x) <10 and 0<=abs(x.y_pos- m_y) < 10):
                self.current=x.number
                return True
            
        
        return(False)
    
    def mover(self,p1,pot,dice):
        ##print("It is in mover")
        if(self.current==5):
            return
        
        x = self.main[self.current]
        list1 = [7]
       #Checking of they are inside still if yes then keeping them out
        if(self.color==(255,0,0)):
           if((120<x.x_pos<225) and (105<x.y_pos<210)) and dice==6:
               x.x_pos,x.y_pos=110,305
               x.inside= False
               x.count = 2
               self.outside.append(self.current)
               self.valid=True;pot.dice_thrower()
               
               return
        elif(self.color==(255,255,0)):
            if((445<x.x_pos<550) and (440<x.y_pos<540)) and dice==6:
                x.x_pos,x.y_pos=550,357
                x.count = 2
                x.inside= False
                self.valid=True;
                self.outside.append(self.current)
                pot.dice_thrower()
                return
        elif(self.color==(0,0,255)):
            if((120<x.x_pos<225) and (440<x.y_pos<540)) and dice==6:
                x.x_pos,x.y_pos=305,550
                x.count = 2
                x.inside= False
                self.valid=True;self.outside.append(self.current);pot.dice_thrower()
                return
        elif(self.color==(0,255,0)):
            if((460<x.x_pos<550) and (125<x.y_pos<200)) and dice==6:
                x.x_pos,x.y_pos=357,110
                x.count = 2
                x.inside = False
                #print("Sairam")
                self.valid=True;self.outside.append(self.current);pot.dice_thrower()
                return
        if(x.inside):#untill 6 comes he shoul wait
            self.valid=False;pot.dice_thrower()
            
            return
        """# hori,veri = True,True;For movement if false then negitive true then positive
    home,inside = False,True#home means it is going inside th estrip, Inside meanseif it is playing or not
    move = True#True is for hori, false is for vertical movement"""
        for i in range(1,dice+1):##Rodda
            
            temp_x,temp_y=-1,-1
            pot.board_printer()
            x.count+=1
            temp = x.changer(self.code)
            
            #print("In the loop:",x.count,x.move,x.hori)
            if(x.move):
                if(x.hori == True):
                    temp_x=1
                x.x_pos += temp_x*40
                
            else:
        
                if(x.veri == True):
                    temp_y=1
                x.y_pos += temp_y*40
                
            #print("Original Coods:",x.x_pos,x.y_pos)
            #print(":++++++++++++++++++")
            
            pygame.display.update()
            time.sleep(0.1)
        
         #Need 2 write a swamp method in token so that it will take care of all mo0vement changes required based on the ccircumstances & coutn

 # need to create the base positions for all the tokens if they got out htey will come and sit there need to do movement and think of
 #Killin"""   

        
    
class Application(Frame):
    FONT,board,clock,players=0,0,0,0
    valid_c=0
    def __init__(self,master = None):
        #self.asalu(['Sairam', 'Om', 'Sai', 'Sri', 4])
        super().__init__(master)
        self.master = master
        self.create_widgets()
    def Validator(self,inp):
        if(len(inp)<=7 and inp[-1]!=" "):
            return True
        return False
    def name_setter(self,te,a):
        a=a.ljust(7-len(a))
        te.insert(0, a)

    def create_widgets(self):
        self.winfo_toplevel().title("Jai Sairam")
        self.reg = self.master.register(self.Validator)#Registering a call back function
        
        p1 = Label(self.master,text="Player 1 Name:").grid(row=1,column=1)
        p2 = Label(self.master,text="Player 2 Name:").grid(row=3,column=1)
        p3 = Label(self.master,text="Player 3 Name:").grid(row=5,column=1)
        p4 = Label(self.master,text="Player 4 Name:").grid(row=7,column=1)
        t1=Label(self.master,text="(Red)").grid(row=1,column=3,sticky = 'W')
        Label(self.master,text="(Blue)").grid(row=7,column=3,sticky = 'W')
        Label(self.master,text="(Green)").grid(row=5,column=3,sticky = 'W')
        Label(self.master,text="(Yellow)").grid(row=3,column=3,sticky = 'W')
        t1=Label(self.master,text=" ").grid(row=2)
        t1=Label(self.master,text=" ").grid(row=4)
        t1=Label(self.master,text=" ").grid(row=6)
        t1=Label(self.master,text=" ").grid(row=8)
        p1n = Entry(self.master,width = 40)
        
        p2n = Entry(self.master,width = 40)
        p3n = Entry(self.master,width = 40)
        p4n = Entry(self.master,width = 40)
        count=p1n.config(validate="key",validatecommand=(self.reg,'%P'))
        p2n.config(validate="key",validatecommand=(self.reg,'%P'))
        p3n.config(validate="key",validatecommand=(self.reg,'%P'))
        p4n.config(validate="key",validatecommand=(self.reg,'%P'))
        p1n.grid(row=1,column=2,sticky=W)
        p2n.grid(row=3,column=2,sticky=W)
        p3n.grid(row=5,column=2,sticky=W)
        p4n.grid(row=7,column=2,sticky=W)
        s1 = Scale(self.master,from_ = 1, to = 4,orient = HORIZONTAL)
        s1.grid(row=9,column=2,sticky=W)
        
        ch1=Checkbutton(self.master,command=lambda: self.name_setter(p1n,"CPU1"))
        ch2=Checkbutton(self.master,command=lambda: self.name_setter(p2n,"CPU2"),onvalue=True,offvalue=False)
        ch3=Checkbutton(self.master,command=lambda: self.name_setter(p3n,"CPU3"),onvalue=True,offvalue=False)
        ch4=Checkbutton(self.master,command=lambda: self.name_setter(p4n,"CPU4"),onvalue=True,offvalue=False)
        
        ch1.grid(row=1,column=4)
        ch2.grid(row=3,column=4)
        ch3.grid(row=5,column=4)
        ch4.grid(row=7,column=4)
        ##print(ch1.get())
        style = Style()
        style.map('D.TButton',foreground = [('pressed' , 'red'),('active','green')], background= [('pressed', '!disabled' , 'orange'),('active','green')])
        btn = Button(self.master,text = "Let's Start",style ="D.TButton",
                        command=lambda:self.asalu([p1n.get(),p2n.get(),p3n.get(),p4n.get(),int(s1.get())],[ch1.state(),ch2.state(),ch3.state(),ch4.state()])).grid(row=16,column = 3,sticky = W)
        Label(self.master,text="No. Of Players:").grid(row=9,column=1)
        Label(self.master,text="0        2        3        4").grid(row=10,column=2,sticky=W)
        Label(self.master,text="- T stands for Token. P for Points in the Top-Right Corner Tabel").grid(row=11,column=1,sticky=W)
        Label(self.master,text="- Click on the inside circle Token to move the Token").grid(row=13,column=1,sticky=W)
        Label(self.master,text="- Home -> 5 Points;Kill -> 10 Points").grid(row=12,column=1,sticky=W)
        Label(self.master,text="- Maximum only 7 Characters are allowed in Name").grid(row=15,column=1,sticky=W)
        Label(self.master,text="- Fill the Name and set the Number of Players and remaining will be played by the CPU").grid(row=14,column=1,sticky=W)
    def asalu(self,valid_l,sega):#SegaM
        
        compu_l=[]
        for x in sega:
            if(x[0]==('selected')):
                #print("Sairam")
                compu_l.append(True)
            else:
                compu_l.append(False)
            
        #print("The computer list",compu_l)
        if valid_l[-1] ==0:
            return
        temp1=valid_l[-1]
        for temp in valid_l:
            if temp!='':
                temp1-=1
        if(temp1!=-1):
            return
        self.master.destroy()
        pygame.init()
        self.players=[]
        self.FONT= pygame.font.Font(None,26)
        self.board = pygame.display.set_mode((1200,650))
        self.clock = pygame.time.Clock()
        self.choice_l=[]
        self.dice_l =  [random.randrange(1, 7) for i in range(250)]
        """self.dice_l[2]=5
        self.dice_l[1]=5
        self.dice_l[3]=6"""
        self.choice=0
        self.d_current=0
        for i in  range(0,4):
            if(valid_l[i]!=''):
                self.choice_l.append(i+1)
                temp = Player(i+1,self.board,valid_l[i])
                self.players.append(temp)
                if(compu_l[i]):
                    #print("It is setting it to true")
                    temp.computer=True
                temp=0
        temp=0
        self.dice_thrower()
        moving = False
        while True:
            temp+=1
            self.clock.tick(10)
            self.board.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for x in self.players:#Problm Loop
                        if(x.clicked(pos,1) and self.choice_l[0]==x.code and moving==False):
                                moving = True
                                self.thinker(x)
                                moving= False
            if(self.players[self.choice_l[0]-1].computer):
                
                self.decision_maker(self.players[self.choice_l[0]-1])#In this decision maker everything should be taken care of including
                #Dice throwing and appending also
            ##print(pygame.mouse.get_pos())                        
            self.board_printer()
            pygame.draw.rect(self.board,(200,25,21),(800,400,160,160))
            
            self.dice_printer(self.dice_l[self.d_current])
            pygame.display.update()
            
            
            
    def decision_maker(self,current):
        #print("It is in the decision_maker function")
        six,append = False,True
        if(self.dice_l[self.d_current] == 6 ):
            if(len(current.outside) < 4):
                for a in current.main:
                    if(a.inside):
                        current.current = a.number
                        current.mover(self.players,self,self.dice_l[self.d_current])
                        self.subthinker(False,True)
                        return
        else:
                append=False
        positions,points = [],[0,0,0,0]
        dummy=0
        dice=self.dice_l[self.d_current]
        for x in self.players:#Creating the Position list
            if(x!=current):
                for t in x.main:
                    positions.append(t.count)
                
#4,3,5,2,6,1        .
                    #CHec if a token is dying if yes give highest points then check for the killing
        for x in current.main:#Looping through the current player
            dummy=0#Creating the new for every iteration
            temp = x.count + dice#The current position of the token
            if(temp>54):#For those coins which went home
                dummy=-200
            if(temp == 54):
                current.current = x.number
                current.mover(self.players,self,self.dice_l[self.d_current])
                append=False
                return
            if(not x.count in  [2,10,15,23,28,36,41,49] ):#Leaving Security
                for j in positions:
                    if(x.count-j==4):
                        dummy+=30
                    elif(x.count-j==3):
                        dummy+=25
                    elif(x.count-j==5):
                        dummy+=20
                    elif(x.count-j==2):
                        dummy+=15
                    elif(x.count-j==6):
                        dummy+=10
                    elif(x.count-j==1):
                        dummy+=5
                
            for j in positions:
                if(j-temp == 0):#killing Condition
                    dummy+=100
                    killing=x.count
                elif(j-temp == 1):
                    dummy+=5
                elif(j-temp==2):
                    dummy+=15
                elif(j-temp==3):
                    dummy+=25
                elif(j-temp==4):
                    dummy+=30
                elif(j-temp==5):
                    dummy+=20
                elif(j-temp==6):
                    dummy+=10
            points[x.number]+=dummy
        
        dummy = max(points)
        current.current = points.index(dummy)
        current.mover(self.players,self,self.dice_l[self.d_current])
        
        time.sleep(0.2)
        self.subthinker(not dice==6,True)
    
    
    
    
    
    
    def player_home(self,code,colr):
    #pygame.draw.rect(board,(255,255,255),code)
        board=self.board;
        x,y=code[0],code[1];x+=15;y+=15
        pygame.draw.rect(board,colr,(x,y,170,170))
        pygame.draw.rect(board,(255,255,255),(x+35,y+30,40,40))
        pygame.draw.rect(board,(255,255,255),(x+100,y+30,40,40))
        pygame.draw.rect(board,(255,255,255),(x+35,y+90,40,40))
        pygame.draw.rect(board,(255,255,255),(x+100,y+90,40,40))
    def sub_filler(self,post,ins,a=6):
        if(ins):
            return("Insd")
        if(0 < post <7):
            if(post+7<10):
                post="0"+str(post+7)
                return("R-"+post)
            return("R-"+str(post+7))
        if(6 < post < 20):
            if(post-6<10):
                post="0"+str(post-6)
                return ("G-"+post)
            return("G-"+str(post-6))
        if(19 < post < 33):
            if(post-19<10):
                post="0"+str(post-19)
                return ("Y-"+post)
            return("Y-"+ str(post-19))
        if(32 < post < 46):
            if(post-32<10):
                post="0"+str(post-32)
                return ("B-"+post)
            return("B-"+str(post-32))
        if(45 < post <=52):
            if(post-45<10):
                post="0"+str(post-45)
                return ("R-"+post)
            return("R-"+str(post-45))
        return("H-0"+str(post-51))
        
    def table_filler(self):
        board=self.board;
        pygame.draw.circle(board,(255,0,0),(695,80),8)
        pygame.draw.circle(board,(0,0,255),(695,275),8)
        pygame.draw.circle(board,(0,255,0),(695,215),8)
        pygame.draw.circle(board,(255,255,0),(695,150),8)
        temp=[[640,70],[640,90],[650,80]]
        dummy = (self.players[self.choice_l[0]-1].code) -1
        ##print(dummy)
        dummy1=30
        for i in temp:
            
            i[1]+=(dummy)*70
        pygame.draw.polygon(board,(255,165,0),temp)
        font_title = pygame.font.Font(None,30)
        announcement = font_title.render("Col       Player          T1         T2         T3        T4       P", True, (255,255,255))
        announcement_rect = announcement.get_rect(center = (922,30))
        self.board.blit(announcement,announcement_rect)
        dummy1=90
        for temp in self.players:#Rodds
            dummy = temp.code

            
            announcement1 = font_title.render(self.sub_filler(temp.main[0].red_changer(dummy),temp.main[0].inside)+"     "+self.sub_filler(temp.main[1].red_changer(dummy),temp.main[1].inside)+"    "+self.sub_filler(temp.main[2].red_changer(dummy),temp.main[2].inside)+"     "+self.sub_filler(temp.main[3].red_changer(dummy),temp.main[3].inside)+"    "+str(temp.points),True,(255,255,255))
            announcement_rect1=announcement.get_rect(center=(1120,dummy1))
            announcement2 = font_title.render(temp.name,True,(255,255,255))
            announcement_rect2=announcement2.get_rect(center=(800,dummy1))
            
            dummy1+=60
            self.board.blit(announcement1,announcement_rect1)
            self.board.blit(announcement2,announcement_rect2)
        pygame.display.flip()

    def board_printer(self):
        board=self.board;
        pygame.draw.rect(board,(255,255,200),(50,50,560,560))
        pygame.draw.rect(board,(255,0,0),(50,50,240,240))#red 
        pygame.draw.rect(board,(0,255,0),(370,50,240,240))#green
        pygame.draw.rect(board,(0,0,255),(50,370,240,240))#blue
        pygame.draw.rect(board,(255,255,0),(370,370,240,240))#yellow
        pygame.draw.rect(board,(0,0,255),(318,370,25,203))#blue strip
        pygame.draw.rect(board,(0,255,0),(318,90,25,200))#greeen strip
        pygame.draw.rect(board,(255,255,0),(370,319,200,25))#yellow strip
        pygame.draw.rect(board,(255,0,0),(90,319,200,25))#red strip
        for x_cod in range(50,600,40):##printing lines,, but it also draw in lines in middle so need to #print a white in it
            pygame.draw.line(board,(0,0,0),(290,x_cod),(370,x_cod),2)
            pygame.draw.line(board,(0,0,0),(x_cod,290),(x_cod,370),2)
        pygame.draw.rect(board,(255,255,255),(290,290,82,82))#Center white part in x - axis
        pygame.draw.polygon(board,(255,0,0),((290,290),(290,370),(330,330)))#Red triangle in center
        pygame.draw.polygon(board,(255,255,0),((370,290),(370,370),(330,330)))#yellow triangel in center
        pygame.draw.polygon(board,(0,255,0),((290,290),(370,290),(330,330)))#Green trianlge in center
        pygame.draw.polygon(board,(0,0,255),((290,370),(370,370),(330,330)))#Blue triangle in center
        pygame.draw.line(board,(0,0,0),(90,290),(130,320),3)#Red Geetha1
        pygame.draw.line(board,(0,0,0),(90,320),(130,290),3)#Red Geetha2
        pygame.draw.line(board,(0,0,0),(530,370),(570,345),3)#yello Geetha1
        pygame.draw.line(board,(0,0,0),(570,370),(530,345),3)#Yellow Geetha2
        pygame.draw.line(board,(0,0,0),(370,130),(340,90),3)#Green Geetha1
        pygame.draw.line(board,(0,0,0),(370,90),(340,130),3)#Green Geetha2
        pygame.draw.line(board,(0,0,0),(290,570),(315,530),3)#BLueGeetha1
        pygame.draw.line(board,(0,0,0),(315,570),(290,530),3)#BlueGeetha2
        pygame.draw.line(board,(0,0,0),(340,490),(370,530),3)#BLueGeetha1 Sec
        pygame.draw.line(board,(0,0,0),(370,490),(340,530),3)#BlueGeetha2 Sec
        pygame.draw.line(board,(0,0,0),(290,130),(315,170),3)#Green Geetha1 Sec
        pygame.draw.line(board,(0,0,0),(290,170),(315,130),3)#Green Geetha2 Sec
        pygame.draw.line(board,(0,0,0),(170,370),(130,345),3)#red Geetha1 Sec
        pygame.draw.line(board,(0,0,0),(130,370),(170,345),3)#red Geetha2 Sec
        pygame.draw.line(board,(0,0,0),(530,290),(490,320),3)#Yellow Geetha1 sec
        pygame.draw.line(board,(0,0,0),(530,320),(490,290),3)#Yellow Geetha2 sec
        pygame.draw.line(board,(0,0,0),(570,345),(650,345),2);pygame.draw.line(board,(0,0,0),(570,320),(650,320),2)#Last box
        pygame.draw.line(board,(0,0,0),(50,345),(90,345),2);pygame.draw.line(board,(0,0,0),(50,320),(90,320),2)#Last box
        pygame.draw.line(board,(0,0,0),(340,50),(340,90),2);pygame.draw.line(board,(0,0,0),(320,50),(320,90),2)#Last box
        pygame.draw.line(board,(0,0,0),(340,570),(340,610),2);pygame.draw.line(board,(0,0,0),(320,570),(320,610),2)#Last box
        self.player_home((70,65),(255,0,0))#Red Player Home
        self.player_home((395,65),(0,255,0))#Green Player Home
        self.player_home((70,395),(0,0,255))#Blue Player Home
        self.player_home((395,395),(255,255,0))#yellow Player Home
        ############Table Printing###############
        
        pygame.draw.rect(self.board,(0,0,0),(665,10,650,300))#Working Here
        #time.sleep(0.1)
        pygame.draw.rect(board,(255,25,225),(667,7,525,305),4)
        pygame.draw.rect(board,(255,225,225),(670,10,520,300),3)
        pygame.draw.line(board,(255,255,25),(670,50),(1190,50),3)
        pygame.draw.line(board,(255,255,25),(670,115),(1190,115),3)
        pygame.draw.line(board,(255,255,25),(670,180),(1190,180),3)
        pygame.draw.line(board,(255,255,25),(670,245),(1190,245),3)
        pygame.draw.line(board,(255,255,25),(720,10),(720,305),3)
        pygame.draw.line(board,(255,255,25),(850,10),(850,305),3)
        pygame.draw.line(board,(255,255,25),(925,10),(925,305),3)
        pygame.draw.line(board,(255,255,25),(1000,10),(1000,305),3)
        pygame.draw.line(board,(255,255,25),(1070,10),(1070,305),3)
        pygame.draw.line(board,(255,255,25),(1140,10),(1140,305),3)
        self.table_filler()
        #pygame.draw.line(board,(255,255,25),(0,10),(850,305),3)
        for i in self.players:
            i.coin()
    def dice_printer(self,temp):
        pygame.draw.rect(self.board,(200,25,21),(800,400,160,160))
        
        if(temp==1):
            pygame.draw.circle(self.board,(255,255,255),(880,480),25);pygame.display.update();time.sleep(0.02);return
               
        if(temp==2):
            pygame.draw.circle(self.board,(255,255,255),(840,440),20)
            pygame.draw.circle(self.board,(255,255,255),(920,520),20);pygame.display.update();time.sleep(0.02);return
        if(temp==3):
            pygame.draw.circle(self.board,(255,255,255),(830,430),15)
            pygame.draw.circle(self.board,(255,255,255),(880,480),15)
            pygame.draw.circle(self.board,(255,255,255),(930,530),15);pygame.display.update();time.sleep(0.02);return
        if(temp==4):
            pygame.draw.circle(self.board,(255,255,255),(840,440),20)
            pygame.draw.circle(self.board,(255,255,255),(840,520),20)
            pygame.draw.circle(self.board,(255,255,255),(920,440),20)
            pygame.draw.circle(self.board,(255,255,255),(920,520),20);pygame.display.update();time.sleep(0.02);return
        if(temp==5):
            pygame.draw.circle(self.board,(255,255,255),(840,440),15)#For 4
            pygame.draw.circle(self.board,(255,255,255),(840,520),15)
            pygame.draw.circle(self.board,(255,255,255),(920,440),15)
            pygame.draw.circle(self.board,(255,255,255),(920,520),15)
            pygame.draw.circle(self.board,(255,255,255),(880,480),15);pygame.display.update();time.sleep(0.02);return
        if(temp==6):
            pygame.draw.circle(self.board,(255,255,255),(830,450),15)
            pygame.draw.circle(self.board,(255,255,255),(880,450),15)
            pygame.draw.circle(self.board,(255,255,255),(930,450),15)
            pygame.draw.circle(self.board,(255,255,255),(830,520),15)
            pygame.draw.circle(self.board,(255,255,255),(880,520),15)
            pygame.draw.circle(self.board,(255,255,255),(930,520),15);pygame.display.update();time.sleep(0.02);return
        
        
    def dice_thrower(self):
        self.d_current+=1
        if(len(self.dice_l)<5):
            self.dice_l =  [random.randrange(1, 7) for i in range(250)]
        for x in range(0,random.randint(4,8)):
            self.board_printer()
            temp = random.randint(1,6)
            self.dice_printer(temp)
        self.dice_printer(self.dice_l[self.d_current])
        
    def subthinker(self,append,dice):
        if(append):
            self.choice_l.append(self.choice_l.pop(0))
        if(dice):
            self.dice_thrower()
            
    def thinker(self,x):#NewFunctio
        #print("Start of the function",x.current,x.outside,self.dice_l[self.d_current])
        if(x.current in x.outside):
            #print("In 1st If")
            if(self.dice_l[self.d_current] == 6):
                x.mover(self.players,self,self.dice_l[self.d_current])
                self.subthinker(False,True);return
            else:
                x.mover(self.players,self,self.dice_l[self.d_current])
                #self.death_home(tok,play)
                self.subthinker(True,True);return
        else:
            if(self.dice_l[self.d_current] == 6):
                #print("In 2nd If")
                x.mover(self.players,self,self.dice_l[self.d_current])
                                #need to call home and death function here
                self.subthinker(False,True);return
            elif(len(x.outside)==0):
                #print("In 3rd If")
                self.subthinker(True,True);return
            else:
                #print("In 4th If")
                self.subthinker(False,False);return

    def death_home(self,tok):#tok is playerNeed to add 
        if(tok.count == 58 and tok.home==False):
            tok.home=True
            #play.points+=10
            return True
        for x in self.players:
            if(x.code!=self.choice_l[0]):
                for j in x.main:
                    if(j.count==tok.count):#need to pop it from outside list
                        sec = [2,10,15,23,28,36,41,49]
                        if(not tok.count in sec):
                            play.outside_l.remove(j.number)#Comedy
                            j.x_pos,j.y_pos =j.b_x,j.b_y#Keeping them in its original places
                            play.points+=15
                            return True
        return False
                
        #print("Leaving the function",x.current,x.outside,self.dice_l[self.d_current])
                
        
        
root = Tk()
app = Application(master = root)
app.mainloop()   
    
"""# need to create the base positions for all the tokens if they got out htey will come and sit there need to do movement and think of
 Killin"""               