import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from staff import Staff
import os
from train import Train

from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer


class Face_Recognition_System:

    def __init__(self, root):
        self.root = root
        # vị trí nhận diện trên màng hình
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
        # first ìmg
        img = Image.open(r"college_images/Background.png")
        img = img.resize((500, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=200)

        # second img
        img1 = Image.open(r"college_images/logo.png")
        img1 = img1.resize((500, 150), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)

        # thirt img
        img2 = Image.open(r"college_images/face_detection2x.png")
        img2 = img2.resize((500, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=200)

        #         bg img
        img3 = Image.open(r"college_images/bg.png")
        img3 = img3.resize((2000, 1000), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1500, height=700)

        title_lbl = Label(bg_img, text="FACE RECOTION ATTENDAN SYSTEM SOFTWARE", font=("time new roman", 30, "bold"),
                          bg="white", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #     studen btn
        img4 = Image.open(r"college_images/details.png")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn1 = Button(bg_img, image=self.photoimg4, command=self.staff_details, cursor="hand2")
        btn1.place(x=200, y=100, width=200, height=200)

        btn1_1 = Button(bg_img, text="Details", cursor="hand2", command=self.staff_details,
                        font=("time new roman", 15, "bold"), bg="#548c3c",
                        fg="white")
        btn1_1.place(x=200, y=300, width=200, height=45)

        # detector
        img5 = Image.open(r"college_images/face-detection.png")
        img5 = img5.resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_recognition_data)
        btn1.place(x=600, y=100, width=200, height=200)

        btn1_1 = Button(bg_img, text="Face Deteror", cursor="hand2", command=self.face_recognition_data,
                        font=("time new roman", 15, "bold"), bg="#548c3c",
                        fg="white")
        btn1_1.place(x=600, y=300, width=200, height=45)

        # Attendance
        img6 = Image.open(r"college_images/immigration.png")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance)
        btn1.place(x=1000, y=100, width=200, height=200)

        btn1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance,
                        font=("time new roman", 15, "bold"), bg="#548c3c",
                        fg="white")
        btn1_1.place(x=1000, y=300, width=200, height=45)



        # train data
        img8 = Image.open(r"college_images/training.png")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        btn1.place(x=350, y=400, width=200, height=200)

        btn1_1 = Button(bg_img, text="train data", cursor="hand2", command=self.train_data,
                        font=("time new roman", 15, "bold"), bg="#548c3c",
                        fg="white")
        btn1_1.place(x=350, y=600, width=200, height=45)





        # exit
        img11 = Image.open(r"college_images/log-out.png")
        img11 = img11.resize((200, 200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        btn1.place(x=850, y=400, width=200, height=200)

        btn1_1 = Button(bg_img, text="exit", cursor="hand2", command=self.iExit, font=("time new roman", 15, "bold"),
                        bg="#548c3c",
                        fg="white")
        btn1_1.place(x=850, y=600, width=200, height=45)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are ou sure exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    #         Funtions buttons

    def staff_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Staff(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognition_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
