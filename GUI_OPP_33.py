from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os,time,MyModule
from string import printable

class Start:
    #tot = []
    def __init__(self,win):
        self.win = win
        self.cond1,self.cond2 = True,True
        self.clean()
        self.img = Image.open(f'Images/CP-II logo screen.png')
        self.img = self.img.resize( (500,500), Image.ANTIALIAS) 
        self.photo1 = ImageTk.PhotoImage( self.img )
        self.label = Label(self.win,  image = self.photo1)
        self.label.pack()
        

        Label(self.win, text='Thanks for visiting our Online Shoping Store',bg='dark cyan',fg='white',font = ('Helvetica' , 12)).place(x=100,y=240)
        self.signupbt = Button(self.win, text='Sign-Up',font = ('verdana' , 10),bg='royal blue', fg='white', command= lambda: self.signupfn())
        self.signupbt.place(x = 160, y=300,height=26, width=70)
        self.loginbt = Button(self.win, text='Log-In',font = ('verdana' , 10),bg='dark slate gray', fg='white', command=lambda : self.loginfn())
        self.loginbt.place(x = 280, y=300,height=26, width=70) 
    def signupfn(self):
        self.clean()
        self.imgname,self.size1,self.size2 = 'W3.jpg',500,500
        self.imageOp()
        if self.cond1 is False:
            self.cond1 = True
            Label(self.win, text='Error!\nPlease Enter valid Username\Password\Email*',bg='red', fg='white',font = ('verdana' , 10)).place(x=130,y=130)
        if self.cond2 is False:
            self.cond2  = True
            Label(self.win, text='Error!\nYou entered weak password\n\nYour password must contain upper and lower case alphabets and\n some numeric numbers\n*',bg='red', fg='white',font = ('verdana' , 10)).place(x=20,y=70)
        self.usname = Label(self.win,text='User Name:',bg='dark orange',font = ('verdana' , 10))
        self.usname.place(x=80,y=200)
        self.usmail = Label(self.win,text='Email: ',bg='dark orange',font = ('verdana' , 10))
        self.usmail.place(x=80,y=230)
        self.uspassword = Label(self.win,text='Password: ',bg='dark orange',font = ('verdana' , 10))
        self.uspassword.place(x=80,y=260)
        self.name = Entry(self.win,width=40,borderwidth=3)
        self.name.place(x=170,y=200)
        self.mail = Entry(self.win,width=40,borderwidth=3)
        self.mail.place(x=170,y=230)
        self.password = Entry(self.win,width=40,borderwidth=3)
        self.password.place(x=170,y=260)
        self.but1 = Button(self.win, text='Sign-Up',bg='navy',fg='light blue',font = ('verdana' , 10), command=lambda : self.signup())
        self.but1.place(x = 320, y=300 , height=26,width=70)
        Button(self.win, text='Back',bg='dark cyan',fg='white',font = ('verdana' , 10), command=lambda : Start(self.win)).place(x = 160, y=300, height=26,width=70 )
    def signup(self):
        self.get1,self.get2,self.get3 = self.name.get(),self.password.get(),self.mail.get()
        if(self.get1=="" or self.get2=="" or self.get3==""):
            self.cond1 = False
            self.signupfn()
            messagebox.showinfo('Error!','Please Enter Somthing')
        if(self.get1!="" or self.get2!="" or self.get3!=""):
            if MyModule.pswdcheck(self.get2) is False:
            # messagebox.showinfo('Error!','You entered Weak Password')
                self.cond2 = False
                self.signupfn()
                messagebox.showinfo('Error!','You entered Weak Password')
            elif '@' not in self.get3:
            # messagebox.showinfo('Error!','You entered WRONG email address')
                self.cond1 = False
                self.signupfn()
                messagebox.showinfo('Error!','You entered WRONG Email Address')
            else:
                with open('Text/signup.txt','a') as files:
                    files.write(f'{(self.name)},{(self.password)},{(self.mail)}\n')
                    #pfdic = {'Name':self.name}
                    #Start.profile.append(self.name)
                    self.clean()
                    self.imgname2,self.size1,self.size2 = 'W1.jpg',500,500
                    self.imageOp()
                    Label(self.win, text='You have successfully Signed-Up\nLets Start Your First shopping',bg='dodger blue', fg='white',font = ('Helvetica' , 13)).place(x=150,y=200)
                    self.btn = Button(self.win, text='Next>>',bg='dark slate gray',fg='snow',font = ('verdana' ,11), command=lambda : Start.shopping(self))
                    self.btn.place(x=230,y=280,height=28,width=78)
            ######Next Button
                ######Function for item display#####
    def loginfn(self):
        self.clean()
        self.imgname,self.size1,self.size2 = 'W3.jpg',500,500
        self.imageOp()
        if self.cond1 is False:
            self.cond1 = True
            #messagebox.showinfo('Error!','No Account with this Information')
            Label(self.win, text='Error!\nPlease Enter valid Username\Password*',bg='red',fg='white',font = ('verdana' , 10)).place(x=160,y=170)
        self.usname2 = Label(self.win,text='User Name:',bg='dark orange',font = ('verdana' , 10))
        self.usname2.place(x=80,y=230)
        self.uspassword2 = Label(self.win,text='Password: ',bg='dark orange',font = ('verdana' , 10))
        self.uspassword2.place(x=80,y=260)
        self.e3 = Entry(self.win,width=40,borderwidth=3)
        self.e3.place(x=170,y=225)
        self.e4 = Entry(self.win,width=40,borderwidth=3)
        self.e4.place(x=170,y=260)
        self.but2 = Button(self.win, text='Log-in',padx=20,pady=30,bg='dark turquoise',font = ('verdana' , 10), command=lambda : self.login())
        self.but2.place(x = 320, y=300 , width = 70, height = 26) 
        Button(self.win, text='Back',bg='dark cyan',fg='white',font = ('verdana' , 10), command=lambda : Start(self.win)).place(x = 160, y=300, height=26,width=70 )

    def login(self):
        self.get4,self.get5 = self.e3.get(),self.e4.get()
        if self.get4=='' or self.get5=='':
            self.cond1 = False
            self.loginfn()
            messagebox.showinfo('Error!','No Account with this Information')
        if self.get4!='' or self.get5!='':
            self.check = False
            with open('Text/signup.txt',"r") as id:
                for i in id: 
                    i=i.rstrip().split('\t')  
                    if(i[0]==self.get4 and i[1]==self.get5):
                        self.check = True  
            if self.check is False:
                self.cond1 = False
                self.loginfn()   
                messagebox.showinfo('Error!','No Account with this Information')

            if self.check is True:
                self.clean()
                self.imgname,self.size1,self.size2 = 'W1.jpg',500,500
                self.imageOp()
                Label(self.win, text='You have successfully Loged-In',bg='dark khaki',fg='black',font = ('Helvetica' , 14)).place(x=130,y=200)
                self.btn = Button(self.win, text='Next>>',bg='dark slate gray',fg='snow',font = ('verdana' ,11), command=lambda : Start.shopping(self))
                self.btn.place(x=230,y=280,height=28,width=78)
            ###########function to display items#######3
            ###########........next button.....#########
    
    def imageOp(self):
        self.img = Image.open(f'Images/{self.imgname}')
        self.img = self.img.resize( (self.size1,self.size2), Image.ANTIALIAS) 
        self.photo1 = ImageTk.PhotoImage( self.img )
        self.label = Label( self.win , image = self.photo1)
        self.label.image = self.photo1
        self.label.pack()
    def shopping(self):
            self.top = Toplevel()
            self.top.title("Sastamall.Pk")
            self.top.iconbitmap('Images/CP-II icon.ico')
            self.top.resizable(0,0)
            self.top.geometry('900x501+30+30')
            NewWin(self.top)     
    def clean(self):
        for i in self.win.winfo_children():
            i.destroy()      
    
class NewWin:
    bill = []
    def __init__(self,top):
        self.top = top
        self.main = True
        self.readfile()

    def readfile(self):
        self.clean()
        self.a, self.b=0,0
        with open(f'Text/Items.txt','r') as file:
            self.x1,self.y1,self.size1,self.size2,self.imgnm = 0,0,950,580,'W2.jpg'
            self.imageplace()
            for i in file:
                self.txt = i.rstrip().split(',')
                self.file2 = self.txt[1]
                #self.filename(self._file2)
                self.bt = Button(self.top, text=f'{self.txt[1]}',padx = 10,bg = 'dark khaki', font = ('verdana' ,11), command=lambda file2=self.file2: self.Items(self.top,file2))
                self.size1,self.size2,self.column1,self.row1,self.imgnm = 120,140,self.a,self.b,f'{self.file2}/{self.file2}'
                self.imageGrid()
                self.bt.grid(column=self.a,row=self.b+1,padx = 10,pady = 15)
                self.a+=1
                if int(self.txt[0])%5==0:
                    self.b+=2
                    self.a=0
            Button(self.top, text=f'Quite',padx=25,pady=3,fg='white', bg = 'crimson', font = ('verdana' ,10,'bold'), command=self.top.quit).grid(column=4,row=self.b+2,padx=5,pady=15)
            if NewWin.bill!=[]:
                #Button(self.top, text='Return to Billing',bg='dark cyan',fg='white',font = ('verdana' , 10), command=lambda : Billing(self.top,False,0,0)).grid(column=3,row=self.b+2,padx=5,pady=20)
                Button(self.top, text='Return to Billing',bg='dark cyan',fg='white',font = ('verdana' , 10), command=lambda : Billing.paymentMtd(self)).grid(column=3,row=self.b+2,padx=5,pady=20)
    class Items:
        def __init__(self,tk,file):
            self.tk = tk
            self.file = file   
            self.itemOpen()     
        def itemOpen(self):
            self.clean()
            self.tk.configure(bg='silver')
            self.fm = Frame(self.tk)
            #self.fm.place(x=0,y=0,height=501,width=900)
            self.mycanv = Canvas(self.fm,height=501,width=900)
            self.mycanv.place(x=0,y=0,height=501,width=900)
            self.yscroll = ttk.Scrollbar(self.fm,orient=VERTICAL,command=self.mycanv.yview)
            self.yscroll.place(x=882,y=0,height=501)
            self.mycanv.configure(yscrollcommand=self.yscroll.set)
            self.mycanv.bind('<Configure>', lambda e: self.mycanv.configure(scrollregion=self.mycanv.bbox('all')))
            self.tk2 = Frame(self.mycanv)
            self.mycanv.create_window((0,0),window=self.tk2, anchor='nw')
            self.fm.place(x=0,y=0,height=501,width=900)
            self.mycanv.configure(bg='lavender')

            self.tk2.configure(bg='lavender')
            
            self.column1, self.row1=0,0
            with open(f'Text/{self.file}.txt','r') as itm:
                for i in itm:
                    self.itm2 = i.rstrip().split(',')
                    self.itm3 = self.itm2[1]
                    self.B1 = Button(self.tk2, text=self.itm2[1], bg = 'sienna',fg='white', font = ('verdana' ,10), command=lambda itm3=self.itm3 : Billing(self.tk,self.file,itm3))
                    self.L1 = Label(self.tk2, text=f'Rs.{self.itm2[2]}', bg = 'light coral', font = ('arial' ,11))
                    if len(self.itm3)>25:
                        c = 1
                        self.size1,self.size2=140,110
                    else:
                        c=30
                        self.size1,self.size2=150,160
                    self.imgnm=f'{self.file}/{self.itm3}'
                    self.tk1 = self.tk2
                    self.imageGrid()
                    self.L1.grid(column=0+self.column1,row=1+self.row1,padx = c ,pady = 3)
                    self.B1.grid(column=0+self.column1,row=2+self.row1,padx = c,pady = 4)
                    self.column1+=1
                    
                    if int(self.itm2[0])%3==0:
                        self.row1+=3
                        self.column1=0
            Button(self.tk2, text='Back',bg='dark cyan',padx = 25,fg='white',font = ('verdana' , 10), command=lambda top=self.tk : NewWin(self.tk)).grid(column=3,row=3+self.row1,padx = 10,pady = 10)

        def  imageGrid(self):
            self.img = Image.open(f'Images/{self.imgnm}.jpg')
            self.img = self.img.resize( (self.size1,self.size2), Image.ANTIALIAS) 
            self.photo3 = ImageTk.PhotoImage( self.img )
            self.label = Label( self.tk1 , image = self.photo3)
            self.label.image = self.photo3
            self.label.grid(column=self.column1,row=self.row1)
        def clean(self):
            for i in self.tk.winfo_children():
                i.destroy()   

    def paymentMtd(self): 
        self.clean()
        self.size1,self.size2,self.x1,self.y1,self.imgnm = 900,501,0,0,'W6.jpg'
        self.imageOp()
        self.main = True
        Label(self.top, text=f'Please tell us your Payment method?', bg='peru', fg='white', font=('Helvetica',14)).place(x=290,y=150)
        Button(self.top, text=f'Cradit/Debit Card',fg='white', bg = 'sea green', font = ('verdana' ,12), command=lambda : self.creditWin()).place(x=200,y=220)
        Button(self.top, text=f'Cash On Delivery',fg='white', bg = 'maroon', font = ('verdana' ,12), command=lambda : self.onDel()).place(x=510,y=220)
    def onDel(self):
        self.clean()
        self.tot = []
        for i in NewWin.bill:
            self.tot.append(i['Total'])
        self.dl = int(((0.5)/100)*sum(self.tot))
        self.imgnm = 'W12.jpg'
        self.imageOp()
        if self.main:
            Label(self.top, text=f'You can pay your total bill of Rs.{(sum(self.tot)+self.dl)} to our delivery boy\nThanks for choosing us:)', bg='olive drab', font=('Helvetica' ,14)).place(x=240,y=150)
        else:
            Label(self.top, text=f'You have paid your total bill of Rs.{(sum(self.tot)+self.dl)}\nThanks for choosing us:)', bg='olive drab', font=('Helvetica' ,14)).place(x=290,y=150)
        Label(self.top, text=f'Rs.{self.dl}(0.5% of bill) is added as Delivery charges', bg='light steel blue', font=('Helvetica' ,12)).place(x=290,y=230)
        Button(self.top, text=f'Proceed to receipt',fg='white', bg = 'sea green', font = ('verdana' ,13), command=lambda : self.showbill()).place(x=360,y=280,height=30)     

    def creditWin(self):
        self.clean()
        self.imgnm = 'W8.jpg'
        self.imageOp()
        Label(self.top, text='Please Enter Cradit Card No.:', bg='dark khaki', font=('Courier' ,13)).place(x=80,y=200)
        self.num = Entry(self.top,width=50,borderwidth=3)
        self.num.place(x=400,y=200)
        Label(self.top, text='Please Enter Key.:', bg='dark khaki', font=('Courier' ,13)).place(x=80,y=240)
        self.pin = Entry(self.top,width=50,borderwidth=3)
        self.pin.place(x=400,y=240)
        Button(self.top, text=f'Ok',fg='white', bg = 'orange', font = ('verdana' ,13), command=lambda : self.entry()).place(x=320,y=290,height=26,width=75)
        Button(self.top, text='Back',bg='dark cyan',fg='white',font = ('verdana' , 10), command=lambda : self.paymentMtd()).place(x = 200, y=290, height=26,width=75 )
    def entry(self):
        self.y = self.num.get()
        self.z = self.pin.get()
        self.credit()

    def credit(self):
        self.clean()
        self.size1 = 1000
        self.imgnm = 'W9.jpg'
        self.imageOp()
        x=False
        cinfo = open('Text/cradit#.txt','r')
        for i in cinfo:
            i = i.rstrip().split(',')
            if(self.y==(i[0]) and self.z==(i[1])):
                x= True
        if x is True:
            self.main = False
            Label(self.top, text='Your Account verification is done', bg='hot pink', font=('Helvetica' ,14)).place(x=290,y=160)
            Button(self.top, text=f'Ok',fg='white', bg = 'sandy brown', font = ('verdana' ,13), command=lambda : self.onDel()).place(x=350,y=240,height=26,width=70)     
        if x is False:
            Label(self.top, text='You Entered Wrong Information\nPlease Enter again:)', bg='orange red', fg='white', font=('Helvetica' ,14)).place(x=290,y=160)
            Button(self.top, text=f'Again',fg='white', bg = 'dark violet', font = ('verdana' ,12), command=lambda : self.creditWin()).place(x=230,y=250,height=30,width=80)
            Button(self.top, text=f'Change Payement Method',fg='white', bg = 'crimson', font = ('verdana' ,12), command=lambda : self.paymentMtd()).place(x=400,y=250)
            
    def showbill(self):
        self.clean()
        self.top.configure(bg='dark gray')
        self.size1 = 900
        self.imgnm = 'W11.jpg'
        self.imageplace()
        Label(self.top, text="Product",bg='indigo',fg='white',font=('Helvetica' ,12)).grid(column=0,row=0,padx=13)
        Label(self.top, text="Quantity",bg='indigo',fg='white',font=('Helvetica' ,12)).grid(column=1,row=0,padx=13)
        Label(self.top, text="Price of each",bg='indigo',fg='white',font=('Helvetica' ,12)).grid(column=2,row=0,padx=13)
        Label(self.top, text="Total Price",bg='indigo',fg='white',font=('Helvetica' ,12)).grid(column=3,row=0,padx=13)
        self.total = []
        x = 1
        for i in NewWin.bill:
            self.total.append((i['Total']))
            Label(self.top,text=i['Product'],font=('arial' ,10)).grid(column=0,row=x, padx=15,pady=3)
            Label(self.top,text=i['Quantity'],font=('arial' ,10)).grid(column=1,row=x,padx=15,pady=3)
            Label(self.top,text=i['Price'],font=('arial' ,10)).grid(column=2,row=x,padx=15,pady=3)
            Label(self.top,text=(i['Total']),font=('arial' ,10)).grid(column=3,row=x,padx=15,pady=3)
            x+=1 
        Label(self.top,text=f'{sum(self.total)}+{self.dl}',bg = 'tan',font=('Courier' ,11)).grid(column=3,row=1+x,padx=15,pady=5)
        Label(self.top,text=f'(+0.2% Delivey Charges)',bg = 'tan',font=('Courier' ,10)).grid(column=4,row=1+x,padx=15,pady=5)
        Label(self.top,text=f'Total = {(sum(self.total))+(self.dl)}',bg = 'dark orange',font=('Courier' ,12)).grid(column=3,row=2+x,padx=15,pady=5)
        
        Button(self.top, text=f'Contnue Shopping',fg='white', bg = 'dark orange', font = ('verdana' ,10), command=lambda : NewWin(self.top)).grid(column=2,row=3+x,padx=10,pady=5)
        Button(self.top, text=f'Quite',fg='white',padx=15,pady=5, bg = 'crimson', font = ('verdana' ,10,'bold'), command=self.top.quit).grid(column=4,row=3+x,padx=20,pady=5)
        Button(self.top, text=f'Cancel Order',fg='white', bg = 'orange red', font = ('verdana' ,10), command=lambda : self.cntShopping()).grid(column=3,row=4+x,padx=10,pady=5)

    def cntShopping(self):
        self.clean()
        self.top.configure(bg='black')
        self.imgnm = 'W10.jpg'
        self.imageOp()
        NewWin.bill = []
        Label(self.top, text=f'Your previous Order is CNACELED', bg='orange red',fg='white', font=('Helvetica',13)).place(x=270,y=100)
        Label(self.top, text=f'Do You want to Start New shoping?', bg='gold', fg='black', font=('Helvetica',13)).place(x=270,y=240)
        Button(self.top, text=f'Yes',fg='black', bg = 'yellow green', font = ('verdana' ,11), command=lambda : NewWin(self.top)).place(x=300,y=300, height=30,width=75)
        Button(self.top, text=f'Quite',fg='white', bg = 'crimson', font = ('verdana' ,10,'bold'), command= self.top.quit).place(x=440,y=300,height=30,width=75) 


    def imageplace(self):
        self.img = Image.open(f'Images/{self.imgnm}')
        self.img = self.img.resize( (self.size1,self.size2), Image.ANTIALIAS) 
        self.photo2 = ImageTk.PhotoImage( self.img )
        self.label = Label( self.top , image = self.photo2)
        self.label.image = self.photo2
        self.label.place(x=self.x1,y=self.y1)
    def  imageGrid(self):
        self.img = Image.open(f'Images/{self.imgnm}.jpg')
        self.img = self.img.resize( (self.size1,self.size2), Image.ANTIALIAS) 
        self.photo3 = ImageTk.PhotoImage( self.img )
        self.label = Label( self.top , image = self.photo3)
        self.label.image = self.photo3
        self.label.grid(column=self.column1,row=self.row1)
    def imageOp(self):
        self.img = Image.open(f'Images/{self.imgnm}')
        self.img = self.img.resize( (self.size1,self.size2), Image.ANTIALIAS) 
        self.photo1 = ImageTk.PhotoImage( self.img )
        self.label = Label( self.top , image = self.photo1)
        #label.image = photo1
        self.label.pack()
    def clean(self):
        for i in self.top.winfo_children():
            i.destroy() 

class Billing(NewWin):
    def __init__(self,tk,itemname1,product):
        super().__init__(tk)
        #self.top = tk
        self.itemname1 = itemname1
        self.product = product
        self.t = StringVar()
        self.Amount = 0
        self.Quantityfn()
        
    def Quantityfn(self):
        self.clean()
        self.size1,self.size2,self.x1,self.y1,self.imgnm=900,501,0,0,'W4.jpg'
        self.imageOp()
        if not self.main:
            self.main = False
            Label(self.top, text='You Entered WRONG Entry', bg='orange red', fg='white', font=('Helvetica' ,13)).place(x=240,y=130)
            
        
        Label(self.top, text=f'You have selected \"{self.product}\"',fg='black', bg='light gray', font=('Courier' ,12)).place(x=220,y=70)
        Label(self.top, text='Please Enter Quantity:',fg='white', bg='saddle brown', font=('Courier' ,12)).place(x=130,y=200)
        self.en = Entry(self.top,width=40,borderwidth=3)
        self.en.place(x=370,y=200)
        
        Button(self.top, text=f'Ok',fg='white', bg = 'sandy brown', font = ('verdana' ,10), command=lambda : self.QnFnChk()).place(x=270,y=250,height=25,width=70)
        Button(self.top, text='Back',bg='dark cyan',fg='white',font = ('verdana' , 10), command=lambda : NewWin.Items(self.top,self.itemname1)).place(x = 170, y=250, height=25,width=70 )


    def QnFnChk(self):
        numeric=False
        for i in self.en.get():
            if not i.isnumeric() or not i.isdigit():
                numeric= True
        if self.en.get()=='' or numeric:
            self.main = False
            self.Quantityfn()
        if self.en.get()!='' and not numeric:
            if (int(self.en.get()))/2!=0:
                self.t.set(self.en.get())
                self.Amount+=int(self.t.get())
                self.billing()
            else:
                self.main = False
                self.Quantityfn()

    def billing(self):
        self.clean()
        self.imgnm='W7.jpg'
        self.imageOp()
        with open(f"Text/{self.itemname1}.txt",'r') as thing:
            for i in thing:
                i = i.rstrip().split(",")
                if i[1] == self.product:
                    self.billdic={'Sr. No.':i[0],'Product':i[1],'Price':i[2], 'Total':((self.Amount)*int(i[2])), 'Quantity':self.Amount}
                    NewWin.bill.append(self.billdic)
                    self.tl = sum([int(i['Total']) for i in NewWin.bill])
                    Label(self.top, text=f'{(self.Amount)} piece(s) of \"{i[1]}\" is added to cart', bg='light Gray', font=('Courier' ,12)).place(x=200,y=100)
                    Label(self.top, text=f'You have done {self.tl} Ruppees shopping', bg='dark khaki', font=('Courier' ,12)).place(x=250,y=130)
                    Label(self.top, text=f'Do You want to continue your shoping?', bg='gold', fg='black', font=('Helvetica',13)).place(x=280,y=200)
                    Button(self.top, text=f'Yes',fg='black', bg = 'yellow green', font = ('verdana' ,13), command=lambda : NewWin(self.top)).place(x=330,y=240, height=25,width=70)
                    Button(self.top, text=f'No',fg='black', bg = 'medium sea green', font = ('verdana' ,13), command=lambda : self.paymentMtd()).place(x=460,y=240,height=25,width=70)
                    Button(self.top, text=f'Cancel Order',fg='white', bg = 'tomato', font = ('verdana' ,11), command=lambda : self.cntShopping()).place(x=370,y=300)

root = Tk()

root.title("Sastamall.Pk")
root.iconbitmap('Images/CP-II icon.ico')
root.resizable(0,0)
root.geometry('500x500+40+40')

s = Start(root)

mainloop()