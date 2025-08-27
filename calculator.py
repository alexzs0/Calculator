import tkinter as tk
import re
#Setting the GUI up of title and the geometry
class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.geometry('380x310')
        #Ensureing the frame sticks to the bottom
        self.root.rowconfigure(0,weight = 1) #top row will expand 
        self.root.rowconfigure(1,weight = 0) #bottom row will stay in place
        self.root.columnconfigure(1, weight = 1) #the column would expand

        #Adding the display of the calculator 
        self.field = tk.Text(self.root, height = 2 , width = 21, font = ('Arial', 24))
        self.field.grid(row = 0, column = 0 , sticky = 'nswe')

        #Adding all the buttons
        self.buttonFrame = tk.Frame(self.root) #Constructs a grid/frame for the calculator
        self.buttonFrame.columnconfigure(0,weight =1)#These will construct each individual columns for the calcultor
        self.buttonFrame.columnconfigure(1,weight =1)
        self.buttonFrame.columnconfigure(2,weight =1)
        self.buttonFrame.columnconfigure(3,weight =1)#When weight is 0, it stays fixed and when it is 1 it expands

        self.btnClear = tk.Button(self.buttonFrame,text = 'AC', font = ('Arial', 18), command = self.clearField) #When command = lambda it means that it is only activated when clicked 
        self.btnClear.grid(column = 0, row = 0 ,sticky = 'snwe')
        self.btnNeg_Pos = tk.Button(self.buttonFrame,text = '+/-', font = ('Arial', 18), command = self.invert) #When no brackets, only executes when pressed, with brackets program runs straight away 
        self.btnNeg_Pos.grid(column = 1, row = 0 ,sticky = 'snwe')
        self.btnPercent = tk.Button(self.buttonFrame,text = '%', font = ('Arial', 18), command = lambda : self.addToField('%'))
        self.btnPercent.grid(column = 2, row = 0 ,sticky = 'snwe')
        self.btnDiv = tk.Button(self.buttonFrame,text = '/', font = ('Arial', 18), command = lambda : self.addToField('/'))
        self.btnDiv.grid(column = 3, row = 0 ,sticky = 'snwe')
        self.btnMul = tk.Button(self.buttonFrame,text = 'x', font = ('Arial', 18), command = lambda : self.addToField('x'))
        self.btnMul.grid(column = 3, row = 1 ,sticky = 'snwe')
        self.btnMinus = tk.Button(self.buttonFrame,text = '-', font = ('Arial', 18), command = lambda : self.addToField('-'))
        self.btnMinus.grid(column = 3, row = 2,sticky = 'snwe')
        self.btnPlus = tk.Button(self.buttonFrame,text = '+', font = ('Arial', 18), command = lambda : self.addToField('+'))
        self.btnPlus.grid(column = 3, row = 3 ,sticky = 'snwe')
        self.btn0 = tk.Button(self.buttonFrame,text = 0 , font = ('Arial', 18), command = lambda : self.addToField('0'))
        self.btn0.grid(column = 0, row = 4 ,sticky = 'snwe')
        self.btnDot = tk.Button(self.buttonFrame,text = '.' , font = ('Arial', 18), command = lambda : self.addToField('.'))
        self.btnDot.grid(column = 1, row = 4 ,sticky = 'snwe')
        self.btnbackSpace = tk.Button(self.buttonFrame,text = '<-' , font = ('Arial', 18), command = self.backSpace)
        self.btnbackSpace.grid(column = 2, row = 4 ,sticky = 'snwe')
        self.btnEqual = tk.Button(self.buttonFrame,text='=',font=('Arial', 18), command = self.calculate) #Without paranthesis when you want to use it when called/When the button is piushed, with paranthesis when want to use it straight away 
        self.btnEqual.grid(column=3, row=4, sticky='snwe')

       # Create buttons 1-9 in the same style as your equals button
        self.btn1 = tk.Button(self.buttonFrame,text='1',font=('Arial', 18),command=lambda: self.addToField('1'))
        self.btn1.grid(column=0, row=1, sticky='snwe')
        self.btn2 = tk.Button(self.buttonFrame,text='2',font=('Arial', 18),command=lambda: self.addToField('2'))
        self.btn2.grid(column=1, row=1, sticky='snwe')
        self.btn3 = tk.Button(  self.buttonFrame,text='3',font=('Arial', 18),command=lambda: self.addToField('3'))
        self.btn3.grid(column=2, row=1, sticky='snwe')
        self.btn4 = tk.Button(self.buttonFrame,text='4',font=('Arial', 18),command=lambda: self.addToField('4'))
        self.btn4.grid(column=0, row=2, sticky='snwe')
        self.btn5 = tk.Button(self.buttonFrame,text='5',font=('Arial', 18),command=lambda: self.addToField('5'))
        self.btn5.grid(column=1, row=2, sticky='snwe')
        self.btn6 = tk.Button(self.buttonFrame,text='6',font=('Arial', 18),command=lambda: self.addToField('6'))
        self.btn6.grid(column=2, row=2, sticky='snwe')
        self.btn7 = tk.Button(self.buttonFrame,text='7',font=('Arial', 18),command=lambda: self.addToField('7'))
        self.btn7.grid(column=0, row=3, sticky='snwe')
        self.btn8 = tk.Button(self.buttonFrame,text='8',font=('Arial', 18),command=lambda: self.addToField('8'))
        self.btn8.grid(column=1, row=3, sticky='snwe')
        self.btn9 = tk.Button(self.buttonFrame , text='9',font=('Arial', 18),command=lambda: self.addToField('9'))
        self.btn9.grid(column=2, row=3, sticky='snwe') #INFO Lambda is used when you need to pass in an aruguement to function

        self.buttonFrame.grid(column=0, row=1, sticky='snwe')

        self.root.mainloop()

    #Adding numbers to the field
    def addToField(self,value):
        self.field.insert(tk.END, value) #Inserts to the textbox field

    def clearField(self):
        self.field.delete(1.0, tk.END)

    def backSpace(self):
        #Get position of the last character
        end_pos = self.field.index(tk.END)
        # Check if there is more than just the initial newline (meaning, actual text exists)
        if end_pos != "1.1": 
            # Calculate the position of the character to delete (2 positions before the END)
            pos_to_delete = f"{end_pos} - 2 chars"
            # Delete that single character
            self.field.delete(pos_to_delete)

    def invert(self):
        #if these operations are in the filed, then we cannot invert 
        opToExclude = ['+','x','/','%']
        current_text = self.field.get(1.0,tk.END).strip()
        run_invert = True
        for op in opToExclude:
            if op in current_text:
                run_invert = False
                break

        if run_invert:
            try:
                current_text = self.field.get(1.0, tk.END).strip()
                num_to_invert = float(current_text) * -1
                self.field.delete(1.0, tk.END)
                self.field.insert(1.0, str(num_to_invert))
            except ValueError:
                # Handle case where field doesn't contain a valid number
                print("Field doesn't contain a valid number")

    def calculate(self):
        #stores all the operators in a list
        operatorList = []
        #Stores all the numbers in a list
        allList = []
        #stores the span of the operators 
        spanList = []
        #gets the field
        fieldOfText = self.field.get(1.0,tk.END).strip()
        op_pattern = r'[^\d\s]' #Finds all things excluding the digits backspace s = whitespaces, backspace d is digits

        #Gets all the operators and adds it to a list 
        for operator in re.finditer(op_pattern,fieldOfText):
            operatorList.append(operator.group())
            spanList.append(operator.span()[0])

        #Gets all the numbers string and add it to the list
        for num in fieldOfText:
            allList.append(num)

        #Now we need to create a list with the numbers together
        combineNum = []
        curNum = ''
        for i in range(len(allList)):
            #checks that i is not in the list
            if allList[i] not in ['/','+','-','x']:
                curNum = curNum + allList[i] #appends the number
            else:
                combineNum.append(curNum)
                curNum = ''
        #Gets the last digit
        if curNum != '':
            combineNum.append(curNum)
        
        #Checking if the equation can be done/no last number at the end
        if len(operatorList) >= len(combineNum):
            return 'ERROR can not perfrom this calculation'
            
        #First perform the division of the equation
        updatedList = combineNum.copy() 
        newOperatorList = operatorList.copy()
        i = 0
        while i < len(newOperatorList):
            if newOperatorList[i] == '/':
                #Calculates the answer 
                answer = float(updatedList[i]) / float(updatedList[i+ 1])
                updatedList[i] = answer
                #Making sure we pop both updatedList and operatorList so it does not become out ofs index
                updatedList.pop(i + 1)
                newOperatorList.pop(i)
            else:
                #only increment when it does not have /
                i += 1
        
        i = 0
        while i < len(newOperatorList):
            if newOperatorList[i] == 'x':
                answer = float(updatedList[i]) * float(updatedList[i+1])
                updatedList[i] = answer 
                updatedList.pop(i + 1)
                newOperatorList.pop(i)
            else:
                i += 1
        
        i = 0
        while i < len(newOperatorList):
            if newOperatorList[i] == '+':
                answer = float(updatedList[i]) + float(updatedList[i+1])
                updatedList[i] = answer 
                updatedList.pop(i + 1)
                newOperatorList.pop(i)
            else:
                i += 1
        
        i = 0
        while i < len(newOperatorList):
            if newOperatorList[i] == '-':
                answer = float(updatedList[i]) - float(updatedList[i+1])
                updatedList[i] = answer     
                updatedList.pop(i + 1)
                newOperatorList.pop(i)
            else:
                i += 1
        finalAnswer = float(updatedList[0])
        self.field.delete(1.0,tk.END)
        self.field.insert(1.0,finalAnswer)



run = GUI()
