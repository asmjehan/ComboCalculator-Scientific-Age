from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Combo Calculator")
root.configure(background = "black")
root.resizable(width= False,height=False)
root.geometry("360x410+0+0")

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = ()
        self.current= ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self,num): 
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)


    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

        
    def display(self,value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)


    def valid_function(self):
        if self.op =="add":
            self.total += self.current
        if self.op =="sub":
            self.total -= self.current
        if self.op =="multi":
            self.total *= self.current
        if self.op =="divide":
            self.total /= self.current
        if self.op =="mod":
            self.total %= self.current
        if self.op=="inv":
            self.total=1/self.current            
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
            
    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum     = True
        self.op = op
        self.result = False



    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)

    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)
        
    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)


    def Clear_Entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

        
    def mathsPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result=False
        self.current=math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
        
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def degrees(self):
        self.result=False
        self.current=math.degrees(float(txtDisplay.get()))
        self.display(self.current)        
        
    def log(self):
        self.result=False
        self.current=math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result=False
        self.current=math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result=False
        self.current=math.log10(float(txtDisplay.get()))
        self.display(self.current)
        
#----------------------Age functions-----------------------------------------------------
def clearAll() :
    # deleting the content from the entry box 
    dayField.delete(0, END) 
    monthField.delete(0, END) 
    yearField.delete(0, END) 
    givenDayField.delete(0, END) 
    givenMonthField.delete(0, END) 
    givenYearField.delete(0, END) 
    rsltDayField.delete(0, END) 
    rsltMonthField.delete(0, END) 
    rsltYearField.delete(0, END)

    
def checkError() : 

    # if any of the entry field is empty 
    # then show an error message and clear 
    # all the entries 
    if (dayField.get() == "" or monthField.get() == "" 
            or yearField.get() == "" or givenDayField.get() == "" 
            or givenMonthField.get() == "" or givenYearField.get() == "") : 

            # show the error message 
            messagebox.showerror("Input Error") 

            # clearAll function calling 
            clearAll() 
            
            return -1

def calculateAge():
    # check for error 
    value = checkError() 

    # if error is occur then return 
    if value == -1 : 
            return
    
    else :	
        # take a value from the respective entry boxes 
        # get method returns current text as string 
        birth_day = int(dayField.get()) 
        birth_month = int(monthField.get()) 
        birth_year = int(yearField.get()) 

        given_day = int(givenDayField.get()) 
        given_month = int(givenMonthField.get()) 
        given_year = int(givenYearField.get()) 
        
        
        # if birth date is greater then given birth_month 
        # then donot count this month and add 30 to the date so 
        # as to subtract the date and get the remaining days 
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        
        if (birth_day > given_day): 
                given_month = given_month - 1
                given_day = given_day + month[birth_month-1] 
                                
                                
        # if birth month exceeds given month, then 
        # donot count this year and add 12 to the 
        # month so that we can subtract and find out 
        # the difference 
        if (birth_month > given_month): 
                given_year = given_year - 1
                given_month = given_month + 12
                                
        # calculate day, month, year 
        calculated_day = given_day - birth_day; 
        calculated_month = given_month - birth_month; 
        calculated_year = given_year - birth_year; 

        # calculated day, month, year write back 
        # to the respective entry boxes 

        # insert method inserting the 
        # value in the text entry box. 
        
        rsltDayField.insert(10, str(calculated_day)) 
        rsltMonthField.insert(10, str(calculated_month)) 
        rsltYearField.insert(10, str(calculated_year)) 	    

        




        
added_value = Calc()           

txtDisplay = Entry(calc, font=("ariel",20,"bold"), bd=30, width=20,justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=4, height = 1,font=("ariel",20,"bold"),
                          bd=4,text = numberpad[i]))
        btn[i].grid(row = j, column=k, pady =1)
        btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)

        i=i+1

#####------------------------Normal-------------------------------#####
btnClear = Button(calc, text="C",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4, command= added_value.Clear_Entry).grid(row=1,column=0,pady=1)

btnAllClear = Button(calc, text="CE",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command= added_value.all_Clear_Entry).grid(row=1,column=1,pady=1)

btnSqr = Button(calc, text="√",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command= added_value.squared).grid(row=1,column=2,pady=1)

btnAdd = Button(calc, text="+",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = lambda: added_value.operation("add")).grid(row=1,column=3,pady=1)


btnSub = Button(calc, text="-",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = lambda: added_value.operation("sub")).grid(row=2,column=3,pady=1)

btnMul = Button(calc, text="*",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = lambda: added_value.operation("multi")).grid(row=3,column=3,pady=1)

btnDiv = Button(calc, text="÷",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = lambda: added_value.operation("divide")).grid(row=4,column=3,pady=1)

btnEqual = Button(calc, text="=",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4, command = added_value.sum_of_total).grid(row=5,column=3,pady=1)


btnZero = Button(calc, text="0",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = lambda: added_value.numberEnter(0)).grid(row=5,column=0,pady=1)

btnDot = Button(calc, text=".",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = lambda: added_value.numberEnter(".")).grid(row=5,column=1,pady=1)

btnPM = Button(calc, text = chr(177),width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command= added_value.mathsPM).grid(row=5,column=2,pady=1)

#####---------------Scientific Calculator-------------######
btnPi = Button(calc, text="π",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4, command = added_value.pi).grid(row=1,column=4,pady=1)

btnCos = Button(calc, text="cos",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4, command = added_value.cos).grid(row=2,column=4,pady=1)

btnSin = Button(calc, text="sin",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.sin).grid(row=3,column=4,pady=1)

btnTan = Button(calc, text="tan",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.tan).grid(row=4,column=4,pady=1)

btnMod = Button(calc, text="Mod",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command=lambda:added_value.operation("mod")).grid(row=5,column=4,pady=1)



btn2Pi = Button(calc, text="2π",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.tau).grid(row=1,column=5,pady=1)

btnCosh = Button(calc, text="cosh",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.cosh).grid(row=2,column=5,pady=1)

btnSinh = Button(calc, text="sinh",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.sinh).grid(row=3,column=5,pady=1)

btnTanh = Button(calc, text="tanh",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.tanh).grid(row=4,column=5,pady=1)

btnLog = Button(calc, text="log",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.log).grid(row=5,column=5,pady=1)



btnE = Button(calc, text="e",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.e).grid(row=1,column=6,pady=1)

btnDeg = Button(calc, text="deg",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.degrees).grid(row=2,column=6,pady=1)

btnInverse = Button(calc, text="x^-1",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command=lambda:added_value.operation("inv")).grid(row=3,column=6,pady=1)

btnLog10 = Button(calc, text="log10",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.log10).grid(row=4,column=6,pady=1)

btnLog2 = Button(calc, text = "log2",width=4, height = 1,font=("ariel",20,"bold"),
                  bd=4,command = added_value.log2).grid(row=5,column=6,pady=1)


#####---------------Age caculator-------------######

#Create a Date Of Birth : label 
dob = Label(calc, text = "Date Of Birth", bg = "powder blue") 

# Create a Given Date : label 
givenDate = Label(calc, text = "Given Date", bg = "powder blue") 

# Create a Day : label 
day = Label(calc, text = "Day", bg = "light green") 

# Create a Month : label 
month = Label(calc, text = "Month", bg = "light green") 

# Create a Year : label 
year = Label(calc, text = "Year", bg = "light green") 

# Create a Given Day : label 
givenDay = Label(calc, text = "Given Day", bg = "light green") 

# Create a Given Month : label 
givenMonth = Label(calc, text = "Given Month", bg = "light green") 

# Create a Given Year : label 
givenYear = Label(calc, text = "Given Year", bg = "light green") 

# Create a Years : label 
rsltYear = Label(calc, text = "Years", bg = "light green") 

# Create a Months : label 
rsltMonth = Label(calc, text = "Months", bg = "light green") 

# Create a Days : label 
rsltDay = Label(calc, text = "Days", bg = "light green") 

# Create a Resultant Age Button and attached to calculateAge function 
resultantAge = Button(calc, text = "Resultant Age", fg = "Black", bg = "Red", command = calculateAge) 

# Create a Clear All Button and attached to clearAll function 
clearAllEntry = Button(calc, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)

author = Label(calc, text = "asmjehan@gmail.com") 



# Create a text entry box for filling or typing the information. 
dayField = Entry(calc) 
monthField = Entry(calc) 
yearField = Entry(calc) 

givenDayField = Entry(calc) 
givenMonthField = Entry(calc) 
givenYearField = Entry(calc) 

rsltYearField = Entry(calc) 
rsltMonthField = Entry(calc) 
rsltDayField = Entry(calc) 


# grid method is used for placing 
# the widgets at respective positions 
# in table like structure . 
dob.grid(row = 0, column = 8,pady=1) 

day.grid(row = 1, column = 7,pady=1) 
dayField.grid(row = 1, column = 8,pady=1) 

month.grid(row = 2, column = 7,pady=1) 
monthField.grid(row = 2, column = 8,pady=1) 

year.grid(row = 3, column = 7,pady=1) 
yearField.grid(row = 3, column = 8,pady=1) 

givenDate.grid(row = 0, column = 11,pady=1) 

givenDay.grid(row = 1, column = 10,pady=1) 
givenDayField.grid(row = 1, column = 11,pady=1) 

givenMonth.grid(row = 2, column = 10,pady=1) 
givenMonthField.grid(row = 2, column = 11,pady=1) 

givenYear.grid(row = 3, column = 10,pady=1) 
givenYearField.grid(row = 3, column = 11,pady=1) 

resultantAge.grid(row = 4, column = 9,pady=1) 

rsltYear.grid(row = 5, column = 9,pady=1) 
rsltYearField.grid(row = 6, column = 9,pady=1) 

rsltMonth.grid(row = 7, column = 9,pady=1) 
rsltMonthField.grid(row = 8, column = 9,pady=1) 

rsltDay.grid(row = 9, column = 9,pady=1) 
rsltDayField.grid(row = 10, column = 9,pady=1) 

clearAllEntry.grid(row = 12, column = 9,pady=1)

author.grid(row=12,column=7,pady=1)
#####-----------------Menu----------------------------######

def iExit():
    iExit = tkinter.messagebox.askyesno("Combo Calculator","Confirm Exit")
    if iExit > 0:
        root.destroy()
        return

def cHelp():
    cHelp = tkinter.messagebox.showinfo("Info","Just Click :) ")

def Scientific():
    root.resizable(width= False,height=False)
    root.geometry("610x410+0+0")

def Standard():
    root.resizable(width= False,height=False)
    root.geometry("360x410+0+0")
    
def AgeCalc():
    root.resizable(width= False,height=False)
    root.geometry("1185x545+0+0")
    	
    

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label= "File",menu=filemenu)
filemenu.add_command(label= "Standard", command = Standard)
filemenu.add_command(label= "Scientific", command = Scientific)
filemenu.add_command(label= "All (Age+Scientific)", command = AgeCalc)
filemenu.add_separator()
filemenu.add_command(label= "Exit", command = iExit)


helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Help",menu= helpmenu)
helpmenu.add_command(label= "View Help", command= cHelp)

root.config(menu=menubar)
root.mainloop()
