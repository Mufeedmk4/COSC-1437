"""--------------------------------------------------------------------------------"""
"""Name: Mufeed Kamal"""
"""ID Number: W215659219"""
"""COSC 1437 - Programming Fundamentals II"""
"""--------------------------------------------------------------------------------"""


from tkinter import *

class tikTacToe:
    def aboutMe(self):
        pass
    def __init__(self): 
        """Initializing the TicTacToe Game GUI."""
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("1200x1200")
        
        self.window.option_add("*Font", 'Times 16')
        self.window.configure(bg='#FFF8DC')
        self.window.resizable(False, False)
        
        """Initializing the number of moves"""
        self.moves = 0
        
        """Creating the Menubar"""
        self.menubar = Menu(self.window)
        self.window.config(menu = self.menubar) 
        
        """Creating the Game Menu"""
        self.GameMenu = Menu(self.menubar, tearoff="off")
        self.menubar.add_cascade(label="Game", menu=self.GameMenu)
        self.GameMenu.add_command(label = "Play", background ='#FAFAD2', activebackground = '#FFFFFF', activeforeground = '#FF0000') # Play button
        self.GameMenu.add_command(label = "Quit", background ='#FAFAD2') # Quit button
        self.GameMenu.add_command(label = "Exit", background ='#FFE4E1', command = exit) # Exit button, that will do the command exit and exit out of the game
        
        """Creating the About Menu"""
        self.AboutMenu = Menu(self.menubar, tearoff="off")
        self.menubar.add_cascade(label="About", menu=self.AboutMenu)
        self.AboutMenu.add_command(label = "About Me", command = self.aboutMe) # About Me page
        self.AboutMenu.add_command(label = "Instructions", command = self.aboutMe) # Instructions page
        self.AboutMenu.add_command(label = "COSC 1437", command = self.aboutMe) # Third button
        self.window.config(menu=self.menubar)
        
        """Instructions had to make three menus, so I made a help menu as well"""
        self.helpMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)
        
        """This is where the title is for the game"""
        Title = Label(self.window, text = 'Tic - Tac - Toe',font = ('Times 18 bold'), bg = '#FFF8DC',fg = "#D2691E")
        Title.grid(row = 0, column = 1, padx = (20,0), pady = (5,0), sticky = 'WS', columnspan = 7)
        
        """This section is to create the radio button that'll choose what team you are playing for"""
        self.radioVar = IntVar() 
        self.radio1 = Radiobutton(self.window, font = ('Times' , 25),text="X", variable=self.radioVar, value=1, command = self.select)
        self.radio2 = Radiobutton(self.window, font = ('Times' , 25),text="O", variable=self.radioVar, value=0, command = self.select)

        self.radio1.grid(row = 1, column = 6, sticky = 'N',pady=(50,0))
        self.radio2.grid(row = 1, column = 7, sticky = 'N',pady=(50,0))
        
        """set default values"""
        self.b11Val, self.b12Val, self.b13Val = 0, 0, 0
        self.b21Val, self.b22Val, self.b23Val = 0, 0, 0
        self.b31Val, self.b32Val, self.b33Val = 0, 0, 0
        
        """Getting our images, I put them in my native VSCode project folder under a subfolder "images" """
        self.ImageX = PhotoImage(file = r"images\PythonX.PNG")
        self.ImageO = PhotoImage(file = r"images\PythonO.PNG")
        self.ImageBase = PhotoImage(file = r"images\PythonBase.PNG")
        self.ImageH = PhotoImage(file = r"images\PythonHorizontal2.PNG")
        self.ImageV = PhotoImage(file = r"images\PythonVertical.PNG")
        
        """This is just the labels for the brownorange bars"""
        vbar1 = Label(self.window, image = self.ImageV, highlightthickness = 0, bd = 0 )
        vbar1.grid(row = 1, column = 2, sticky = 'W', rowspan = 6, ipadx=0, ipady=0, pady=(50,0))
        vbar2 = Label(self.window, image = self.ImageV , highlightthickness = 0, bd = 0)
        vbar2.grid(row = 1, column = 4, sticky = 'W', rowspan = 6, ipadx=0, ipady=0, pady=(50,0))
        hbar1 = Label(self.window, image = self.ImageH, highlightthickness = 0, bd = 0 )
        hbar1.grid(row = 2, column = 0, sticky = 'W', columnspan = 6, ipadx=0, ipady=0,padx=(20,0))
        hbar2 = Label(self.window, image = self.ImageH , highlightthickness = 0, bd = 0)
        hbar2.grid(row = 4, column = 0, sticky = 'W', columnspan = 6, ipadx=0, ipady=0, padx=(20,0))
        
        """This is all the buttons all 9 of them."""
        self.b11 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b11.grid(row = 1, column = 1, sticky = 'W',ipadx=0, ipady=0, padx=(20,0), pady=(50,0))
        self.b12 = Button(self.window, image = self.ImageBase, command = self.cycle12, highlightthickness = 0, bd = 0)
        self.b12.grid(row = 1, column = 3, sticky = 'W', ipadx=0, ipady=0, pady=(50,0))
        self.b13 = Button(self.window, image = self.ImageBase, command = self.cycle13, highlightthickness = 0, bd = 0)
        self.b13.grid(row = 1, column = 5, sticky = 'W', ipadx=0, ipady=0, pady=(50,0))
        self.b21 = Button(self.window, image = self.ImageBase, command = self.cycle21, highlightthickness = 0, bd = 0)
        self.b21.grid(row = 3, column = 1, sticky = 'W', ipadx=0, ipady=0, padx=(20,0))
        self.b22 = Button(self.window, image = self.ImageBase, command = self.cycle22, highlightthickness = 0, bd = 0)
        self.b22.grid(row = 3, column = 3, sticky = 'W', ipadx=0, ipady=0)
        self.b23 = Button(self.window, image = self.ImageBase, command = self.cycle23, highlightthickness = 0, bd = 0)
        self.b23.grid(row = 3, column = 5, sticky = 'W', ipadx=0, ipady=0)
        self.b31 = Button(self.window, image = self.ImageBase, command = self.cycle31, highlightthickness = 0, bd = 0)
        self.b31.grid(row = 5, column = 1, sticky = 'W', ipadx=0, ipady=0, padx=(20,0))
        self.b32 = Button(self.window, image = self.ImageBase, command = self.cycle32, highlightthickness = 0, bd = 0)
        self.b32.grid(row = 5, column = 3, sticky = 'W', ipadx=0, ipady=0)
        self.b33 = Button(self.window, image = self.ImageBase, command = self.cycle33, highlightthickness = 0, bd = 0)
        self.b33.grid(row = 5, column = 5, sticky = 'W', ipadx=0, ipady=0)
        
        """The spec required to have a label at the bottom showing winner or tie, this is that label, initialized"""
        self.winnerLabel = Label(self.window, text="", font=('Times', 16), bg='#FFF8DC', fg='#000000')
        self.winnerLabel.grid(row=7, column=1, columnspan=7, pady=(10, 0))
        
        self.window.mainloop()
    
    """This is the select method where it prints to the console, which player is currently active"""   
    def select(self):
        selection = self.radioVar.get()
        if selection == 1:
            print("Player X has the next move")
        else:
            print("Player O has the next move")
            
    
    """---------------------------------------------------------------------------------------------------------------------------------"""        
    """This is one of nine cycle methods, I will write descriptive comments for this one, and all further cycle methods are the same"""        
    def cycle11(self):
        self.moves += 1 # This increases the move count since the moves been done
        if self.radioVar.get() == 1: # This is to select what player is selected based on the radio value. 
            self.b11.configure(image = self.ImageX ) # This is to set the image to X if X was chosen. 
            self.b11Val = 1  
            play = "X"
        else:
            self.b11.configure(image = self.ImageO ) # This is the set the image to O if O was chosen
            self.b11Val = -1  
            play = "O"
        self.b11["state"] = "disabled" # This disables the button so you cant change the selection
        self.report(f"{play} played a move at Square (1,1)") # This will push a report to the console when the move has been made

    def cycle12(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b12.configure(image = self.ImageX )
            self.b12Val = 1 
            play = "X"
        else:
            self.b12.configure(image = self.ImageO )
            self.b12Val = -1 
            play = "O"
        self.b12["state"] = "disabled"
        self.report(f"{play} played a move at Square (1,2)") 
    
    def cycle13(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b13.configure(image = self.ImageX )
            self.b13Val = 1 
            play = "X"
        else:
            self.b13.configure(image = self.ImageO )
            self.b13Val = -1 
            play = "O"
        self.b13["state"] = "disabled"
        self.report(f"{play} played a move at Square (1,3)") 
        
    def cycle21(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b21.configure(image = self.ImageX )
            self.b21Val = 1 
            play = "X"
        else:
            self.b21.configure(image = self.ImageO )
            self.b21Val = -1 
            play = "O"
        self.b21["state"] = "disabled"
        self.report(f"{play} played a move at Square (2,1)") 
    
    def cycle22(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b22.configure(image = self.ImageX )
            self.b22Val = 1 
            play = "X"
        else:
            self.b22.configure(image = self.ImageO )
            self.b22Val = -1 
            play = "O"
        self.b22["state"] = "disabled"
        self.report(f"{play} played a move at Square (2,2)") 
        
    def cycle23(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b23.configure(image = self.ImageX )
            self.b23Val = 1 
            play = "X"
        else:
            self.b23.configure(image = self.ImageO )
            self.b23Val = -1 
            play = "O"
        self.b23["state"] = "disabled"
        self.report(f"{play} played a move at Square (2,3)") 

    def cycle31(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b31.configure(image = self.ImageX )
            self.b31Val = 1 
            play = "X"
        else:
            self.b31.configure(image = self.ImageO )
            self.b31Val = -1 
            play = "O"
        self.b31["state"] = "disabled"
        self.report(f"{play} played a move at Square (3,1)") 
        
    def cycle32(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b32.configure(image = self.ImageX )
            self.b32Val = 1 
            play = "X"
        else:
            self.b32.configure(image = self.ImageO )
            self.b32Val = -1 
            play = "O"
        self.b32["state"] = "disabled"
        self.report(f"{play} played a move at Square (3,2)") 
        
    def cycle33(self):
        self.moves += 1 
        if self.radioVar.get() == 1:
            self.b33.configure(image = self.ImageX )
            self.b33Val = 1 
            play = "X"
        else:
            self.b33.configure(image = self.ImageO )
            self.b33Val = -1 
            play = "O"
        self.b33["state"] = "disabled"
        self.report(f"{play} played a move at Square (3,3)") 
    
    """---------------------------------------------------------------------------------------------------"""
    
    
    """Disable board method to make further selection disabled"""    
    def disableBoard(self):
        self.b11["state"] = "disabled"
        self.b12["state"] = "disabled"
        self.b13["state"] = "disabled"
        self.b21["state"] = "disabled"
        self.b22["state"] = "disabled"
        self.b23["state"] = "disabled"
        self.b31["state"] = "disabled"
        self.b32["state"] = "disabled"
        self.b33["state"] = "disabled"   
    
    """This is to determine the winner"""    
    def isWinner(self): # simple calculation to get the sum of values
            hch1 = self.b11Val + self.b12Val + self.b13Val 
            hch2 = self.b21Val + self.b22Val + self.b23Val
            hch3 = self.b31Val + self.b32Val + self.b33Val
            vch1 = self.b11Val + self.b21Val + self.b31Val
            vch2 = self.b12Val + self.b22Val + self.b32Val
            vch3 = self.b13Val + self.b23Val + self.b33Val
            dch1 = self.b11Val + self.b22Val + self.b33Val
            dch2 = self.b13Val + self.b22Val + self.b31Val
            
            # This is to check the winning condition, and to see if its been met, for X its 3, for O its -3.
            winnerX = hch1== 3 or hch2== 3 or hch3== 3 or vch1== 3 or vch2== 3 or vch3== 3 or dch1== 3 or dch2== 3
            winnerO = hch1==-3 or hch2==-3 or hch3==-3 or vch1==-3 or vch2==-3 or vch3==-3 or dch1==-3 or dch2==-3
            self.winner = "" # Had to initialize a winner empty string, to add the tie function
            if winnerX: # This is where it actually checks the winner, and then turns off the board if there is one. 
                self.winner = "X"
                self.disableBoard()
                return True
            elif winnerO:
                self.winner = "O"
                self.disableBoard()
                return True
            else:
                if self.moves == 9: # If there is no winner, adn there have been made 9 moves, there is a tie. 
                    self.winner = "tie" # Settign the winner value to tie
                    self.disableBoard()
                else:
                    return False    
    """report method, where we print to the screen on the previously initialized winnerLabel."""    
    def report(self, moveInfo):
        print(moveInfo)
        if self.isWinner():
            self.winnerLabel.config(text=f"{self.winner} has won the game")
        elif self.winner == "tie":
            self.winnerLabel.config(text="There is a tie")
        else:
            self.winnerLabel.config(text="No winner yet")
            
            
            
    
        
        
if __name__ == "__main__":
    tikTacToe() # Create GUI 