from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from copy import deepcopy
## FRAME
frame = Tk()
frame.title("Kõrvaerila Kalkulaator v0.1")
frame.config(bg = "#F8F8F8")
frame.geometry("300x105")
## FUNCTIONS
def users_subjects():
    values = []
    for j in range(len(p_eriala_choose)):
        values.append(j)
    n = 0
    while n <= len(p_eriala_choose)-1:
        values[n] = var[n].get()
        n += 1
    values_true = deepcopy(values)
def getpeaeriala(arg):
    global p_eriala
    p_eriala = peaeriala.get()
def getkorvaeriala(arg):
    global k_eriala
    k_eriala = korvaeriala.get()
def info():
    mes = "App lihtsa Kõrvaeriala kalkuleerimise jaoks. Made by Alan Durnev and Nikita Kirienko (2014)."
    messagebox.showinfo(message=mes)
def getday(arg):
    global d_ay
    d_ay = day.get()
def getmonth(arg):
    global m_onth
    m_onth = month.get()
def getyear(arg):
    global y_ear
    y_ear = year.get()
## STEP 2
def step2():
    Z = 1
    key_1 = 0
    while Z <= 5:
        try:
            Z_1 = p_eriala
            Z_2 = k_eriala
            Z_3 = d_ay
            Z_4 = m_onth
            Z_5 = y_ear
        except:
            messagebox.showinfo(message="Kõik peab olema täidetud")
            break
        Z += 1
        if Z == 5:
            key_1 = 1
    if key_1 == 0:
        frame.mainloop()
    else:
        frame.destroy()
        ##
        global p_eriala_choose
        p_eriala_choose = []
        p_file = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\peaeriala\\" + str(p_eriala.lower()) + ".txt", encoding = "UTF-8")
        p_files = p_file.readlines()
        p_files[0] = p_files[0].replace("\ufeff", "")
        for p in p_files:
            splited = p.split(";")
            p_eriala_choose.append(splited[1])
        sum_length = str(len(p_eriala_choose)*20 + 10)
        ##
        frame2 = Tk()
        frame2.title("Kõrvaerila Kalkulaator v0.1")
        frame2.config(bg = "#F8F8F8")
        frame2.geometry("300x" + sum_length)
        ##
        check_p = []
        n = 0
        while n < len(p_eriala_choose):
            check_p.append("check_p_"+ str(n))
            n+=1
        #print(check_p)
        global var
        var = []
        for j in range(len(p_eriala_choose)):
            var.append(j)
        for n in range(len(p_eriala_choose)):
            var[n] = IntVar()
            check_p[n] = Checkbutton(frame2,text = str(p_eriala_choose[n]),variable = var[n],offvalue = 0, onvalue = 1, command = users_subjects)
            check_p[n].config(bg = "#F8F8F8")
            check_p[n].place(x = 5, y = (5+n*20))
        ##
## FONTS
p_k_font = font.Font(size = 15, weight = "bold")
b_i_font = font.Font(weight = "bold", size = 10)
## Peaeriala LABEL + COMBOBOX
p_label = Label(frame, text = "Peaeriala", font = p_k_font, bg = "#F8F8F8")
p_label.place(x = 5, y = 10)

peaeriala = ttk.Combobox(frame)
peaeriala["values"] = ["Arvutitehnika","Bioloogia","Bioloogia","Bioloogia","Bioloogia","Bioloogia","Bioloogia"]
peaeriala.pack()
peaeriala.place(x = 5, y =40 )

peaeriala.bind("<<ComboboxSelected>>", getpeaeriala)
## Kõrvaeriala LABEL + COMBOBOX
k_label = Label(frame, text = "Kõrvaeriala", font = p_k_font, bg = "#F8F8F8")
k_label.place(x = 150, y = 10)

korvaeriala = ttk.Combobox(frame)
korvaeriala["values"] = ["Arvutitehnika","Bioloogia","Bioloogia","Bioloogia","Bioloogia","Bioloogia","Bioloogia"]
korvaeriala.pack()
korvaeriala.place(x = 150, y = 40)

korvaeriala.bind("<<ComboboxSelected>>", getkorvaeriala)
## INFO_BUTTON
button_info = Button(frame,text = "?", command = info, bg = "#0099CC", font = b_i_font)
button_info.place(x = 5, y = 70)
## DATE
day_values = []
for d in range(1,32):
    day_values.append(d)    
day = ttk.Combobox(frame, width = 2)
day["values"] = day_values
day.pack()
day.place(x = 53, y = 73)
day.bind("<<ComboboxSelected>>", getday)

month = ttk.Combobox(frame, width = 10)
month["values"] = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"]
month.pack()
month.place(x = 90, y = 73)
month.bind("<<ComboboxSelected>>", getmonth)

year = ttk.Combobox(frame, width = 4)
year["values"] = [2014, 2015, 2016]
year.pack()
year.place(x = 175, y = 73)
year.bind("<<ComboboxSelected>>", getyear)
## NEXT BUTTON
button_next = Button(frame, text = "Edasi", command = step2, bg = "#00CC33", font = b_i_font)
button_next.place(x = 245, y = 70)
