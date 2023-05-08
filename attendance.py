import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from  tkinter import filedialog
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import numpy as np
import csv


mydata=[]
class Attendance:

    def __init__(self, root):
        self.root = root
        # vị trí nhận diện trên màng hình
        self.root.geometry("1530x900+0+0")
        self.root.title("face Recogniton System")

        # varaibles

        self.var_atten_id=StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


        # first ìmg
        img = Image.open(r"college_images/face.png")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # second img
        img1 = Image.open(r"college_images/facerecognition.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        #         bg img
        img3 = Image.open(r"college_images/facerecognition.jpg")
        img3 = img3.resize((1530, 1000), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=700)
        title_lbl = Label(bg_img, text="STAFF ATTENDANCE SYSTEM", font=("time new roman", 25, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=30)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=35, width=1500, height=650)

        # left_label_frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Attendance Detais",
                                font=("time new roman", 12, "bold"))
        Left_frame.place(x=5, y=10, width=750, height=600)

        img_left = Image.open(r"college_images/logo-bg.png")
        img_left = img_left.resize((730, 170), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=150)

        # Class students information
        left_inside_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                       text=" Class staff information",
                                       font=("time new roman", 12, "bold"))
        left_inside_frame.place(x=5, y=180, width=730, height=310)
        # AttendanceId
        attendanceID_label = Label(left_inside_frame, text="AttendanceId",
                                   font=("time new roman", 12, "bold"), bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id,
                                       font=("time new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentsName_label = Label(left_inside_frame, text="Student name",
                                   font=("time new roman", 12, "bold"), bg="white")
        studentsName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentsName_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name,
                                       font=("time new roman", 12, "bold"))
        studentsName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Time
        class_label = Label(left_inside_frame, text="Time",
                            font=("time new roman", 12, "bold"), bg="white")
        class_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        class_entry = Entry(left_inside_frame, width=20,textvariable=self.var_atten_time,
                            font=("time new roman", 12, "bold"))
        class_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Day
        email_label = Label(left_inside_frame, text="Day",
                            font=("time new roman", 12, "bold"), bg="white")
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        email_entry = Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,
                            font=("time new roman", 12, "bold"))
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Attendance
        dep_label = Label(left_inside_frame, text="Attendance Status",
                          font=("time new roman", 12, "bold"))
        dep_label.grid(row=3, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(left_inside_frame, font=("time new roman", 12, "bold"),
                                 width=17)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # Roll no
        rollNo_label = Label(left_inside_frame, text="Roll no",
                             font=("time new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        rollNo_entry = Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll,
                             font=("time new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(left_inside_frame, text="Department",
                          font=("time new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("time new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # btn frames
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=200, width=710, height=80)

        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv,
                          font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        save_btn.grid(row=0, column=0, padx=5, pady=3)

        update_frame = Button(btn_frame, text="Export csv", command=self.exportCsv,
                              font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        update_frame.grid(row=0, column=1, padx=5, pady=3)

        delete_frame = Button(btn_frame, text="Update",
                              font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        delete_frame.grid(row=0, column=2, padx=5, pady=3)

        Reset = Button(btn_frame, text="Reset",
                       font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        Reset.grid(row=0, column=3, padx=5, pady=3)

        # right_label_frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Detais",
                                 font=("time new roman", 12, "bold"))
        Right_frame.place(x=770, y=10, width=720, height=600)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=10, width=710, height=445)

        # scroll bar table

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendaceReportTable = ttk.Treeview(table_frame, columns=(
        "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set,
                                                 yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Attendance ID")
        self.AttendaceReportTable.heading("roll", text="Roll")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("attendance", text="Attendance ")

        self.AttendaceReportTable["show"]="headings"
        self.AttendaceReportTable.column("id", width=100)
        self.AttendaceReportTable.column("roll", width=100)
        self.AttendaceReportTable.column("name", width=100)
        self.AttendaceReportTable.column("department", width=100)
        self.AttendaceReportTable.column("time", width=100)
        self.AttendaceReportTable.column("date", width=100)
        self.AttendaceReportTable.column("attendance", width=100)


        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

#  fetch data


    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
    # importCsv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
#  Export Csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open Csv",
                                             filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as  myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)

                messagebox.showinfo("Data Export", "Your data exported to"+os.path.basename(fln)+"successfully")

        except Exception as  es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self, event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
