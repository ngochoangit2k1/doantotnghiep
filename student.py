from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import  cv2

class Student:

    def __init__(self, root):
        self.root = root
        # vị trí nhận diện trên màng hình
        self.root.geometry("1530x900+0+0")
        self.root.title("face Recogniton System")
        # variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dod = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        # first ìmg
        img = Image.open(r"college_images/face_detection2x.png")
        img = img.resize((500, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=5, y=0, width=500, height=200)

        # second img
        img1 = Image.open(r"college_images/face_detection2x.png")
        img1 = img1.resize((500, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=500, height=200)

        # thirt img
        img2 = Image.open(r"college_images/face_detection2x.png")
        img2 = img2.resize((500, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1015, y=0, width=500, height=200)
        #         bg img
        img3 = Image.open(r"college_images/face_detection2x.png")
        img3 = img3.resize((2000, 1000), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=2000, height=700)

        title_lbl = Label(bg_img, text="STUDENTS MANAGEMENT SYSTEM", font=("time new roman", 25, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=30)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=35, width=1500, height=650)

        # left_label_frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Detais",
                                font=("time new roman", 12, "bold"))
        Left_frame.place(x=5, y=10, width=750, height=600)

        img_left = Image.open(r"college_images/face_detection2x.png")
        img_left = img_left.resize((730, 200), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=150)

        # current course

        Current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information",
                                          font=("time new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=130, width=730, height=130)

        # Department
        dep_label = Label(Current_course_frame, text="Department",
                          font=("time new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_dep, font=("time new roman", 12, "bold"),
                                 width=17)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(Current_course_frame, text="Course",
                             font=("time new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_course,
                                    font=("time new roman", 12, "bold"), width=17)
        course_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechnical")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(Current_course_frame, text="Year",
                           font=("time new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_year, font=("time new roman", 12, "bold"),
                                  width=17)
        year_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechnical")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(Current_course_frame, text="Semester",
                               font=("time new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_semester,
                                      font=("time new roman", 12, "bold"), width=17)
        semester_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechnical")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class students information
        Class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text=" Class students information",
                                         font=("time new roman", 12, "bold"))
        Class_student_frame.place(x=5, y=260, width=730, height=310)

        # StudentID
        studentsID_label = Label(Class_student_frame, text="StudentID",
                                 font=("time new roman", 12, "bold"), bg="white")
        studentsID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentsID_entry = ttk.Entry(Class_student_frame, textvariable=self.var_std_id, width=20,
                                     font=("time new roman", 12, "bold"))
        studentsID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentsName_label = Label(Class_student_frame, text="Student name",
                                   font=("time new roman", 12, "bold"), bg="white")
        studentsName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentsName_entry = ttk.Entry(Class_student_frame, textvariable=self.var_std_name, width=20,
                                       font=("time new roman", 12, "bold"))
        studentsName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division
        class_label = Label(Class_student_frame, text="class division",
                            font=("time new roman", 12, "bold"), bg="white")
        class_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        # class_entry = Entry(Class_student_frame, textvariable=self.var_div, width=20,
        #                     font=("time new roman", 12, "bold"))
        # class_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(Class_student_frame, textvariable=self.var_div,
                                 font=("time new roman", 12, "bold"), width=17)
        div_combo["values"] = ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Roll no
        rollNo_label = Label(Class_student_frame, text="Roll no",
                             font=("time new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        rollNo_entry = Entry(Class_student_frame, textvariable=self.var_roll, width=20,
                             font=("time new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(Class_student_frame, text="Gender",
                             font=("time new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        # gender_entry = Entry(Class_student_frame, textvariable=self.var_gender, width=20,
        #                      font=("time new roman", 12, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(Class_student_frame, textvariable=self.var_gender,
                                    font=("time new roman", 12, "bold"), width=17)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # DOB
        dob_label = Label(Class_student_frame, text="DOB",
                          font=("time new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = Entry(Class_student_frame, textvariable=self.var_dod, width=20, font=("time new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(Class_student_frame, text="Email",
                            font=("time new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = Entry(Class_student_frame, textvariable=self.var_email, width=20,
                            font=("time new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone number
        phone_label = Label(Class_student_frame, text="Phone number",
                            font=("time new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(Class_student_frame, textvariable=self.var_phone, width=20,
                                font=("time new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(Class_student_frame, text="Address",
                              font=("time new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = Entry(Class_student_frame, textvariable=self.var_address, width=20,
                              font=("time new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_label = Label(Class_student_frame, text="Teacher name",
                              font=("time new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = Entry(Class_student_frame, textvariable=self.var_teacher, width=20,
                              font=("time new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_student_frame, variable=self.var_radio1, text="take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=5, column=0)
        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(Class_student_frame, variable=self.var_radio1, text="no Photo Sample",
                                    value="No")
        radiobtn2.grid(row=5, column=1)

        # btn frames
        btn_frame = Frame(Class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=200, width=710, height=80)

        save_btn = Button(btn_frame, text="Save", command=self.add_data,
                          font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        save_btn.grid(row=0, column=0, padx=5, pady=3)

        update_frame = Button(btn_frame, text="Update", command=self.update_data,
                              font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        update_frame.grid(row=0, column=1, padx=5, pady=3)

        delete_frame = Button(btn_frame, text="Delete", command=self.delete_data,
                              font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        delete_frame.grid(row=0, column=2, padx=5, pady=3)

        Reset = Button(btn_frame, text="Reset", command=self.reset_data,
                       font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        Reset.grid(row=0, column=3, padx=5, pady=3)

        take_photo_btn = Button(btn_frame, text="Take photo", command=self.generate_dataset,
                                font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        take_photo_btn.grid(row=1, column=0, padx=5, pady=3)



        update_photo_btn = Button(btn_frame, text="Update photo",
                                  font=("time new roman", 12, "bold"), bg="blue", fg="white", width=15)
        update_photo_btn.grid(row=1, column=1, padx=5, pady=3)
        # right_label_frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Detais",
                                 font=("time new roman", 12, "bold"))
        Right_frame.place(x=770, y=10, width=720, height=600)

        img_right = Image.open(r"college_images/face_detection2x.png")
        img_right = img_right.resize((730, 200), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=705, height=150)

        #  search system
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search system",
                                  font=("time new roman", 12, "bold"))
        Search_frame.place(x=5, y=130, width=705, height=100)

        search_label = Label(Search_frame, text="Search by:", font=("time new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("time new roman", 12, "bold"), width=17)
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=18, font=("time new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search",
                            font=("time new roman", 12, "bold"), bg="blue", fg="white", width=8)
        search_btn.grid(row=0, column=3, padx=5, pady=3)

        showAll_btn = Button(Search_frame, text="Reset",
                             font=("time new roman", 12, "bold"), bg="blue", fg="white", width=8)
        showAll_btn.grid(row=0, column=4, padx=5, pady=3)

        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=705, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          columns=(
                                              "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                              "dod", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("gender", text="Gender")

        self.student_table.heading("dod", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teachers")
        self.student_table.heading("photo", text="PhotoSample")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dod", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)

        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #    function decration
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="abc.123",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dod.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="abc.123",
                                       database="face_recognizer")

        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dod.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # update data

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this students details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="abc.123",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student set Dep=%s, course=%s, year=%s, semester=%s,  name=%s, division=%s, roll=%s, gender=%s, dod=%s, email=%s, phone=%s ,address=%s, teacher=%s, photoSample=%s where Student_Id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dod.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfylly update complete ", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #     delete function

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("error", "Student id must be required ", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="abc.123",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "DELETE from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully delete student detals", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"DUe to:{str(es)}", parent=self.root)

    #   reset data
    def reset_data(self):
        self.var_dep.set("SELECT Department")
        self.var_course.set("SELECT course")
        self.var_year.set("SELECT year")
        self.var_semester.set("SELECT semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("SELECT division ")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dod.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #  Gennere data set or Take     photo sample

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="abc.123",
                                                   database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                        id+=1
                my_cursor.execute(
                    "UPDATE student set Dep=%s, course=%s, year=%s, semester=%s,  name=%s, division=%s, roll=%s, gender=%s, dod=%s, email=%s, phone=%s ,address=%s, teacher=%s, photoSample=%s where Student_Id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dod.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

    #             load predifiend data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #             Scaling factor=1.3
    #             Minimum Neighbor=5
                    for ( x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return  face_cropped

                cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50) ,cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets compled!!!")
            except Exception as  es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
