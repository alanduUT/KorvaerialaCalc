from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from copy import deepcopy
from os import listdir
## FRAME
frame = Tk()
frame.title("Kõrvaerila Kalkulaator v0.1")
frame.config(bg = "#F8F8F8")
frame.geometry("300x105")
## FUNCTIONS
def step2_hash(list_peaeriala,korvaeriala_module):
    values_true_hash = set()
    for v_t in range(len(list_peaeriala)):
        if list_peaeriala[v_t] == 1:
            var_2 = (p_eriala_choose[v_t])
            values_true_hash.add(var_2)
    k_eriala_hash = set()
    ## IT IS NOT DONE, MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS
    if (len(k_peaeriala_choose) != len(k_eriala_choose)) and len(k_peaeriala_choose) != 1:
        file_2 = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\" + str(k_eriala.lower()) + "\\" + "suunamoodul\\" + str(korvaeriala_module), encoding = "UTF-8")
        file_3 = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\" + str(k_eriala.lower()) + "\\" + "erialamoodul\\" + str(k_peaeriala_module.lower()),encoding = "UTF-8")
        files_2 = file_2.readlines()
        files_3 = file_3.readlines()
        files_2[0] = files_2[0].replace("\ufeff", "")
        files_3[0] = files_3[0].replace("\ufeff", "")
        for f_2 in files_2:
            splited_2 = f_2.split(";")
            var_2 = (splited_2[1])
            k_eriala_hash.add(var_2)
        for f_3 in files_3:
            splited_3 = f_3.split(";")
            var_3 = (splited_3[1])
            k_eriala_hash.add(var_3)
    else:
        file_2 = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\" + str(k_eriala.lower()) + "\\" + "suunamoodul\\" + str(korvaeriala_module), encoding = "UTF-8")
        file_3 = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\" + str(k_eriala.lower()) + "\\" + "erialamoodul\\" + str(k_eriala.lower()) + ".txt",encoding = "UTF-8")
        files_2 = file_2.readlines()
        files_3 = file_3.readlines()
        files_2[0] = files_2[0].replace("\ufeff", "")
        files_3[0] = files_3[0].replace("\ufeff", "")
        for f_2 in files_2:
            splited_2 = f_2.split(";")
            var_2 = (splited_2[1])
            k_eriala_hash.add(var_2)
        for f_3 in files_3:
            splited_3 = f_3.split(";")
            var_3 = (splited_3[1])
            k_eriala_hash.add(var_3)
    result_hash = k_eriala_hash - values_true_hash
    return print(result_hash)
## STEP 3
def step3():
    ## CONDITIONS TO PASS STEP 2
    while True:
        try:
            if values_true.count(1) != 0:
                break
        except:
            messagebox.showinfo(message="Teie peaeriala ainede nimekiri on tühi")
            frame2.mainloop()
    while True:
        try:
            if len(k_eriala_module) != 1:
                break
        except:
            messagebox.showinfo(message="Valige kõrvaeriala, kui must punkt on olemas siis vajutage  must punkti UUESTI!")
            frame2.mainloop()
    ## FRAME 3
    frame2.destroy()
    global frame3
    frame3 = Tk()
    frame3.title("Kõrvaerila Kalkulaator v0.1")
    frame3.config(bg = "#F8F8F8")
    frame3.geometry("1100x700")
    step2_hash(values_true, k_eriala_module)
    ##
    return print("Hey")
def year_semester(day,month,year):
    global date
    if month.lower() == "jaanuar": 
        month = 1

    elif month.lower() == "veebruar": 
        month = 2

    elif month.lower() == "märts": 
        month = 3

    elif month.lower() == "aprill": 
        month = 4

    elif month.lower() == "mai": 
        month = 5

    elif month.lower() == "juuni": 
        month = 6

    elif month.lower() == "juuli": 
        month = 7

    elif month.lower() == "august": 
        month = 8

    elif month.lower() == "september": 
        month = 9
        
    elif month.lower() == "oktoober": 
        month = 10
        
    elif month.lower() == "november": 
        month = 11
              
    elif month.lower() == "detsember": 
        month = 12
        
    if month == 1 or (month == 2 and int(day) < 9):
        date = []
        date.append(str(int(year)-1)[2:5]+"/"+str(year)[2:5])
        date.append("K")
        return date
    
    elif month == 2 and int(day) >= 9:
        date = []
        date.append(str(year)[2:5] +"/"+str(int(year)+1)[2:5])
        date.append("S")
        return date
    
    elif month > 2 and month < 9 or (month == 9 and int(day) < 16):
        date = []
        date.append(str(year)[2:5] +"/"+str(int(year)+1)[2:5])
        date.append("S")
        return date

    elif month == 9 and int(day) >= 16:
        date = []
        date.append(str(year)[2:5] +"/"+str(int(year)+1)[2:5])
        date.append("K")
        return date
    
def chosen_module():
    if (len(k_peaeriala_choose) != len(k_eriala_choose)) and len(k_peaeriala_choose) != 1:
        global k_peaeriala_module
        k_peaeriala_module = string_2.get()
        global k_eriala_module
        k_eriala_module = string.get()
        return (k_eriala_module, k_peaeriala_module)
    else:
        k_eriala_module = string.get()
        return k_eriala_module 
def users_subjects():
    global values_true
    values = []
    for j in range(len(p_eriala_choose)):
        values.append(j)
    n = 0
    while n <= len(p_eriala_choose)-1:
        values[n] = var[n].get()
        n += 1
    values_true = deepcopy(values)
    return values_true
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
    ## CONDITION TO PASS
    Z = 1
    key_1 = 0
    while Z <= 5:
        try:
            Z_1 = p_eriala
            Z_2 = k_eriala
            Z_3 = d_ay
            Z_4 = m_onth
            Z_5 = y_ear
            if Z_1 == Z_2:
                messagebox.showinfo(message="Kõrvaeriala ja peaeriala peavad olema erinevad!")
                break
        except:
            messagebox.showinfo(message="Kõik peab olema täidetud")
            break
        Z += 1
        if Z == 6:
            key_1 = 1
    if key_1 == 0:
        frame.mainloop()
    else:
        frame.destroy()
        ## DEFINE EVERY MODULE FROM KORVAERIALA
        global k_eriala_choose
        k_eriala_choose = []
        path = str(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\") + str(k_eriala.lower()) + "\suunamoodul"
        k_file = listdir(path)
        for k in k_file:
            k_eriala_choose.append(str(k))
        ## DEFINE EVERY SUBJECTED CONNECTED WITH PEAERIALA
        global p_eriala_choose
        p_eriala_choose = []
        p_file = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\peaeriala\\" + str(p_eriala.lower()) + ".txt", encoding = "UTF-8")
        p_files = p_file.readlines()
        p_files[0] = p_files[0].replace("\ufeff", "")
        for p in p_files:
            splited = p.split(";")
            p_eriala_choose.append(splited[1])
        sum_length = str(45*20 + 10)
        ## CONSTRUCT FRAME2 WITH GIVEN VARIABLES
        global frame2
        frame2 = Tk()
        frame2.title("Kõrvaerila Kalkulaator v0.1")
        frame2.config(bg = "#F8F8F8")
        frame2.geometry("1100x" + sum_length)
        ## CHECKBOX NAME CONSTRUCTOR
        check_p = []
        n = 0
        while n < len(p_eriala_choose):
            check_p.append("check_p_"+ str(n))
            n+=1
        ## CHECKBOX CONTROLLER
        global var
        var = []
        for j in range(len(p_eriala_choose)):
            var.append(j)
        for n in range(len(p_eriala_choose)):
            var[n] = IntVar()
            if n >= 45:
                check_p[n] = Checkbutton(frame2,text = str(p_eriala_choose[n]),variable = var[n],offvalue = 0, onvalue = 1, command = users_subjects)
                check_p[n].config(bg = "#F8F8F8")
                check_p[n].place(x = 400, y = (5+(n-45)*20))
            else:  
                check_p[n] = Checkbutton(frame2,text = str(p_eriala_choose[n]),variable = var[n],offvalue = 0, onvalue = 1, command = users_subjects)
                check_p[n].config(bg = "#F8F8F8")
                check_p[n].place(x = 5, y = (5+n*20))
        ##  RADIOBUTTON FOR KORVAERIALA  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS  MORE CONDITIONS 
        k_choose_label = Label(frame2, text = ("Valige " + str(k_eriala).upper() +" suunamoodul"), font = k_choose_font, bg = "#F8F8F8")
        k_choose_label.place( x = 700, y = (int(sum_length)/2-40))
        global string
        string = StringVar()
        for k in range(len(k_eriala_choose)):
            k_eriala_choose[k] = Radiobutton(frame2, text = str(k_eriala_choose[k][:len(k_eriala_choose[k])-4]).capitalize()+" suunamoodul", variable = string, value = k_eriala_choose[k], command = chosen_module)
            k_eriala_choose[k].config(bg = "#F8F8F8")
            k_eriala_choose[k].place(x = 700, y = (int(sum_length)/2+k*20))
        print(year_semester(d_ay,m_onth,y_ear))
        ## CONDITION FOR KORVAERIALA ERIALA MOODUL
        global k_peaeriala_choose
        k_eriala_path = (r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\" + str(k_eriala.lower())+"\\" +"erialamoodul\\")
        k_peaeriala_choose = listdir(k_eriala_path)
        if (len(k_peaeriala_choose) != len(k_eriala_choose)) and len(k_peaeriala_choose) != 1:
            k_peaeriala_choose_label = Label(frame2, text = ("Valige" + str(k_eriala).upper() + " erialamoodul"), font = k_choose_font, bg = "#F8F8F8")
            k_peaeriala_choose_label.place(x = 700, y = (int(sum_length)/2 + (k+3)*20))
            global string_2
            string_2 = StringVar()
            for k_p in range(len(k_peaeriala_choose)):
                print(k_peaeriala_choose[k_p])
                k_peaeriala_choose[k_p] = Radiobutton(frame2, text = (str(k_peaeriala_choose[k_p][:len(k_peaeriala_choose[k_p])-4]).capitalize() + " erialamoodul"), variable = string_2, value = k_peaeriala_choose[k_p], command = chosen_module)
                k_peaeriala_choose[k_p].config(bg = "#F8F8F8")
                k_peaeriala_choose[k_p].place(x = 700, y = (int(sum_length)/2 + (k+5)*20 + 20*k_p))
        ## BUTTON STEP 3
        button_step_3 = Button(frame2, text = "Edasi", bg = "#00CC33", font = b_i_font, command = step3)
        button_step_3.place(x = 750, y = (int(sum_length)/2+k*20 +180))
## FONTS
global b_i_font
p_k_font = font.Font(size = 15, weight = "bold")
b_i_font = font.Font(weight = "bold", size = 10)
global k_choose_font
k_choose_font = font.Font(weight = "bold", size = 20)
## Peaeriala LABEL + COMBOBOX
p_label = Label(frame, text = "Peaeriala", font = p_k_font, bg = "#F8F8F8")
p_label.place(x = 5, y = 10)

peaeriala = ttk.Combobox(frame)
peaeriala["values"] = ["Arvutitehnika","Bioloogia","Haridusteadus","Keemia","Keskkonnatehnoloogia","Materjaliteadus","Ökoloogia","Geograafia","Füüsika","Geoloogia"]
peaeriala.pack()
peaeriala.place(x = 5, y =40 )

peaeriala.bind("<<ComboboxSelected>>", getpeaeriala)
## Kõrvaeriala LABEL + COMBOBOX
k_label = Label(frame, text = "Kõrvaeriala", font = p_k_font, bg = "#F8F8F8")
k_label.place(x = 150, y = 10)

korvaeriala = ttk.Combobox(frame)
korvaeriala["values"] = ["Arvutitehnika","Bioloogia","Keemia","Materjaliteadus","Ökoloogia","Geograafia","Bioloogia"]
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
##
