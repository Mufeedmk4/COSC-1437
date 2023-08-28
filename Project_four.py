"""--------------------------------------------------------------------------------"""
"""Name: Mufeed Kamal"""
"""ID Number: W215659219"""
"""COSC 1437 - Programming Fundamentals II"""
"""--------------------------------------------------------------------------------"""

from Rational import *

class RationalFileProcessor:
    """ Initializes a RationalFileProcessor object """    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        
    """ This function will construct a rational number, then return it in a string """
    def try_construct_rational(self, numerator, denominator):
        try:
            numerator = int(numerator)  # Converts the numerator to an integer
            denominator = int(denominator)  # This does the same thing but to the denominator
            if denominator == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")  # Brings up an error if the denominator is equal to 0.
            rational_number = Rational(numerator, denominator)  # This creates the Rational object
            return str(rational_number)  # This will convert the rational_number to a string. 
        except ValueError as e:
            self.rational_number_error_handler(e, f"{numerator}, {denominator}")  # Handler for the ValueError
            return "Invalid input: Numerator and denominator must be integers."
        except ZeroDivisionError as e:
            self.rational_number_error_handler(e, f"{numerator}, {denominator}")  # Handler for the ZeroDivisionError
            return "Cannot divide by zero."
        except Exception as e:
            print("Exception:", e)  # If there are other errors that are not expected, this will print it. 
            return "An unexpected error occurred."

    """ This function will print rational error and show the error object, and then the data that caused the error """
    def rational_number_error_handler(self, exception_object_error, input_line):
        print(f"Rational Error: {exception_object_error}, Data Value: {input_line}")
        
    """ This function will show the error, then say file not found, and then exit out the program gracefully """
    def input_file_error_handler(self, exception_object_error):
        print(f"Error: {exception_object_error}, File not found. Exiting.")
        exit()
        
    """ Reads the lines from the input file and then returns it as a list of lines """
    def read_lines_from_input_file(self):
        try:
            with open(self.input_file, 'r') as file: # Opens the input file in read mode
                lines = file.readlines() # Reads the lines from the input file
                return [line.strip() for line in lines] # Returns a list of lines
        except FileNotFoundError as e:
            self.input_file_error_handler(e)

    """ Processes the input data and then returns a list of results """
    def process_input_data(self, lines):
        results = []  # Initializing empty to store results
        for line in lines:
            line = line.strip()  # Removes any spaces that are in the line
            numerator, denominator = line.split(',')  # This will further split the line into the numerator and denominator
            result = self.try_construct_rational(numerator, denominator)
            if result is not None:  # If its not none, itll append the result to the results
                results.append(result)
        return results
    
    """ This will take th restuls from the previous function and write it to an output file """
    def write_results_to_output_file(self, results):
        with open(self.output_file, 'w') as file: # This opens the output file in write mode
            for result in results:
                file.write(f"{result}\n") # This will write the results one by one on a new line to the output file

    """ This is where the processing of the iput and output files take place, calling other previously defined functions """
    def process_files(self):
        lines = self.read_lines_from_input_file() # This will read the lines from the input file and put it to lines
        results = self.process_input_data(lines) # This will process the lines and put it to results
        self.write_results_to_output_file(results) # This will write the reuslts to the new output file


if __name__ == "__main__":
    input_file = "data_01.txt"
    output_file = "output.txt"
    processor = RationalFileProcessor(input_file, output_file)
    processor.process_files()
    print("Name: Mufeed Kamal")
    print("ID Number: W215659219")
    print("COSC 1437 - Programming Fundamentals II")