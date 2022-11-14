def initialize_file ():
    '''repeatedly prompts for a file until one is successfully opened'''
    while True:
        fp = input("\nEnter a file name: ")
        try:
            file = open(fp, "r")
            return file
        except FileNotFoundError:
            print("\n    Error: File not found.")
            continue 

def read_file (fp):
    '''opens file for reading'''
    file = open(fp, "r")
    return file

def write_file (fp):
    '''opens file for writing'''
    file = open(fp, "a")
    return file

def unknown_input():
    print("I didn't understand that.\n")