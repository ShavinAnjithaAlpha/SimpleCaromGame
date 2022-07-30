import math
from tkinter import *
import random
import time
from PIL import Image, ImageTk

class CaromGame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("CaromGameByShavMind version 2020.1.0")
        self.master.config(bg="#7d390b")
        self.grid()

        self.c = 30
        self.w = 450 + 2 * self.c
        self.h = 450 + 2 * self.c
        self.vx, self.vy = float(), float()
        self.s = int()
        self.score = int()
        self.r = 14
        self.r2 = 9
        self.r3 = 5
        # cofficient of friction force on the disks
        self.a = 3.2  # initial value is 2.6
        self.R = 17
        self.R2 = 9
        self.spaceR = 24
        self.sq3 = math.sqrt(3)
        self.line_r = 60
        # time interval
        self.dt = 0.005
        self.fallen = False

        self.boardimg_full = ImageTk.PhotoImage(Image.open("full_carom_board.png").resize((520, 520), Image.ANTIALIAS))
        self.boardimg_full_rotate = ImageTk.PhotoImage(Image.open("full_carom_board.png").resize((520, 520), Image.ANTIALIAS).rotate(180))

        self.reddiskimg = ImageTk.PhotoImage(Image.open("blackdiskimage2.png").resize((2 * self.r, 2 * self.r), Image.ANTIALIAS))
        self.blackdisk = ImageTk.PhotoImage(Image.open("whitediskimage2.png").resize((2 * self.r, 2 * self.r), Image.ANTIALIAS))
        self.whitedisk = ImageTk.PhotoImage(Image.open("whitediskimage2.png").resize((2 * self.r, 2 * self.r), Image.ANTIALIAS))
        self.maindisk = ImageTk.PhotoImage(Image.open("main_disk.png").resize((2 * self.R, 2 * self.R), Image.ANTIALIAS))
        self.partner = "partner_1"


        self.list_ball, self.list_fallen = list(), list()
        self.n = 19
        self.list_ofxy = [(self.w / 2, self.h / 2), (self.w / 2 + 2 * self.r, self.h / 2), (self.w / 2 - 2 * self.r, self.h / 2), (self.w / 2 + self.r, self.h / 2 - self.sq3 * self.r),
             (self.w / 2 + self.r, self.h / 2 + self.sq3 * self.r), \
             (self.w / 2 - self.r, self.h / 2 - self.sq3 * self.r), (self.w / 2 - self.r, self.h / 2 + self.sq3 * self.r), (self.w / 2 + 4 * self.r, self.h / 2), (self.w / 2 - 4 * self.r, self.h / 2),
             (self.w / 2 + 2 * self.r, self.h / 2 - self.sq3 * 2 * self.r), (self.w / 2 + 2 * self.r, self.h / 2 + self.sq3 * 2 * self.r), \
             (self.w / 2 - 2 * self.r, self.h / 2 - self.sq3 * 2 * self.r), (self.w / 2 - 2 * self.r, self.h / 2 + self.sq3 * 2 * self.r), (self.w / 2, self.h / 2 - 4 * self.r),
             (self.w / 2, self.h / 2 + 4 * self.r), (self.w / 2 + 3 * self.r, self.h / 2 - self.sq3 * self.r), \
             (self.w / 2 + 3 * self.r, self.h / 2 + self.sq3 * self.r), (self.w / 2 - 3 * self.r, self.h / 2 + self.sq3 * self.r), (self.w / 2 - 3 * self.r, self.h / 2 - self.sq3 * self.r)]

        self.canvas = Canvas(self, width=self.w, height=self.h, bg="#ac24003b7", bd=0, highlightthickness=0)
        self.canvas.grid(row=1, column=0)

        self.canvas_m = Canvas(self, width=self.w, height=self.h, bg="#ac24003b7", bd=0, highlightthickness=0)
        self.canvas_m.grid(row=1, column=1)

        self.canvas_scale = Canvas(self, width=self.w, height="35", bg="#4a1b04", bd=0, highlightthickness=0)
        self.canvas_scale.grid(row=2, column=0)
        self.canvas_scale_m = Canvas(self, width=self.w, height="35", bg="#4a1b04", bd=0, highlightthickness=0)
        self.canvas_scale_m.grid(row=2, column=1, padx=2)
        self.canvas_scale.create_image(self.w / 2, 15, image=self.maindisk, tag="scale_disc")

        # create main menu
        self.main_menu = Menu(self)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(menu=self.file_menu, label="file")

        self.file_menu.add_command(label="New game", command=self.new_game)

        # design the scale canvas
        self.design_scaling_canvas()

        self.canvas_scale.bind("<B1-Motion>", self.scale_disc)
        self.canvas_scale_m.bind("<B1-Motion>", self.scale_disc_m)

        self.canvas.bind("<B1-Motion>", self.set_maindisc_velocity)
        self.canvas.bind("<ButtonRelease-1>", self.start)

        self.canvas_m.bind("<B1-Motion>", self.set_maindisc_velocity_m)
        self.canvas_m.bind("<ButtonRelease-1>", self.start)

        # initialize the new game
        self.new_game()


    def scale_disc(self, event):
        if event.x > self.line_r + 3 * self.R + self.c - 5 and event.x < self.w - self.line_r - 3 * self.R - self.c + 5 and self.partner == "partner_1":
            self.canvas_scale.delete("scale_disc")
            self.canvas_scale.create_image(event.x, 15, image=self.maindisk, tag="scale_disc")
            self.main_disc["x"] = event.x
            self.main_disc["y"] = self.h - (self.line_r + self.R + self.c)
            self.canvas.delete("main_ball")
            self.canvas_m.delete("main_ball")
            self.canvas.create_image(self.main_disc["x"], self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
            self.canvas_m.create_image(self.w - self.main_disc["x"], self.h - self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])

    def scale_disc_m(self, event):
        if event.x > self.line_r + 3 * self.R + self.c - 5 and event.x < self.w - self.line_r - 3 * self.R - self.c + 5 and self.partner == "partner_2":
            self.canvas_scale_m.delete("scale_disc")
            self.canvas_scale_m.create_image(event.x, 15, image=self.maindisk, tag="scale_disc")
            self.main_disc["x"] = event.x
            self.main_disc["y"] = self.h - (self.line_r + self.R + self.c)
            self.canvas.delete("main_ball")
            self.canvas_m.delete("main_ball")
            self.canvas_m.create_image(self.main_disc["x"], self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
            self.canvas.create_image(self.w - self.main_disc["x"], self.h - self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])


    def getsin_cos(self, tantheta, type_trig):
        if type_trig == "sin":
            cot = 1 / tantheta
            cosec = math.sqrt(1 + pow(cot, 2))
            sin = 1 / cosec
            return sin
        elif type_trig == "cos":
            sec = math.sqrt(1 + pow(tantheta, 2))
            cos = 1 / sec
            return cos


    def set_maindisc_velocity(self ,event):
        if self.partner == "partner_1":
            click_x, click_y = self.main_disc["x"], self.main_disc["y"]
            l = math.sqrt(pow(click_x - event.x, 2) + pow(click_y - event.y, 2))
            self.main_disc["vx"] = 40 * l * ((click_x - event.x) / l)
            self.main_disc["vy"] = 40 * l * ((event.y - click_y) / l)
            self.canvas.delete("vline")
            self.canvas.create_line(click_x, click_y, click_x + (click_x - event.x), click_y - (event.y - click_y), fill="blue2",
                       tag="vline", width="1.2")
            # canvas.create_line(event.x,event.y,click_x,click_y,fill="yellow",tag="vline",width="2",dash=(200,1))
            self.canvas.create_oval(click_x - l, click_y - l, click_x + l, click_y + l, outline="blue2", tag="vline", width="1.2",
                       dash=(2, 2))

    def set_maindisc_velocity_m(self ,event):
        if self.partner == "partner_2":
            click_x, click_y = self.main_disc["x"], self.main_disc["y"]
            l = math.sqrt(pow(click_x - event.x, 2) + pow(click_y - event.y, 2))
            self.main_disc["vx"] = 40 * l * ((click_x - event.x) / l)
            self.main_disc["vy"] = 40 * l * ((event.y - click_y) / l)
            self.canvas_m.delete("vline")
            self.canvas_m.create_line(click_x, click_y, click_x + (click_x - event.x), click_y - (event.y - click_y), fill="blue2",
                       tag="vline", width="1.2")
            # canvas.create_line(event.x,event.y,click_x,click_y,fill="yellow",tag="vline",width="2",dash=(200,1))
            self.canvas_m.create_oval(click_x - l, click_y - l, click_x + l, click_y + l, outline="blue2", tag="vline", width="1.2",
                       dash=(2, 2))


    def set_velocity(self, ball_1, ball_2):
        e = 0.9
        l = math.sqrt(pow(ball_1["y"] - ball_2["y"], 2) + pow(ball_1["x"] - ball_2["x"], 2))
        sin = (ball_1["y"] - ball_2["y"]) / l
        cos = (ball_2["x"] - ball_1["x"]) / l
        vx1 = ball_1["vx"]
        vx2 = ball_2["vx"]

        vy1 = ball_1["vy"]
        vy2 = ball_2["vy"]

        k1 = (vx1 - vx2) * cos + (vy1 - vy2) * sin
        v1 = k1 * (1 - e) / 2
        v2 = k1 * (1 + e) / 2
        ball_1["vx"] = v1 * cos + (vx1 * sin - vy1 * cos) * sin + vx2
        ball_1["vy"] = v1 * sin + (vy1 * cos - vx1 * sin) * cos + vy2
        ball_2["vx"] = v2 * cos + vx2
        ball_2["vy"] = v2 * sin + vy2


    def start(self, event):

        def check_impact_with_maindisk():
            for b in self.list_ball:
                if math.sqrt(pow(b["y"] - self.main_disc["y"], 2) + pow(b["x"] - self.main_disc["x"], 2)) < self.r + self.R:
                    self.set_velocity(b, self.main_disc)
                    l1 = math.sqrt(pow(b["y"] - self.main_disc["y"], 2) + pow(b["x"] - self.main_disc["x"], 2))
                    b["x"] = self.main_disc["x"] + (self.R + self.r) * ((b["x"] - self.main_disc["x"]) / l1)
                    b["y"] = self.main_disc["y"] - (self.R + self.r) * ((self.main_disc["y"] - b["y"]) / l1)

        def check_collide_with_walls_maindisk():
            if self.main_disc["x"] + self.R > self.w - self.c:
                self.main_disc["vx"] = -0.8 * self.main_disc["vx"]
                self.main_disc["x"] = self.w - self.R - self.c
            if self.main_disc["x"] - self.R < self.c:
                self.main_disc["vx"] = -0.8 * self.main_disc["vx"]
                self.main_disc["x"] = self.R + self.c
            if self.main_disc["y"] + self.R > self.h - self.c:
                self.main_disc["vy"] = -0.8 * self.main_disc["vy"]
                self.main_disc["y"] = self.h - self.R - self.c
            if self.main_disc["y"] - self.R < self.c:
                self.main_disc["vy"] = -0.8 * self.main_disc["vy"]
                self.main_disc["y"] = self.R + self.c
        # global r, ball_list, a, r2, r3, R, main_disc, s, list_fallen
        self.s = 1
        self.canvas.delete("vline")
        self.canvas_m.delete("vline")
        self.fallen = False
        while self.s == 1:
            # first check the impact of disks and main disk
            check_impact_with_maindisk()
            # next set the disks accele. of main disk
            # set the ax component
            am = -self.a * self.main_disc["vx"]
            # set the ay components
            an = -self.a * self.main_disc["vy"]
            # set the main disk new velocities
            self.main_disc["vx"] += am * self.dt
            self.main_disc["vy"] += an * self.dt
            # set main disk velocity
            self.main_disc["x"] += self.main_disc["vx"] * self.dt
            self.main_disc["y"] += (-self.main_disc["vy"] * self.dt)
            # check is main disk collide with walls
            check_collide_with_walls_maindisk()
            self.canvas.delete("main_ball")
            self.canvas_m.delete("main_ball")
            # draw the main disk in the main canvas
            if self.partner == "partner_1":
                self.canvas.create_image(self.main_disc["x"], self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
                # draw the main disk in the other canvas
                self.canvas_m.create_image(self.w - self.main_disc["x"], self.h - self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
            else:
                self.canvas_m.create_image(self.main_disc["x"], self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
                # draw the main disk in the other canvas
                self.canvas.create_image(self.w - self.main_disc["x"], self.h - self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
            # end of the processes of the main disk


            # start of the processes of disks
            remove_disks = []
            for b1 in self.list_ball:
                if not (b1["vx"] == 0 and b1["vy"] == 0):
                    for b2 in self.list_ball:
                        if not (b1 == b2) and not(b2 in remove_disks) :
                            if math.sqrt(pow(b1["y"] - b2["y"], 2) + pow(b1["x"] - b2["x"], 2)) < 2 * self.r:
                                self.set_velocity(b1, b2)
                                l = math.sqrt(pow(b1["y"] - b2["y"], 2) + pow(b1["x"] - b2["x"], 2))
                                # tantheta=b1["y"]-b2["y"]/(b2["x"]-b1["x"])
                                b2["x"] = b1["x"] + 2 * self.r * ((b2["x"] - b1["x"]) / (l))
                                b2["y"] = b1["y"] - 2 * self.r * ((b1["y"] - b2["y"]) / (l))
                    # set the disk ax component
                    ax = -self.a * b1["vx"]
                    # set the disk ay component
                    ay = -self.a * b1["vy"]
                    # set the disk velocities
                    b1["vx"] += ax * self.dt
                    b1["vy"] += ay * self.dt
                    # set the disk displacement components
                    b1["x"] += b1["vx"] * self.dt
                    b1["y"] += (-b1["vy"] * self.dt)
                    # check the if disk are collide with the walls
                    if b1["x"] + self.r > self.w - self.c:
                        b1["vx"] = -0.8 * b1["vx"]
                        b1["x"] = self.w - self.r - self.c
                    if b1["x"] - self.r < self.c:
                        b1["vx"] = -0.8 * b1["vx"]
                        b1["x"] = self.r + self.c
                    if b1["y"] + self.r > self.h - self.c:
                        b1["vy"] = -0.8 * b1["vy"]
                        b1["y"] = self.h - self.c - self.r
                    if b1["y"] - self.r < self.c:
                        b1["vy"] = -0.8 * b1["vy"]
                        b1["y"] = self.c + self.r

                    # end of the check the collide with walls

                    # draw the disk s in the both two canvases
                    self.canvas.delete(b1["id"])
                    self.canvas_m.delete(b1["id"])
                    if b1["color"] == 1:
                        if self.partner == "partner_1":
                            self.canvas.create_image(b1["x"], b1["y"], image=self.reddiskimg, tag=b1["id"])
                            self.canvas_m.create_image(self.w - b1["x"], self.h - b1["y"], image=self.reddiskimg, tag=b1["id"])
                        else:
                            self.canvas_m.create_image(b1["x"], b1["y"], image=self.reddiskimg, tag=b1["id"])
                            self.canvas.create_image(self.w - b1["x"], self.h - b1["y"], image=self.reddiskimg, tag=b1["id"])
                    else:
                        if self.partner == "partner_1":
                            self.canvas.create_image(b1["x"], b1["y"], image=self.blackdisk, tag=b1["id"])
                            self.canvas_m.create_image(self.w - b1["x"], self.h - b1["y"], image=self.blackdisk, tag=b1["id"])
                        else:
                            self.canvas_m.create_image(b1["x"], b1["y"], image=self.blackdisk, tag=b1["id"])
                            self.canvas.create_image(self.w - b1["x"], self.h - b1["y"], image=self.blackdisk, tag=b1["id"])

                    #
                    # check the disk_fallen_to_space
                    if (math.sqrt(pow(b1["x"] - (self.spaceR + self.c), 2) + pow(b1["y"] - (self.spaceR + self.c), 2)) < self.spaceR - self.r
                        or math.sqrt(pow(b1["x"] - (self.w - self.spaceR - self.c), 2) + pow(b1["y"] - (self.spaceR + self.c), 2)) < self.spaceR - self.r
                        or math.sqrt(pow(b1["x"] - (self.spaceR + self.c), 2) + pow(b1["y"] - (self.h - self.spaceR - self.c), 2)) < self.spaceR - self.r
                        or math.sqrt(pow(b1["x"] - (self.w - self.spaceR - self.c), 2) + pow(b1["y"] - (self.h - self.spaceR - self.c), 2)) < self.spaceR - self.r) and (
                    abs(b1["vx"] < 3000)) and abs(b1["vy"]) < 3000:
                        self.list_fallen.append(b1)
                        self.list_ball.remove(b1)
                        # time.sleep(0.06)
                        # set the fallen var to true
                        self.fallen = True
                        self.canvas.delete(b1["id"])
                        self.canvas_m.delete(b1["id"])

                        #
                    n = 0
                    for disk in self.list_ball:
                        if abs(disk["vx"]) < 2 and abs(disk["vy"]) < 2:
                            n += 1
                        if abs(self.main_disc["vx"]) < 2 and abs(self.main_disc["vy"]) < 2:
                            n += 1
                        # main_disc["vx"],main_disc["vy"]=0,0
                        if n == len(self.list_ball) + 1:
                            if self.fallen:
                                if self.partner == "partner_1":
                                    self.partner = "partner_2"
                                else:
                                    self.partner = "partner_1"
                            self.new()

                    remove_disks.append(b1)

            self.canvas.update()
            self.canvas_m.update()
            self.canvas.after(int(self.dt * 1000))

    def new(self):
        # invert the partner
        if self.partner == "partner_1":
            self.partner = "partner_2"
        else:
            self.partner = "partner_1"
        # set main disk velocities
        self.main_disc["vx"] = 0
        self.main_disc["vy"] = 0
        self.main_disc["x"] = self.w / 2
        self.main_disc["y"] = self.h - self.line_r - self.R - self.c
        self.s = 0
        self.canvas.delete("main_ball")
        if self.partner == "partner_1":
            self.canvas.create_image(self.main_disc["x"], self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
            self.canvas_scale.delete("scale_disc")
            self.canvas_scale.create_image(self.main_disc["x"], 15, image=self.maindisk, tag="scale_disc")
        else:
            self.canvas_m.delete("main_ball")
            self.canvas_m.create_image(self.main_disc["x"], self.main_disc["y"], image=self.maindisk, tag=self.main_disc["id"])
            self.canvas_scale_m.delete("scale_disc")
            self.canvas_scale_m.create_image(self.main_disc["x"], 15, image=self.maindisk, tag="scale_disc")
        if not(self.fallen):
            self.invert_disks()

    def invert_disks(self):
        for ball in self.list_ball:
            ball["x"] = self.w - ball["x"]
            ball["y"] = self.h - ball["y"]



    def new_game(self):
        # initialize the new carom board and the new game
        self.canvas.delete(ALL)
        self.canvas_m.delete(ALL)
        # for i in range(0, self.n):
          #   self.canvas.delete(f"{i}ball")
            # self.canvas_m.delete(f"{i}ball")
        self.canvas.delete("main_ball")
        self.canvas.create_image(260, 260, image=self.boardimg_full)
        self.canvas_m.create_image(260, 260, image=self.boardimg_full)

        for i in range(0, self.n):
            color = random.randint(0, 1)
            x = random.randrange(self.r, self.w - self.r)
            y = random.randrange(self.r, self.h - self.r)
            ball = {"x": self.list_ofxy[i][0],
                "y": self.list_ofxy[i][1],
                "vx": 0,
                "vy": 0,
                "id": f"{i}ball",
                "color": color,
                }
            self.list_ball.append(ball)

        self.main_disc = {"x": self.w / 2,
                 "y": self.h / 2,
                 "vx": 0,
                 "vy": 0,
                 "id": "main_ball",
                 }

        # draw disk in carom board
        for b in self.list_ball:
            if b["color"] == 1:
                # create the disk in the main canvas
                self.canvas.create_image(b["x"], b["y"], image=self.reddiskimg, tag=b["id"])
                # create the disk in the oppinient canvas
                self.canvas_m.create_image(self.w - b["x"], self.h - b["y"], image=self.reddiskimg, tag=b["id"])
            else:
                # create the disk in the main canvas
                self.canvas.create_image(b["x"], b["y"], image=self.blackdisk, tag=b["id"])
                # create the disk in the oppinient canvas
                self.canvas_m.create_image(self.w - b["x"], self.h - b["y"], image=self.blackdisk, tag=b["id"])

    def design_scaling_canvas(self):
        color_scale = ["#f46925" ,"#e9530a" ,"#d24b08","#b84208","#a33a07"]
        k = 0
        for i in range(25, 0, -5):
            center_x11, center_y11 = self.line_r + 3 * self.R + self.c - 5 -i, 35 / 2
            self.canvas_scale.create_oval(center_x11 - 35 / 2, center_y11 - 35 / 2, center_x11 + 35 / 2, center_y11 + 35 / 2,
                                      fill=color_scale[k], outline=color_scale[k])
            self.canvas_scale_m.create_oval(center_x11 - 35 / 2, center_y11 - 35 / 2, center_x11 + 35 / 2, center_y11 + 35 / 2,
                                        fill=color_scale[k], outline=color_scale[k])

            center_x22, center_y22 = self.w - self.line_r - 3 * self.R - self.c + 5 +i, 35 / 2
            self.canvas_scale.create_oval(center_x22 - 35 / 2, center_y22 - 35 / 2, center_x22 + 35 / 2, center_y22 + 35 / 2,
                                      fill=color_scale[k], outline=color_scale[k])
            self.canvas_scale_m.create_oval(center_x22 - 35 / 2, center_y22 - 35 / 2, center_x22 + 35 / 2, center_y22 + 35 / 2,
                                        fill=color_scale[k], outline=color_scale[k])
            k += 1
        # main path of main disk
        center_x1 , center_y1 = self.line_r + 3 * self.R + self.c - 5 , 35/2
        self.canvas_scale.create_oval(center_x1-35/2, center_y1-35/2 ,center_x1+35/2, center_y1+35/2, fill="#7c2f09", outline="#7c2f09")
        self.canvas_scale_m.create_oval(center_x1 - 35 / 2, center_y1 - 35 / 2, center_x1 + 35 / 2, center_y1 + 35 / 2,fill="#7c2f09", outline="#7c2f09")

        center_x2, center_y2 = self.w - self.line_r - 3 * self.R - self.c + 5 , 35/2
        self.canvas_scale.create_oval(center_x2 - 35 / 2, center_y2 - 35 / 2, center_x2 + 35 / 2, center_y2 + 35 / 2,
                                      fill="#7c2f09", outline="#7c2f09")
        self.canvas_scale_m.create_oval(center_x2 - 35 / 2, center_y2 - 35 / 2, center_x2 + 35 / 2, center_y2 + 35 / 2,
                                        fill="#7c2f09", outline="#7c2f09")

        # create the rectangle
        self.canvas_scale.create_rectangle(center_x1, 0, center_x2, 35, fill="#7c2f09", outline="#7c2f09")
        self.canvas_scale_m.create_rectangle(center_x1, 0, center_x2, 35, fill="#7c2f09", outline="#7c2f09")



def main():
    CaromGame().mainloop()

if __name__ == "__main__":
    main()

