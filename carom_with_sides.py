from tkinter import*
import math
import random
import time

root=Tk()
root.config(bg="#262c3d")

c=35
w=450+2*c
h=450+2*c
vx=float()
vy=float()
s=int()
score=int()
r=12
r2=9
r3=5
a=2.4
R=15
R2=10
spaceR=22
sq3=math.sqrt(3)
line_r=55
boardimg=PhotoImage(file="caromboard.gif")
partner="partner_2"
s_1=int()
s_2=int()

kulaRed = ["#500000","#6e0000","#ff0000","#ff5050", "#ff8c8c", "#ffc8c8" ]
#,"#a00000",
list_ball,list_fallen=list(),list()
n=19
list_ofxy=[(w/2,h/2),(w/2+2*r+2,h/2),(w/2-2*r-2,h/2),(w/2+r+2,h/2-sq3*r-2),(w/2+r+2,h/2+sq3*r+2),\
            (w/2-r-2,h/2-sq3*r-2),(w/2-r-2,h/2+sq3*r+2),(w/2+4*r+2,h/2),(w/2-4*r-2,h/2),(w/2+2*r+2,h/2-sq3*2*r-2),(w/2+2*r+2,h/2+sq3*2*r+2),\
            (w/2-2*r-2,h/2-sq3*2*r-2),(w/2-2*r-2,h/2+sq3*2*r+2), (w/2,h/2-4*r), (w/2,h/2+4*r), (w/2+3*r+2,h/2-sq3*r-2), \
            (w/2+3*r+2,h/2+sq3*r+2), (w/2-3*r-2,h/2+sq3*r+2), (w/2-3*r-2,h/2-sq3*r-4)]




for i in range(0,n):
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
    global main_disc,s,partner
    s=0
    if partner=="partner_1":
            partner="partner_2"
    elif partner=="partner_2":
            partner="partner_1"
    print(partner)
    main_disc["vx"]=0
    main_disc["vy"]=0
    main_disc["x"]=w/2
    main_disc["y"]=h-line_r-R-c
    canvas.delete("main_ball")
    canvas_m.delete("main_ball")
    #canvas
    canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
    canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])
    #canvas_m
    canvas_m.create_oval(w-(main_disc["x"]-R),h-(main_disc["y"]-R),w-(main_disc["x"]+R),h-(main_disc["y"]+R),fill="black",width=0,tag=main_disc["id"])
    canvas_m.create_oval(w-(main_disc["x"]-R2),h-(main_disc["y"]-R2),w-(main_disc["x"]+R2),h-(main_disc["y"]+R2),fill="white",width=0,tag=main_disc["id"])
    canvas_scale.delete("scale_disc")
    canvas_scale.create_oval(main_disc["x"]-R,25-R,main_disc["x"]+R,25+R,fill="black",width=0,tag="scale_disc")
    canvas_scale.create_oval(main_disc["x"]-R2,25-R2,main_disc["x"]+R2,25+R2,fill="white",tag="scale_disc")
def set_score(color):
    global s_1,s_2,partner,s
    s=0
    if partner=="partner_1":
        partner="partner_2"
        if color==0:
            s_1+=5
        elif color==1:
            s_1+=10
    print(s_1,s_2)
    if partner=="partner_2":
        partner="partner_1"
        if color==0:
            s_2+=5
        elif color==1:
            s_2+=10
    print(s_1,s_2)
    

def scale_disc(event):
    if event.x>line_r+R+c and event.x<w-line_r-R-c and partner=="partner_1":
        canvas_scale.delete("scale_disc")
        canvas_scale.create_oval(event.x-R,17-R,event.x+R,17+R,fill="black",width=0,tag="scale_disc")
        canvas_scale.create_oval(event.x-R2,17-R2,event.x+R2,17+R2,fill="white",tag="scale_disc")
        main_disc["x"]=event.x
        main_disc["y"]=h-line_r-R-c
        canvas.delete("main_ball")
        canvas_m.delete("main_ball")
        canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])
        canvas_m.create_oval(w-main_disc["x"]-R,h-main_disc["y"]-R,w-main_disc["x"]+R,h-main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas_m.create_oval(w-main_disc["x"]-R2,h-main_disc["y"]-R2,w-main_disc["x"]+R2,h-main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])

def scale_disc_m(event):
    if event.x>line_r+R+c and event.x<w-line_r-R-c and partner=="partner_2":
        canvas_scale_m.delete("scale_disc_m")
        canvas_scale_m.create_oval(event.x-R,17-R,event.x+R,17+R,fill="black",width=0,tag="scale_disc_m")
        canvas_scale_m.create_oval(event.x-R2,17-R2,event.x+R2,17+R2,fill="white",tag="scale_disc_m")
        main_disc["x"]=w-event.x
        main_disc["y"]=line_r+R+c
        canvas.delete("main_ball")
        canvas_m.delete("main_ball")
        canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])
        canvas_m.create_oval(w-main_disc["x"]-R,h-main_disc["y"]-R,w-main_disc["x"]+R,h-main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas_m.create_oval(w-main_disc["x"]-R2,h-main_disc["y"]-R2,w-main_disc["x"]+R2,h-main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])



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
     if partner=="partner_1":
        click_x,click_y=main_disc["x"],main_disc["y"]
        l=math.sqrt(pow(click_x-event.x,2)+pow(click_y-event.y,2))
        main_disc["vx"]=35*l*((click_x-event.x)/l)
        main_disc["vy"]=35*l*((event.y-click_y)/l)
        canvas.delete("vline")
        canvas_m.delete("vline")
        canvas.create_line(click_x,click_y,click_x+(click_x-event.x),click_y-(event.y-click_y),fill="red",tag="vline",width="2")
        canvas_m.create_line(w-click_x,w-click_y,w-(click_x+(click_x-event.x)),h-(click_y-(event.y-click_y)),fill="red",tag="vline",width="2")
       # canvas.create_line(event.x,event.y,click_x,click_y,fill="yellow",tag="vline",width="2",dash=(200,1))
        canvas.create_oval(click_x-l,click_y-l,click_x+l,click_y+l,outline="white",tag="vline",width="2",dash=(50,2))
        canvas_m.create_oval(w-(click_x-l),h-(click_y-l),w-(click_x+l),h-(click_y+l),outline="white",tag="vline",width="2",dash=(50,2))

def set_maindisc_velocity_m(event):
    if partner=="partner_2":
        click_x,click_y=w-main_disc["x"],h-main_disc["y"]
        l=math.sqrt(pow(click_x-event.x,2)+pow(click_y-event.y,2))
        main_disc["vx"]=-35*l*((click_x-event.x)/l)
        main_disc["vy"]=-35*l*((event.y-click_y)/l)
        canvas.delete("vline")
        canvas_m.delete("vline")
        canvas_m.create_line(click_x,click_y,click_x+(click_x-event.x),click_y-(event.y-click_y),fill="red",tag="vline",width="2")
        canvas.create_line(w-click_x,h-click_y,w-(click_x+(click_x-event.x)),h-(click_y-(event.y-click_y)),fill="red",tag="vline",width="2")
       # canvas.create_line(event.x,event.y,click_x,click_y,fill="yellow",tag="vline",width="2",dash=(200,1))
        canvas_m.create_oval(click_x-l,click_y-l,click_x+l,click_y+l,outline="white",tag="vline",width="2",dash=(50,2))
        canvas.create_oval(w-(click_x-l),h-(click_y-l),w-(click_x+l),h-(click_y+l),outline="white",tag="vline",width="2",dash=(50,2))
        



def set_velocity(ball_1,ball_2):
    e=0.60514
    vx1=max((ball_1["vx"]),(ball_2["vx"]))
    vx2=min(ball_1["vx"],ball_2["vx"])

    vy1=max(ball_1["vy"],ball_2["vy"])
    vy2=min(ball_1["vy"],ball_2["vy"])
    if abs(ball_1["vx"])>abs(ball_2["vx"]):
        ball_1["vx"]=(1+e)*vx1/2+(1-e)*vx2/2
        ball_2["vx"]=(1-e)*vx1/2+(1+e)*vx2/2
    else:
          ball_2["vx"]=(1+e)*vx1/2+(1-e)*vx2/2
          ball_1["vx"]=(1-e)*vx1/2+(1+e)*vx2/2  
    if abs(ball_1["vy"])>abs(ball_2["vy"]):
        ball_1["vy"]=(1+e)*vy1/2+(1-e)*vy2/2
        ball_2["vy"]=(1-e)*vy1/2+(1+e)*vy2/2
    else:
          ball_2["vy"]=(1+e)*vy1/2+(1-e)*vy2/2
          ball_1["vy"]=(1-e)*vy1/2+(1+e)*vy2/2  
   
    


      
def start(event):
    global r,ball_list,a,r2,r3,R,main_disc,s,list_fallen,partner
    s=1
    canvas.delete("vline")
    canvas_m.delete("vline")
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
        if main_disc["x"]+R>w-c :
                main_disc["vx"]=-0.8*main_disc["vx"]
                main_disc["x"]=w-R-c
        if  main_disc["x"]-R<c:
                 main_disc["vx"]=-0.8*main_disc["vx"]
                 main_disc["x"]=R+c
        if main_disc["y"]+R>h-c: 
                main_disc["vy"]=-0.8*main_disc["vy"]
                main_disc["y"]=h-R-c
        if main_disc["y"]-R<c:
            main_disc["vy"]=-0.8*main_disc["vy"]
            main_disc["y"]=R+c
        canvas.delete("main_ball")
        canvas_m.delete("main_ball")
        canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,width=0,fill="white",tag=main_disc["id"])

        canvas_m.create_oval(w-main_disc["x"]-R,h-main_disc["y"]-R,w-main_disc["x"]+R,h-main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas_m.create_oval(w-main_disc["x"]-R2,h-main_disc["y"]-R2,w-main_disc["x"]+R2,h-main_disc["y"]+R2,width=0,fill="white",tag=main_disc["id"])



        
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
                    ax=-a*pow(b1["vx"],1)
                elif b1["vx"]<0:
                    ax=-a*pow(b1["vx"],1)
                elif b1["vx"]==0:
                    ax=0
                ############
                if b1["vy"]>0:
                    ay=-a*pow(b1["vy"],1)
                elif b1["vy"]<0:
                    ay=-a*pow(b1["vy"],1)
                elif abs(b1["vy"])==0:
                    ay=0
                b1["vx"]+=ax*0.003
                b1["vy"]+=ay*0.005
                ############
                b1["x"]+=b1["vx"]*0.003
                b1["y"]+=(-b1["vy"]*0.003)
                ###############
                if b1["x"]+r>w-c :
                    b1["vx"]=-0.9*b1["vx"]
                    b1["x"]=w-r-c
                if  b1["x"]-r<c:
                    b1["vx"]=-0.9*b1["vx"]
                    b1["x"]=r+c
                if b1["y"]+r>h-c: 
                    b1["vy"]=-0.9*b1["vy"]
                    b1["y"]=h-c-r
                if  b1["y"]-r<c:
                    b1["vy"]=-0.9*b1["vy"]
                    b1["y"]=c+r
                    
                ########################    
                
                ################
                canvas.delete(b1["id"])
                canvas_m.delete(b1["id"])
                if b1["color"]==1:
                    canvas.create_oval(b1["x"]-r,b1["y"]-r,b1["x"]+r,b1["y"]+r,fill="#fffe30000", width="0",tag=b1["id"],outline=None)
                    canvas.create_oval(b1["x"]-r2,b1["y"]-r2,b1["x"]+r2,b1["y"]+r2,fill="#f54f9ebb6",width="0", tag=b1["id"],outline="#a18000000")
                    canvas.create_oval(b1["x"]-r3,b1["y"]-r3,b1["x"]+r3,b1["y"]+r3,fill="#ffffff692", width="0",tag=b1["id"],outline="#edb000000")

                    canvas_m.create_oval(w-b1["x"]-r,h-b1["y"]-r,w-b1["x"]+r,h-b1["y"]+r,fill="#fffe30000", width="0",tag=b1["id"],outline=None)
                    canvas_m.create_oval(w-b1["x"]-r2,h-b1["y"]-r2,w-b1["x"]+r2,h-b1["y"]+r2,fill="#f54f9ebb6",width="0", tag=b1["id"],outline="#a18000000")
                    canvas_m.create_oval(w-b1["x"]-r3,h-b1["y"]-r3,w-b1["x"]+r3,h-b1["y"]+r3,fill="#ffffff692", width="0",tag=b1["id"],outline="#edb000000")

                else:
                    canvas.create_oval(b1["x"]-r,b1["y"]-r,b1["x"]+r,b1["y"]+r,fill="black", width="0",tag=b1["id"],outline=None)
                    canvas.create_oval(b1["x"]-r2,b1["y"]-r2,b1["x"]+r2,b1["y"]+r2,fill="black",width="0", tag=b1["id"],outline="#a18000000")
                    canvas.create_oval(b1["x"]-r3,b1["y"]-r3,b1["x"]+r3,b1["y"]+r3,fill="#30c2c330c", width="0",tag=b1["id"],outline="#edb000000")

                    canvas_m.create_oval(w-b1["x"]-r,h-b1["y"]-r,w-b1["x"]+r,h-b1["y"]+r,fill="black", width="0",tag=b1["id"],outline=None)
                    canvas_m.create_oval(w-b1["x"]-r2,h-b1["y"]-r2,w-b1["x"]+r2,h-b1["y"]+r2,fill="black",width="0", tag=b1["id"],outline="#a18000000")
                    canvas_m.create_oval(w-b1["x"]-r3,h-b1["y"]-r3,w-b1["x"]+r3,h-b1["y"]+r3,fill="#30c2c330c", width="0",tag=b1["id"],outline="#edb000000")
                ######################
                n=0
                for disk in list_ball:
                    if abs(disk["vx"])<4 and abs(disk["vy"])<4:
                        n+=1
                        #disk["vx"],disk["vy"]=0,0
                if abs(main_disc["vx"])<4 and abs(main_disc["vy"])<4:
                    n+=1
                    #main_disc["vx"],main_disc["vy"]=0,0
                if n==len(list_ball)+1:
                    new()
                    break
                #######################################
                ####################disk_fallen_to_space
                if (math.sqrt(pow(b1["x"]-(spaceR+c),2)+pow(b1["y"]-(spaceR+c),2))<spaceR
                    or math.sqrt(pow(b1["x"]-(w-spaceR-c),2)+pow(b1["y"]-(spaceR+c),2))<spaceR
                    or math.sqrt(pow(b1["x"]-(spaceR+c),2)+pow(b1["y"]-(h-spaceR-c),2))<spaceR
                    or math.sqrt(pow(b1["x"]-(w-spaceR-c),2)+pow(b1["y"]-(h-spaceR-c),2))<spaceR) and (abs(b1["vx"]<2000)) and abs(b1["vy"])<2000:
                    list_fallen.append(b1)
                    list_ball.remove(b1)
                    time.sleep(0.2)
                    canvas.delete(b1["id"])
                    canvas_m.delete(b1["id"])
                    set_score(b1["color"])
       
        canvas.update()
        canvas.after(3)



canvas=Canvas(root,width=w,height=h,bg="#ac24003b7")
canvas.grid(row=1,column=0)
canvas.create_image(0,0,image=boardimg)

canvas_m=Canvas(root,width=w,height=h,bg="#ac24003b7")
canvas_m.grid(row=1,column=2)
canvas_m.create_image(0,0,image=boardimg)

canvas_scale=Canvas(root,width=w,height="34",bg="brown")
canvas_scale.grid(row=2,column=0)
canvas_scale_m=Canvas(root,width=w,height="34",bg="brown")
canvas_scale_m.grid(row=2,column=2)
################origin_scale_disc
if partner=="partner_1":
    canvas_scale.create_oval(w/2-R,17-R,w/2+R,17+R,fill="black",tag="scale_disc")
    canvas_scale.create_oval(w/2-R2,17-R2,w/2+R2,17+R2,fill="white",tag="scale_disc")
    canvas_scale_m.create_oval(w/2-R,17-R,w/2+R,17+R,fill="red",tag="scale_disc_m")
elif partner=="partner_2":
    canvas_scale_m.create_oval(w/2-R,17-R,w/2+R,17+R,fill="black",tag="scale_disc_m")
    canvas_scale_m.create_oval(w/2-R2,17-R2,w/2+R2,17+R2,fill="white",tag="scale_disc_m")
    canvas_scale.create_oval(w/2-R,17-R,w/2+R,17+R,fill="red",tag="scale_disc",outline="red")
###############
canvas_scale.bind( "<B1-Motion>",scale_disc)
canvas_scale_m.bind( "<B1-Motion>",scale_disc_m)

canvas.bind("<B1-Motion>", set_maindisc_velocity)
canvas_m.bind("<B1-Motion>", set_maindisc_velocity_m)
canvas.bind("<ButtonRelease-1>", start)
canvas_m.bind("<ButtonRelease-1>", start)
####################carom_board_sides
ls=[(0,0,w,c),(0,h-c,w,h),(0,0,c,h),(w-c,0,w,h)]

for is1 in range(0,len(ls)):
    canvas.create_rectangle(ls[is1],fill="#7b61e8018",width=0)
    canvas_m.create_rectangle(ls[is1],fill="#7b61e8018",width=0)
#############################################################carom_board_ovals
l3=[(line_r+c,h-line_r-2*R-c,line_r+2*R+c,h-line_r-c),(w-2*R-line_r-c,h-line_r-2*R-c,w-line_r-c,h-line_r-c),\
    (line_r+c,line_r+c,line_r+2*R+c,line_r+2*R+c),(w-line_r-c,line_r+c,w-line_r-2*R-c,line_r+2*R+c)]

for i3 in range(0, len(l3)):
    canvas.create_oval(l3[i3],fill="red",width=2,outline="blue")
    canvas_m.create_oval(l3[i3],fill="red",width=2,outline="blue")

######################################################carom_board_blanks
l_blank=[(c,c,2*spaceR+c,2*spaceR+c),(w-2*spaceR-c,c,w-c,2*spaceR+c),(c,h-2*spaceR-c,2*spaceR+c,h-c),\
         (w-2*spaceR-c,h-2*spaceR-c,w-c,h-c)]

for iblank in range(0,len(l_blank)):
    canvas.create_oval(l_blank[iblank],fill="black",outline="black")
    canvas_m.create_oval(l_blank[iblank],fill="black",outline="black")
################################################
l2=[(line_r+R+c,line_r+R+c,150+c,150+c),(w-line_r-R-c,line_r+R+c,w-150-c,150+c), (line_r+R+c,h-line_r-R-c,150+c,h-150-c),\
    (w-line_r-R-c,h-line_r-R-c,w-150-c,h-150-c)]

for i2 in range(0,len(l2)):
    canvas.create_line(l2[i2],width="2",fill="red")
    canvas_m.create_line(l2[i2],width="2",fill="red")

##################################################carom_board_lines
l1=[(line_r+R+c,h-line_r-2*R-c,w-line_r-R-c,h-line_r-2*R-c),     (line_r+R+c,h-line_r-c,w-line_r-R-c,h-line_r-c),\
    (line_r+R+c,line_r+2*R+c,w-line_r-R-c,line_r+2*R+c),          (line_r+R+c,line_r+c,w-line_r-R-c,line_r+c),\
    (line_r+c,line_r+R+c,line_r+c,h-line_r-R-c),     (line_r+2*R+c,line_r+R+c,line_r+2*R+c,h-line_r-R-c),\
    (w-line_r-c,line_r+R+c,w-line_r-c,h-line_r-R-c),     (w-line_r-2*R-c,line_r+R+c,w-line_r-2*R-c,h-line_r-R-c)]

for i1 in range(0,len(l1)):
    canvas.create_line(l1[i1],fill="blue", width="2")
    canvas_m.create_line(l1[i1],fill="blue", width="2")

############################
canvas.create_oval(w/2-5*r,h/2-5*r,w/2+5*r,h/2+5*r,fill=None,outline="red",width="2")
canvas.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill=None,outline="black",width="2")
canvas_m.create_oval(w/2-5*r,h/2-5*r,w/2+5*r,h/2+5*r,fill=None,outline="red",width="2")
canvas_m.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill=None,outline="black",width="2")
################################################################


for b in list_ball:
    if b["color"]==1:
        canvas.create_oval(b["x"]-r,b["y"]-r,b["x"]+r,b["y"]+r,fill="#fffe30000", width="0",tag=b["id"],outline=None)
        canvas.create_oval(b["x"]-r2,b["y"]-r2,b["x"]+r2,b["y"]+r2,fill="#f54f9ebb6",width="0", tag=b["id"],outline="#a18000000")
        canvas.create_oval(b["x"]-r3,b["y"]-r3,b["x"]+r3,b["y"]+r3,fill="#ffffff692", width="0",tag=b["id"],outline="#edb000000")

        canvas_m.create_oval(w-b["x"]-r,h-b["y"]-r,w-b["x"]+r,h-b["y"]+r,fill="#fffe30000", width="0",tag=b["id"],outline=None)
        canvas_m.create_oval(w-b["x"]-r2,h-b["y"]-r2,w-b["x"]+r2,h-b["y"]+r2,fill="#f54f9ebb6",width="0", tag=b["id"],outline="#a18000000")
        canvas_m.create_oval(w-b["x"]-r3,h-b["y"]-r3,w-b["x"]+r3,h-b["y"]+r3,fill="#ffffff692", width="0",tag=b["id"],outline="#edb000000")
    else:
        canvas.create_oval(b["x"]-r,b["y"]-r,b["x"]+r,b["y"]+r,fill="black", width="0",tag=b["id"],outline=None)
        canvas.create_oval(b["x"]-r2,b["y"]-r2,b["x"]+r2,b["y"]+r2,fill="black",width="0", tag=b["id"],outline="#a18000000")
        canvas.create_oval(b["x"]-r3,b["y"]-r3,b["x"]+r3,b["y"]+r3,fill="#30c2c330c", width="0",tag=b["id"],outline="#edb000000")
        
        canvas_m.create_oval(w-b["x"]-r,h-b["y"]-r,w-b["x"]+r,h-b["y"]+r,fill="black", width="0",tag=b["id"],outline=None)
        canvas_m.create_oval(w-b["x"]-r2,h-b["y"]-r2,w-b["x"]+r2,h-b["y"]+r2,fill="black",width="0", tag=b["id"],outline="#a18000000")
        canvas_m.create_oval(w-b["x"]-r3,h-b["y"]-r3,w-b["x"]+r3,h-b["y"]+r3,fill="#30c2c330c", width="0",tag=b["id"],outline="#edb000000")

        
root.mainloop()
