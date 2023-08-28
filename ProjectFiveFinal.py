import tkinter as tk
from tkinter import filedialog

def setup_gui():
    
    """ Configuring the main Tkinter window, will return tk.Tk """
    root = tk.Tk()
    root.title("Palindrome Checker")
    root.configure(bg="#FFFFFF") # I went with a white background cause its minimal
    
    # Center the GUI on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800
    window_height = 600
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    return root

def readStrings(fileName):
    """ This function reads the file with the list of strings, and returns a list of strings """
    try:
        with open(fileName, 'r') as file:
            strings = [line.strip() for line in file]
            return strings
    except FileNotFoundError: # Error handling for the FileNotFoundError
        print(f"File '{fileName}' not found.")
        return []

def isPalindrome(string):
    """ This function takes a single string, and determines in a boolean fashion whether or not the string is a palindrome """
    spaceAndLower = ''.join(string.split()).lower() # Gets rid of spaces and lower cases everything
    if len(spaceAndLower) <= 1: # Base Case
        return True
    
    # Recursive Case
    if spaceAndLower[0] != spaceAndLower[-1]:
        return False
    else:
        return isPalindrome(spaceAndLower[1:-1])
    pass

def processList(strings):
    """ This funciton checks the strings as a list, and then gives out a list of booleans for each string showing whether they are a palindrome or not"""
    palindromeStatus = [] # Initializing an empty list
    for string in strings:
        palindromeStatus.append(isPalindrome(string)) # Calling previous function, isPalindrome for each string in strings list.
    return palindromeStatus

def displayResults(strings, palindromes):
    """ This function is all about displaying the results on the tkinter window. Takes in a list of strings to display on there. """
    result_window = tk.Tk()
    result_window.title("Palindrome Results")
    result_window.geometry("600x400")

    title_label = tk.Label(result_window, text="Palindrome Results", font=("Arial", 18, "bold"), fg="#2E86C1")
    title_label.pack(pady=10)

    for string, is_palindrome in zip(strings, palindromes): # This is iterating through the list of strings and their palindromes status
        status_text = "Palindrome" if is_palindrome else "Not Palindrome"
        status_color = "#2ECC71" if is_palindrome else "#E74C3C" # UI related functionality, changing color depending on boolean
        
        # UI mods
        string_label = tk.Label(result_window, text=string, font=("Arial", 14), fg="#333333")
        status_label = tk.Label(result_window, text=status_text, font=("Arial", 14, "bold"), fg=status_color)
        string_label.pack(pady=5)
        status_label.pack(pady=5)

    result_window.mainloop()

def initiateCheckPalindromes():
    """ Calls the readStrings, processList, and displayResults function to make things initiate """
    file_name = filedialog.askopenfilename(title="Select File", filetypes=[("Text files", "*.txt")])
    if file_name:
        strings = readStrings(file_name)
        if strings:
            palindromes = processList(strings)
            displayResults(strings, palindromes)

def main():
    """ Creates the tkinter window, adds widgets to the window and runs the Tkinter main loop"""
    root = setup_gui()

    check_button = tk.Button(root, text="Check Palindromes", command=initiateCheckPalindromes, bg="#2E86C1", fg="#FFFFFF", font=("Arial", 14), padx=20)  # Blue button with white text
    check_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
