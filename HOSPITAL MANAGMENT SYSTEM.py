from tkinter import *

from tkinter import ttk

from tkinter import messagebox

import cx_Oracle

def main():

    try:

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur = conn.cursor()

        x = cur.execute('select * from docrec')

    except:

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur0 = conn.cursor()

        y = cur0.execute(

            "create table docrec (docid int , name varchar(20) , age varchar(10) , gender varchar(10) , city varchar(20) , experience varchar(20) , address varchar(100) , mobilenumber varchar(20))")

        cur0.execute(

            "insert into docrec values (0 ,'Vaibhav' ,'16', 'Male' , 'Aligarh' ,'4 yrs' , 'Rambagh' ,'0000000001')")

        cur0.execute("commit")

    try:

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur = conn.cursor()

        x = cur.execute('select * from patrec')

    except:

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur0 = conn.cursor()

        y = cur0.execute(

            "create table patrec (patid int , name varchar(20) ,disease  varchar(20),bgroup  varchar(20),dname  varchar(20), age varchar(10) , gender varchar(10) , city varchar(20) ,weight  varchar(20), height  varchar(20) , address varchar(100) , mobilenumber varchar(20))")

        cur0.execute("commit")

    try:   

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur = conn.cursor()

        x = cur.execute('select * from openadmin')

    except:

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur0 = conn.cursor()

        cur0.execute("create table openadmin(username varchar(20),pass varchar(20))")

        cur0.execute("insert into openadmin values('mukesh',1000)")

        cur0.execute("insert into openadmin values('rohit',1001)")

        cur0.execute("commit")

    try:

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur = conn.cursor()

        x = cur.execute('select * from openuser')

    except:

        conn = cx_Oracle.connect('system/anwar@localhost')

        cur0 = conn.cursor()

        cur0.execute("create table openuser(username varchar(20),pass varchar(20))")

        cur0.execute("insert into openuser values('vaibhav',100)")

        cur0.execute("commit")

    def fa():

        def doct():

            qk.destroy()

            r = Tk()

            r.iconbitmap(r"hms.ico")

            r.title('Hospital Managment System')

            r.geometry('1365x727')

            r.config(bg="#6e6e48")

            DoctorID = IntVar()

            Name = StringVar()

            Experience = StringVar()

            City = StringVar()

            Age = StringVar()

            Gender = StringVar()

            Address = StringVar()

            Mobile = StringVar()

            MainFrame = Frame(r, bg="#6e6e48")

            MainFrame.grid()

            TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)

            TitFrame.pack(side=TOP)

            lbltit = Label(TitFrame, font=('arial', 47, 'bold'), text="Hospital  Management System", bg="Ghost White")

            lbltit.grid()

            ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White",

                                relief=RIDGE)

            ButtonFrame.pack(side=BOTTOM)

            DataFrame = Frame(MainFrame, width=1300, height=400, bd=1, padx=20, pady=20, bg="#6e6e48")

            DataFrame.pack(side=BOTTOM)

            DataFrameLEFT = LabelFrame(DataFrame, width=1000, height=600, bd=1, padx=20, bg="Ghost White", relief=RIDGE,

                                       text="Doctor information\n", font=('arial', 20, 'bold'))

            DataFrameLEFT.pack(side=LEFT)

            DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White",

                                        relief=RIDGE, text="Doctor Details\n", font=('arial', 20, 'bold'))

            DataFrameRIGHT.pack(side=RIGHT)

            lblDoctorID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Doctor ID", bg="Ghost White", padx=2,

                                pady=2)

            lblDoctorID.grid(row=0, column=0, sticky=W)

            txtDoctorID = ttk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoctorID, width=40)

            txtDoctorID.grid(row=0, column=1)

            txtDoctorID.focus()

            lblname = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Name", bg="Ghost White", padx=2, pady=3)

            lblname.grid(row=1, column=0, sticky=W)

            txtname = ttk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Name, width=40)

            txtname.grid(row=1, column=1)

            txtname.focus()

            lblage = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age (yrs)", bg="Ghost White", padx=2, pady=3)

            lblage.grid(row=2, column=0, sticky=W)

            txtage = ttk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=40)

            txtage.grid(row=2, column=1)

            txtage.focus()

            lblgen = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender", bg="Ghost White", padx=2, pady=3)

            lblgen.grid(row=3, column=0, sticky=W)

            txtgen = ttk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=40)

            txtgen.grid(row=3, column=1)

            txtgen.focus()

            lblcity = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="City", bg="Ghost White", padx=2, pady=2)

            lblcity.grid(row=4, column=0, sticky=W)

            txtcity = ttk.Entry(DataFrameLEFT, textvariable=City, font=('arial', 20, 'bold'), width=40)

            txtcity.grid(row=4, column=1)

            txtcity.focus()

            lblexp = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Experience (yrs)", bg="Ghost White", padx=2,

                           pady=2)

            lblexp.grid(row=5, column=0, sticky=W)

            txtexp = ttk.Entry(DataFrameLEFT, textvariable=Experience, font=('arial', 20, 'bold'), width=40)

            txtexp.grid(row=5, column=1)

            txtexp.focus()

            lbladd = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address", bg="Ghost White", padx=2, pady=3)

            lbladd.grid(row=6, column=0, sticky=W)

            txtadd = ttk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=40)

            txtadd.grid(row=6, column=1)

            txtadd.focus()

            lblmob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile-Number", bg="Ghost White", padx=2,

                           pady=3)

            lblmob.grid(row=7, column=0, sticky=W)

            txtmob = ttk.Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=40)

            txtmob.grid(row=7, column=1)

            txtmob.focus()

            def iexit():


                iexit = messagebox.askokcancel("Hospital Managment System", " Do you want to exit ")

                if iexit > 0:

                    r.destroy()

                    fa()

                    return

            def cleardata():

                txtDoctorID.delete(0, END)

                txtname.delete(0, END)

                txtage.delete(0, END)

                txtgen.delete(0, END)

                txtcity.delete(0, END)

                txtexp.delete(0, END)

                txtadd.delete(0, END)

                txtmob.delete(0, END)

            def viewdata():

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                cur.execute("select * from docrec")

                row = cur.fetchall()

                conn.close

                return row

            def ssearchdata(x):

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                cur.execute("select * from docrec where docid = %d  " % x)

                row = cur.fetchall()

                conn.close

                return row

            def adddocrec(txtDoctor, txtname, txtexp, txtcity, txtage, txtgen, txtadd, txtmob):

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                cur.execute("insert into docrec values (%d , '%s' ,'%s' , '%s' , '%s' , '%s' , '%s' , '%s')" % (

                txtDoctor, txtname, txtexp, txtcity, txtage, txtgen, txtadd, txtmob))

                cur.execute("commit")

                conn.close

            def deleterec(docid):

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                cur.execute("delete  from docrec where docid = %d" % docid)

                cur.execute("commit")

                conn.close

            def adddata():

                adddocrec(int(txtDoctorID.get()), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtexp.get(), txtadd.get(), txtmob.get())

                doclist.delete(0, END)

                doclist.insert(END, (

                txtDoctorID.get(), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtexp.get(), txtadd.get(),txtmob.get()))

                messagebox.showinfo('Hospiital Mangement System','New Doctor Added Successfully')

            def displaydata():

                doclist.delete(0, END)

                for row in viewdata():

                    doclist.insert(END, row, str(" "))

            def docrec(event):

                global sd

                searchpat = doclist.curselection()[0]

                sd = doclist.get(searchpat)

                txtDoctorID.delete(0, END)

                txtDoctorID.insert(END, sd[0])

                txtname.delete(0, END)

                txtname.insert(END, sd[1])

                txtage.delete(0, END)

                txtage.insert(END, sd[2])

                txtgen.delete(0, END)

                txtgen.insert(END, sd[3])

                txtcity.delete(0, END)

                txtcity.insert(END, sd[4])

                txtexp.delete(0, END)

                txtexp.insert(END, sd[5])

                txtadd.delete(0, END)

                txtadd.insert(END, sd[6])

                txtmob.delete(0, END)

                txtmob.insert(END, sd[7])

            def deletedata():

                searchpat = doclist.curselection()[0]

                sd = doclist.get(searchpat)

                deleterec(sd[0])

                cleardata()

                displaydata()

                messagebox.showinfo('Hospiital Mangement System', ' Doctor Deleted Successfully')

            def searchdata():

                doclist.delete(0, END)

                for row in ssearchdata(int(txtDoctorID.get())):

                    cleardata()


                    doclist.insert(END, row, str(""))

                    x=row[1]

                    x0=row[2]

                    x1=row[5]

                    x3=row[4]

                    x4=row[3]

                    x5=row[6]

                    x6=row[7]

                    x00=row[0]

                    txtDoctorID.insert(0,x00)

                    txtmob.insert(0,x6)

                    txtadd.insert(0,x5)

                    txtgen.insert(0,x4)

                    txtcity.insert(0,x3)

                    txtexp.insert(0,x1)

                    txtage.insert(0,x0)

                    txtname.insert(0,x)

            def update():

                searchpat = doclist.curselection()[0]

                sd = doclist.get(searchpat)

                doclist.delete(0, END)

                deleterec(sd[0])

                adddocrec(int(txtDoctorID.get()), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtexp.get(), txtadd.get(), txtmob.get())

                doclist.delete(0, END)

                doclist.insert(END, (int(txtDoctorID.get()), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtexp.get(), txtadd.get(), txtmob.get()))

                messagebox.showinfo('Hospiital Mangement System', 'New Information Updated Successfully')

            scroll = Scrollbar(DataFrameRIGHT)

            scroll.grid(row=0, column=1, sticky='NS'),

            doclist = Listbox(DataFrameRIGHT, width=41, height=16, font=("arial", 12, "bold"),

                              yscrollcommand=scroll.set)

            doclist.bind('<<ListboxSelect>>',docrec)

            doclist.grid(row=0, column=0, padx=8)

            scroll.config(command=doclist.yview)

            btn1 = Button(ButtonFrame, text="Add New", font=("arial", 20, "bold"), height=1, width=10, bd=4,

                          command=adddata)

            btn1.grid(row=0, column=0)

            btn2 = Button(ButtonFrame, text="Display", font=("arial", 20, "bold"), height=1, width=10, bd=4,

                          command=displaydata)

            btn2.grid(row=0, column=1)

            btn3 = Button(ButtonFrame, text="Clear", font=("arial", 20, "bold"), height=1, width=10, bd=4,

                          command=cleardata)

            btn3.grid(row=0, column=2)

            btn4 = Button(ButtonFrame, text="Delete", font=("arial", 20, "bold"), height=1, width=10, bd=4,

                          command=deletedata)

            btn4.grid(row=0, column=3)

            btn5 = Button(ButtonFrame, text="Search", font=("arial", 20, "bold"), height=1, width=10, bd=4,

                          command=searchdata)

            btn5.grid(row=0, column=4)

            btn6 = Button(ButtonFrame, text="Update", font=("arial", 20, "bold"), height=1, width=10, bd=4,

                          command=update)

            btn6.grid(row=0, column=5)

            btn7 = Button(ButtonFrame, text="Exit", font=("arial", 20, "bold"), height=1, width=10, bd=4, command=iexit)

            btn7.grid(row=0, column=6)

            r.mainloop()

        def deladmin():

            nam = StringVar()

            qk.destroy()

            admin0 = Tk()

            admin0.config(bg='gray10')

            admin0.iconbitmap(r"hms.ico")

            admin0.title("Delete Admin")

            admin0.geometry("300x120")

            admin0.resizable(0, 0)

            name0 = Label(admin0,bg='gray10',fg='light green', text="Enter Admin to be deleted :")

            name0.place(x=10, y=10)

            nam0 = ttk.Entry(admin0, textvariable=nam)

            nam0.place(x=170, y=10)

            def deleteadmin():

                adm = nam0.get()

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                x = cur.execute("delete from openadmin where username = '%s'" %adm )

                cur.execute("commit")

                sentence = 'Admin ' + adm + ' , deleted successfully.'

                messagebox.showinfo('Admin deleted', sentence)

            def canceell():

                admin0.destroy()

                fa()

            bn = Button(admin0,bg='green',fg='white', text="DELETE", width=37, command=deleteadmin,relief = 'raise' , bd = 7)

            bn.place(x=10, y=40)

            bn0 = Button(admin0,bg='green',fg='white', text='CANCEL', width=37, command=canceell,relief = 'raise',bd = 7)

            bn0.place(x=10, y=80)

        def deluser():

            nam = StringVar()

            qk.destroy()

            user0 = Tk()

            user0.config(bg='gray10')

            user0.iconbitmap(r"hms.ico")

            user0.title("Delete User")

            user0.geometry("300x120")

            user0.resizable(0, 0)

            name0 = Label(user0,bg='gray10',fg='light green', text="Enter User to be deleted :")

            name0.place(x=10, y=10)

            nam0 = ttk.Entry(user0, textvariable=nam)

            nam0.place(x=170, y=10)

            def deleteuser():

                adm = nam0.get()

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                x = cur.execute("delete from openuser where username = '%s'" %adm )

                cur.execute("commit")

                sentence = 'User ' + adm + ' , deleted successfully.'

                messagebox.showinfo('User deleted', sentence)

            def canceelll():

                user0.destroy()

                fa()

            bn = Button(user0,bg='green',fg='white', text="DELETE", width=37, command=deleteuser,relief = 'raise' , bd = 7)

            bn.place(x=10, y=40)

            bn0 = Button(user0,bg='green',fg='white', text='CANCEL', width=37, command=canceelll,relief = 'raise' , bd = 7)

            bn0.place(x=10, y=80)

        def addadmin():

            nam = StringVar()

            paso= StringVar()

            qk.destroy()

            admin = Tk()

            admin.config(bg='gray10')
            
            admin.iconbitmap(r"hms.ico")

            admin.title("Add Admin")

            admin.geometry("260x180")

            admin.resizable(0, 0)

            name0 = Label(admin,bg='gray10',fg='cyan', text="Enter Admin Name :")

            name0.place(x=10, y=10)

            nam0 = ttk.Entry(admin,textvariable=nam)

            nam0.place(x=120, y=10)

            pass0 = Label(admin,bg='gray10',fg='cyan', text="Enter Password :")

            pass0.place(x=10, y=40)

            pas0 = ttk.Entry(admin, show="*")

            pas0.place(x=120, y=40)

            pass1 = Label(admin,bg='gray10',fg='cyan', text="Confirm Password :")

            pass1.place(x=10, y=70)

            pas1 = ttk.Entry(admin, show="*",textvariable = paso)

            pas1.place(x=120, y=70)

            def cancell():

                admin.destroy()

                fa()

                return
 
            def newadmin():

                newwn = nam0.get()

                newp = pas1.get()

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                x = cur.execute("insert into openadmin values('%s' , '%s')"%(newwn , newp))

                cur.execute("commit")

                sentence= 'New admin ' +newwn+  ' , added successfully.'

                messagebox.showinfo('Admin added',sentence)

            bn = Button(admin,bg='cadet blue',fg='white', text="ADD", width=32, command=newadmin,relief = 'raise' , bd = 7)

            bn.place(x=10, y=100)

            bn0 = Button(admin,bg='cadet blue',fg='white', text='CANCEL', width=32, command=cancell,relief = 'raise' , bd = 7)

            bn0.place(x=10, y=140)

            return

        def adduser():

            nam = StringVar()

            paso = StringVar()

            qk.destroy()

            user = Tk()

            user.config(bg='gray10')

            user.iconbitmap(r"hms.ico")

            user.title("Add User")

            user.geometry("260x180")

            user.resizable(0, 0)

            name0 = Label(user,bg='gray10',fg='cyan', text="Enter User Name :")

            name0.place(x=10, y=10)

            nam0 = ttk.Entry(user, textvariable=nam)

            nam0.place(x=120, y=10)

            pass0 = Label(user,bg='gray10',fg='cyan', text="Enter Password :")

            pass0.place(x=10, y=40)

            pas0 = ttk.Entry(user, show="*")

            pas0.place(x=120, y=40)

            pass1 = Label(user,bg='gray10',fg='cyan', text="Confirm Password :")

            pass1.place(x=10, y=70)

            pas1 = ttk.Entry(user, show="*", textvariable=paso)

            pas1.place(x=120, y=70)

            def cancelll():

                user.destroy()

                fa()

                return

            def newuser():

                newwn = nam0.get()

                newp = pas1.get()

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                x = cur.execute("insert into openuser values('%s' , '%s')" % (newwn, newp))

                cur.execute("commit")

                sentence = 'New user ' + newwn + ' , added successfully.'

                messagebox.showinfo('User added', sentence)

                return

            bn = Button(user,bg='cadet blue',fg='white', text="ADD", width=32,command = newuser,relief = 'raise' , bd = 7)

            bn.place(x=10, y=100)

            bn0 = Button(user,bg='cadet blue',fg='white',text= 'CANCEL',width=32,command = cancelll,relief = 'raise' , bd = 7)

            bn0.place(x=10,y=140)

        def goto():

            qk.destroy()

            patient = Tk()

            patient.geometry("1365x740")

            patient.config(bg="gray10")

            patient.title("Hospital Mangement System")

            patient.iconbitmap(r"hms.ico")

            PatID = IntVar()

            Name = StringVar()

            Disease = StringVar()

            City = StringVar()

            Height = StringVar()

            Age = StringVar()

            Gender = StringVar()

            Address = StringVar()

            Mobile = StringVar()

            AppointmentNo = StringVar()

            Weight = StringVar()

            Bloodgroup = StringVar()

            Title = Label(patient, font=('castellar', 35, 'bold'), text="Hospital  Mangement  System", fg="cyan",bg="gray", bd=7, anchor="w",relief="raise")

            Title.place(x=250,y=10)

            LeftFrametop=Frame(patient, bd=8, relief="raise",bg="gray",width = 841, height = 268)

            LeftFrametop.place(x=0,y=165)

            LeftFramebottomleft=Frame(patient, width=405, height=207, bd=8, relief="raise",bg="gray")

            LeftFramebottomleft.place(x=0,y=468)

            LeftFramebottomright=Frame(patient, width=405, height=207, bd=8, relief="raise",bg="gray")

            LeftFramebottomright.place(x=442,y=468)

            ScrollFrame=Frame(patient, width=603, height=200, bd=8, relief="raise",bg="powder blue")

            ScrollFrame.place(x=940 ,y= 165)

            ButtonFrame=Frame(patient, width=295, height=400, bd=8, relief="raise",bg="powder blue")

            ButtonFrame.place(x= 940,y= 500)

            lblPatID = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient ID",width = 15,bg="gray", fg="cyan", bd=7, relief="ridge")

            lblPatID.place(x=0,y=20)

            txtPatID = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = PatID, relief="ridge")

            txtPatID.place(x=200 , y=20)

            lblname = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient Name",bg="gray", fg="cyan", bd=7, relief="ridge",width = 15)

            lblname.place(x=0,y=80)

            txtname = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = Name, relief="ridge")

            txtname.place(x=200 , y=80)

            lblAddress = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Address",bg="gray", fg="cyan", bd=7, relief="ridge",width = 15)

            lblAddress.place(x=0 , y=140)

            txtAddress = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = Address, relief="ridge")

            txtAddress.place(x=200 , y=140)

            lblAppointmentNo = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Appointment No.",bg="gray", fg="cyan", bd=7, relief="ridge",width = 15)

            lblAppointmentNo.place(x=0 , y=200)

            txtAppointmentNo = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = AppointmentNo, relief="ridge")

            txtAppointmentNo .place(x=200 , y=200)

            lblCity = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="City",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lblCity.place(x=0,y=0)

            txtCity = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = City, relief="ridge")

            txtCity.place(x=175,y=0)

            lblHeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Height (cms)",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lblHeight.place(x=0,y=50)

            txtHeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Height, relief="ridge")

            txtHeight.place(x=175,y=50)

            lblgender = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Gender",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lblgender.place(x=0,y=100)

            gen=['Male','Female'];

            txtgender = OptionMenu(LeftFramebottomleft,Gender,*gen)

            txtgender.config(relief="ridge",font=('arial', 14, 'bold'), bd=4, width=15, bg="powder blue", justify="center")

            txtgender.place(x=175,y=100)

            lblWeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Weight (kgs)",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lblWeight.place(x=0,y=150)

            txtWeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Weight, relief="ridge")

            txtWeight.place(x=175,y=150)

            lblage = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Age (yrs) ",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lblage.place(x=0,y=0)

            txtage = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Age, relief="ridge")

            txtage.place(x=175,y=0)

            lblmobile = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Mobile number",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lblmobile.place(x=0,y=50 )

            txtmobile = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Mobile, relief="ridge")

            txtmobile.place(x=175,y=50)

            lbldisease = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Disease",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lbldisease.place(x=0,y=100)

            txtdisease = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Disease, relief="ridge")

            txtdisease.place(x=175,y=100)

            lblbldgrp = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Blood Group",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

            lblbldgrp.place(x=0,y=150)

            txtbldgrp = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Bloodgroup, relief="ridge")

            txtbldgrp.place(x=175,y=150)

            def  iexit():

                iexit = messagebox.askokcancel("Hospital Managment System"," Do you want to exit ")

                if  iexit > 0:

                    patient.destroy ()

                    fa()

                    return

            def cleardata():

                txtPatID.delete(0,END)

                txtname.delete(0,END)

                txtage.delete(0,END)

                txtCity.delete(0,END)

                txtdisease.delete(0,END)

                txtAddress.delete(0,END)

                txtAppointmentNo.delete(0,END)

                txtHeight.delete(0,END)

                txtmobile.delete(0,END)

                txtWeight.delete(0,END)

                txtbldgrp.delete(0,END)

                Gender.set('')

            def adddocrec(a, b, c, d, e, f, g,  h ,i , j , k , l):

                            conn = cx_Oracle.connect('system/anwar@localhost')

                            cur = conn.cursor()

                            cur.execute("insert into patrec values (%d , '%s' ,'%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s')" % (a, b, c, d, e, f, g,  h ,i , j , k , l))

                            cur.execute("commit")

                            conn.close

            def adddata():

                            adddocrec(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

                            patlist.delete(0, END)

                            patlist.insert(END, (

                            txtPatID.get() , txtname.get(),txtdisease.get(),txtbldgrp.get(), AppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()),)

                            messagebox.showinfo('Hospiital Mangement System','New Patient Added Successfully')

            def viewdata():

                        conn = cx_Oracle.connect('system/anwar@localhost')

                        cur = conn.cursor()

                        cur.execute("select * from patrec")

                        row = cur.fetchall()

                        conn.close

                        return row

            def displaydata():

                        patlist.delete(0, END)

                        for row in viewdata():

                            patlist.insert(END, row, str(" "))

            def patrec(event):

                global sd

                searchpat = patlist . curselection() [0]

                sd = patlist . get( searchpat )

                txtPatID.delete(0,END)

                txtPatID.insert(END,sd[0])

                txtbldgrp.delete(0,END)

                txtbldgrp.insert(END,sd[3])

                txtWeight.delete(0,END)

                txtWeight.insert(END,sd[8])

                txtHeight.delete(0,END)

                txtHeight.insert(END,sd[9])

                txtAppointmentNo.delete(0,END)

                txtAppointmentNo.insert(END,sd[4])

                txtname.delete(0,END)

                txtname.insert(END,sd[1])

                txtage.delete(0,END)

                txtage.insert(END,sd[5])

                Gender.set('')

                Gender.set(sd[6])

                txtCity.delete(0,END)

                txtCity.insert(END,sd[7])

                txtdisease.delete(0,END)

                txtdisease.insert(END,sd[2])

                txtAddress.delete(0,END)

                txtAddress.insert(END,sd[10])

                txtmobile.delete(0,END)

                txtmobile.insert(END,sd[11])

            def deleterec(patid):

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                cur.execute("delete  from patrec where patid = %d" % patid)

                cur.execute("commit")

                conn.close

            def deletedata():

                searchpat = patlist.curselection()[0]

                sd = patlist.get(searchpat)

                deleterec(sd[0])

                cleardata()

                displaydata()

                messagebox.showinfo('Hospiital Mangement System', ' User Deleted Successfully')

            def ssearchdata(x):

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                cur.execute("select * from patrec where patid = %d  " % x)

                row = cur.fetchall()

                conn.close

                return row

            def searchdata():

                patlist.delete(0, END)

                for row in ssearchdata(int(txtPatID.get())):

                    cleardata()

                    patlist.insert(END, row, str(""))

                    x00=row[0]

                    x=row[1]

                    x0=row[4]

                    x1=row[2]

                    x3=row[3]

                    x4=row[5]

                    x5=row[6]

                    x6=row[7]

                    x7=row[8]

                    x8=row[9]

                    x9=row[10]

                    x10=row[11]

                    txtPatID.insert(0,x00)

                    txtCity.insert(0,x6)

                    Gender.set(x5)

                    txtage.insert(0,x4)

                    txtbldgrp.insert(0,x3)

                    txtdisease.insert(0,x1)

                    txtAppointmentNo.insert(0,x0)

                    txtname.insert(0,x)

                    txtWeight.insert(0,x7)

                    txtHeight.insert(0,x8)

                    txtAddress.insert(0,x9)

                    txtmobile.insert(0,x10)

            def update():

                searchpat = patlist.curselection()[0]

                sd = patlist.get(searchpat)

                patlist.delete(0, END)

                deleterec(sd[0])

                adddocrec(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

                patlist.delete(0, END)

                patlist.insert(END, (

                int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()))

                messagebox.showinfo('Hospiital Mangement System', 'New Information Updated Successfully')

            scroll=Scrollbar(ScrollFrame)

            scroll.grid(row=0,column=1,sticky='NS')

            patlist=Listbox(ScrollFrame,   width=41,  height=16,font=("arial",12,"bold"), yscrollcommand=scroll.set )

            patlist.bind('<<ListboxSelect>>',patrec)

            patlist.grid(row=0,column=0,  padx=8)

            scroll.config(command = patlist.yview)

            btn1 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                    text="Add New", bg="gray", command=adddata, relief="raise").grid(row=0, column=0)

            btn2 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                    text="Display", bg="gray", command=displaydata, relief="raise").grid(row=0, column=1)

            btn3 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                    text="Search", bg="gray", command=searchdata, relief="raise").grid(row=0, column=2)

            btn4 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                    text="Clear", bg="gray", command=cleardata, relief="raise").grid(row=1, column=0)

            btn5 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                    text="Delete", bg="gray", command=deletedata, relief="raise").grid(row=1, column=1)

            btn6 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                    text="Update", bg="gray", command=update, relief="raise").grid(row=1, column=2)

            btn7 = Button(patient, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=30, bd=7,

                    text="Exit", bg="gray", command=iexit, relief="raise").place(x=940, y=625)

            patient.mainloop()


        def shadmin():

            qk.destroy()

            win = Tk()

            win.config(bg='gray10')

            win.title ('Showing all administrators')

            win.iconbitmap(r"hms.ico")

            win.geometry("400x400")

            scr = Scrollbar(win)

            scr.grid(row=0, column=1, sticky='NS')

            pa = Listbox(win, width=41, height=16,fg='maroon',bg='light gray', font=("castellar", 12, "bold"), yscrollcommand=scr.set)

            pa.grid(row=0, column=0, padx=8)

            scr.config(command=pa.yview)

            conn = cx_Oracle.connect('system/anwar@localhost')

            cur = conn.cursor()

            x = cur.execute("select  username from openadmin")

            for row in x:

                pa.insert(END, row, '\n')

            def cing():

                win.destroy()

                fa()

            Button(win,text = 'CANCEL',command = cing , width = 30,bd=7,relief='raise',bg='maroon',fg='white').grid(row = 2,column = 0)

            win . mainloop()

        def shuser():

            qk.destroy()

            win = Tk()

            win.config(bg='gray10')

            win.title('Showing all users')

            win.iconbitmap(r"hms.ico")

            win.geometry("400x400")

            scr = Scrollbar(win)

            scr.grid(row=0, column=1, sticky='NS')

            pa = Listbox(win, width=41, height=16,fg='maroon',bg='light gray', font=("castellar", 12, "bold"), yscrollcommand=scr.set)

            pa.grid(row=0, column=0, padx=8)

            scr.config(command=pa.yview)

            conn = cx_Oracle.connect('system/anwar@localhost')

            cur = conn.cursor()

            x = cur.execute("select  username from openuser")

            for row in x:

                pa.insert(END, row, '\n')

            def cing():

                win.destroy()

                fa()

            Button(win, text='CANCEL', command=cing, width=30,bd=7,relief='raise',bg='maroon',fg='white').grid(row = 2,column = 0)

            win.mainloop()

        def iex():

            qk.destroy()

            main()

        qk=Tk()

        qk.title("ADMINISITRATOR")

        qk.iconbitmap(r"hms.ico")

        qk.resizable(0,0)

        qk.config(bg='gray10')

        qk.geometry("350x460")

        sen = 'Welcome Mr. ' + usser + '\n  you have logged in successfully'

        Label(qk,text=sen,bg='gray10',fg='white', font=('castellar', 10, 'bold','italic')).pack()

        bt0=Button(qk,bg='maroon',fg='white',text='Add New Administrator',command = addadmin,width = 30,relief='raise',bd=7,font=('calibri',10,'bold'))

        bt0.place(x=70,y=50)

        bt1=Button(qk,bg='maroon',fg='white',text='Add New User',width = 30,command = adduser,relief='raise',bd=7,font=('calibri',10,'bold'))

        bt1.place(x=70,y=95)

        bt2 =Button(qk, text='Doctors',bg='maroon',fg='white',command=doct,width = 30,relief='raise',font=('calibri',10,'bold'),bd=7)

        bt2.place(x=70,y=140)

        bt3 =Button(qk, text='Patients',command=goto,bg='maroon',fg='white',width = 30,relief='raise',font=('calibri',10,'bold'),bd=7)

        bt3.place(x=70,y=185)

        bt4 = Button(qk, text='Delete administrator', command=deladmin,bg='maroon',font=('calibri',10,'bold'),fg='white',width=30,relief='raise',bd=7)

        bt4.place(x=70,y=230)

        bt5 = Button(qk, text='Delete user', command = deluser ,font=('calibri',10,'bold'),bg='maroon',fg='white',width=30,relief='raise',bd=7)

        bt5.place(x=70,y=275)

        bt6 = Button(qk, text='Show all administrators',font=('calibri',10,'bold'), command=shadmin,bg='maroon',fg='white', width=30,relief='raise',bd=7)

        bt6.place(x=70,y=320)

        bt7 = Button(qk, text='Show all users', command=shuser,font=('calibri',10,'bold'),bg='maroon',fg='white',width=30,relief='raise',bd=7)

        bt7.place(x=70,y=365)

        bt8 =Button(qk, text = 'Exit', command=iex,bg='maroon',font=('calibri',10,'bold'),fg='white',width = 30,relief='raise',bd=7)

        bt8.place(x=70,y=410)

        qk.mainloop()

    def fu():

        patient = Tk()

        patient.geometry("1365x740")

        patient.config(bg="gray10")

        patient.title("Hospital Mangement System")

        patient.iconbitmap(r"hms.ico")

        PatID = IntVar()

        Name = StringVar()

        Disease = StringVar()

        City = StringVar()

        Height = StringVar()

        Age = StringVar()

        Gender = StringVar()

        Address = StringVar()

        Mobile = StringVar()

        AppointmentNo = StringVar()

        Weight = StringVar()

        Bloodgroup = StringVar()

        Title = Label(patient, font=('castellar', 35, 'bold'), text="Hospital  Mangement  System", fg="cyan",bg="gray", bd=7, anchor="w",relief="raise")

        Title.place(x=250,y=10)

        LeftFrametop=Frame(patient, bd=8, relief="raise",bg="gray",width = 841, height = 268)

        LeftFrametop.place(x=0,y=165)

        LeftFramebottomleft=Frame(patient, width=405, height=207, bd=8, relief="raise",bg="gray")

        LeftFramebottomleft.place(x=0,y=468)

        LeftFramebottomright=Frame(patient, width=405, height=207, bd=8, relief="raise",bg="gray")

        LeftFramebottomright.place(x=442,y=468)

        ScrollFrame=Frame(patient, width=603, height=200, bd=8, relief="raise",bg="powder blue")

        ScrollFrame.place(x=940 ,y= 165)

        ButtonFrame=Frame(patient, width=295, height=400, bd=8, relief="raise",bg="powder blue")

        ButtonFrame.place(x= 940,y= 500)

        lblPatID = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient ID",width = 15,bg="gray", fg="cyan", bd=7, relief="ridge")

        lblPatID.place(x=0,y=20)

        txtPatID = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = PatID, relief="ridge")

        txtPatID.place(x=200 , y=20)

        lblname = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient Name",bg="gray", fg="cyan", bd=7, relief="ridge",width = 15)

        lblname.place(x=0,y=80)

        txtname = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = Name, relief="ridge")

        txtname.place(x=200 , y=80)

        lblAddress = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Address",bg="gray", fg="cyan", bd=7, relief="ridge",width = 15)

        lblAddress.place(x=0 , y=140)

        txtAddress = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = Address, relief="ridge")

        txtAddress.place(x=200 , y=140)

        lblAppointmentNo = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Appointment No.",bg="gray", fg="cyan", bd=7, relief="ridge",width = 15)

        lblAppointmentNo.place(x=0 , y=200)

        txtAppointmentNo = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue", justify="center", textvariable = AppointmentNo, relief="ridge")

        txtAppointmentNo .place(x=200 , y=200)

        lblCity = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="City",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lblCity.place(x=0,y=0)

        txtCity = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = City, relief="ridge")

        txtCity.place(x=175,y=0)

        lblHeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Height (cms)",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lblHeight.place(x=0,y=50)

        txtHeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Height, relief="ridge")

        txtHeight.place(x=175,y=50)

        lblgender = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Gender",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lblgender.place(x=0,y=100)

        gen=['Male','Female'];

        txtgender = OptionMenu(LeftFramebottomleft,Gender,*gen)

        txtgender.config(relief="ridge",font=('arial', 14, 'bold'), bd=4, width=15, bg="powder blue", justify="center")

        txtgender.place(x=175,y=100)

        lblWeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Weight (kgs)",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lblWeight.place(x=0,y=150)

        txtWeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Weight, relief="ridge")

        txtWeight.place(x=175,y=150)

        lblage = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Age (yrs) ",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lblage.place(x=0,y=0)

        txtage = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Age, relief="ridge")

        txtage.place(x=175,y=0)

        lblmobile = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Mobile number",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lblmobile.place(x=0,y=50 )

        txtmobile = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Mobile, relief="ridge")

        txtmobile.place(x=175,y=50)

        lbldisease = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Disease",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lbldisease.place(x=0,y=100)

        txtdisease = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Disease, relief="ridge")

        txtdisease.place(x=175,y=100)

        lblbldgrp = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Blood Group",bg="gray", fg="cyan", bd=7, relief="ridge",width = 13)

        lblbldgrp.place(x=0,y=150)

        txtbldgrp = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue", justify="center", textvariable = Bloodgroup, relief="ridge")

        txtbldgrp.place(x=175,y=150)

        def  iexit():

            iexit = messagebox.askokcancel("Hospital Managment System"," Do you want to exit ")

            if  iexit > 0:

                patient.destroy ()

                main()

                return

        def cleardata():

            txtPatID.delete(0,END)

            txtname.delete(0,END)

            txtage.delete(0,END)

            txtCity.delete(0,END)

            txtdisease.delete(0,END)

            txtAddress.delete(0,END)

            txtAppointmentNo.delete(0,END)

            txtHeight.delete(0,END)

            txtmobile.delete(0,END)

            txtWeight.delete(0,END)

            txtbldgrp.delete(0,END)

            Gender.set('')

        def adddocrec(a, b, c, d, e, f, g,  h ,i , j , k , l):

                        conn = cx_Oracle.connect('system/anwar@localhost')

                        cur = conn.cursor()

                        cur.execute("insert into patrec values (%d , '%s' ,'%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s')" % (a, b, c, d, e, f, g,  h ,i , j , k , l))

                        cur.execute("commit")

                        conn.close

        def adddata():

                        adddocrec(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

                        patlist.delete(0, END)

                        patlist.insert(END, (

                        txtPatID.get() , txtname.get(),txtdisease.get(),txtbldgrp.get(), AppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()),)

                        messagebox.showinfo('Hospiital Mangement System','New Patient Added Successfully')

        def viewdata():

                    conn = cx_Oracle.connect('system/anwar@localhost')

                    cur = conn.cursor()

                    cur.execute("select * from patrec")

                    row = cur.fetchall()

                    conn.close

                    return row

        def displaydata():

                    patlist.delete(0, END)

                    for row in viewdata():

                        patlist.insert(END, row, str(" "))

        def patrec(event):

            global sd

            searchpat = patlist . curselection() [0]

            sd = patlist . get( searchpat )

            txtPatID.delete(0,END)

            txtPatID.insert(END,sd[0])

            txtbldgrp.delete(0,END)

            txtbldgrp.insert(END,sd[3])

            txtWeight.delete(0,END)

            txtWeight.insert(END,sd[8])

            txtHeight.delete(0,END)

            txtHeight.insert(END,sd[9])

            txtAppointmentNo.delete(0,END)

            txtAppointmentNo.insert(END,sd[4])

            txtname.delete(0,END)

            txtname.insert(END,sd[1])

            txtage.delete(0,END)

            txtage.insert(END,sd[5])

            Gender.set('')

            Gender.set(sd[6])

            txtCity.delete(0,END)

            txtCity.insert(END,sd[7])

            txtdisease.delete(0,END)

            txtdisease.insert(END,sd[2])

            txtAddress.delete(0,END)

            txtAddress.insert(END,sd[10])

            txtmobile.delete(0,END)

            txtmobile.insert(END,sd[11])

        def deleterec(patid):

            conn = cx_Oracle.connect('system/anwar@localhost')

            cur = conn.cursor()

            cur.execute("delete  from patrec where patid = %d" % patid)

            cur.execute("commit")

            conn.close

        def deletedata():

            searchpat = patlist.curselection()[0]

            sd = patlist.get(searchpat)

            deleterec(sd[0])

            cleardata()

            displaydata()

            messagebox.showinfo('Hospiital Mangement System', ' User Deleted Successfully')

        def ssearchdata(x):

            conn = cx_Oracle.connect('system/anwar@localhost')

            cur = conn.cursor()

            cur.execute("select * from patrec where patid = %d  " % x)

            row = cur.fetchall()

            conn.close

            return row

        def searchdata():

            patlist.delete(0, END)

            for row in ssearchdata(int(txtPatID.get())):

                cleardata()

                patlist.insert(END, row, str(""))

                x00=row[0]

                x=row[1]

                x0=row[4]

                x1=row[2]

                x3=row[3]

                x4=row[5]

                x5=row[6]

                x6=row[7]

                x7=row[8]

                x8=row[9]

                x9=row[10]

                x10=row[11]

                txtPatID.insert(0,x00)

                txtCity.insert(0,x6)

                Gender.set(x5)

                txtage.insert(0,x4)

                txtbldgrp.insert(0,x3)

                txtdisease.insert(0,x1)

                txtAppointmentNo.insert(0,x0)

                txtname.insert(0,x)

                txtWeight.insert(0,x7)

                txtHeight.insert(0,x8)

                txtAddress.insert(0,x9)

                txtmobile.insert(0,x10)

        def update():

            searchpat = patlist.curselection()[0]

            sd = patlist.get(searchpat)

            patlist.delete(0, END)

            deleterec(sd[0])

            adddocrec(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

            patlist.delete(0, END)

            patlist.insert(END, (

            int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()))

            messagebox.showinfo('Hospiital Mangement System', 'New Information Updated Successfully')

        scroll=Scrollbar(ScrollFrame)

        scroll.grid(row=0,column=1,sticky='NS')

        patlist=Listbox(ScrollFrame,   width=41,  height=16,font=("arial",12,"bold"), yscrollcommand=scroll.set )

        patlist.bind('<<ListboxSelect>>',patrec)

        patlist.grid(row=0,column=0,  padx=8)

        scroll.config(command = patlist.yview)

        btn1 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                text="Add New", bg="gray", command=adddata, relief="raise").grid(row=0, column=0)

        btn2 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                text="Display", bg="gray", command=displaydata, relief="raise").grid(row=0, column=1)

        btn3 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                text="Search", bg="gray", command=searchdata, relief="raise").grid(row=0, column=2)

        btn4 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                text="Clear", bg="gray", command=cleardata, relief="raise").grid(row=1, column=0)

        btn5 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                text="Delete", bg="gray", command=deletedata, relief="raise").grid(row=1, column=1)

        btn6 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

                text="Update", bg="gray", command=update, relief="raise").grid(row=1, column=2)

        btn7 = Button(patient, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=30, bd=7,

                text="Exit", bg="gray", command=iexit, relief="raise").place(x=940, y=625)

        patient.mainloop()


    def vadmin():

        r.destroy()

        mn=Tk()

        mn.iconbitmap(r"hms.ico")

        mn.title("LOG IN ADMIN")

        mn.geometry("255x110")

        mn.config(bg='gray10')

        mn.resizable(0,0)

        name=StringVar()

        passc=StringVar()

        e=Label(mn,bg='gray10',fg='yellow',text="Enter Admin Name :")

        e.place(x=10,y=10)

        q=ttk.Entry(mn,textvariable=name)

        q.place(x=120,y=10)

        p=Label(mn,bg='gray10',fg='yellow',text="Enter Password :")

        p.place(x=10,y=40)

        w=ttk.Entry(mn,textvariable=passc,show='*')

        w.place(x=120,y=40)

        def wa():

            global usser

            usser=q.get()

            user=str(usser)

            ppass=w.get()

            try:

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                x = cur.execute("select  username from openadmin where pass = '%s' "%ppass)

                for i in x:

                    pr=i

                if pr == (usser,) :

                    mn.destroy()

                    fa()

                else:

                    messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")

            except:

                messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")

        y=Button(mn,fg='gray10',bg='yellow',bd=7,text="LOG IN",width=32,relief='raise',command=wa)

        y.place(x=10,y=70)

        mn.mainloop()

    def vuser():

        r.destroy()

        mn=Tk()

        mn.config(bg='gray10')

        mn.iconbitmap(r"hms.ico")

        mn.title("LOG IN USER")

        mn.geometry("255x110")

        mn.resizable(0,0)

        name=StringVar()

        passc=StringVar()

        e=Label(mn,bg='gray10',fg='cyan',text="Enter User Name :")

        e.place(x=10,y=10)

        q=ttk.Entry(mn,textvariable=name)

        q.place(x=120,y=10)

        p=Label(mn,bg='gray10',fg='cyan',text="Enter Password :")

        p.place(x=10,y=40)

        w=ttk.Entry(mn,textvariable=passc,show='*')

        w.place(x=120,y=40)

        def wu ():

            ussser=q.get()

            user=str(ussser)

            ppass=w.get()

            try :
                
                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                conn = cx_Oracle.connect('system/anwar@localhost')

                cur = conn.cursor()

                xm = cur.execute("select  username from openuser where pass = '%s' "%ppass)

                for i in xm:

                    pr2=i

                if pr2 == (ussser,) :

                    mn.destroy()         

                    fu()

                else:

                    messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")

            except:

                messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")

        y=Button(mn,fg='gray10',bg='cyan',bd = 7,relief='raise',text="LOG  IN",width=32,command=wu)

        y.place(x=10,y=70)

        mn.mainloop()

    def exitt():

        f=messagebox.askokcancel("Verification","Confirm if you wan to exit")

        if f > 0:

            r.destroy()

    r = Tk()

    r.iconbitmap(r"hms.ico")

    r.title("Verification")

    r.resizable(0, 0)

    m = Frame(r)

    m.pack()

    c = Canvas(m, width=650, height=430)

    c.pack()

    p = PhotoImage(file=r"hms3.png")

    c.create_image(0, 0, image=p, anchor="nw")

    l = Label(m, text="Hospital Mangement System", font=('castellar', 16, 'bold', 'italic'),bg= 'light gray', fg="black")

    l.place(x=120, y=10)
    
    value = IntVar()

    value.set(2)

    photo = PhotoImage(file=r"hms2.png")

    photo0 = PhotoImage(file=r"hms1.png")

    rd0 = Radiobutton(m, image=photo, bg="light gray", value=1, variable=value, command=vadmin)

    rd0.place(x=65, y=70)

    lb0 = Label(m, text="Administrator", font=('castellar', 30, 'bold', 'italic'), height=2)

    lb0.place(x=219, y=70)

    rd = Radiobutton(m, image=photo0, bg="light gray", value=2, variable=value, command=vuser)

    rd.place(x=65, y=200)

    lb = Label(m, text="user", font=('castellar', 30, 'bold', 'italic'), height=2)

    lb.place(x=200, y=200)

    x = value.get()

    def bg5():

        p.config(file=r"hms3.png")

        btn0.config(command=bg)

    def bg4():

        p.config(file=r"hms4.png")

        btn0.config(command=bg5)
       
    def bg3():

        p.config(file=r"hms5.png")

        btn0.config(command=bg4)
       
    def  bg2():

        p.config(file=r"hms6.png")

        btn0.config(command=bg3)
       
    def bg1():

        p.config(file=r"hms7.png")

        btn0.config(command=bg2)
       
    def bg0():
       
        p.config(file=r"hms8.png")

        btn0.config(command=bg1)
       
    def bg():
        
        p.config(file=r"hms9.png")

        btn0.config(command=bg0)

    btn = Button(m, text="EXIT", font=("algerian", 20, "bold"), bg="gray", height=1, width=30, bd=7,relief = 'raise',command=exitt)

    btn.place(x=45, y=320)

    phot = PhotoImage(file=r"hms0.png")

    btn0 = Button(m, image = phot,command=bg,bg='black')

    btn0['border']='0'
    
    btn0.place(x=0, y=0)

    r.mainloop()

main()
