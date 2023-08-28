from tkinter import *
class myApp: # declaring the class the same way as the powerpoint had shown. 
    def __init__(self):
        self.root = Tk()

        self. root.title('Day Finder')

        self.root.geometry('640x480+300+300')
        self.root.resizable(False, False)

        self.root.option_add("*Font", "Times 14 normal")
        self.root.option_add('*Foreground', '#000000')
        self.root.configure(bg='#FFF') # Changed the bg, I hate the eggshell color lol

        self.root.option_add("*Label.Font", "Times 18 bold")
        
        self.create_gui()
        self.root.mainloop()
        
    def create_gui(self): # Creating the interface which the user will interact with, and input data we can use. 
        # Title label
        label1 = Label(self.root, text="Day of the Week Calculator (Using Zeller's Congruence)", font=("Times", 20, "bold"))
        label1.grid(row=0, column=0, columnspan=2, padx=10, pady=20) # Positioning the Title at the top

        # Month selection
        label2 = Label(self.root, text="Enter the Month", font=("Times", 16))
        label2.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.monthChoice = StringVar() # Taking the data as a string (Will convert this string to a number later down)
        
        # The instructions ask for an ENTRY rather than a drop down option menu, therefore I have changed the code to accept an entry
        entry1 = Entry(self.root, textvariable=self.monthChoice, font=("Times", 14))
        entry1.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        
        
        
        # Day selection
        label3 = Label(self.root, text="Select the Day", font=("Times", 16))
        label3.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        
        self.dayChoice = StringVar()
        self.dayChoice.set("Select a Day")
        
        days = [x for x in range(1,32)] # List Comprehension as stating in specification 6, so we dont have to list out each number in an array or string
        
        daybox = OptionMenu(self.root, self.dayChoice, *days) # Using an option menu here for the drop down menu as requested in specificaitons
        daybox.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        
        # Year Entry
        label4 = Label(self.root, text="Enter the Year", font=("Times", 16))
        label4.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        self.yearChoice = StringVar() # Taken as a string, but will int() onclick.
        entry2 = Entry(self.root, textvariable=self.yearChoice, font=("Times", 14)) # Entry as requested. 
        entry2.grid(row=3, column=1, padx=10, pady=5, sticky='w') 
        
        # Calculate Button
        button1 = Button(self.root, text="Calculate!", command=self.onClick, font=("Times", 16)) # Button that will run the command below onClick
        button1.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
        
    
    def onClick(self):
        # Month is convereted to integer through if/elif statements below
        # Year and Day are converted from string to int()
        # Zeller's Congruence is used throughout with modifications and additions to meet the specifications
        month = self.monthChoice.get()
        year = int(self.yearChoice.get())
        day = int(self.dayChoice.get())
        
        # Had to create an if/elif to convert the name of the month to a value. 
        if month.lower() == "january":
            month_number = 1
        elif month.lower() == "february":
            month_number = 2
        elif month.lower() == "march":
            month_number = 3
        elif month.lower() == "april":
            month_number = 4
        elif month.lower() == "may":
            month_number = 5
        elif month.lower() == "june":
            month_number = 6
        elif month.lower() == "july":
            month_number = 7
        elif month.lower() == "august":
            month_number = 8
        elif month.lower() == "september":
            month_number = 9
        elif month.lower() == "october":
            month_number = 10
        elif month.lower() == "november":
            month_number = 11
        elif month.lower() == "december":
            month_number = 12
        else:
            month_number = None
        
        
        if month_number == 1 or month_number == 2:
            month_number += 12
            year -= 1
        m = month_number
        k = year % 100
        j = year // 100
        q = day
        h = (q + 26*(m + 1)//10 + k + k//4 + j//4 + 5*j) % 7
        
        if h == 0: dstring = "Saturday"
        elif h == 1: dstring = "Sunday"
        elif h == 2: dstring = "Monday"
        elif h == 3: dstring = "Tuesday"
        elif h == 4: dstring = "Wednesday"
        elif h == 5: dstring = "Thursday"
        elif h == 6: dstring = "Friday"
        
        # Adding statement to the end of the label5, based on staticmethod made below, taking in the year. 
        if self.is_leap_year(year):
            leap_message = "a leap year"
        else:
            leap_message = "not a leap year."
        
        # Label will have all the information requested from the onClick
        label5 = Label(
            self.root, # attach to root window object
            text = f"The date of {self.monthChoice.get()} {self.dayChoice.get()}, {self.yearChoice.get()} is a {dstring} and {leap_message} ",
            font = ('Times 18 normal'), # set font values
            bg = '#FFF8DC', # set background Color to Cornsilk
            fg = '#000000' # Set foreground color to Black
        )
        label5.grid(row = 5, column = 0, sticky = 'W', pady = 10, columnspan=2)
        
    
    @staticmethod # Boolean result for if its a leap year. 
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False
    
window1 = myApp()
if __name__ == "__main__":
    app = myApp()