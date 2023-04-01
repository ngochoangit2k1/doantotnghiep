from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import  cv2

class Developer:

    def __init__(self, root):
        self.root = root
        # vị trí nhận diện trên màng hình
        self.root.geometry("1530x900+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("time new roman", 25, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=30)

        img_top = Image.open(r"college_images/face_detection2x.png")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)


        # Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=1500, height=650)


        img_top1 = Image.open(r"college_images/face_detection2x.png")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

#         Developer info

        dev_label=Label(main_frame, text="hello my name, Hoang", font=("time new roman", 20, "bold"), bg="white")
        dev_label.place(x=0, y=5)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
