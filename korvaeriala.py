from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from copy import deepcopy
from os import listdir
from urllib.request import urlopen
## FRAME
frame = Tk()
frame.title("Kõrvaerila Kalkulaator v0.1")
frame.config(bg = "#F8F8F8")
frame.geometry("300x105")
## FUNCTIONS
def lõpp():
    if nickname.get() != "":
        nick = nickname.get()
        frame4.destroy()
    else:
        return messagebox.showinfo(message="Sisestage USER")
    #print(date)
    #print(final_hash)
    #print(_best_list)
    #subject_code_finder(_best_list)
    #print(yeark)
    finish = open("C:\\Users\\" + str(nick) + "\\" + "Desktop\\" + str(p_eriala.lower()) + str(k_eriala.lower()) + ".txt", "w")
    finish.write("Praegu Te olete: " + str(date)+"\n")
    for y_s in subject_code_finder(_best_list):
        if len(y_s) != 0:
            for y in y_s:
                finish.write(str(y) + "\n")
    print("done")
    finish.close()
def step4():
    global _best_list
    #print(result_hash)
    global final_hash
    med_hash = set({})
    while True:
        try:
            if 1 in valikained_true:
                for one in range(len(valikained_true)):
                    if valikained_true[one] == 1:
                        one_ = (best_list[one])
                        med_hash.add(one_)
                #print(result_hash)
                #print(final_hash)
                        
                final_hash = result_hash - med_hash
                break
            else:
                final_hash = result_hash
                break
        except:
            final_hash = result_hash
            break
    _best_list = deepcopy(best_list)
    for b in best_list:
        if not (b in final_hash):
            _best_list.remove(b)
    global date
    year_semester(d_ay,m_onth,y_ear)
    global frame4
    global nickname
    frame3.destroy()
    frame4 = Tk()
    frame4.title("Kõrvaerila Kalkulaator v0.1")
    frame4.config(bg = "#F8F8F8")
    frame4.geometry("150x120")
    nickname_label = Label(frame4, text = "Sisestage USER")
    nickname_label.config(bg = "#F8F8F8")
    nickname_label.place(x = 25, y = 5)
    nickname = Entry(frame4)
    nickname.place(x= 5, y = 30, width = 140, height = 20)
    finish_button = Button(frame4, text = "Lõpp", command = lõpp, bg = "#00CC33", font = b_i_font)
    finish_button.place(x = 40, y = 70)

    
            
def step2_hash(list_peaeriala,korvaeriala_module):
    peaeriala_eap = 0
    values_true_hash = set()
    for v_t in range(len(list_peaeriala)):
        if list_peaeriala[v_t] == 1:
            var_2 = (p_eriala_choose[v_t])
            values_true_hash.add(var_2)
    path_peaeriala_point = str(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\peaeriala\\" + str(p_eriala.lower()) +".txt")
    peaeriala_open = open(path_peaeriala_point, encoding = "UTF-8")
    p_op = peaeriala_open.readlines()
    p_op[0] = p_op[0].replace("\ufeff","")
    for l_pe in range(len(list_peaeriala)):
        if list_peaeriala[l_pe] == 1:
            peaeriala_eap += int(p_op[l_pe].split(";")[2].strip())
    global yeark
    if peaeriala_eap <= 60:
        yeark = 1
    elif peaeriala_eap > 60 and peaeriala_eap <= 120:
        yeark = 2
    else:
        yeark = 3
        
            
        
    global k_super_list
    k_super_list = list()
    k_korvaeriala_hash_list = list()
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
            k_korvaeriala_hash_list.append(var_2)
        for f_3 in files_3:
            splited_3 = f_3.split(";")
            var_3 = (splited_3[1])
            k_eriala_hash.add(var_3)
            k_korvaeriala_hash_list.append(var_3)
    elif len(k_eriala_choose) > 2:
        file_2 = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\" + str(k_eriala.lower()) + "\\" + "suunamoodul\\" + str(korvaeriala_module), encoding = "UTF-8")
        file_3 = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\korvaeriala\\" + str(k_eriala.lower()) + "\\" + "erialamoodul\\" + str(korvaeriala_module.lower()),encoding = "UTF-8")
        files_2 = file_2.readlines()
        files_3 = file_3.readlines()
        files_2[0] = files_2[0].replace("\ufeff", "")
        files_3[0] = files_3[0].replace("\ufeff", "")
        for f_2 in files_2:
            splited_2 = f_2.split(";")
            var_2 = (splited_2[1])
            k_eriala_hash.add(var_2)
            k_korvaeriala_hash_list.append(var_2)
        for f_3 in files_3:
            splited_3 = f_3.split(";")
            var_3 = (splited_3[1])
            k_eriala_hash.add(var_3)
            k_korvaeriala_hash_list.append(var_3)
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
            k_korvaeriala_hash_list.append(var_2)
        for f_3 in files_3:
            splited_3 = f_3.split(";")
            var_3 = (splited_3[1])
            k_eriala_hash.add(var_3)
            k_korvaeriala_hash_list.append(var_3)
    global result_hash
    result_hash = k_eriala_hash - values_true_hash
    for k in k_korvaeriala_hash_list:
        if (k in result_hash):
            k_super_list.append(k)
    global best_list
    best_list = deepcopy(k_super_list)
    return (result_hash, k_super_list)
## STEP 3
def step3():
    ## CONDITIONS TO PASS STEP 2
    while True:
        key_2 = 0
        try:
            if values_true.count(1) != 0:
                key_2 += 1
                break
            else:
                return messagebox.showinfo(message="Teie peaeriala ainede nimekiri on tühi")
        except:
            return messagebox.showinfo(message="Teie peaeriala ainede nimekiri on tühi")
    if (len(k_peaeriala_choose) != len(k_eriala_choose)) and len(k_peaeriala_choose) != 1:
        while True:
            try:
                if len(k_peaeriala_module) != 0 and len(k_eriala_module) != 0:
                    key_2 += 1
                    break
                else:
                    return messagebox.showinfo(message="Valige kõrvaeriala, kui must punkt on olemas siis vajutage  must punkti UUESTI!")
            except:
                return messagebox.showinfo(message="Valige kõrvaeriala, kui must punkt on olemas siis vajutage  must punkti UUESTI!")
                
    else:
        while True:
            try:
                if len(k_eriala_module) != 0:
                    key_2 += 1
                    break
                else:
                    return messagebox.showinfo(message="Valige kõrvaeriala, kui must punkt on olemas siis vajutage  must punkti UUESTI!")
            except:
                return messagebox.showinfo(message="Valige kõrvaeriala, kui must punkt on olemas siis vajutage  must punkti UUESTI!")
    if key_2 == 2:
        frame2.destroy()
    else:
        frame2.mainloop()
    ## FRAME 3 FRAME 3 FRAME 3 FRAME 3 FRAME 3 FRAME 3
    step2_hash(values_true, k_eriala_module)
    global frame3
    global var_valik
    var_valik = []
    for v_va in k_super_list:
        if (v_va in result_hash):
            var_valik.append(k_super_list.index(v_va))
    frame3 = Tk()
    frame3.title("Kõrvaerila Kalkulaator v0.1")
    frame3.config(bg = "#F8F8F8")
    frame3.geometry("200x"+str(20*len(var_valik) + 100))
    for v_val in range(len(var_valik)):
        var_valik[v_val] = IntVar()
        k_super_list[v_val] = Checkbutton(frame3, text = str(k_super_list[v_val]), variable = var_valik[v_val], offvalue = 0, onvalue = 1, command = valikained)
        k_super_list[v_val].config(bg = "#F8F8F8")
        k_super_list[v_val].place(x = 5, y = (5+v_val*20))
    ##STEP 4 BUTTON
    button_step_4 = Button(frame3, text = "Edasi", bg = "#00CC33", font = b_i_font, command = step4)
    button_step_4.place(x = 100, y = (50+v_val*20))
    ##
## FUNCTIONS
def subject_code_finder(best_list):
    global best_list_points
    global best_list_code
    best_list_code = []
    best_list_points = []
    
    if len(best_list) == 0:
        return "Hey"
    codes = open(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\\" + "code.txt",encoding = "UTF-8")
    cod = codes.readlines()
    cod[0] = cod[0].replace("\ufeff","")
    for c in cod:
        splited = c.strip().split(";")
        if splited[0].lower() == str(k_eriala).lower():
            korvaeriala_code = splited[1]

    path_everything = str(r"C:\Users\alandocs\Documents\korvaerialaproject\KorvaerialaCalc\everything\\" + str(k_eriala.lower()) +".txt")
    everything_open = open(path_everything, encoding = "UTF-8")
    p_ev = everything_open.readlines()
    p_ev[0] = p_ev[0].replace("\ufeff","")
    for b_l in best_list:
        for p__ev in p_ev:
            p_splited = p__ev.split(";")
            if b_l == p_splited[1]:
                best_list_code.append(p_splited[0])
                best_list_points.append(p_splited[2])
                break
    
    oppekava_web = urlopen(r"https://www.is.ut.ee/pls/ois/!tere.tulemast?leht=OK.BL.PU&id_a_oppekava=" + korvaeriala_code)
    opp_web = oppekava_web.readlines()
    
    to_be_sorted = []
    sorted_ = []
    index_blist = 0
    while index_blist <= len(best_list_code)-1:
        for ow in range(len(opp_web)):
            ow1 = opp_web[ow].decode()
            if str(best_list_code[index_blist]) in ow1:
                to_be_sorted.append(opp_web[ow+1].decode())
        index_blist += 1
    for ts in to_be_sorted:
        bs = ts.strip(";\n")
        num = ts.find("vorm.id_register.value=")
        if bs[num+len("vorm.id_register.value="):] in sorted_:
            continue
        else:
            sorted_.append(bs[num+len("vorm.id_register.value="):])
    toimumised = []
    for s_ in sorted_:
        ainekava_file = urlopen(r"https://www.is.ut.ee/pls/ois/!tere.tulemast?leht=OA.RE.VA&id_register=" + str(s_))
        ainekava_ = ainekava_file.readlines()
        toimumised += [toimumise_calc(ainekava_)]
    return schedule(toimumised)
## SCHEDULE FUNCTIONS NEEDS YEAR CONTROLLER, ON WHATS YEAR STUDENT IS AT THE MOMENT OF USING APP
def schedule(toimumised):     
    years_schedule = []
    for y in range(3):
        years_schedule += [[]]
    semester_start = 0
    if "K" in date:
        semester_max = 15
    else:
        semester_max = 20
    year = 0
    while year <= 3-yeark:
        semester_start = 0
        while semester_start < semester_max:
            if toimumised.count(0) == len(toimumised):
                break
            for to in range(len(toimumised)):
                
                if semester_start >= semester_max:
                    break
                if toimumised[to] == 0:
                    continue
                if year == 0:
                    if str(date) in toimumised[to]:
                        years_schedule[year] += [str(_best_list[to])+ " - " + str(date) +" - " + str(best_list_points[to].strip()) + "EAP"]
                        toimumised[to] = 0
                        _best_list[to] = 0
                        semester_start += int(best_list_points[to])
                    elif str(str(date[:5]) + " " + "K") in toimumised[to] and (not "K" in date):
                        years_schedule[year] += [str(str(_best_list[to]) + " - " + str(str(date[:5]) + " " + "K") + " - " + str(best_list_points[to].strip()) + "EAP")]
                        toimumised[to] = 0
                        _best_list[to] = 0
                        semester_start += int(best_list_points[to])
                    else:
                        if to == len(toimumised) -1 :
                            semester_start += 12
                        else:
                            continue
                        #toim = str(str(_best_list[to]) + " - " + str(int(date[:2]) + year_)+ "/" + str(int(date[3:5]) + year_) + " " + str(frequency(toimumised[to])) + " - " + str(best_list_points[to].strip()) + "EAP")
                        #years_schedule[year] += [toim]
                        #toimumised[to] = 0
                        #_best_list[to] = 0
                        #semester_start += int(best_list_points[to])
                else:
                    print(to)
                    toim = str(str(_best_list[to]) + " - " + str(int(date[:2]) + year)+ "/" + str(int(date[3:5]) + year) + " " + str(frequency(toimumised[to])) + " - " + str(best_list_points[to].strip()) + "EAP")
                    years_schedule[year] += [toim]
                    toimumised[to] = 0
                    _best_list[to] = 0
                    semester_start += int(best_list_points[to])
        year += 1        
    return years_schedule
                        
def frequency(intoim):
    semester_max = []
    for into in intoim:
        semester_max.append(into[-1])
    _S_ = semester_max.count("S")
    _K_ = semester_max.count("K")
    if _S_ > _K_:
        return "S"
    elif _K_ >= _S_:
        return "K"
    
def toimumise_calc(ainekava):
    toimumised_non_sorted = []
    toimumised_sorted = []
    for ava in ainekava:
        ava1 = ava.decode()
        if "Stats" in ava1:
            toimumised_non_sorted.append(ava1)
    for tns in toimumised_non_sorted:
        index_stats = tns.find("Stats")
        toimumised_sorted.append(tns[index_stats-8:index_stats -1])  
    return toimumised_sorted    
        
def valikained():
    global valikained
    global valikained_true
    valikained = []
    for q in range(len(var_valik)):
        valikained.append(q)
    v_val = 0
    while v_val <= len(var_valik)-1:
        valikained[v_val] = var_valik[v_val].get()
        v_val += 1
    valikained_true = deepcopy(valikained)
    return valikained_true                                       
#_KEY_ = ["date","1/1","4/5","2/6","11/2"]        
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
        #date = []
        date = (str(int(year)-1)[2:5]+"/"+str(year)[2:5] +" " + "K")
        #date.append("K")
        return date
    
    elif month == 2 and int(day) >= 9:
        #date = []
        date = (str(year)[2:5] +"/"+str(int(year)+1)[2:5] + " " + "S")
        #date.append("S")
        return date
    
    elif month > 2 and month < 9 or (month == 9 and int(day) < 16):
        #date = []
        date = (str(year)[2:5] +"/"+str(int(year)+1)[2:5] + " " + "S")
        #date.append("S")
        return date

    elif month == 9 and int(day) >= 16:
        #date = []
        date = (str(year)[2:5] +"/"+str(int(year)+1)[2:5] + " " + "K")
        #date.append("K")
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
        #print(year_semester(d_ay,m_onth,y_ear))
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
                k_peaeriala_choose[k_p] = Radiobutton(frame2, text = (str(k_peaeriala_choose[k_p][:len(k_peaeriala_choose[k_p])-4]).capitalize() + " erialamoodul"), variable = string_2, value = k_peaeriala_choose[k_p], command = chosen_module)
                k_peaeriala_choose[k_p].config(bg = "#F8F8F8")
                k_peaeriala_choose[k_p].place(x = 700, y = (int(sum_length)/2 + (k+5)*20 + 20*k_p))
        ## BUTTON STEP 3
        button_step_3 = Button(frame2, text = "Edasi", bg = "#00CC33", font = b_i_font, command = step3)
        button_step_3.place(x = 750, y = (int(sum_length)/2+k*20 +180))
        ## END OF STEP 2
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
peaeriala["values"] = ["Arvutitehnika","Bioloogia","Füüsika","Geenitehnoloogia","Geograafia","Geoloogia","Haridusteadus","Keemia","Keskkonnatehnoloogia","Materjaliteadus","Ökoloogia","Informaatika","Matemaatika","Matemaatiline statistika"]
peaeriala.pack()
peaeriala.place(x = 5, y =40 )

peaeriala.bind("<<ComboboxSelected>>", getpeaeriala)
## Kõrvaeriala LABEL + COMBOBOX
k_label = Label(frame, text = "Kõrvaeriala", font = p_k_font, bg = "#F8F8F8")
k_label.place(x = 150, y = 10)

korvaeriala = ttk.Combobox(frame)
korvaeriala["values"] = ["Arvutitehnika","Bioloogia","Füüsika","Geenitehnoloogia","Geograafia","Geoloogia","Keemia","Keskkonnatehnoloogia","Materjaliteadus","Ökoloogia","Informaatika","Matemaatika","Matemaatiline statistika"]
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
