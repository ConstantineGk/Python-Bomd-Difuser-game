
import Buttons
from threading import Thread
import pygame,random,sys

pygame.init()
pygame.font.init()
clock=pygame.time.Clock()
##################################
text='0'
import tkinter as tk
class Initial:
    def __init__(self,root):
        self.p=root
        bg=tk.PhotoImage(file='bg.png')
        bglabel=tk.Label(root,image=bg,borderwidth=2)
        bglabel.place(x=4, y=0, relwidth=1, relheight=1)
        bglabel.image = bg
        
        
        
        label=tk.Label(root,text="Captain or Lieutenant",font='Arial 15')
        label.grid(row=1,column=1)
        self.tbox=tk.Entry(root,width=40,bg='white')
        self.tbox.grid(row=2,column=1)
        label2=tk.Label(root,text="Enter Server IP Address",font='Arial 15')
        label2.grid(row=5,column=1)
        self.tbox2=tk.Entry(root,width=40)
        self.tbox2.grid(row=6,column=1)
        button=tk.Button(root,text='Start',font='Arial 15',bg='red', width=22,command=self.f2)
        button.grid(row=8,column=1)
        
    def f2(self):
        global text,ip
        text=self.tbox.get()
        ip=self.tbox2.get()
        self.p.destroy()
    
w=tk.Tk()
w.title("BitterBomb")
w.geometry('600x400')
myapp=Initial(w)
w.mainloop()


#######################
if text!='Captain' and text!='Lieutenant':
    sys.exit()
if text=='Lieutenant':
    scenelist={'sc1':[193,271,388,432],'sc3':[523,537,113,268],'sc4':[622,637,113,268],'sc5':[722,737,113,268],'sc6':[822,837,113,268],'sc7':[64,152,193,268],'sc9':[285,372,191,264]}
    def choosescene():
        global scene,scenecoords
        scene=random.choice(list(scenelist.keys()))
        scenecoords=scenelist[scene]
        if scene=='sc1':
            del scenelist[scene]
            scenelist.update({'sc2':[193,271,535,583]})
        elif scene=='sc2':
            del scenelist[scene]
            scenelist.update({'sc1':[193,271,388,432]})
        elif scene=='sc7':
            del scenelist[scene]
            scenelist.update({'sc8':[67,152,90,157]})
        elif scene=='sc8':
            del scenelist[scene]
            scenelist.update({'sc7':[64,152,193,268]})
        elif scene=='sc9':
            del scenelist[scene]
            scenelist.update({'sc10':[283,374,87,156]})
        elif scene=='sc10':
            del scenelist[scene]
            scenelist.update({'sc9':[285,372,191,264]})
        else:
            del scenelist[scene]
        
    def loadscreen(x):
        layout=Layout1()
        while True:
            layout.surf=pygame.image.load(x+'.png')
            layout.rect=layout.surf.get_rect(midbottom=(625,650))
            screen1.blit(layout.surf,layout.rect)
            layout.surf10=pygame.image.load('exit.png').convert_alpha()
            layout.rect10=layout.surf10.get_rect(midbottom=(1150,640))
            screen1.blit(layout.surf10,layout.rect10)
            mouse=pygame.mouse.get_pos()
            for i in pygame.event.get():
                if i.type==pygame.MOUSEBUTTONDOWN:
                    if (mouse[0]>1070 and mouse[0]<1230) and (mouse[1]>567 and mouse[1]<628):
                        pygame.quit()
                        sys.exit()
                        break
            pygame.display.update()
        
    class Layout1():
    ##########screen################
        global screen1,myfont,tfont
        myfont=pygame.font.SysFont('Arial',18)
        tfont=pygame.font.SysFont('Consolas',80)
        width=1250
        height=650
        screen1=pygame.display.set_mode((width,height))
        clock=pygame.time.Clock()
        gray=(175,175,175)
        screen1.fill(gray)
        dgray=(49,79,79)
        black=(0,0,0)
        ##############
        pygame.draw.lines(screen1,dgray, False, [(0,1), (1250,1)], 5)
        pygame.draw.lines(screen1,dgray, False, [(0,325), (900,325)], 5)
        pygame.draw.lines(screen1,dgray, False, [(450,0), (450,650)], 5)
        pygame.draw.lines(screen1,dgray, False, [(1,0), (1,650)], 5)
        pygame.draw.lines(screen1,dgray, False, [(900,0), (900,650)], 5)
        pygame.draw.lines(screen1,dgray, False, [(450,270), (900,270)], 5)
        pygame.draw.lines(screen1,dgray, False, [(450,36), (900,36)], 5)
        pygame.draw.lines(screen1,dgray, False, [(126,325), (126,650)], 5)
        pygame.draw.lines(screen1,dgray, False, [(333,325), (333,650)], 5)
        pygame.draw.lines(screen1,dgray, False, [(0,649), (1250,649)], 15)
        pygame.draw.lines(screen1,dgray, False, [(1248,0), (1248,650)], 5)
        pygame.draw.lines(screen1,dgray, False, [(900,550), (1250,550)], 5)
        pygame.draw.lines(screen1,dgray, False, [(530,0), (530,325)], 5)
        pygame.draw.lines(screen1,dgray, False, [(630,0), (630,325)], 5)
        pygame.draw.lines(screen1,dgray, False, [(730,0), (730,325)], 5)
        pygame.draw.lines(screen1,dgray, False, [(830,0), (830,325)], 5)
        pygame.draw.lines(screen1,dgray, False, [(0,303), (450,303)], 5)
        pygame.draw.lines(screen1,dgray, False, [(0,40), (450,40)], 5)
        pygame.draw.lines(screen1,dgray, False, [(197,0), (197,325)], 5)
        pygame.draw.lines(screen1,dgray, False, [(241,0), (241,325)], 5)
        pygame.draw.lines(screen1,dgray, False, [(50,170), (241,170)], 5)
        def __init__(self):
            self.surf=pygame.image.load('s2.jpg').convert_alpha()
            self.rect=self.surf.get_rect(midbottom=(230,640))
            self.surf1=pygame.image.load('orangec.png').convert_alpha()
            self.rect1=self.surf1.get_rect(midbottom=(530,298))
            self.surf2=pygame.image.load('purplec.png').convert_alpha()
            self.rect2=self.surf2.get_rect(midbottom=(630,298))
            self.surf3=pygame.image.load('brownc.png').convert_alpha()
            self.rect3=self.surf3.get_rect(midbottom=(730,298))
            self.surf4=pygame.image.load('grayc.png').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(830,298))
            self.surf5=pygame.image.load('text.png').convert_alpha()
            self.rect5=self.surf5.get_rect(midbottom=(1080,428))
            self.surf6=pygame.image.load('διακοπτης2.jpg').convert_alpha()
            self.rect6=self.surf6.get_rect(midbottom=(110,300))
            self.surf7=pygame.image.load('διακοπτης2.jpg').convert_alpha()
            self.rect7=self.surf7.get_rect(midbottom=(330,300))
            self.surf10=pygame.image.load('exit.png').convert_alpha()
            self.rect10=self.surf10.get_rect(midbottom=(1150,640))
            self.timer=tfont.render('',0,(0,0,0)).convert_alpha()
            self.rect_t=self.timer.get_rect(midbottom=(673,525))
        def draw(self):
            screen1.blit(self.surf,self.rect)
            screen1.blit(self.surf1,self.rect1)
            screen1.blit(self.surf2,self.rect2)
            screen1.blit(self.surf3,self.rect3)
            screen1.blit(self.surf4,self.rect4)
            screen1.blit(self.surf5,self.rect5)
            screen1.blit(self.surf6,self.rect6)
            screen1.blit(self.surf7,self.rect7)
            screen1.blit(self.surf10,self.rect10)
            screen1.blit(self.timer,self.rect_t)
    class Inter1():
        layout=Layout1()
        layout.draw()        
        x=60
        import socket
        import sys
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ip
        port = 8888
        try:
            soc.connect((host, port))
        except:
            load('conerrorscreen')
            print("Connection error")
            sys.Exit()

        choosescene()
        mes='1.'+scene
        try:
            soc.sendall(mes.encode("utf8"))
        except:
            loadscreen('conerrorscreen')
            sys.exit()
            
        l=[]
        con1=None
        con2=None
        done=False
        error=False
        while x>0 and done==False and error==False:
            c=Buttons.scenaria(scenecoords[0],scenecoords[1],scenecoords[2],scenecoords[3],scene)
            message ='fine'
            try:
                soc.sendall(message.encode("utf8"))
                data=soc.recv(5120).decode("utf8")
                if data!='0':
                    
                    if 'Player2' in data:
                        if 'sc1.2' in data:
                            ins='redbutton'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc2.2' in data:
                            ins='yellowbutton'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc3.2'in data:
                            ins='greenbutton'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc4.2' in data:
                            ins='press1'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc5.2' in data:
                            ins='press2'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc6.2' in data:
                            ins='press3'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc7.2' in data:
                            ins='press4'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc8.2' in data:
                            ins='press5'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc9.2' in data:
                            ins='press6'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc10.2' in data:
                            ins='press7'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc11.2' in data:
                            ins='press8'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc12.2' in data:
                            ins='press9'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc13.2'in data:
                            ins='press0'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc14.2' in data:
                            ins='blackcable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc15.2' in data:
                            ins='redcable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc16.2' in data:
                            ins='greencable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc17.2' in data:
                            ins='yellowcable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc18.2' in data:
                            ins='bluecable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'sc19.2' in data:
                            ins='press6'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen1.blit(layout.surf5,layout.rect5)
                        elif 'done2' in data:
                            con2='fin'
                    elif 'Player1' in data:
                        if 'done1' in data:
                            con1='fin'
                    elif 'wcable' in data:
                        x=0
                    elif 'timer' in data:
                        x-=1
                    elif 'wrong' in data:
                        x-=4
                    
            except:
                error=True
                print('Connection Error')
            if len(l)==10:
                try:
                    soc.sendall('done1'.encode('utf8'))
                except:error=True
            if con1=='fin' and con2=='fin':
                done=True

            layout.timer=pygame.image.load('black.png').convert_alpha()
            layout.rect_t=layout.timer.get_rect(midbottom=(673,550))
            screen1.blit(layout.timer,layout.rect_t)
            layout.timer=tfont.render('{}'.format(x),0,(255,0,0),).convert_alpha()
            layout.rect_t=layout.timer.get_rect(midbottom=(673,525))
            screen1.blit(layout.timer,layout.rect_t)
            mouse=pygame.mouse.get_pos()
                ###
            if mouse[0]>0 and mouse[0]<1250 and mouse[1]>0 and mouse[1]<650:layout.draw()
                ###
            if pygame.mouse.get_pressed()[0]:
                if (mouse[0]>193 and mouse[0]<271) and (mouse[1]>535 and mouse[1]<583):
                    layout.surf=pygame.image.load('s2.jpg').convert_alpha()
                    layout.rect=layout.surf.get_rect(midbottom=(230,640))
                    screen1.blit(layout.surf,layout.rect)
                elif (mouse[0]>193 and mouse[0]<271) and (mouse[1]>388 and mouse[1]<432):
                    layout.surf=pygame.image.load('s1.jpg').convert_alpha()
                    layout.rect=layout.surf.get_rect(midbottom=(230,640))
                    screen1.blit(layout.surf,layout.rect)
                elif (mouse[0]>523 and mouse[0]<537) and (mouse[1]>113 and mouse[1]<268):
                    layout.surf1=pygame.image.load('orangec2.png').convert_alpha()
                    layout.rect1=layout.surf1.get_rect(midbottom=(530,298))
                    screen1.blit(layout.surf1,layout.rect1)
                elif (mouse[0]>622 and mouse[0]<637) and (mouse[1]>113 and mouse[1]<268):
                    layout.surf2=pygame.image.load('purplec2.png').convert_alpha()
                    layout.rect2=layout.surf2.get_rect(midbottom=(630,298))
                    screen1.blit(layout.surf2,layout.rect2)
                elif (mouse[0]>722 and mouse[0]<737) and (mouse[1]>113 and mouse[1]<268):
                    layout.surf3=pygame.image.load('brownc2.png').convert_alpha()
                    layout.rect3=layout.surf3.get_rect(midbottom=(730,298))
                    screen1.blit(layout.surf3,layout.rect3)
                elif (mouse[0]>822 and mouse[0]<837) and (mouse[1]>113 and mouse[1]<268):
                    layout.surf4=pygame.image.load('grayc2.png').convert_alpha()
                    layout.rect4=layout.surf4.get_rect(midbottom=(830,298))
                    screen1.blit(layout.surf4,layout.rect4)
                elif (mouse[0]>64 and mouse[0]<152) and (mouse[1]>193 and mouse[1]<260):
                    layout.surf6=pygame.image.load('διακοπτης1.jpg').convert_alpha()
                    layout.rect6=layout.surf6.get_rect(midbottom=(110,300))
                    screen1.blit(layout.surf6,layout.rect6)
                elif (mouse[0]>67 and mouse[0]<152) and (mouse[1]>90 and mouse[1]<157):
                    layout.surf6=pygame.image.load('διακοπτης2.jpg').convert_alpha()
                    layout.rect6=layout.surf6.get_rect(midbottom=(110,300))
                    screen1.blit(layout.surf6,layout.rect6)
                elif (mouse[0]>285 and mouse[0]<372) and (mouse[1]>191 and mouse[1]<264):
                    layout.surf7=pygame.image.load('διακοπτης1.jpg').convert_alpha()
                    layout.rect7=layout.surf7.get_rect(midbottom=(330,300))
                    screen1.blit(layout.surf7,layout.rect7)
                elif (mouse[0]>283 and mouse[0]<374) and (mouse[1]>87 and mouse[1]<156):
                    layout.surf7=pygame.image.load('διακοπτης2.jpg').convert_alpha()
                    layout.rect7=layout.surf7.get_rect(midbottom=(330,300))
                    screen1.blit(layout.surf7,layout.rect7)
                        ##########
                elif (mouse[0]>1070 and mouse[0]<1230) and (mouse[1]>567 and mouse[1]<628):
                    pygame.quit()
                    break
                        ##########
          
        
            # s1-->on
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if i.type==pygame.MOUSEBUTTONDOWN:
                    c=Buttons.scenaria(scenecoords[0],scenecoords[1],scenecoords[2],scenecoords[3],scene)
                    state=Buttons.scenaria.checkcoord(c)
                    if state=='ACK':
                        l.append('ACK')
                        choosescene()
                        mes='1.'+scene
                        try:
                            soc.sendall(mes.encode("utf8"))
                        except:
                            error=True
                            print('Connecton Error')
                    else:
                        try:
                            soc.sendall(str(state).encode('utf8'))
                        except:
                            error=True
                            print('Connection Error')
            pygame.display.update()
        else:
            if x==0 or x<0:
                loadscreen('losescreen')
            elif done==True:
                loadscreen('winscreen')
            elif error==True:
                loadscreen('conerrorscreen')
                

if text=='Captain':
    scenelist={'sc1':[163,287,52,175],'sc2':[315,438,52,175],'sc3':[14,138,52,175],'sc4':[150,195,385,425],'sc5':[207,250,385,425],'sc6':[264,306,385,425],'sc7':[152,195,440,483],'sc8':[208,250,440,483],'sc9':[262,307,440,483],'sc10':[152,195,499,542],'sc11':[209,252,499,542],'sc12':[264,310,499,542],'sc13':[208,252,556,598],'sc14':[574,587,112,272],'sc15':[622,636,112,272],'sc16':[672,687,112,272],'sc17':[723,737,112,272],'sc18':[774,789,112,272]}
    def choosescene2():
        global scene,scenecoords
        layout=Layout2()
        try:
            scene=random.choice(list(scenelist.keys()))
            scenecoords=scenelist[scene]
            del scenelist[scene]
        except:
            pass
    def loadscreen(x):
        layout=Layout2()
        while True:
            layout.surf=pygame.image.load(x+'.png')
            layout.rect=layout.surf.get_rect(midbottom=(625,650))
            screen.blit(layout.surf,layout.rect)
            layout.surf10=pygame.image.load('exit.png').convert_alpha()
            layout.rect10=layout.surf10.get_rect(midbottom=(1150,640))
            screen.blit(layout.surf10,layout.rect10)
            mouse=pygame.mouse.get_pos()
            for i in pygame.event.get():
                if i.type==pygame.MOUSEBUTTONDOWN:
                    if (mouse[0]>1070 and mouse[0]<1230) and (mouse[1]>567 and mouse[1]<628):
                        pygame.quit()
                        sys.exit()
                        break
            pygame.display.update()
            clock.tick(60)
    class Layout2():
    ##########screen################
        global screen,tfont,myfont
        myfont=pygame.font.SysFont('Arial',18)
        tfont=pygame.font.SysFont('Consolas',80)
        width=1250
        height=650
        screen=pygame.display.set_mode((width,height))
        clock=pygame.time.Clock()
        gray=(175,175,175)
        screen.fill(gray)
        dgray=(49,79,79)
        black=(0,0,0)
        pygame.draw.lines(screen,dgray, False, [(0,1), (1250,1)], 5)
        pygame.draw.lines(screen,dgray, False, [(0,325), (900,325)], 5)
        pygame.draw.lines(screen,dgray, False, [(450,0), (450,650)], 5)
        pygame.draw.lines(screen,dgray, False, [(1,0), (1,650)], 5)
        pygame.draw.lines(screen,dgray, False, [(900,0), (900,650)], 5)
        pygame.draw.lines(screen,dgray, False, [(75,0), (75,325)], 3)
        pygame.draw.lines(screen,dgray, False, [(225,0), (225,325)], 3)
        pygame.draw.lines(screen,dgray, False, [(375,0), (375,325)], 3)
        pygame.draw.lines(screen,dgray, False, [(450,272), (900,272)], 5)
        pygame.draw.lines(screen,dgray, False, [(450,37), (900,37)], 5)
        pygame.draw.lines(screen,dgray, False, [(0,621), (450,621)], 5)
        pygame.draw.lines(screen,dgray, False, [(0,362), (450,362)], 5)
        pygame.draw.lines(screen,dgray, False, [(126,325), (126,650)], 5)
        pygame.draw.lines(screen,dgray, False, [(333,325), (333,650)], 5)
        pygame.draw.lines(screen,dgray, False, [(0,649), (1250,649)], 10)
        pygame.draw.lines(screen,dgray, False, [(1248,0), (1248,650)], 5)
        pygame.draw.lines(screen,dgray, False, [(900,550), (1250,550)], 5)
        def __init__(self):
            self.surf=pygame.image.load('greenb.png').convert_alpha()
            self.rect=self.surf.get_rect(midbottom=(75,200))
            self.surf1=pygame.image.load('redb.png').convert_alpha()
            self.rect1=self.surf1.get_rect(midbottom=(225,200))
            self.surf2=pygame.image.load('yellowb.png').convert_alpha()
            self.rect2=self.surf2.get_rect(midbottom=(375,200))
            self.surf3=pygame.image.load('blackc.png').convert_alpha()
            self.rect3=self.surf3.get_rect(midbottom=(580,300))
            self.surf4=pygame.image.load('pad.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
            self.surf5=pygame.image.load('text.png').convert_alpha()
            self.rect5=self.surf5.get_rect(midbottom=(1080,428))
            self.surf6=pygame.image.load('redc.png').convert_alpha()
            self.rect6=self.surf6.get_rect(midbottom=(630,300))
            self.surf7=pygame.image.load('greenc.png').convert_alpha()
            self.rect7=self.surf7.get_rect(midbottom=(680,300))
            self.surf8=pygame.image.load('yellowc.png').convert_alpha()
            self.rect8=self.surf8.get_rect(midbottom=(730,300))
            self.surf9=pygame.image.load('bluec.png').convert_alpha()
            self.rect9=self.surf9.get_rect(midbottom=(780,300))
            self.surf10=pygame.image.load('exit.png').convert_alpha()
            self.rect10=self.surf10.get_rect(midbottom=(1150,640))
            self.timer=tfont.render('',0,(0,0,0)).convert_alpha()
            self.rect_t=self.timer.get_rect(midbottom=(673,525))
        def draw(self):
            screen.blit(self.surf,self.rect)
            screen.blit(self.surf1,self.rect1)
            screen.blit(self.surf2,self.rect2)
            screen.blit(self.surf3,self.rect3)
            screen.blit(self.surf4,self.rect4)
            screen.blit(self.surf5,self.rect5)
            screen.blit(self.surf6,self.rect6)
            screen.blit(self.surf7,self.rect7)
            screen.blit(self.surf8,self.rect8)
            screen.blit(self.surf9,self.rect9)
            screen.blit(self.surf10,self.rect10)
            screen.blit(self.timer,self.rect_t)
    ###  BUTTONS   ###
    class GreenButton():
        def __init__(self):
            self.surf=pygame.image.load('greenb2.png').convert_alpha()
            self.rect=self.surf.get_rect(midbottom=(75,200))
        def draw(self):
            screen.blit(self.surf,self.rect)
    class RedButton():
        def __init__(self):
            self.surf1=pygame.image.load('redb2.png').convert_alpha()
            self.rect1=self.surf1.get_rect(midbottom=(225,200))
        def draw(self):
            screen.blit(self.surf1,self.rect1)
    class YellowButton():
        def __init__(self):
            self.surf2=pygame.image.load('yellowb2.png').convert_alpha()
            self.rect2=self.surf2.get_rect(midbottom=(375,200))
        def draw(self):
            screen.blit(self.surf2,self.rect2)
    ###  BUTTONS END  ###

    ### PAD ###

    class Pad0():
        def __init__(self):
            self.surf4=pygame.image.load('pad0.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad1():
        def __init__(self):
            self.surf4=pygame.image.load('pad1.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad2():
        def __init__(self):
            self.surf4=pygame.image.load('pad2.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad3():
        def __init__(self):
            self.surf4=pygame.image.load('pad3.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad4():
        def __init__(self):
            self.surf4=pygame.image.load('pad4.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad5():
        def __init__(self):
            self.surf4=pygame.image.load('pad5.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad6():
        def __init__(self):
            self.surf4=pygame.image.load('pad6.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad7():
        def __init__(self):
            self.surf4=pygame.image.load('pad7.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad8():
        def __init__(self):
            self.surf4=pygame.image.load('pad8.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Pad9():
        def __init__(self):
            self.surf4=pygame.image.load('pad9.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Padast():
        def __init__(self):
            self.surf4=pygame.image.load('padast.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Paddi():
        def __init__(self):
            self.surf4=pygame.image.load('paddie.jpg').convert_alpha()
            self.rect4=self.surf4.get_rect(midbottom=(230,620))
        def draw(self):
            screen.blit(self.surf4,self.rect4)
    class Inter2():
        layout=Layout2()
        layout.draw()
        gb=GreenButton()
        rb=RedButton()
        yb=YellowButton()
        p1=Pad1()
        p2=Pad2()
        p3=Pad3()
        p4=Pad4()
        p5=Pad5()
        p6=Pad6()
        p7=Pad7()
        p8=Pad8()
        p9=Pad9()
        p0=Pad0()
        past=Padast()
        pdi=Paddi()
        turn=0
        x=60
        import socket
        import sys
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ip
        port = 8888
        try:
            soc.connect((host, port))
        except:
            loadscreen('conerrorscreen')
            print("Connection error")
            sys.exit()
#############################################################
        choosescene2()
        mes='2.'+scene
        try:
            soc.sendall(mes.encode("utf8"))
        except:
            loadscreen('conerrorscreen')
            sys.Exit()
        l=[]
        con1=None
        con2=None
        done=False
        error=False
        while x>0 and done==False and error==False:
            message = 'fine'
            try:
                soc.sendall(message.encode("utf8"))
                data=soc.recv(5120).decode("utf8")
                if data!='0':
                    if 'Player1' in data:
                        if 'sc1.1' in data:
                            ins='tswitchon'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc2.1' in data:
                            ins='tswitchoff'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc3.1'in data:
                            ins='orangecable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc4.1' in data:
                            ins='purplecable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc5.1' in data:
                            ins='browncable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc6.1' in data:
                            ins='graycable'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc7.1' in data:
                            ins='openlswitch'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc8.1' in data:
                            ins='closelswitch'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc9.1' in data:
                            ins='openrswitch'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'sc10.1' in data:
                            ins='closerswitch'
                            layout.surf5=pygame.image.load(ins+'.png').convert_alpha()
                            layout.rect5=layout.surf5.get_rect(midbottom=(1080,428))
                            screen.blit(layout.surf5,layout.rect5)
                        elif 'done1' in data:
                            con1='fin'
                    elif 'Player2' in data:
                        if 'done2' in data:
                            con2='fin'
                    elif 'wcable' in data:
                        x=0
                    elif 'timer' in data:
                        x-=1
                    elif 'wrong' in data:
                        x-=4
                    
            except:
                print('Connection Error')
                error=True
            if len(l)==10:
                try:
                    soc.sendall('done2'.encode('utf8'))
                    
                except:error=True
            if con1=='fin' and con2=='fin':
                done=True
            
            layout.timer=pygame.image.load('black.png').convert_alpha()
            layout.rect_t=layout.timer.get_rect(midbottom=(673,550))
            screen.blit(layout.timer,layout.rect_t)
            layout.timer=tfont.render('{}'.format(x),0,(255,0,0),).convert_alpha()
            layout.rect_t=layout.timer.get_rect(midbottom=(673,525))
            screen.blit(layout.timer,layout.rect_t)
            mouse=pygame.mouse.get_pos()
            ###
            if mouse[0]>0 and mouse[0]<1250 and mouse[1]>0 and mouse[1]<650:layout.draw()
            ###
            if (mouse[0]>163 and mouse[0]<287) and (mouse[1]>52 and mouse[1]<175):
                if pygame.mouse.get_pressed()[0]:
                    rb.draw()
                else:layout.draw()
            elif (mouse[0]>315 and mouse[0]<438) and (mouse[1]>52 and mouse[1]<175):
                if pygame.mouse.get_pressed()[0]:
                    yb.draw()
                else:layout.draw()
            elif (mouse[0]>14 and mouse[0]<138) and (mouse[1]>52 and mouse[1]<175):
                if pygame.mouse.get_pressed()[0]:
                    gb.draw()
                else:layout.draw()
            elif (mouse[0]>150 and mouse[0]<195) and (mouse[1]>385 and mouse[1]<425):
                if pygame.mouse.get_pressed()[0]:
                    p1.draw()
                else:layout.draw()
            elif (mouse[0]>207 and mouse[0]<250) and (mouse[1]>385 and mouse[1]<425):
                if pygame.mouse.get_pressed()[0]:
                    p2.draw()
                else:layout.draw()
            elif (mouse[0]>264 and mouse[0]<306) and (mouse[1]>385 and mouse[1]<425):
                if pygame.mouse.get_pressed()[0]:
                    p3.draw()
                else:layout.draw()
            elif (mouse[0]>152 and mouse[0]<195) and (mouse[1]>440 and mouse[1]<483):
                if pygame.mouse.get_pressed()[0]:
                    p4.draw()
                else:layout.draw()
            elif (mouse[0]>208 and mouse[0]<250) and (mouse[1]>440 and mouse[1]<483):
                if pygame.mouse.get_pressed()[0]:
                    p5.draw()
                else:layout.draw()
            elif (mouse[0]>262 and mouse[0]<307) and (mouse[1]>440 and mouse[1]<483):
                if pygame.mouse.get_pressed()[0]:
                    p6.draw()
                else:layout.draw()
            elif (mouse[0]>152 and mouse[0]<195) and (mouse[1]>499 and mouse[1]<542):
                if pygame.mouse.get_pressed()[0]:
                    p7.draw()
                else:layout.draw()
            elif (mouse[0]>209 and mouse[0]<252) and (mouse[1]>499 and mouse[1]<542):
                if pygame.mouse.get_pressed()[0]:
                    p8.draw()
                else:layout.draw()
            elif (mouse[0]>264 and mouse[0]<310) and (mouse[1]>499 and mouse[1]<542):
                if pygame.mouse.get_pressed()[0]:
                    p9.draw()
                else:layout.draw()
            elif (mouse[0]>151 and mouse[0]<194) and (mouse[1]>556 and mouse[1]<598):
                if pygame.mouse.get_pressed()[0]:
                    past.draw()
                else:layout.draw()
            elif (mouse[0]>208 and mouse[0]<252) and (mouse[1]>556 and mouse[1]<598):
                if pygame.mouse.get_pressed()[0]:
                    p0.draw()
                else:layout.draw()
            elif (mouse[0]>264 and mouse[0]<309) and (mouse[1]>556 and mouse[1]<598):
                if pygame.mouse.get_pressed()[0]:
                    pdi.draw()
                else:layout.draw()
        #############
            if pygame.mouse.get_pressed()[0]:
                if (mouse[0]>574 and mouse[0]<587) and (mouse[1]>112 and mouse[1]<272):
                    layout.surf3=pygame.image.load('blackc2.png').convert_alpha()
                    layout.rect3=layout.surf3.get_rect(midbottom=(580,300))
                    screen.blit(layout.surf3,layout.rect3)       
                elif (mouse[0]>622 and mouse[0]<636) and (mouse[1]>112 and mouse[1]<272):
                    layout.surf6=pygame.image.load('redc2.png').convert_alpha()
                    layout.rect6=layout.surf6.get_rect(midbottom=(630,300))
                    screen.blit(layout.surf6,layout.rect6)       
                elif (mouse[0]>672 and mouse[0]<687) and (mouse[1]>112 and mouse[1]<272):
                    layout.surf7=pygame.image.load('greenc2.png').convert_alpha()
                    layout.rect7=layout.surf7.get_rect(midbottom=(680,300))
                    screen.blit(layout.surf7,layout.rect7)      
                elif (mouse[0]>723 and mouse[0]<737) and (mouse[1]>112 and mouse[1]<272):
                    layout.surf8=pygame.image.load('yellowc2.png').convert_alpha()
                    layout.rect8=layout.surf8.get_rect(midbottom=(730,300))
                    screen.blit(layout.surf8,layout.rect8)        
                elif (mouse[0]>774 and mouse[0]<789) and (mouse[1]>112 and mouse[1]<272):
                   layout.surf9=pygame.image.load('bluec2.png').convert_alpha()
                   layout.rect9=layout.surf9.get_rect(midbottom=(780,300))
                   screen.blit(layout.surf9,layout.rect9) 
                ##########
                elif (mouse[0]>1070 and mouse[0]<1230) and (mouse[1]>567 and mouse[1]<628):
                    pygame.quit()
                    break
                ##########
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if i.type==pygame.MOUSEBUTTONDOWN:
                    c=Buttons.scenaria(scenecoords[0],scenecoords[1],scenecoords[2],scenecoords[3],scene)
                    state=Buttons.scenaria.checkcoord2(c)
                    if state=='ACK':
                        l.append('ACK')
                        choosescene2()
                        mes='2.'+scene
                        try:
                            soc.sendall(mes.encode("utf8"))
                        except:
                            error=True
                            print('Connection Error')
                    else:
                        try:
                            soc.sendall(str(state).encode('utf8'))
                        except:
                            error=True
                            print('Connection Error')
                  
            pygame.display.update()
            clock.tick(60)
        else:
            if x==0 or x<0:
                loadscreen('losescreen')
            elif done==True:
                loadscreen('winscreen')
            elif error==True:
                loadscreen('conerrorscreen')
