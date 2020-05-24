import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sqlite3
import CenterWindow
import smtplib


def about():
    root = Tk()
    root.title('About Fitness Calculator')
    CenterWindow.center_window(root, 600, 400)
    frame1 = Frame(root, bg='gold')
    frame1.pack(fill=X)

    abt = """The main objective of this project is to provide proper Fitness details to the students and faculty of the university.\nThis project tells us about how fit a person is. \nA proper way of getting details about the health of the user will keep the user updated about his \nhealth and he will get a quick check up if he is having any disease or not.
        \nThis interface will provide the user to input his details and will get a proper report of his health.\n
        Our prime motive is if the patient is not well, he will come to know about his illness and get a proper \ntreatment on time. \nWith this a precious life can be saved.
        """

    Label(frame1, text='Fitness Calculator', bg='gold', font="Verdana 20 bold").pack()
    Label(frame1, text='v0.1', bg='green', fg='white', font="Verdana 10 bold").pack()

    frame2 = Frame(root, bg='powder blue')
    frame2.pack(fill=BOTH, expand=1)

    Label(frame2, text=abt, bg='orange').pack()

    frame3 = Frame(root, bg='White')
    frame3.pack(fill=BOTH, expand=1)
    Label(frame3, text='Front-End Developer: Aman Deep', bg='powder blue', font="Verdana 10 bold").place(x=200, y=20)
    Label(frame3, text='Back-End Developer: Sitesh Roy', bg='powder blue', font="Verdana 10 bold").place(x=200, y=40)
    Label(frame3, text='Design: Basit Manzoor', bg='powder blue', font="Verdana 10 bold").place(x=200, y=60)


def history():
    global name, email
    root = Tk()
    root.title('Enter details')
    CenterWindow.center_window(root, 650, 200)

    frame1 = Frame(root, bg='gold')
    frame1.pack(fill=X)

    Label(frame1, text='Check your History', bg='gold', font="Verdana 10 bold").pack()

    frame2 = Frame(root, bg='powder blue')
    frame2.pack(fill=BOTH, expand=1)

    Label(frame2, text='Name', font="Verdana 20", bg='powder blue').grid(row=1, column=7, padx=10, pady=10)
    name = Entry(frame2, width=15, font="Verdana 20")
    name.grid(row=1, column=8, padx=10, pady=10, ipady=5)

    Label(frame2, text='Email', font="Verdana 20", bg='powder blue').grid(row=2, column=7, padx=10, pady=10)
    email = Entry(frame2, width=15, font="Verdana 20")
    email.grid(row=2, column=8, padx=10, pady=10, ipady=5)

    Button(frame2, text='Show Details', bg='green', fg='white', command=showdetails, font="Verdana 10").grid(row=3, column=8, padx=10, pady=10)
    Button(frame2, text='Back', bg='red', fg='white', command=root.destroy, font="Verdana 10").grid(row=3, column=1, padx=10, pady=10)


def send_mail():
    sender = ""
    receiver = set_email.get()
    password = ""
    mail_con = smtplib.SMTP("smtp.gmail.com", 587)
    mail_con.starttls()
    mail_con.login(sender, password)

    msg = """From: Fitness Calculator <%s>
            To: %s <%s>
            Subject: Fitness Report

            Name: %s
            Age: %s
            Email: %s
            Weight: %s
            Height: %s
            BP: %s
            Pulse rate: %s
            RBC count: %s
            WBC count: %s
            Platelets: %s
            HB: %s
            Uric acid: %s
            Cholestrol: %s
            Report Date: %s

    """ % (sender, full_name.get(), set_email.get(), full_name.get(), age_val.get(), set_email.get(), weight_val.get(), height_val.get(), bp_val.get(), pulse_rate_val.get(), rbc_count_val.get(), wbc_count_val.get(), platelets_val.get(), hb_val.get(), uric_acid_val.get(), cholesterol_val.get(), set_date.get())

    mail_con.sendmail(sender, receiver, msg)
    mail_con.quit()


def showdetails():
    cnx = sqlite3.connect('data.db')
    cursor = cnx.cursor()
    data = cursor.execute("SELECT * FROM report WHERE fullname='" + name.get() + "' and email='" + email.get() + "'")

    root = Tk()
    root.title('History about ' + name.get())
    listbox = Listbox(root, width=60, height=20)
    listbox.pack()

    for i in data:
        print(i)
        listbox.insert(END, 'Name = ' + i[0])
        listbox.insert(END, 'Age = ' + i[1])
        listbox.insert(END, 'Email = ' + i[2])
        listbox.insert(END, 'Weight = ' + i[3])
        listbox.insert(END, 'Height = ' + i[4])
        listbox.insert(END, 'BP = ' + i[5])
        listbox.insert(END, 'Pulse rate = ' + i[6])
        listbox.insert(END, 'RBC count = ' + i[7])
        listbox.insert(END, 'WBC count = ' + i[8])
        listbox.insert(END, 'Platelets = ' + i[9])
        listbox.insert(END, 'HB = ' + i[10])
        listbox.insert(END, 'Uric acid = ' + i[11])
        listbox.insert(END, 'Cholestrol = ' + i[12])
        listbox.insert(END, 'Report Date = ' + i[13])
        listbox.insert(END, '\n\n**********************************************************')

    cnx.commit()
    cursor.close()
    cnx.close()


def call_bmi():
    weight_val1 = weight_val.get()
    height_val1 = ((height_val.get())/100)

    try:
        bmi_val = (weight_val1)/(height_val1*height_val1)
        return str(round(bmi_val, 2))

    except ZeroDivisionError:
        bmi_val = 0
        return str(bmi_val)


def BMI_catg():
    x = call_bmi()
    if x in range(0, 19):
        return '(Underweight)'
    elif x in range(25, 31):
        return '(Overweight)'
    elif x in range(19, 25):
        return '(Healthy weight)'
    else:
        return '(Obese)'
    

def call_me():
    top = Toplevel()
    top.geometry("500x500+150+150")
    top.title('Confirm')

    label = Label(top, text = "RBC Count").place(x=40, y=50)

    label_a = Label(top, text=str(fetch7.get())).place(x=90, y=50)
    label_b =Label(top, text=str(RCB_Cal())).place(x=120, y=50)


def BP_Cal():

     a1=bp_val.get()
     if a1 in range(40,90):
        return  '(Low)'
     elif a1 in range(90,120):
        return '(Normal)'
     elif a1 in range(120,140):
        return '(Prehypertension)'
     elif a1 in range(140,160):
        return '(High: stage 1 hypertension)'
     elif a1 in range(180,300):
        return '(High: stage 2 hypertension)'
     else:
        return '(Dead)'
        
def Pulserate_Cal():
    
    b1=pulse_rate_val.get()
    if b1 in range(60,100):
        return  '(Low)'
    elif b1 in range(0,60):
        return '(Normal)'
    elif b1 in range(100,200):
        return '(High)'
    else:
        return '(Dead)'

        
def RCB_Cal():
    c1=rbc_count_val.get()
    if c1 in range(4,6):
        return '(Normal)'
    elif c1 in range(0,4):
        return  '(Low)'
    elif c1 in range(6,12):
        return '(High)'
    else:
        return '(Not defined)'


def WBC_cal():
    d1=wbc_count_val.get()
    if d1 in range(4500,11000):
        return '(Normal)'
    elif d1 in range(0,4500):
        return  '(Low)'
    elif d1 in range(11000,20000):
        return '(High)'
    else:
        return '(Not defined)'


def Platelets_cal():

    e1 = platelets_val.get()
    if e1 in range(150000,450000):
        return '(Normal)'
    elif e1 in range(0,150000):
        return '(Thrombocytopenia)'
    elif e1 in range(450000,750000):
        return '(Thrombocytosis)'
    else:
        return '(Not defined)'


def hb_Cal():
    f1 = hb_val.get()
    if f1 in range(14, 18):
        return '(Normal)'
    elif f1 in range(0, 14):
        return  '(Low)'
    elif f1 in range(18, 50):
        return '(High)'
    else:
        return '(Not defined)'


def Uricacid_Cal():
    g1 = uric_acid_val.get()
    if g1 in range(3, 6):
        return '(Normal)'
    elif g1 in range(0, 3):
        return '(Asymptomatic hyperuricemia)'
    elif g1 in range(6, 9):
        return '(Hyperuricemia)'
    else:
        return '(Not defined)'


def cholesterol_Cal():
    h1 = cholesterol_val.get()
    if h1 in range(100, 200):
        return '(Normal)'
    elif h1 in range(200, 239):
        return '(Borderline high)'
    elif h1 in range(239, 400):
        return '(High)'
    elif h1 in range(0, 100):
        return  '(Low)'   
    else:
        return '(Not defined)'


def Submission_successful():
    if check_validation() == True:
        save_database()
        messagebox.showinfo("Success", "Your submission is successful!")
        # send_mail()
        # messagebox.showinfo("Email", "Your Report has been mailed!")
        toplevel()   # Calling the function topLevel()
    else:
        messagebox.showwarning("Inputs missing", "Kindly fill up all the details!")


def not_saved():
    response = messagebox.askquestion("Alert", "Your data will not be saved, still want to exit?")
    if response == 'yes':
        root.destroy()


def int_validate(inp):
    if inp.isdigit():
        return True
    elif inp is "":
        return True
    else:
        return False


def toplevel():
    top = Toplevel()
    top.title("Final Report")
    CenterWindow.center_window(top, 650, 600)
    top.resizable(0, 0)

    label_top0 = Label(top, text="Fitness Report", width=20, font=('bold', 20))
    label_top0.place(x=170, y=120)
    label_top0.pack()

    canvas1 = Canvas(top)
    canvas1.pack()
    line1 = canvas1.create_line(10, 3, 400, 3, fill="green")

    label_top0 = Label(top, text="Date : ", width=20, font=myFont3)
    label_top0.place(x=460, y=70)

    label_top0a = Label(top, text=set_date.get(), font=myFont5).place(x=500, y=90)

    label_top1 = Label(top, text="1. Full Name : ", width=15, font=myFont3, relief=RAISED, bg = 'turquoise1')
    label_top1.place(x=80, y=130)

    label_top1a = Label(top, text=full_name.get()).place(x=210, y=130)

    label_top2 = Label(top, text="2. Age : ", width=15, font=myFont3, relief=RAISED, bg='turquoise1')
    label_top2.place(x=340, y=130)

    label_top2a = Label(top, text=str(age_val.get())+' yrs' ).place(x=470, y=130)

    label_top3 = Label(top, text="3. Weight : ", width=15, font=myFont3, relief = RAISED, bg = 'turquoise1')
    label_top3.place(x=80, y=160)

    label_top3a = Label(top, text=str(weight_val.get())+' kg').place(x=210, y=160)

    label_top4 = Label(top, text="4. Height : ", width=15, font=myFont3, relief = RAISED, bg = 'turquoise1')
    label_top4.place(x=340, y=160)

    label_top4a = Label(top, text=str(weight_val.get())+' cm').place(x=470,y=160)

    label_top5 = Label(top, text="5. BMI : ", width=15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top5.place(x=80, y=190)

    label_top5a = Label(top, text = call_bmi()).place(x=210,y=190)
    label_top5b = Label(top, text = str(BMI_catg())).place(x=240,y=190)

    label_top6 = Label(top, text = "6. BP : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top6.place(x=80,y=215)

    label_top6a = Label(top, text = str(bp_val.get())).place(x=210,y=215)
    label_top6b = Label(top, text = str(BP_Cal())).place(x=240,y=215)
    
    label_top7 = Label(top, text = "7. Pulse Rate : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top7.place(x=80,y=240)

    label_top7a = Label(top, text = str(pulse_rate_val.get())).place(x=210,y=240)
    label_top7b = Label(top, text = str(Pulserate_Cal())).place(x=240,y=240)

    label_top8 = Label(top, text = "8. RBC Count : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top8.place(x=80,y=265)

    label_top8a = Label(top, text = str(rbc_count_val.get())).place(x=210,y=265)
    label_top8b = Label(top, text = str(RCB_Cal())).place(x=240,y=265)
    
    label_top9 = Label(top, text = "9. WBC Count : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top9.place(x=80,y=290)

    label_top9a = Label(top, text = str(wbc_count_val.get())).place(x=210,y=290)
    label_top9b = Label(top, text = str(WBC_cal())).place(x=240,y=290)

    label_top10 = Label(top, text = "10. Platelets : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top10.place(x=80,y=315)

    label_top10a = Label(top, text = str(platelets_val.get())).place(x=210,y=315)
    label_top10b = Label(top, text = str(Platelets_cal())).place(x=240,y=315)    

    label_top11 = Label(top, text = "11. HB : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top11.place(x=80,y=340)

    label_top11a = Label(top, text = str(hb_val.get())).place(x=210,y=340)
    label_top11b = Label(top, text = str(hb_Cal())).place(x=240,y=340)

    label_top12 = Label(top, text = "12. Uric Acid : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top12.place(x=80,y=365)

    label_top12a = Label(top, text = str(uric_acid_val.get())).place(x=210,y=365)
    label_top12b = Label(top, text = str(Uricacid_Cal())).place(x=240,y=365)

    label_top13 = Label(top, text = "13. Cholesterol : ", width= 15, font = myFont3, relief = RAISED, bg = 'turquoise1')
    label_top13.place(x=80,y=390)

    label_top13a = Label(top, text = str(cholesterol_val.get())).place(x=210,y=390)
    label_top13b = Label(top, text = str(cholesterol_Cal())).place(x=240,y=390)

    top.mainloop()

#def email_validation():


def check_validation():
    fullname = full_name.get()
    age = age_val.get()
    email = set_email.get()
    weight = weight_val.get()
    height = height_val.get()
    BP = bp_val.get()
    pulserate = pulse_rate_val.get()
    rbccount = rbc_count_val.get()
    wbccount = wbc_count_val.get()
    platelets = platelets_val.get()
    hb = hb_val.get()
    uricacid = uric_acid_val.get()
    cholestrol = cholesterol_val.get()
    report_date = set_date.get()

    gender = var.get()

    if fullname == '':
        return False
    elif age == '':
        return False
    elif email == '':
        return False
    elif weight == '':
        return False
    elif weight == '':
        return False
    elif height == '':
        return False
    elif BP == '':
        return False
    elif gender != 1 and gender != 2:
        return False
    elif pulserate == '':
        return False
    elif rbccount == '':
        return False
    elif wbccount == '':
        return False
    elif platelets == '':
        return False
    elif hb == '':
        return False
    elif uricacid == '':
        return False
    elif cholestrol == '':
        return False
    elif report_date == '':
        return False
    else:
        return True


def save_database():
    fullname = full_name.get()
    age = age_val.get()
    email = set_email.get()
    weight = weight_val.get()
    height = height_val.get()
    BP = bp_val.get()
    pulserate = pulse_rate_val.get()
    rbccount = rbc_count_val.get()
    wbccount = wbc_count_val.get()
    platelets = platelets_val.get()
    hb = hb_val.get()
    uricacid = uric_acid_val.get()
    cholestrol = cholesterol_val.get()
    report_date = set_date.get()


    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS report(fullname TEXT, age TEXT, email TEXT, weight TEXT, height TEXT, BP TEXT, pulserate TEXT, rbccount TEXT, wbccount TEXT, platelets TEXT, hb TEXT, uricacid TEXT, cholestrol TEXT, report_date TEXT)")
    cur.execute("INSERT INTO report VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (fullname, age, email, weight, height, BP, pulserate, rbccount, wbccount, platelets, hb, uricacid, cholestrol, report_date))
    # print(fullname, age, email, weight, height, BP, pulserate, rbccount, wbccount, platelets, hb, uricacid, cholestrol, report_date)
    con.commit()
    cur.close()
    con.close()


root = Tk()
CenterWindow.center_window(root, 650, 600)
root.resizable(0, 0)
root.title("Fitness Calculator")
root.configure(background="powder blue")


#Declaration of different font-family
myFont1 = Font(family="Times New Roman", weight = "bold",size= 100)
myFont2 = Font(family="Courier",size=10,weight='bold')
myFont3 = Font(family="Helvetic",size=10, slant = 'italic')
myFont4 = Font(family="OpenSymbol",size=10, slant = 'italic')
myFont5 = Font(family="OpenSymbol",size=10, slant = 'italic', underline = 1)


top_frame = Frame(root, width=650, height = 100,background='gold').place(x=0,y=0)
label_0 = Label(top_frame, text="Fitness Calculator", width=20, font="Verdana 20 bold", bg='gold')
label_0.place(x=160, y=30)

canvas = Canvas(top_frame)
canvas.place(x=160, y=97)
line1 = canvas.create_line(6, 2, 400, 2, fill="green")

second_frame= Frame(root, width=650, height=500, background="powder blue").place(x=0, y=100)

label_1 = Label(second_frame, text="Full Name", width=20, font=myFont3, bg="powder blue")
label_1.place(x=40, y=130)


full_name = StringVar()                                                                                                     #Variable Used = full_name
entry_1 = Entry(second_frame, bd=3, textvariable=full_name)
entry_1.place(x=170, y=130)
entry_1.focus()                                                                                                                  # Set the focus/ cursor automatically on the entry box of Full Name


reg = root.register(int_validate)

label_2 = Label(second_frame, text="Age", width=20,font=myFont3,bg="powder blue")
label_2.place(x=320,y=130)

age_val = IntVar()                                                                                                              #Variable Used = age_val
entry_2 = Entry(second_frame, bd=3)
entry_2.place(x=430,y=130)
entry_2.config(validate="key", validatecommand=(reg, '%P'), textvariable= age_val)


label_3a = Label(second_frame, text="Email",  width=20,font=myFont2, bg="powder blue")
label_3a.place(x=40, y=160)

set_email = StringVar()   # Variable Used = set_email
entry_3a = Entry(second_frame, textvariable=set_email, bd=3)
entry_3a.place(x=170, y=160)
set_email.set("@gmail.com")

label_3b = Label(second_frame, text="Date", width=20, font=myFont2, bg="powder blue")
label_3b.place(x=320, y=160)

set_date = StringVar()   # Variable Used = set_date

entry_3b = Entry(second_frame, textvariable=set_date, bd=3)
set_date.set(datetime.date.today())

entry_3b.place(x=430, y=160)

label_4 = Label(second_frame, text="Gender", width=20, font=myFont4, bg="powder blue")
label_4.place(x=40, y=190)
var = IntVar()                                                                                                                       #Variable Used = var(verify it as it is a radiobutton variable)
Radiobutton(second_frame, text="Male", padx=5,variable=var, value=1,font=myFont4, bg="powder blue").place(x=165,y=190)
Radiobutton(second_frame, text="Female", padx=20,variable=var, value=2, font=myFont4, bg="powder blue").place(x=220,y=190)


label_4a = Label(second_frame, text="Height", width=20, font=myFont4, bg="powder blue")
label_4a.place(x=320, y=190)

height_val = IntVar()         # Variable Used = height_val
entry_4a = Entry(second_frame, bd=3, textvariable=height_val)
entry_4a.place(x=430,y=190)
entry_4a.config(validate="key", validatecommand=(reg, '%P'))


label_5 = Label(second_frame, text="Weight", width=20, font=("bold", 10), bg="powder blue")
label_5.place(x=40, y=215)

weight_val = IntVar()                                                                                                                       #Variable Used = weight_val
entry_5 = Entry(second_frame, bd=3, textvariable=weight_val)
entry_5.place(x=170, y=215)
entry_5.config(validate="key", validatecommand=(reg, '%P'))



'''label_6 = Label(root, text="Height", width=20,font=("bold",10))
label_6.place(x=40,y=235)

entry_6 = Entry(root, fg='magenta', bd  = 3)
entry_6.place(x=170,y=235)
entry_6.config(validate="key", validatecommand=(reg, '%P'))'''



label_7 = Label(second_frame, text="BP", width=20,font=("bold",10), bg="powder blue")
label_7.place(x=40, y=235)

bp_val = IntVar()         # Variable Used =bp_val
entry_7 = Entry(second_frame, bd=3, textvariable = bp_val)
entry_7.place(x=170,y=235)


label_8 = Label(second_frame, text="Pulse Rate", width=20,font=("bold",10), bg="powder blue")
label_8.place(x=40,y=255)

pulse_rate_val = IntVar()                                                                                                                   #Variable Used = pulse_rate_val
entry_8 = Entry(second_frame, bd  = 3, textvariable = pulse_rate_val)
entry_8.place(x=170,y=255)
entry_8.config(validate="key", validatecommand=(reg, '%P'))

label_9 = Label(second_frame,text="RBC Count", width=20,font=("bold",10), bg="powder blue")
label_9.place(x=40,y=275)


rbc_count_val= IntVar()                                                                                                                       #Variable Used = rbc_count_val
entry_9 = Entry(second_frame, bd  = 3, textvariable = rbc_count_val)
entry_9.place(x=170,y=275)
entry_9.config(validate="key", validatecommand=(reg, '%P'))

label_10 = Label(second_frame, text="WBC Count", width=20,font=("bold",10), bg="powder blue")
label_10.place(x=40,y=295)


wbc_count_val = IntVar()                                                                                                                    #Variable Used = wbc_count_val
entry_10 = Entry(second_frame, bd  = 3,  textvariable = wbc_count_val )
entry_10.place(x=170,y=295)
entry_10.config(validate="key", validatecommand=(reg, '%P'))

label_11= Label(second_frame, text="Platelets", width=20,font=("bold",10), bg="powder blue")
label_11.place(x=40,y=315)

platelets_val = IntVar()                                                                                                                       #Variable Used = platelets_val
entry_11 = Entry(second_frame, bd  = 3,  textvariable = platelets_val)
entry_11.place(x=170,y=315)
entry_11.config(validate="key", validatecommand=(reg, '%P'))

label_12= Label(second_frame, text="HB", width=20,font=("bold",10), bg="powder blue")
label_12.place(x=40,y=335)

hb_val = IntVar()                                                                                                                                   #Variable Used = hb_val
entry_12= Entry(second_frame, bd  = 3, textvariable = hb_val)
entry_12.place(x=170,y=335)
entry_12.config(validate="key", validatecommand=(reg, '%P'))

label_13 = Label(second_frame, text="Uric Acid", width=20,font=("bold",10), bg="powder blue")
label_13.place(x=40,y=355)

uric_acid_val = IntVar()                                                                                                                       #Variable Used = uric_acid_val
entry_13 = Entry(second_frame, bd  = 3, textvariable = uric_acid_val)
entry_13.place(x=170,y=355)
entry_13.config(validate="key", validatecommand=(reg, '%P'))

label_14 = Label(second_frame, text="Cholesterol", width=20,font=("bold",10), bg="powder blue")
label_14.place(x=40,y=375)

cholesterol_val = IntVar()                                                                                                                       #Variable Used = cholesterol_val
entry_14 = Entry(second_frame, bd=3, textvariable = cholesterol_val )
entry_14.place(x=170, y=375)
entry_14.config(validate="key", validatecommand=(reg, '%P'))



b = Button(second_frame, text='Generate Report',width=20, height=2, font="Verdana 10", bg='blue',fg='white',command=Submission_successful).place(x=250,y=450)

#root.title("Exit Button")
exitButton = Button(second_frame, text="Quit", bg='red', fg='white', width=10, font="Verdana 8", command=not_saved)
exitButton.place(x=520, y=550)


aboutButton = Button(second_frame, text="About", width=13, bg='blue', fg='white',command=about)
aboutButton.place(x=280, y=540)

historyButton = Button(second_frame, text="History", width=13, bg='blue', fg='white', command=history)
historyButton.place(x=80, y=540)

root.mainloop()







