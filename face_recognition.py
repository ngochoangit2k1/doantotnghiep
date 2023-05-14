import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import numpy as np
import gspread

from oauth2client.service_account import ServiceAccountCredentials
import time
import asyncio
import threading

from  dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())
connection_string = f"mongodb+srv://shopforme34:shopforme34@cluster0.f3g5jcd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()

class Face_Recognition:

    def __init__(self, root):
        self.root = root
        # vị trí nhận diện trên màng hình
        self.root.geometry("1530x900+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("time new roman", 25, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=30)


        # bg img
        img_bottom = Image.open(r"college_images/face-recognition.png")
        img_bottom = img_bottom.resize((1530, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=55, width=1530, height=700)

        # btn
        b1_1 = Button(f_lbl, text="Face Recognition ", command=self.face_recog
                      , cursor="hand2", font=("time new roman", 18, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=350, y=600, width=250, height=60)

    #         attendence
    #     def mark_attendence(self,i , r , n ,d):
    #         with open("kiran.csv", "r+", newline="\n") as f:
    #             myDataList = f.readline()
    #             name_list=[]
    #
    #             for line in myDataList:
    #                 entry=line.split((","))
    #                 name_list.append((entry[0]))
    #             if((i not in name_list) and (r not  in name_list) and (n not  in name_list) and (d not  in name_list)):
    #                 now=datetime.now()
    #                 d1=now.strftime("%d-%m-%Y")
    #                 dtString=now.strftime("%H:%M:%S")
    #
    #                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")

    #         face recogmition
    def write_sheet(self, i, r, n, d):
        name_list = []
        creds = ServiceAccountCredentials.from_json_keyfile_name("face-api.json")
        file = gspread.authorize(creds)
        workbook = file.open('dataface')
        sheet = workbook.sheet1
        # data = pd.DataFrame(sheet.get_all_records())
        # print(data)
        if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
            now = datetime.now()
            d1 = now.strftime("%d-%m-%Y")
            dtString = now.strftime("%H:%M:%S")

            def write_data():
                data1 = [i, r, n, d, dtString, d1, 'Preset']
                sheet.insert_row(data1, len(sheet.get_all_values()) + 1)

            write_data()
            messagebox.showinfo("Thông báo", "Ghi dữ liệu thành công!")
            t = threading.Thread(target=self.face_recog)
            t.start()

    def write_data(self, i, r, n, d):
        name_list = []
        test = client.test
        timekeeping = test.timekeepings
        if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
            now = datetime.now()
            d1 = now.strftime("%d-%m-%Y")
            dtString = now.strftime("%H:%M:%S")

            doc = {"Id":i, "roll": r, "name": n, "Dep": d, "day": d1, "time": dtString}
            name_list.append(doc)
        timekeeping.insert_many(name_list)



    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            test = client.test
            timekeeping = test.users
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # vẽ hình chữ nhật lấy img làm gốc
                id , predict = clf.predict(gray_image[y:y + h,
                                          x:x + w])  # dự đoán đối tượng trong hình chữ nhật trên kết qảu dự đoán lưu trên id và phần trăm giống lưu trên predict
                confidence = int((100 * (1 - predict / 300)))  # kết quả phần trăm dự đoán

                name = timekeeping.find_one({"zid": id})
                n = name["fullname"]
                # n = "+".join(n)

                roll = timekeeping.find_one({"zid": id})
                r = roll["role"]
                # r = "+".join(r)

                dep = timekeeping.find_one({"zid": id})
                d = dep["deparment"]
                # d = "+".join(d)

                id = timekeeping.find_one({"zid": id})
                i = id["zid"]
                # i = "+".join(i)

                if confidence > 77:  # kết quả dự đoán lớn hơn 77%
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    # asyncio.ensure_future(self.wait_and_run(1, self.write_sheet(i, r, n, d)))

                    # time.sleep(5)

                    self.write_data(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):  # vẽ đường viền xung quanh khuôn mặt nhận diện
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")  # chuyên dùng để sử lý pát hiện khuôn mặt
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()