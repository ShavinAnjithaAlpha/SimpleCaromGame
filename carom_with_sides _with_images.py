from tkinter import*
import math
import random
import time
from PIL import ImageTk, Image


root = Tk()
root.config(bg="brown")
root.title("CaromGameByShavMind version 2020.1.0")

c = 30
w = 450+2*c
h = 450+2*c
vx = float()
vy = float()
s = int()
score = int()
r = 14
r2 = 9
r3 = 5
a = 2.9  # initial value is 2.6
R = 17
R2 = 9
spaceR = 24
sq3 = math.sqrt(3)
line_r = 60

img = ImageTk.PhotoImage(Image.open("smoothboard.jpg").resize((1200,1200),Image.ANTIALIAS))
boardimg = ImageTk.PhotoImage(Image.open("original_cardboard.jpg").resize((1150,1150),Image.ANTIALIAS))
boardimg_full = ImageTk.PhotoImage(Image.open("full_carom_board.png").resize((520,520),Image.ANTIALIAS))
boardimg_full_rotate = ImageTk.PhotoImage(Image.open("full_carom_board.png").resize((520,520),Image.ANTIALIAS).rotate(180))

reddiskimg = ImageTk.PhotoImage(Image.open("blackdiskimage2.png").resize((2*r,2*r),Image.ANTIALIAS))
blackdisk = ImageTk.PhotoImage(Image.open("whitediskimage2.png").resize((2*r,2*r),Image.ANTIALIAS))
whitedisk = ImageTk.PhotoImage(Image.open("whitediskimage2.png").resize((2*r,2*r),Image.ANTIALIAS))
maindisk = ImageTk.PhotoImage(Image.open("main_disk.png").resize((2*R,2*R),Image.ANTIALIAS))
partner = "partner_1"

kulaRed = ["#500000","#6e0000","#ff0000","#ff5050", "#ff8c8c", "#ffc8c8" ]
# ,"#a00000",
list_ball,list_fallen = list(),list()
n = 13
list_ofxy = [(w/2,h/2),(w/2+2*r,h/2), (w/2-2*r,h/2), (w/2+r,h/2-sq3*r), (w/2+r,h/2+sq3*r),\
            (w/2-r,h/2-sq3*r), (w/2-r,h/2+sq3*r), (w/2+4*r,h/2), (w/2-4*r,h/2), (w/2+2*r,h/2-sq3*2*r), (w/2+2*r,h/2+sq3*2*r),\
            (w/2-2*r,h/2-sq3*2*r), (w/2-2*r,h/2+sq3*2*r), (w/2,h/2-4*r), (w/2,h/2+4*r), (w/2+3*r,h/2-sq3*r), \
            (w/2+3*r,h/2+sq3*r), (w/2-3*r,h/2+sq3*r), (w/2-3*r,h/2-sq3*r)]






def new():
    global main_disc,s
    main_disc["vx"]=0
    main_disc["vy"]=0
    main_disc["x"]=w/2
    main_disc["y"]=h-line_r-R-c
    s=0
    canvas.delete("main_ball")
    canvas.create_image(main_disc["x"],main_disc["y"],image=maindisk,tag=main_disc["id"])
    #canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])
    canvas_scale.delete("scale_disc")
    canvas_scale.create_image(main_disc["x"],15,image=maindisk,tag="scale_disc")
    #canvas_scale.create_oval(main_disc["x"]-R2,25-R2,main_disc["x"]+R2,25+R2,fill="white",tag="scale_disc")

def scale_disc(event):
    if event.x>line_r+3*R+c-5 and event.x<w-line_r-3*R-c+5 and partner=="partner_1":
        canvas_scale.delete("scale_disc")
        canvas_scale.create_image(event.x,15,image=maindisk,tag="scale_disc")
        #canvas_scale.create_oval(event.x-R2,15-R2,event.x+R2,15+R2,fill="white",tag="scale_disc")
        main_disc["x"]=event.x
        main_disc["y"]=h-line_r-R-c
        canvas.delete("main_ball")
        canvas_m.delete("main_ball")
        canvas.create_image(main_disc["x"],main_disc["y"],image=maindisk,tag=main_disc["id"])
        #canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])
        canvas_m.create_image(w-main_disc["x"],h-main_disc["y"],image=maindisk,tag=main_disc["id"])
        #canvas_m.create_oval(w-main_disc["x"]-R2,h-main_disc["y"]-R2,w-main_disc["x"]+R2,h-main_disc["y"]+R2,fill="white",width=0,tag=main_disc["id"])


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
    main_disc["vx"]=40*l*((click_x-event.x)/l)
    main_disc["vy"]=40*l*((event.y-click_y)/l)
    canvas.delete("vline")
    canvas.create_line(click_x,click_y,click_x+(click_x-event.x),click_y-(event.y-click_y),fill="blue2",tag="vline",width="1.2")
   # canvas.create_line(event.x,event.y,click_x,click_y,fill="yellow",tag="vline",width="2",dash=(200,1))
    canvas.create_oval(click_x-l,click_y-l,click_x+l,click_y+l,outline="blue2",tag="vline",width="1.2",dash=(2,2))
    



def set_velocity(ball_1,ball_2):
    e=0.9
    l=math.sqrt(pow(ball_1["y"]-ball_2["y"],2)+pow(ball_1["x"]-ball_2["x"],2))
    sin=(ball_1["y"]-ball_2["y"])/l
    cos=(ball_2["x"]-ball_1["x"])/l
    vx1=ball_1["vx"]
    vx2=ball_2["vx"]

    vy1=ball_1["vy"]
    vy2=ball_2["vy"]
   
    k1=(vx1-vx2)*cos+(vy1-vy2)*sin
    v1=k1*(1-e)/2
    v2=k1*(1+e)/2
    ball_1["vx"]=v1*cos+(vx1*sin-vy1*cos)*sin+vx2
    ball_1["vy"]=v1*sin+(vy1*cos-vx1*sin)*cos+vy2
    ball_2["vx"]=v2*cos+vx2
    ball_2["vy"]=v2*sin+vy2
    


      
def start(event):
    global r,ball_list,a,r2,r3,R,main_disc,s,list_fallen
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
        # set main disk velocity
        main_disc["x"]+=main_disc["vx"]*0.01
        main_disc["y"]+=(-main_disc["vy"]*0.01)
        # check is main disk collide with walls
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
        #canvas.create_oval(main_disc["x"]-R,main_disc["y"]-R,main_disc["x"]+R,main_disc["y"]+R,fill="black",width=0,tag=main_disc["id"])
        canvas.create_image(main_disc["x"],main_disc["y"],image=maindisk,tag=main_disc["id"])
        #canvas.create_oval(main_disc["x"]-R2,main_disc["y"]-R2,main_disc["x"]+R2,main_disc["y"]+R2,width=0,fill="white",tag=main_disc["id"])

        canvas_m.create_image(w-main_disc["x"],h-main_disc["y"],image=maindisk,tag=main_disc["id"])
        #canvas_m.create_oval(w-main_disc["x"]-R2,h-main_disc["y"]-R2,w-main_disc["x"]+R2,h-main_disc["y"]+R2,width=0,fill="white",tag=main_disc["id"])



        
        for b1 in list_ball:
            if not(b1["vx"]==0 and b1["vy"]==0):
                for b2 in list_ball:
                    if not(b1==b2):
                        if math.sqrt(pow(b1["y"]-b2["y"],2)+pow(b1["x"]-b2["x"],2))<2*r:
                            set_velocity(b1,b2)
                            l=math.sqrt(pow(b1["y"]-b2["y"],2)+pow(b1["x"]-b2["x"],2))
                            #tantheta=b1["y"]-b2["y"]/(b2["x"]-b1["x"])
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
                b1["vx"]+=ax*0.01
                b1["vy"]+=ay*0.01
                ############
                b1["x"]+=b1["vx"]*0.01
                b1["y"]+=(-b1["vy"]*0.01)
                ###############
                if b1["x"]+r>w-c :
                    b1["vx"]=-0.8*b1["vx"]
                    b1["x"]=w-r-c
                if  b1["x"]-r<c:
                    b1["vx"]=-0.8*b1["vx"]
                    b1["x"]=r+c
                if b1["y"]+r>h-c: 
                    b1["vy"]=-0.8*b1["vy"]
                    b1["y"]=h-c-r
                if  b1["y"]-r<c:
                    b1["vy"]=-0.8*b1["vy"]
                    b1["y"]=c+r
                    
                ########################    
                
                ################
                canvas.delete(b1["id"])
                canvas_m.delete(b1["id"])
                if b1["color"]==1:
                    canvas.create_image(b1["x"],b1["y"],image=reddiskimg,tag=b1["id"])
                    #canvas.create_oval(b1["x"]-r2,b1["y"]-r2,b1["x"]+r2,b1["y"]+r2,fill="#a18000000",width="0", tag=b1["id"],outline="#a18000000")
                    #canvas.create_oval(b1["x"]-r3,b1["y"]-r3,b1["x"]+r3,b1["y"]+r3,fill="#edb000000", width="0",tag=b1["id"],outline="#edb000000")

                    canvas_m.create_image(w-b1["x"],h-b1["y"],image=reddiskimg,tag=b1["id"])
                    #canvas_m.create_oval(w-b1["x"]-r2,h-b1["y"]-r2,w-b1["x"]+r2,h-b1["y"]+r2,fill="#a18000000",width="0", tag=b1["id"],outline="#a18000000")
                    #canvas_m.create_oval(w-b1["x"]-r3,h-b1["y"]-r3,w-b1["x"]+r3,h-b1["y"]+r3,fill="#edb000000", width="0",tag=b1["id"],outline="#edb000000")

                else:
                    canvas.create_image(b1["x"],b1["y"],image=blackdisk,tag=b1["id"])
                    #canvas.create_oval(b1["x"]-r2,b1["y"]-r2,b1["x"]+r2,b1["y"]+r2,fill="#00030c418",width="0", tag=b["id"],outline="#a18000000")
                    #canvas.create_oval(b1["x"]-r3,b1["y"]-r3,b1["x"]+r3,b1["y"]+r3,fill="#30c2c330c", width="0",tag=b["id"],outline="#edb000000")

                    canvas_m.create_image(w-b1["x"],h-b1["y"],image=blackdisk,tag=b1["id"])
                    #canvas_m.create_oval(w-b1["x"]-r2,h-b1["y"]-r2,w-b1["x"]+r2,h-b1["y"]+r2,fill="#00030c418",width="0", tag=b["id"],outline="#a18000000")
                    #canvas_m.create_oval(w-b1["x"]-r3,h-b1["y"]-r3,w-b1["x"]+r3,h-b1["y"]+r3,fill="#30c2c330c", width="0",tag=b["id"],outline="#edb000000")
                ######################
                n=0
                for disk in list_ball:
                    if abs(disk["vx"])<20 and abs(disk["vy"])<20:
                        n+=1
                        #disk["vx"],disk["vy"]=0,0
                if abs(main_disc["vx"])<20 and abs(main_disc["vy"])<20:
                    n+=1
                    #main_disc["vx"],main_disc["vy"]=0,0
                if n==len(list_ball)+1:
                    new()
                #######################################
                ####################disk_fallen_to_space
                if (math.sqrt(pow(b1["x"]-(spaceR+c),2)+pow(b1["y"]-(spaceR+c),2))<spaceR-r
                    or math.sqrt(pow(b1["x"]-(w-spaceR-c),2)+pow(b1["y"]-(spaceR+c),2))<spaceR-r
                    or math.sqrt(pow(b1["x"]-(spaceR+c),2)+pow(b1["y"]-(h-spaceR-c),2))<spaceR-r
                    or math.sqrt(pow(b1["x"]-(w-spaceR-c),2)+pow(b1["y"]-(h-spaceR-c),2))<spaceR-r) and (abs(b1["vx"]<2000)) and abs(b1["vy"])<2000:
                    list_fallen.append(b1)
                    list_ball.remove(b1)
                    # time.sleep(0.06)
                    canvas.delete(b1["id"])
                    canvas_m.delete(b1["id"])
       
        canvas.update()
        canvas.after(9)

def new_game():
    global list_ofxy,list_ball,main_disc,n

    for i in range(0,n):
        canvas.delete(f"{i}ball")
        canvas_m.delete(f"{i}ball")
    canvas.delete("main_ball")
    canvas.create_image(260, 260, image=boardimg_full)
    canvas_m.create_image(260, 260, image=boardimg_full_rotate)

    for i in range(0, n):
        color = random.randint(0, 1)
        x = random.randrange(r, w - r)
        y = random.randrange(r, h - r)
        ball = {"x": list_ofxy[i][0],
                "y": list_ofxy[i][1],
                "vx": 0,
                "vy": 0,
                "id": f"{i}ball",
                "color": color,
                }
        list_ball.append(ball)

    main_disc = {"x": w / 2,
                 "y": h / 2,
                 "vx": 258,
                 "vy": 356,
                 "id": "main_ball",
                 }

    # draw disk in carom board
    for b in list_ball:
        if b["color"] == 1:
            canvas.create_image(b["x"], b["y"], image=reddiskimg, tag=b["id"])

            canvas_m.create_image(w - b["x"], h - b["y"], image=reddiskimg, tag=b["id"])
        else:
            canvas.create_image(b["x"], b["y"], image=blackdisk, tag=b["id"])

            canvas_m.create_image(w - b["x"], h - b["y"], image=blackdisk, tag=b["id"])




canvas = Canvas(root, width=w, height=h, bg="#ac24003b7", bd=0, highlightthickness=0)
canvas.grid(row=1,column=0)


canvas_m = Canvas(root, width=w, height=h, bg="#ac24003b7", bd=0, highlightthickness=0)
canvas_m.grid(row=1,column=2)


canvas_scale = Canvas(root, width=w, height="35", bg="brown2", bd=0, highlightthickness=0)
canvas_scale.grid(row=2, column=0)
canvas_scale_m = Canvas(root, width=w, height="35", bg="brown2", bd=0, highlightthickness=0)
canvas_scale_m.grid(row=2, column=2, padx=2)
canvas_scale.create_image(w/2,15,image=maindisk,tag="scale_disc")

# create main menu
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(menu=file_menu, label="file")

file_menu.add_command(label="New game", command=new_game)

canvas_scale.bind( "<B1-Motion>",scale_disc)

canvas.bind("<B1-Motion>", set_maindisc_velocity)
canvas.bind("<ButtonRelease-1>", start)
# ###################carom_board_sides
ls=[(0,0,w,c),(0,h-c,w,h),(0,0,c,h),(w-c,0,w,h)]


# carom_board_ovals
l3=[(line_r+c,h-line_r-2*R-c,line_r+2*R+c,h-line_r-c),(w-2*R-line_r-c,h-line_r-2*R-c,w-line_r-c,h-line_r-c),\
    (line_r+c,line_r+c,line_r+2*R+c,line_r+2*R+c),(w-line_r-c,line_r+c,w-line_r-2*R-c,line_r+2*R+c)]

# carom_board_blanks
l_blank=[(c,c,2*spaceR+c,2*spaceR+c),(w-2*spaceR-c,c,w-c,2*spaceR+c),(c,h-2*spaceR-c,2*spaceR+c,h-c),\
         (w-2*spaceR-c,h-2*spaceR-c,w-c,h-c)]

#
l2=[(line_r+R+c,line_r+R+c,150+c,150+c),(w-line_r-R-c,line_r+R+c,w-150-c,150+c), (line_r+R+c,h-line_r-R-c,150+c,h-150-c),\
    (w-line_r-R-c,h-line_r-R-c,w-150-c,h-150-c)]

# for i2 in range(0,len(l2)):
    #canvas.create_line(l2[i2],width="2",fill="red")
  #  canvas_m.create_line(l2[i2],width="2",fill="red")

# carom_board_lines
l1=[(line_r+R+c,h-line_r-2*R-c,w-line_r-R-c,h-line_r-2*R-c),     (line_r+R+c,h-line_r-c,w-line_r-R-c,h-line_r-c),\
    (line_r+R+c,line_r+2*R+c,w-line_r-R-c,line_r+2*R+c),          (line_r+R+c,line_r+c,w-line_r-R-c,line_r+c),\
    (line_r+c,line_r+R+c,line_r+c,h-line_r-R-c),     (line_r+2*R+c,line_r+R+c,line_r+2*R+c,h-line_r-R-c),\
    (w-line_r-c,line_r+R+c,w-line_r-c,h-line_r-R-c),     (w-line_r-2*R-c,line_r+R+c,w-line_r-2*R-c,h-line_r-R-c)]

# initialize the new game
new_game()


root.mainloop()
