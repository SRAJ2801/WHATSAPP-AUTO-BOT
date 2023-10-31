#*************Disclaimer -- Do not use this app for the bussiness purpose*******************This is only for learning purpose********
from tkinter import *
from tkinter import filedialog
import webbrowser
import time
import pyautogui as gui
import csv
from tkinter import messagebox
from io import BytesIO
import win32clipboard
from PIL import Image
import urllib.parse

global path
global success
global numentry
global imagepath
global image_success
global message
global instruct

imagepath = ""
path = ""
root = Tk()
root.title("Whatsapp messages")
root.configure(background="snow", height=700, width=1000)


def closeinstruct():
    global instruct
    instruct.place_forget()


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def selectimage():
    global imagepath
    global image_success

    root.imagename = filedialog.askopenfilename(initialdir="d:", title="select a file"
                                                , filetype=(("JPEG Files", "*.jpg"), ("PNG files", "*.png")))
    imagepath = root.imagename
    if imagepath != "":
        image_success = Label(root, text="Image received", fg="red", bg="snow", font="times 14")
        image_success.place(relx=0.72, rely=0.72)


def selectfile():
    global path
    global success
    root.filename = filedialog.askopenfilename(initialdir="d:", title="select a file"
                                               , filetype=(("CSV Files", "*.csv"), ("all files", "*.*")))
    path = root.filename
    if path != "":
        success = Label(root, text="File has been received", fg="red", bg="snow", font="times 14")
        success.place(relx=0.47, rely=0.54)


def submitt():
    global path
    global imagepath
    global numentry
    global success
    global image_success
    global message
    numbers = []
    messages = []
    names = []
    if path != "":
        success.place_forget()
        with open(path, 'rt') as f:
            data = csv.reader(f)
            for row in data:
                if len(row) >= 3:  # beta please-Ensure the row has at least three elements (name, phone, message)
                    name = row[0].strip()
                    phone = row[1].strip()
                    emessage = row[2].strip()
                
                    if len(phone) > 2:
                        if phone[0] == "+" or phone.isnumeric():
                            numbers.append(phone)
                            names.append(name)
                            messages.append(emessage)
    else:
        st = numentry.get()
        if st == "" or st == "Enter Numbers with their country code...":
            messagebox.showerror("No data?", "Please Upload a file or type numbers")
        else:
            numbers = [i.strip().rstrip() for i in st.split(",")]
    try:
        msg = urllib.parse.quote(message.get())
    except Exception:
        messagebox.showerror("Sorry!", "Given Message is not supported!No emojis please!")
    if msg == "" and imagepath == "":
        messagebox.showerror("No data?", "Please type or attach a msg")
    else:
        c = 1
        if imagepath == "":
            print(len(numbers))
            for i in range(20):
                if c == 1:
                    webbrowser.open("https://web.whatsapp.com")
                    time.sleep(20)
                    gui.keyDown('ctrl')
                    gui.press('w')
                    gui.keyUp('ctrl')
                    time.sleep(20)
                    c += 1
                url = "https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(numbers[i], "Hi "+names[i]+" "+messages[i])
                webbrowser.open(url)
                time.sleep(10)
                gui.press('enter')
                time.sleep(10)
                #gui.keyDown('ctrl')
                #gui.press('w')
                #gui.keyUp('ctrl')
                #time.sleep(5)
                #gui.press('enter')
                if i == numbers[-1]:
                    time.sleep(10)
                else:
                    time.sleep(10)
        else:
            image_success.place_forget()
            filepath = imagepath
            try:
                image = Image.open(filepath)
                output = BytesIO()
                image.convert("RGB").save(output, "BMP")
                data = output.getvalue()[14:]
                output.close()
                send_to_clipboard(win32clipboard.CF_DIB, data)
            except Exception:
                messagebox.showerror("sorry", "Not suitable attachment")
                return

            for i in range(10):
                if c == 1:
                    webbrowser.open("https://web.whatsapp.com")
                    time.sleep(10)
                    gui.keyDown('ctrl')
                    gui.press('w')
                    gui.keyUp('ctrl')
                    time.sleep(10)
                    c += 1
                url = "https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(numbers[i], msg)
                webbrowser.open(url)
                time.sleep(10)
                gui.keyDown('ctrl')   
                gui.press('v')
                gui.keyUp('ctrl')
                time.sleep(10)
                gui.press('enter')
                time.sleep(10)
                gui.keyDown('ctrl')
                gui.press('w')
                gui.keyUp('ctrl')
                time.sleep(10)
                gui.press('enter')
                if i == numbers[-1]:
                    time.sleep(10)
                else:
                    time.sleep(10)
        imagepath = ""
        path = ""
        numentry.delete(0, END)
        message.delete(0, END)


canvas1 = Canvas(root, bg="lightblue")
canvas1.place(relx=0, rely=0, relwidth=1, relheight=0.2)

f1 = Frame(canvas1, bg="lightblue")
f1.place(relx=0.02, rely=0.02, relwidth=0.9, relheight=0.5)

head_text = Label(f1, text="what-a-bot by Sonu raj", font="Helvetica 40 bold", fg="black", bg="lightblue")
head_text.place(relx=0.18, rely=0.03)

number = Label(root, text="Enter(,) separated numbers(without '+')", font="Helvetica 16 bold", bg="snow")
number.place(relx=0.02, rely=0.22)

numentry = Entry(root, font="Helvetica 16")
numentry.place(relx=0.02, rely=0.30, relwidth=0.9, relheight=0.15)

insert_label = Label(root, text="or insert .csv file", bg="snow", font="Helvetica 14 bold")
insert_label.place(relx=0.02, rely=0.48)

select = Button(root, text="Select a file", command=selectfile)
select.place(relx=0.05, rely=0.54, relwidth=0.4)

Message_label = Label(root, text="Enter your message below", font="Helvetica 16 bold", bg="snow")
Message_label.place(relx=0.02, rely=0.6)

attachment_label = Label(root, text="Add an image:", font="Helvetica 16 bold", bg="snow")
attachment_label.place(relx=0.65, rely=0.6)

select_image = Button(root, text="Select an attachment", command=selectimage)
select_image.place(relx=0.65, rely=0.66, relwidth=0.3)

message = Entry(root, font="Helvetica 18")
message.place(relx=0.02, rely=0.65, relwidth=0.6, relheight=0.2)

submit = Button(root, text="Submit", font="impact 20 bold", fg="white", bg="green", command=submitt)
submit.place(relx=0.3, rely=0.87, relwidth=0.4)


root.mainloop()