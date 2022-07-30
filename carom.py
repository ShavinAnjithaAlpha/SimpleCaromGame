from tkinter import*
import math
import random
import time
import image

root=Tk()
root.config(bg="#262c3d")

w=600
h=600
vx=float()
vy=float()
s=int()
score=int()
r=18
r2=14
r3=9
a=2.4
R=25
R2=20
spaceR=28
sq3=math.sqrt(3)
boardimg=PhotoImage(file="caromboard.gif")
line_r=80
kulaRed = ["#500000","#6e0000","#ff0000","#ff5050", "#ff8c8c", "#ffc8c8" ]
#,"#a00000",
list_ball=list()
n=19
list_ofxy=[(w/2,h/2),(w/2+2*r+2,h/2),(w/2-2*r-2,h/2),(w/2+r+2,h/2-sq3*r-2),(w/2+r+2,h/2+sq3*r+2),\
            (w/2-r-2,h/2-sq3*r-2),(w/2-r-2,h/2+sq3*r+2),(w/2+4*r+2,h/2),(w/2-4*r-2,h/2),(w/2+2*r+2,h/2-sq3*2*r-2),(w/2+2*r+2,h/2+sq3*2*r+2),\
            (w/2-2*r-2,h/2-sq3*2*r-2),(w/2-2*r-2,h/2+sq3*2*r+2), (w/2,h/2-4*r), (w/2,h/2+4*r), (w/2+3*r+2,h/2-sq3*r-2), \
            (w/2+3*r+2,h/2+sq3*r+2), (w/2-3*r-2,h/2+sq3*r+2), (w/2-3*r-2,h/2-sq3*r-4)]




for i in range(0,n):
    vx=random.randrange(-800,800)
    vy=random.randrange(-800,800)
    color=random.randint(0,1)
    x=random.randrange(r,w-r)
    y=random.randrange(r,h-r)
    ball={"x": list_ofxy[i][0],
            "y" : list_ofxy[i][1],
            "vx" : 0,
            "vy" : 0,
            "id": str(i)+"ball",
            "color":color,
        }
    list_ball.append(ball)



main_disc={"x": w/2,
            "y" : h/2,
            "vx" : 258,
            "vy" : 356,
            "id": "main_ball",
       }

def new():
    global main_disc,s
    main_disc["vx"]=0
    main_disc["vy"]=0
    main_disc["x"]=w/2
    main_disc["y"]=h-line_r-R
    s=0
    canvas.delete("main_ball")
    canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
    canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])
    canvas_scale.delete("scale_disc")
    canvas_scale.create_oval(main_disc["x"]-R,25-R,main_disc["x"]+R,25+R,fill="black",width=0,tag="scale_disc")
    canvas_scale.create_oval(main_disc["x"]-R2,25-R2,main_disc["x"]+R2,25+R2,fill="white",tag="scale_disc")

def scale_disc(event):
    if event.x>line_r+R and event.x<w-line_r-R:
        canvas_scale.delete("scale_disc")
        canvas_scale.create_oval(event.x-R,26-R,event.x+R,26+R,fill="black",width=0,tag="scale_disc")
        canvas_scale.create_oval(event.x-R2,26-R2,event.x+R2,26+R2,fill="white",tag="scale_disc")
        main_disc["x"]=event.x
        main_disc["y"]=h-line_r-R
        canvas.delete("main_ball")
        canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])


def getsin_cos(tantheta, type_trig):
    if type_trig=="sin":
        cot=1/tantheta
        cosec=math.sqrt(1+pow(cot,2))
        sin=1/cosec
        return sin
    elif type_trig=="cos":
        sec=math.sqrt(1+pow(tantheta,2))
        cos=1/sec
        return cos


def set_maindisc_velocity(event):
    click_x,click_y=main_disc["x"],main_disc["y"]
    l=math.sqrt(pow(click_x-event.x,2)+pow(click_y-event.y,2))
    main_disc["vx"]=30*l*((click_x-event.x)/l)
    main_disc["vy"]=30*l*((event.y-click_y)/l)
    canvas.delete("vline")
    canvas.create_line(click_x,click_y,click_x+(click_x-event.x),click_y-(event.y-click_y),fill="yellow",tag="vline",width="2")
   # canvas.create_line(event.x,event.y,click_x,click_y,fill="yellow",tag="vline",width="2",dash=(200,1))
    canvas.create_oval(click_x-l,click_y-l,click_x+l,click_y+l,outline="yellow",tag="vline",width="2",dash=(100,2))
    



def set_velocity(ball_1,ball_2):
    vx1=ball_1["vx"]
    vx2=ball_2["vx"]

    vy1=ball_1["vy"]
    vy2=ball_2["vy"]

    ball_1["vx"]=vx2*0.9-(vx1+vx2)*0.02
    ball_2["vx"]=vx1*0.9+(vx1+vx2)*0.02
    ball_1["vy"]=vy2*0.9+(vy1+vy2)*0.02
    ball_2["vy"]=vy1*0.9-(vy1+vy2)*0.02
   
    


      
def start(event):
    global r,ball_list,a,r2,r3,R,main_disc,s
    s=1
    canvas.delete("vline")
    while s==1:
        for b in list_ball:
            if math.sqrt(pow(b["y"]-main_disc["y"],2)+pow(b["x"]-main_disc["x"],2))<r+R:
                            set_velocity(b,main_disc)
                            l1=math.sqrt(pow(b["y"]-main_disc["y"],2)+pow(b["x"]-main_disc["x"],2))
                            b["x"]=main_disc["x"]+(R+r)*((b["x"]-main_disc["x"])/l1)
                            b["y"]=main_disc["y"]-(R+r)*((main_disc["y"]-b["y"])/l1)
        if main_disc["vx"]>0:
                am=-a*main_disc["vx"]
        elif main_disc["vx"]<0:
                am=-a*main_disc["vx"]
        elif main_disc["vx"]==0:
                am=0
        if main_disc["vy"]>0:
                    an=-a*main_disc["vy"]
        elif main_disc["vy"]<0:
                    an=-a*main_disc["vy"]
        elif main_disc["vy"]==0:
                    an=0
        main_disc["vx"]+=am*0.01
        main_disc["vy"]+=an*0.01
        ############
        main_disc["x"]+=main_disc["vx"]*0.01
        main_disc["y"]+=(-main_disc["vy"]*0.01)
        ###############
        if main_disc["x"]+R>w :
                main_disc["vx"]=-main_disc["vx"]
                main_disc["x"]=w-R
        if  main_disc["x"]-R<0:
                 main_disc["vx"]=-main_disc["vx"]
                 main_disc["x"]=R
        if main_disc["y"]+R>h or main_disc["y"]-R<0:
                main_disc["vy"]=-main_disc["vy"]
        canvas.delete("main_ball")
        canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,width=0,fill="white",tag=main_disc["id"])



        
        for b1 in list_ball:
            if not(b1["vx"]==0 and b1["vy"]==0):
                for b2 in list_ball:
                    if not(b1==b2):
                        if math.sqrt(pow(b1["y"]-b2["y"],2)+pow(b1["x"]-b2["x"],2))<2*r:
                            set_velocity(b1,b2)
                            l=math.sqrt(pow(b1["y"]-b2["y"],2)+pow(b1["x"]-b2["x"],2))
                            tantheta=b1["y"]-b2["y"]/(b2["x"]-b1["x"])
                            b2["x"]=b1["x"]+2*r*((b2["x"]-b1["x"])/(l))
                            b2["y"]=b1["y"]-2*r*((b1["y"]-b2["y"])/(l))
                if b1["vx"]>0:
                    ax=-a*b1["vx"]
                elif b1["vx"]<0:
                    ax=-a*b1["vx"]
                elif b1["vx"]==0:
                    ax=0
                ############
                if b1["vy"]>0:
                    ay=-a*b1["vy"]
                elif b1["vy"]<0:
                    ay=-a*b1["vy"]
                elif abs(b1["vy"])==0:
                    ay=0
                b1["vx"]+=ax*0.01
                b1["vy"]+=ay*0.01
                ############
                b1["x"]+=b1["vx"]*0.01
                b1["y"]+=(-b1["vy"]*0.01)
                ###############
                if b1["x"]+r>w :
                    b1["vx"]=-b1["vx"]
                    b1["x"]=w-r
                if  b1["x"]-r<0:
                    b1["vx"]=-b1["vx"]
                    b1["x"]=r
                if b1["y"]+r>h or b1["y"]-r<0:
                    b1["vy"]=-b1["vy"]
                ########################    
                ####################disk_fallen_to_space
                if math.sqrt(pow(b1["x"]-spaceR,2)+pow(b1["y"]-spaceR,2))<spaceR and (b1["vx"]<100) and b1["vy"]<100:
                    b1["vx"]=0
                    b1["vy"]=0
                    b1["x"]=1000000
                    b1["y"]=100000
                    time.sleep(0.2)
                ################
                canvas.delete(b1["id"])
                if b1["color"]==1:
                    canvas.create_oval(b1["x"]-r,b1["y"]-r,b1["x"]+r,b1["y"]+r,fill="#692000000", width="0",tag=b1["id"],outline=None)
                    canvas.create_oval(b1["x"]-r2,b1["y"]-r2,b1["x"]+r2,b1["y"]+r2,fill="#a18000000",width="0", tag=b1["id"],outline="#a18000000")
                    canvas.create_oval(b1["x"]-r3,b1["y"]-r3,b1["x"]+r3,b1["y"]+r3,fill="#edb000000", width="0",tag=b1["id"],outline="#edb000000")
                else:
                    canvas.create_oval(b1["x"]-r,b1["y"]-r,b1["x"]+r,b1["y"]+r,fill="black", width="0",tag=b1["id"],outline=None)
                    canvas.create_oval(b["x"]-r2,b["y"]-r2,b["x"]+r2,b["y"]+r2,fill="#00030c418",width="0", tag=b["id"],outline="#a18000000")
                    canvas.create_oval(b["x"]-r3,b["y"]-r3,b["x"]+r3,b["y"]+r3,fill="#30c2c330c", width="0",tag=b["id"],outline="#edb000000")
                ######################
                n=0
                for disk in list_ball:
                    if abs(disk["vx"])<10 and abs(disk["vy"])<10:
                        n+=1
                if abs(main_disc["vx"])<10 and abs(main_disc["vy"])<10:
                    n+=1
                if n==20:
                    new()
                #######################################
       
        canvas.update()
        canvas.after(10)



canvas=Canvas(root,width=w,height=h,bg="#ac24003b7")
canvas.grid(row=1,column=0)
canvas.create_image(0,0,image=boardimg)

canvas_scale=Canvas(root,width=w,height="52",bg="brown")
canvas_scale.grid(row=2,column=0)
canvas_scale.create_oval(w/2-R,26-R,w/2+R,26+R,fill="black",tag="scale_disc")
canvas_scale.create_oval(w/2-R2,26-R2,w/2+R2,26+R2,fill="white",tag="scale_disc")

canvas_scale.bind( "<B1-Motion>",scale_disc)

canvas.bind("<B1-Motion>", set_maindisc_velocity)
canvas.bind("<ButtonRelease-1>", start)
#############################################################carom_board_ovals
canvas.create_oval(line_r,h-line_r-2*R,line_r+2*R,h-line_r,fill="red",width=2,outline="blue")
canvas.create_oval(w-2*R-line_r,h-line_r-2*R,w-line_r,h-line_r,fill="red",width=2,outline="blue")
canvas.create_oval(line_r,line_r,line_r+2*R,line_r+2*R,fill="red",width=2,outline="blue")
canvas.create_oval(w-line_r,line_r,w-line_r-2*R,line_r+2*R,fill="red",width=2,outline="blue")
######################################################carom_board_blanks
canvas.create_oval(0,0,2*spaceR,2*spaceR,fill="black",outline="black")
canvas.create_oval(w-2*spaceR,0,w,2*spaceR,fill="black",outline="black")
canvas.create_oval(0,h-2*spaceR,2*spaceR,h,fill="black",outline="black")
canvas.create_oval(w-2*spaceR,h-2*spaceR,w,h,fill="black",outline="black")
################################################
canvas.create_line(line_r+R,line_r+R,200,200,width="2",fill="red")
canvas.create_line(w-line_r-R,line_r+R,w-200,200,width="2",fill="red")
canvas.create_line(line_r+R,h-line_r-R,200,h-200,width="2",fill="red")
canvas.create_line(w-line_r-R,h-line_r-R,w-200,h-200,width="2",fill="red")


##################################################carom_board_lines
canvas.create_line(line_r+R,h-line_r-2*R,w-line_r-R,h-line_r-2*R,fill="blue",width="2")
canvas.create_line(line_r+R,h-line_r,w-line_r-R,h-line_r,fill="blue",width="2")

canvas.create_line(line_r+R,line_r+2*R,w-line_r-R,line_r+2*R,fill="blue",width="2")
canvas.create_line(line_r+R,line_r,w-line_r-R,line_r,fill="blue",width="2")

canvas.create_line(line_r,line_r+R,line_r,h-line_r-R,fill="blue",width="2")
canvas.create_line(line_r+2*R,line_r+R,line_r+2*R,h-line_r-R,fill="blue",width="2")

canvas.create_line(w-line_r,line_r+R,w-line_r,h-line_r-R,fill="blue",width="2")
canvas.create_line(w-line_r-2*R,line_r+R,w-line_r-2*R,h-line_r-R,fill="blue",width="2")

canvas.create_oval(w/2-5*r,h/2-5*r,w/2+5*r,h/2+5*r,fill=None,outline="red",width="2")
canvas.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill=None,outline="black",width="2")
################################################################


for b in list_ball:
    if b["color"]==1:
        canvas.create_oval(b["x"]-r,b["y"]-r,b["x"]+r,b["y"]+r,fill="#692000000", width="0",tag=b["id"],outline=None)
        canvas.create_oval(b["x"]-r2,b["y"]-r2,b["x"]+r2,b["y"]+r2,fill="#a18000000",width="0", tag=b["id"],outline="#a18000000")
        canvas.create_oval(b["x"]-r3,b["y"]-r3,b["x"]+r3,b["y"]+r3,fill="#edb000000", width="0",tag=b["id"],outline="#edb000000")
    else:
        canvas.create_oval(b["x"]-r,b["y"]-r,b["x"]+r,b["y"]+r,fill="black", width="0",tag=b["id"],outline=None)
        canvas.create_oval(b["x"]-r2,b["y"]-r2,b["x"]+r2,b["y"]+r2,fill="#00030c418",width="0", tag=b["id"],outline="#a18000000")
        canvas.create_oval(b["x"]-r3,b["y"]-r3,b["x"]+r3,b["y"]+r3,fill="#30c2c330c", width="0",tag=b["id"],outline="#edb000000")
root.mainloop()
