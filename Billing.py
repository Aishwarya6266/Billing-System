from tkinter import *
import math,random
import os
import mysql.connector

class Billing:
    def __init__(self,root):    #root is name of bill window
        self.root=root  #initialize root
        self.root.geometry("1610x790+0+0") #root window will get geometry as "lxb" 0 is x & y co-ordinator as window starts from initial
        self.root.title("Billing System") #title to root window bydefault it is 'tk'
        bg_color="#074463" #set background color
        title=Label(self.root,text="Billing System",bd=12,relief=GROOVE,bg=bg_color,fg='white',font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

        #============================Variables=====================================================
        self.green_gram = IntVar()
        self.Red = IntVar()
        self.black = IntVar()
        self.Mustard = IntVar()
        self.Cumin = IntVar()
        self.Ground = IntVar()
        self.salt = IntVar()
        self.Sugar = IntVar()
        self.Rice = IntVar()
        self.wheat = IntVar()
        self.Gram = IntVar()
        self.Corn = IntVar()
        self.Cinnamon = IntVar()
        self.Clove = IntVar()
        self.cashew = IntVar()
        self.vege = IntVar()
        self.onion = IntVar()
        self.jaggery = IntVar()

        self.Cost = StringVar()
        self.Tax = StringVar()

        self.cname = StringVar()
        self.cmobile = StringVar()
        self.cbill = StringVar()
        x=random.randint(100,9999)
        self.cbill.set(str(x))


        # Customers Details
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.cname,font=("arial",15),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        cmobile_lbl = Label(F1, text="Mobile No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cmobile_txt = Entry(F1, width=20,textvariable=self.cmobile, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0, column=3,padx=10,pady=5)
        cbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=20,textvariable=self.cbill, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0, column=5,padx=10,pady=5)



        #========================Grocery item Details================================================
        F2=LabelFrame(self.root,bd=10,text="Grocery Items",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        green_gram_lbl=Label(F2,text="Green Gram",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        green_gram_txt=Entry(F2,width=10,textvariable=self.green_gram,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=0,column=1,padx=10,pady=10)
        Red_gram_lbl=Label(F2,text="Red Gram",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Red_gram_txt=Entry(F2,width=10,textvariable=self.Red,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=1,column=1,padx=10,pady=10)
        Black_gram_lbl=Label(F2,text="Black Gram",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Black_gram_txt=Entry(F2,width=10,textvariable=self.black,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=2,column=1,padx=10,pady=10)
        Mustard_lbl=Label(F2,text="Mustard Seed",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Mustard_txt=Entry(F2,width=10,textvariable=self.Mustard,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=3,column=1,padx=10,pady=10)
        Cumin_lbl=Label(F2,text="Cumin",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Cumin_txt=Entry(F2,width=10,textvariable=self.Cumin,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=4,column=1,padx=10,pady=10)
        GroundNuts_lbl=Label(F2,text="Ground nuts",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        GroundNuts_txt=Entry(F2,width=10,textvariable=self.Ground,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=5,column=1,padx=10,pady=10)

        # ========================Grocery item Details================================================
        F3 = LabelFrame(self.root, bd=10, text="Grocery Items", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F3.place(x=345, y=180, width=325, height=380)
        Salt_lbl=Label(F3,text="Salt",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Salt_txt=Entry(F3,width=10,textvariable=self.salt,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=0,column=1,padx=10,pady=10)
        Sugar_lbl=Label(F3,text="Sugar",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Sugar_txt=Entry(F3,width=10,textvariable=self.Sugar,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=1,column=1,padx=10,pady=10)
        Rice_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Rice_txt=Entry(F3,width=10,textvariable=self.Rice,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=2,column=1,padx=10,pady=10)
        Wheat_lbl=Label(F3,text="Wheat",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=3,column=1,padx=10,pady=10)
        Gram_flour_lbl=Label(F3,text="Gram flour",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Gram_flour_txt=Entry(F3,width=10,textvariable=self.Gram,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=4,column=1,padx=10,pady=10)
        Corn_flour_lbl=Label(F3,text="Corn Flour",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Corn_flour_txt=Entry(F3,width=10,textvariable=self.Corn,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=5,column=1,padx=10,pady=10)

        #=========================================Grocery Items=======================================================
        F4 = LabelFrame(self.root, bd=10, text="Grocery Items", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F4.place(x=690, y=180, width=325, height=380)
        Cinnamon_lbl=Label(F4,text="Cinnamon",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Cinnamon_txt=Entry(F4,width=10,textvariable=self.Cinnamon,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=0,column=1,padx=10,pady=10)
        Clove_lbl=Label(F4,text="Clove",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Clove_txt=Entry(F4,width=10,textvariable=self.Clove,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=1,column=1,padx=10,pady=10)
        cashew_lbl=Label(F4,text="Cashew",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        cashew_txt=Entry(F4,width=10,textvariable=self.cashew,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=2,column=1,padx=10,pady=10)
        Vege_lbl=Label(F4,text="Vegetable Oil",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Vege_txt=Entry(F4,width=10,textvariable=self.vege,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=3,column=1,padx=10,pady=10)
        Onion_lbl=Label(F4,text="Onion",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Onion_txt=Entry(F4,width=10,textvariable=self.onion,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=4,column=1,padx=10,pady=10)
        jaggery_lbl=Label(F4,text="Jaggery",font=("times new roman",15,"bold"),bg=bg_color,fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        jaggery_txt=Entry(F4,width=10,textvariable=self.jaggery,font=("times new roman",15,"bold"),relief=SUNKEN,bd=5).grid(row=5,column=1,padx=10,pady=10)

        #============================================Billing area=======================================================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1060,y=180,width=420,height=380)
        bill_title=Label(F5,text="Bill page",font=("arial", 15, "bold"),bd=7,relief=GROOVE).pack(fill=X)
        #===Scroll bar========
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #==================================Bill Button========================================================
        F6=LabelFrame(self.root, bd=10, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F6.place(x=0, y=565, relwidth=1, height=140)
        m1=Label(F6,text="Total Grocery Cost:",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,sticky="w")
        m1_txt=Entry(F6,width=13,textvariable=self.Cost,font=("times new roman",18,"bold"),relief=SUNKEN,bd=5).grid(row=0,column=1,padx=20,pady=20)
        c1 = Label(F6, text="Total Grocery Tax:", font=("times new roman", 18, "bold"), bg=bg_color, fg="white").grid(row=0, column=3, sticky="w")
        c1_txt = Entry(F6, width=13,textvariable=self.Tax, font=("times new roman", 18, "bold"), relief=SUNKEN, bd=5).grid(row=0, column=4,padx=20, pady=20)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=850,width=650,height=105)

        total_btn=Button(btn_F,text="Total",command=self.total,width=11,font=("arial",14,"bold"),pady=15,bg="cadetblue",fg="white").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,width=11,font=("arial",14,"bold"),pady=15,bg="cadetblue",fg="white").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.Clear_Bill,width=11,font=("arial",14,"bold"),pady=15,bg="cadetblue",fg="white").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.Exit_screen,width=11,font=("arial",14,"bold"),pady=15,bg="cadetblue",fg="white").grid(row=0,column=3,padx=5,pady=5)
        self.wel_bill()

        F7=Label(self.root, bd=10, text="!!!!!Visit Again!!!!!", font=("times new roman", 18, "bold"), fg="gold",bg="Black")
        F7.place(x=0, y=710, relwidth=1, height=80)
        F7.config(anchor=CENTER)

        #======================================Cost Calculation================================================

    def total(self):
        #Assinging a variable to every single product to calculate its cost
        self.a=self.green_gram.get() * 75
        self.b=self.Red.get() * 65
        self.c=self.black.get() * 70
        self.d=self.Mustard.get() * 20
        self.e=self.Cumin.get() * 25
        self.f=self.Ground.get() * 75
        self.g=self.salt.get() * 20
        self.h=self.Sugar.get() * 45
        self.i=self.Rice.get() * 80
        self.j=self.wheat.get() * 65
        self.k=self.Gram.get() * 25
        self.l=self.Corn.get() * 30
        self.m=self.Cinnamon.get() * 45
        self.n=self.Clove.get() * 40
        self.o=self.cashew.get() * 150
        self.p=self.vege.get() * 750
        self.q=self.onion.get() * 25
        self.r=self.jaggery.get() * 40
        self.Total_cost =float (
                 self.a+
                 self.b+
                 self.c+
                 self.d+
                 self.e+
                 self.f+
                 self.g+
                 self.h+
                 self.i+
                 self.j+
                 self.k+
                 self.l+
                 self.m+
                 self.n+
                 self.o+
                 self.p+
                 self.q
                )
        self.Cost.set("Rs."+str(self.Total_cost))
        self.Tax_calc=0.03*self.Total_cost
        self.Tax.set("Rs."+str(self.Tax_calc))
        self.Total_Bill=float(self.Tax_calc+self.Total_cost)

    def wel_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t Welcome Grocery Shop")
        self.txtarea.insert(END,f"\n Bill Number:{self.cbill.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.cname.get()}")
        self.txtarea.insert(END,f"\n Contact Number:{self.cmobile.get()}")
        self.txtarea.insert(END,"\n***********************************************")
        self.txtarea.insert(END,"\nPRODUCT\t\tQTY\t\tPRICE")
        self.txtarea.insert(END, "\n***********************************************")

    def bill_area(self):
        self.wel_bill()
        # If we want to execute multiple if conditions or all if conditions then write if after if
        # Don't use elif bcoz it execute single condition among all conditional stm.
        if self.green_gram.get()!=0:
            self.txtarea.insert(END,f"\nGreen Gram\t\t{self.green_gram.get()}\t\t{self.a}")
        if self.Red.get()!=0:
            self.txtarea.insert(END,f"\nRed Gram\t\t{self.Red.get()}\t\t{self.b}")
        if self.black.get()!=0:
            self.txtarea.insert(END,f"\nBlack Gram\t\t{self.black.get()}\t\t{self.c}")
        if self.Mustard.get()!=0:
            self.txtarea.insert(END,f"\nMustard seed\t\t{self.Mustard.get()}\t\t{self.d}")
        if self.Cumin.get()!=0:
            self.txtarea.insert(END,f"\nCumin\t\t{self.Cumin.get()}\t\t{self.e}")
        if self.Ground.get()!=0:
            self.txtarea.insert(END,f"\nGround Nuts\t\t{self.Ground.get()}\t\t{self.f}")
        if self.salt.get()!=0:
            self.txtarea.insert(END,f"\nsalt\t\t{self.salt.get()}\t\t{self.g}")
        if self.Sugar.get()!=0:
            self.txtarea.insert(END,f"\nSugar\t\t{self.Sugar.get()}\t\t{self.h}")
        if self.Rice.get()!=0:
            self.txtarea.insert(END,f"\nRice\t\t{self.Rice.get()}\t\t{self.i}")
        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t\t{self.j}")
        if self.Gram.get()!=0:
            self.txtarea.insert(END,f"\nGram Flour\t\t{self.Gram.get()}\t\t{self.k}")
        if self.Corn.get()!=0:
            self.txtarea.insert(END,f"\nCorn Flour\t\t{self.Corn.get()}\t\t{self.l}")
        if self.Cinnamon.get()!=0:
            self.txtarea.insert(END,f"\nCinnamon\t\t{self.Cinnamon.get()}\t\t{self.m}")
        if self.Clove.get()!=0:
            self.txtarea.insert(END,f"\nClove\t\t{self.Clove.get()}\t\t{self.n}")
        if self.cashew.get()!=0:
            self.txtarea.insert(END,f"\nCashew\t\t{self.cashew.get()}\t\t{self.o}")
        if self.vege.get()!=0:
            self.txtarea.insert(END,f"\nVegetable Oil\t\t{self.vege.get()}\t\t{self.p}")
        if self.onion.get()!=0:
            self.txtarea.insert(END,f"\nOnion\t\t{self.onion.get()}\t\t{self.q}")
        if self.jaggery.get()!=0:
            self.txtarea.insert(END,f"\nJaggery\t\t{self.jaggery.get()}\t\t{self.r}")

        #Print Total calculated cost and tax on Generated Bill page
        self.txtarea.insert(END,"\n--------------------------------------------")
        if self.Tax.get()!="Rs.0.0":    #as Tax variable is StringVar
            self.txtarea.insert(END,f"\nTotal grocery tax:\t\t{self.Tax.get()}")
        self.txtarea.insert(END,f"\nTotal Grocery Cost:\t\t{self.Cost.get()}")
        self.txtarea.insert(END,f"\nTotal Bill:\t\tRs.{self.Total_Bill}")
        self.txtarea.insert(END, "\n-------------------------------------------")
        self.txtarea.insert(END,"\n\nTHANK YOU VISIT AGAIN")
        self.save_bill()  #when we click on generate bill it will save bill also

    ###############save Bill in Billnumber format by using file handling######################
    def save_bill(self):
        try:
            self.bill_data=self.txtarea.get('1.0',END)
            with open(os.path.join("D:\Python_Internship\Billing_System\Custmer_Bill",str(self.cbill.get())+".txt"),"w") as fh:
                fh.write(self.bill_data)
        except Exception as e:
            print(e)


    #####################Clear Billl area ##########################################
    def Clear_Bill(self):
        self.green_gram.set(0)
        self.Red.set(0)
        self.black.set(0)
        self.Mustard.set(0)
        self.Cumin.set(0)
        self.Ground.set(0)
        self.salt.set(0)
        self.Sugar.set(0)
        self.Rice.set(0)
        self.wheat.set(0)
        self.Gram.set(0)
        self.Corn.set(0)
        self.Cinnamon.set(0)
        self.Clove.set(0)
        self.cashew.set(0)
        self.vege.set(0)
        self.onion.set(0)
        self.jaggery.set(0)

        self.Cost.set("")
        self.Tax.set("")

        self.cname.set("")
        self.cmobile.set("")
        self.cbill.set("")
        x = random.randint(100, 9999)
        self.cbill.set(str(x))
        self.wel_bill()

    def Exit_screen(self):
        self.root.destroy()

##########################DataBase Work######################################################
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="aish@1999", database="billing_db")
        self.mycursor = self.mydb.cursor()
        name=self.cname
        phone=self.cmobile
        bill=self.cbill
        self.mycursor.callproc("put_C_details",(name,phone,bill))
        self.mydb.commit()
        self.Getdata()

    def Getdata(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="aish@1999", database="billing_db")
        self.mycursor = self.mydb.cursor()
        self.mycursor.callproc("get_C_details")
        for result in self.mycursor.stored_results():
            print(result.fetchall())
        self.mydb.commit()

root=Tk()
obj=Billing(root)
root.mainloop()

