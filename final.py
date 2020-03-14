

from tkinter import *
#import PIL.Image, PIL.ImageTk
top=Tk()
top.geometry("1400x700+0+0")
top.title("HOTEL MANAGEMENT SYSTEM")


filename = PhotoImage(file = "hotel2.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#functions
    
    
def user_login():
    Op=Tk()
    Op.geometry("800x400+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    Top=Frame(Op, width=1400, height=100, bd=16)
    Top.pack(side=TOP)
    CF=Frame(Op, width=700, height=750, bd=16, relief="raise")
    CF.pack()
   
    Top.configure(background="blue")
    CF.configure(background="red")
    TopInfo =Label(Top,font=("Arial Rounded MT Bold",35,'bold'),text= "USER LOGIN ",bd="10")
    TopInfo.grid(row = 0,column = 0)
    global textusername
    global textuserpassword
    lb1username=Label(CF,font=("arial",12,"bold"),text=" USERNAME",width=20,fg="black",bd="8")
    lb1username.grid(row=0, column=0)
    textusername=Entry(CF,font=("arial",12,"bold"),bd="10",width="50",bg="white")
    textusername.grid(row=0, column=1)
    lb1userpassword=Label(CF,font=("arial",12,"bold"),text=" PASSWORD",width=20,fg="black",bd="8")
    lb1userpassword.grid(row=2, column=0)
    textuserpassword=Entry(CF,font=("arial",12,"bold"),bd="10",width="50",bg="white")
    textuserpassword.grid(row=2,column=1)
    b1=Button(CF, font=("arial",14,"bold"), text="Submit", width=30,fg="red", command=User_Details)
    b1.grid(row=4, column=1)
  

def Confirm_login():
    Op=Tk()
    Op.geometry("800x100+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    TopInfo =Label(Op,font=("Arial Rounded MT Bold",20,'bold'),text= " SUCCESSFULLY LOGGED IN ",bd="10")
    TopInfo.grid(row = 0,column = 4)
    
def User_Details():
    import sqlite3
    conn=sqlite3.connect('hotel.db')
    c=conn.cursor()
    a=textusername.get()
    b=textuserpassword.get()

    c.execute("INSERT INTO Udetails(username, password) VALUES(?,?)",(a,b))
    conn.commit()
    conn.close()
    Confirm_login()
"""def Admin_login():
    Op=Tk()
    Op.geometry("800x400+0+0")
    Op.title("WELCOME ADMIN")
    Top=Frame(Op, width=1400, height=100, bd=16)
    Top.pack(side=TOP)
    CF=Frame(Op, width=700, height=750, bd=16, relief="raise")
    CF.pack()
    Top.configure(background="blue")
    CF.configure(background="red")
    TopInfo =Label(Top,font=("Arial Rounded MT Bold",35,'bold'),text= "ADMIN LOGIN ",bd="10")
    TopInfo.grid(row = 0,column = 0)
    global textadminid
    global textadminname
    global textadminpassword
    lb1adminid=Label(CF,font=("arial",12,"bold"),text=" ADMIN ID",width=20,fg="black",bd="8")
    lb1adminid.grid(row=0, column=0)
    textadminid=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textadminid.grid(row=0, column=1)
    lb1adminname=Label(CF,font=("arial",12,"bold"),text=" Admin name",width=20,fg="black",bd="8")
    lb1adminname.grid(row=1, column=0)
    textadminname=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textadminname.grid(row=1,column=1)
    lb1adminpassword=Label(CF,font=("arial",12,"bold"),text=" PASSWORD",width=20,fg="black",bd="8")
    lb1adminpassword.grid(row=2, column=0)
    textadminpassword=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textadminpassword.grid(row=2,column=1)
    b1=Button(CF, font=("arial",14,"bold"), text="Submit", width=20,fg="red", command=Admin_Details)
    b1.grid(row=4, column=1)
    b1=Button(CF, font=("arial",14,"bold"), text="CONFIRM LOGIN", width=20,fg="red", command= Confirm_login)
    b1.grid(row=5, column=1)

def Confirm_login():
    Op=Tk()
    Op.geometry("800x100+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    TopInfo =Label(Op,font=("Arial Rounded MT Bold",20,'bold'),text= " SUCCESSFULLY LOGGED IN ",bd="10")
    TopInfo.grid(row = 0,column = 4)
def Admin_Details():
    import sqlite3
    conn=sqlite3.connect('hotel.db')
    c=conn.cursor()
    f=textadminid.get()  
    g=textadminname.get()
    h=textadminpassword.get()

    c.execute("INSERT INTO Adetails(adminid,name,password) VALUES(?,?,?)",(f,g,h))
    conn.commit()
    conn.close()"""

def Register():
    Op=Tk()
    Op.geometry("900x800+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    Top=Frame(Op, width=1400, height=100, bd=16)
    Top.pack(side=TOP)
    CF=Frame(Op, width=700, height=750, bd=16, relief="raise")
    CF.pack()
    Top.configure(background="blue")
    CF.configure(background="red")
    TopInfo =Label(Top,font=("Arial Rounded MT Bold",35,'bold'),text= " NEW USER CAN REGISTER HERE ",bd="10")
    TopInfo.grid(row = 0,column = 0)
    global textfirstname
    global textlastname
    global textpassword
    global textgmail
    global textaddress
    global textphoneno
    lb1firstname=Label(CF,font=("arial",12,"bold"),text=" FIRST NAME",width=20,fg="black",bd="8")
    lb1firstname.grid(row=0, column=0)
    textfirstname=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textfirstname.grid(row=0, column=1)
    lb1lastname=Label(CF,font=("arial",12,"bold"),text=" LASTNAME",width=20,fg="black",bd="8")
    lb1lastname.grid(row=1, column=0)
    textlastname=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textlastname.grid(row=1,column=1)
    lb1password=Label(CF,font=("arial",12,"bold"),text=" PASSWORD",width=20,fg="black",bd="8")
    lb1password.grid(row=2, column=0)
    textpassword=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textpassword.grid(row=2,column=1)
    lb1gmail=Label(CF,font=("arial",12,"bold"),text=" GMAIL",width=20,fg="black",bd="8")
    lb1gmail.grid(row=3, column=0)
    textgmail=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textgmail.grid(row=3,column=1)
    lb1address=Label(CF,font=("arial",12,"bold"),text=" ADDRESS",width=20,fg="black",bd="8")
    lb1address.grid(row=4, column=0)
    textaddress=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textaddress.grid(row=4,column=1)
    lb1phoneno=Label(CF,font=("arial",12,"bold"),text="PHONENO",width=20,fg="black",bd="8")
    lb1phoneno.grid(row=5, column=0)
    textphoneno=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textphoneno.grid(row=5,column=1)
    b1=Button(CF, font=("arial",14,"bold"), text="Submit", width=20,fg="red", command=Register_Details)
    b1.grid(row=6, column=1)
    
def Confirm_registration():
    Op=Tk()
    Op.geometry("800x100+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    TopInfo =Label(Op,font=("Arial Rounded MT Bold",20,'bold'),text= " SUCCESSFULLY REGISTERED ",bd="10")
    TopInfo.grid(row = 0,column = 4)
    
def Register_Details():
    import sqlite3
    conn=sqlite3.connect('hotel.db')
    c=conn.cursor()
    n=textfirstname.get()
    m=textlastname.get()
    p=textpassword.get()
    o=textgmail.get()
    q=textaddress.get()
    r=textphoneno.get()
    c.execute("INSERT INTO Rdetails(firstname,lastname,password,gmail,address,phoneno) VALUES(?,?,?,?,?,?)",(n,m,p,o,q,r))
    conn.commit()
    conn.close()
    Confirm_registration()
def Feedback():
    Op=Tk()
    Op.geometry("900x400+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    Top=Frame(Op, width=1400, height=100, bd=16)
    Top.pack(side=TOP)
    CF=Frame(Op, width=700, height=750, bd=16, relief="raise")
    CF.pack()
    Top.configure(background="blue")
    CF.configure(background="red")
    TopInfo =Label(Top,font=("Kristen ITC",35,'bold'),text= " FEEDBACK ",bd="10")
    TopInfo.grid(row = 0,column = 0)
    global textname
    global textgmail
    global textfeedback
    lb1name=Label(CF,font=("arial",12,"bold"),text=" user name",width=20,fg="black",bd="8")
    lb1name.grid(row=0, column=0)
    textname=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textname.grid(row=0, column=1)
    lb1gmail=Label(CF,font=("arial",12,"bold"),text=" gmail",width=20,fg="black",bd="8")
    lb1gmail.grid(row=1, column=0)
    textgmail=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textgmail.grid(row=1,column=1)
    lb1feedback=Label(CF,font=("arial",12,"bold"),text=" feedback",width=20,fg="black",bd="8")
    lb1feedback.grid(row=2, column=0)
    textfeedback=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textfeedback.grid(row=2,column=1)
    b1=Button(CF, font=("arial",14,"bold"), text="Submit", width=20,fg="red", command=feedback_Details)
    b1.grid(row=4, column=1)
   
def Confirm_feedback():
    Op=Tk()
    Op.geometry("800x100+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    TopInfo =Label(Op,font=("Arial Rounded MT Bold",20,'bold'),text= " THANK YOU FOR GIVING YOUR FEEDBACK :) ",bd="10")
    TopInfo.grid(row = 0,column = 4)

def feedback_Details():
    import sqlite3
    conn=sqlite3.connect('hotel.db')
    c=conn.cursor()
    a=textname.get()  
    o=textgmail.get()
    z=textfeedback.get()

    c.execute("INSERT INTO Fdetails(username,gmail,feedback) VALUES(?,?,?)",(a,o,z))
    conn.commit()
    conn.close()
    Confirm_feedback()

def Room_booking():
    Op=Tk()
    Op.geometry("900x500+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    Top=Frame(Op, width=1400, height=100, bd=16)
    Top.pack(side=TOP)
    CF=Frame(Op, width=700, height=750, bd=16, relief="raise")
    CF.pack()
    Top.configure(background="blue")
    CF.configure(background="red")
    TopInfo =Label(Top,font=("Arial Rounded MT Bold",35,'bold'),text= " ENTER THE REQUIRED DETAILS ",bd="10")
    TopInfo.grid(row = 0,column = 0)
    global textusername
    global textaddress
    global textphoneno
    global textroomtype
    global textnoofbeds
    global textstartingdate
    global texttotaldays
    lb1username=Label(CF,font=("arial",12,"bold"),text=" NAME",width=20,fg="black",bd="8")
    lb1username.grid(row=0, column=0)
    textusername=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textusername.grid(row=0, column=1)
    lb1address=Label(CF,font=("arial",12,"bold"),text=" address",width=20,fg="black",bd="8")
    lb1address.grid(row=1, column=0)
    textaddress=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textaddress.grid(row=1,column=1)
    lb1phoneno=Label(CF,font=("arial",12,"bold"),text=" phone number",width=20,fg="black",bd="8")
    lb1phoneno.grid(row=2, column=0)
    textphoneno=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textphoneno.grid(row=2,column=1)
    lb1roomtype=Label(CF,font=("arial",12,"bold"),text=" room type-ac/non ac",width=20,fg="black",bd="8")
    lb1roomtype.grid(row=3, column=0)
    textroomtype=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textroomtype.grid(row=3,column=1)
    lb1noofbeds=Label(CF,font=("arial",12,"bold"),text=" no of beds",width=20,fg="black",bd="8")
    lb1noofbeds.grid(row=4, column=0)
    textnoofbeds=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textnoofbeds.grid(row=4,column=1)
    lb1startingdate=Label(CF,font=("arial",12,"bold"),text=" starting date",width=20,fg="black",bd="8")
    lb1startingdate.grid(row=5, column=0)
    textstartingdate=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textstartingdate.grid(row=5,column=1)
    lb1totaldays=Label(CF,font=("arial",12,"bold"),text=" total no of days",width=20,fg="black",bd="8")
    lb1totaldays.grid(row=6, column=0)
    texttotaldays=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    texttotaldays.grid(row=6,column=1)
    
    b1=Button(CF, font=("arial",14,"bold"), text="Submit", width=20,fg="red", command=Room_Details)
    b1.grid(row=8, column=1)
    

def Confirm_room():
    Op=Tk()
    Op.geometry("800x100+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    TopInfo =Label(Op,font=("Arial Rounded MT Bold",20,'bold'),text= " ROOM BOOKED SUCCUESSFULLY :) ",bd="10")
    TopInfo.grid(row = 0,column = 4)   
def Room_Details():
    import sqlite3
    conn=sqlite3.connect('hotel.db')
    c=conn.cursor()
    a=textusername.get()
    q=textaddress.get()
    r=textphoneno.get()
    x=textroomtype.get()
    y=textnoofbeds.get()
    u=textstartingdate.get()
    v=texttotaldays.get()
    c.execute("INSERT INTO Roomdetails(username,address,phoneno,roomtype,noofbeds,startingdate,totaldays) VALUES(?,?,?,?,?,?,?)",(a,q,r,x,y,u,v))
    conn.commit()
    conn.close()
    Confirm_room()
def Cab_booking():
    Op=Tk()
    Op.geometry("900x500+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    Top=Frame(Op, width=1400, height=100, bd=16)
    Top.pack(side=TOP)
    CF=Frame(Op, width=700, height=750, bd=16, relief="raise")
    CF.pack()
    Top.configure(background="blue")
    CF.configure(background="red")
    TopInfo =Label(Top,font=("Arial Rounded MT Bold",35,'bold'),text= " BOOK YOUR CAB ",bd="10")
    TopInfo.grid(row = 0,column = 0)
    global textpickuplocation
    global textdestination
    global textdate
    global texttime
    global textcabtype
    global textnoofpersons
    global textcontactnumber
    lb1pickuplocation=Label(CF,font=("arial",12,"bold"),text=" PICKUP LOCATION",width=20,fg="black",bd="8")
    lb1pickuplocation.grid(row=0, column=0)
    textpickuplocation=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textpickuplocation.grid(row=0, column=1)
    lb1destination=Label(CF,font=("arial",12,"bold"),text=" DESTINATION ADDRESS",width=20,fg="black",bd="8")
    lb1destination.grid(row=1, column=0)
    textdestination=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textdestination.grid(row=1,column=1)
    lb1date=Label(CF,font=("arial",12,"bold"),text=" DATE",width=20,fg="black",bd="8")
    lb1date.grid(row=2, column=0)
    textdate=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textdate.grid(row=2,column=1)
    lb1time=Label(CF,font=("arial",12,"bold"),text=" TIME",width=20,fg="black",bd="8")
    lb1time.grid(row=3, column=0)
    texttime=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    texttime.grid(row=3,column=1)
    lb1cabtype=Label(CF,font=("arial",12,"bold"),text=" CABTYPE",width=20,fg="black",bd="8")
    lb1cabtype.grid(row=4, column=0)
    textcabtype=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textcabtype.grid(row=4,column=1)
    lb1noofpersons=Label(CF,font=("arial",12,"bold"),text=" NO OF PERSONS",width=20,fg="black",bd="8")
    lb1noofpersons.grid(row=5, column=0)
    textnoofpersons=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textnoofpersons.grid(row=5,column=1)
    lb1contactnumber=Label(CF,font=("arial",12,"bold"),text=" CONTACT NUMBER",width=20,fg="black",bd="8")
    lb1contactnumber.grid(row=6, column=0)
    textcontactnumber=Entry(CF,font=("arial",12,"bold"),bd="8",width="50",bg="white")
    textcontactnumber.grid(row=6,column=1)
    
    b1=Button(CF, font=("arial",14,"bold"), text="Submit", width=20,fg="red", command=Cab_Details)
    b1.grid(row=8, column=1)
    
def Confirm_cab():
    Op=Tk()
    Op.geometry("850x100+0+0")
    Op.title("HOTEL MANAGEMENT SYSTEM")
    TopInfo =Label(Op,font=("Kristen ITC",20,'bold'),text= " DONT WORRY YOUR CAB IS COMING WITHIN 15 MIN :) ",bd="10")
    TopInfo.grid(row = 0,column = 4)   
def Cab_Details():
    import sqlite3
    conn=sqlite3.connect('hotel.db')
    c=conn.cursor()
    a=textpickuplocation.get()
    q=textdestination.get()
    r=textdate.get()
    x=texttime.get()
    y=textcabtype.get()
    u=textnoofpersons.get()
    v=textcontactnumber.get()
    c.execute("INSERT INTO cabdetails(pickuplocation,destination,date,time,cabtype,noofpersons,contactnumber ) VALUES(?,?,?,?,?,?,?)",(a,q,r,x,y,u,v))
    conn.commit()
    conn.close()
    Confirm_cab()
#frames
Tops=Frame(top, width=1300, height=100, bd=16, relief="raise")
Tops.pack(side=TOP)








TopsInfo =Label(Tops,font=("Kristen ITC",50,'bold'),text= "HOTEL MANAGEMENT SYSTEM",bd="8")
TopsInfo.grid(row = 0,column = 0)
LB1=Button(top, font=("Kristen ITC",15,"bold"), text="REGISTER ->", width=12, height=2,bg="yellow",command=Register)
LB1.place(x=360,y=200)
LB2=Button(top, font=("Kristen ITC",16,"bold"), text="ROOM BOOKING", width=15, height=2,bg="green" ,command=Room_booking)
LB2.place(x=530,y=430)
LB3=Button(top, font=("Kristen ITC",15,"bold"), text="USER LOGIN", width=12, height=2,bg="grey" ,command=user_login)
LB3.place(x=555,y=200)
LB4=Button(top, font=("Kristen ITC",16,"bold"), text="CAB BOOKING", width=15, height=2,bg="green",command=Cab_booking)
LB4.place(x=530,y=330)
LB5=Button(top, font=("Kristen ITC",15,"bold"), text="FEEDBACK", width=13, height=2,bg="yellow" ,command=Feedback)
LB5.place(x=750,y=200)
"""LB5=Button(top, font=("Kristen ITC",15,"bold"), text="ADMIN LOGIN", width=12, height=2,bg="grey" ,command=Admin_login)
LB5.place(x=700,y=200)"""

top.mainloop()
