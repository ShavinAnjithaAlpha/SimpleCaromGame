from tkinter import*
import math
import random

root=Tk()
root.config(bg="#262c3d")

w=800
h=600
vx=float()
vy=float()
s=int()
score=int()

def new():
    global px,py,l,rx1,y1,vx,vy,s
    canvas.delete(ALL)
    canvas.create_rectangle(x1,y1,x1+l,y1+d,fill="blue2",tag="rect_x")
    canvas.create_rectangle(x1+l,y1+d,x1+l+d,y1+d+l,fill="blue2",tag="rect_y")
    canvas.create_oval(x1+l,y1,x1+l+d,y1+d,fill="red",tag="ball")
    top=random.randrange(b,h-b)
    canvas.delete("line")
    canvas.create_line(2*w/3,0,2*w/3,top,fill="red",width="2",tag="line")
    canvas.create_line(2*w/3,top+b,2*w/3,h,fill="red",width="2",tag="line")
    px=x1+l+r
    py=y1+r
    vx=0
    vy=0
    s=2

def set_ballv(event):
    global vx,vy,r,l,x1,y1,b
    ob=canvas.find_closest(event.x,event.y)[0]
    tag=canvas.gettags(ob)
    
    if tag[0]=="ball":
        canvas.delete("ball","rect_x","rect_y")
        canvas.create_oval(event.x-r,event.y-r,event.x+r,event.y+r,tag="ball",fill="red")
        canvas.create_rectangle(x1,y1,event.x-r,event.y+r,tag="rect_x",fill="blue2")
        canvas.create_rectangle(event.x-r,event.y+r,event.x+r,y1+r+l,tag="rect_y",fill="blue2")
        x=x1+l-(event.x-r)
        y=(event.y+r)-(y1+d)
        vx=30*x
        vy=30*y
        px=event.x
        py=event.y

        
def start(event):
    global vx,vy,s,px,py,r,top,b,score
    org_x=px
    org_y=py
    s=1
    canvas.create_text(9*w/10,50,text=str(score),font=('verdana',15),fill="white")
    while s==1:
        ax=-0.1*vx
        ay=-0.1*vy-900
        vx=vx+ax*0.01
        vy=vy+ay*0.01
        px=px+vx*0.01
        py=py-vy*0.01
        canvas.delete("ball")
        canvas.create_oval(px-r,py-r,px+r,py+r,fill="red",tag="ball")
        canvas.create_line(org_x,org_y,px,py,fill="red")
        org_x=px
        org_y=py
        if px+r>w or px-r<0:
            vx=-0.9*vx
        if py+r>h or py-r<0:
            vy=-0.9*vy
        if (px+r>2*w/3 and (py+r>top+b and py-r<top)):
            score+=5
            print(score)
        elif px+r>2*w/3 and not(py+r>top+b and py-r<top):
            vx=-0.9*vx
            print(score)
        
        canvas.update()
        canvas.after(10)

canvas=Canvas(root,width=w,height=h,bg="#262c3d")
canvas.pack(side=LEFT)
Button(root,text="New",width="20",relief=FLAT,command=new).pack(side=LEFT, padx=5)

l=70
d=20
r=d/2
x1=40
y1=200
canvas.create_rectangle(x1,y1,x1+l,y1+d,fill="blue2",tag="rect_x")
canvas.create_rectangle(x1+l,y1+d,x1+l+d,y1+d+l,fill="blue2",tag="rect_y")
canvas.create_oval(x1+l,y1,x1+l+d,y1+d,fill="red",tag="ball")

px=x1+l+r
py=y1+r

canvas.bind("<B1-Motion>",set_ballv)
canvas.bind("<ButtonRelease-1>",start)
b=2*r+100
top=random.randrange(b,h-b)

canvas.create_line(2*w/3,0,2*w/3,top,fill="red",width="2",tag="line")
canvas.create_line(2*w/3,top+b,2*w/3,h,fill="red",width="2",tag="line")
























root.mainloop()
