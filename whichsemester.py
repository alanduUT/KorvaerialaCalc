def which_semester(d_ay,m_onth,y_ear):
    if m_onth.lower() == "jaanuar": 
        m_onth = 1

    elif m_onth.lower() == "veebruar": 
        m_onth = 2

    elif m_onth.lower() == "märts": 
        m_onth = 3

    elif m_onth.lower() == "aprill": 
        m_onth = 4

    elif m_onth.lower() == "mai": 
        m_onth = 5

    elif m_onth.lower() == "juuni": 
        m_onth = 6

    elif m_onth.lower() == "juuli": 
        m_onth = 7

    elif m_onth.lower() == "august": 
        m_onth = 8

    elif m_onth.lower() == "september": 
        m_onth = 9
        
    elif m_onth.lower() == "oktoober": 
        m_onth = 10
        
    elif m_onth.lower() == "november": 
        m_onth = 11
              
    elif m_onth.lower() == "detsember": 
        m_onth = 12
        
    if m_onth == 1 or (m_onth == 2 and int(d_ay) < 9):
        return str(int(y_ear)-1)+"/"+y_ear + " 2 semester"
    
    elif m_onth == 2 and int(d_ay) >= 9:
        return y_ear +"/"+str(int(y_ear)+1) + " 1 semester"
    
    elif m_onth > 2 and m_onth < 9 or (m_onth == 9 and int(d_ay) < 16):
        return y_ear +"/"+str(int(y_ear)+1) + " 1 semester"

    elif m_onth == 9 and int(d_ay) >= 16:
        return y_ear +"/"+str(int(y_ear)+1) + " 2 semester"

    
#print(which_semester("9/Veebruar/2015"))   
