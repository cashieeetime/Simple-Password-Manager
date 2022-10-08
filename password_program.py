use_hardcoded_filename = False

def open_file ():
    '''repeatedly prompts for a file until one is successfully opened'''
    if use_hardcoded_filename:
        file = open("cashie-passwords.txt")
        return file
    else:
        while True:
            fp = input("Enter a file: ")
            try:
                file = open(fp, "r")
                return file
            except FileNotFoundError:
                print("Error: File not found.")
                
                continue 

def read_file (file):
    ''' Reads the file and separates lines, then calls a function to form the dictionary'''
    data_dict = {}
    
    file.readline()
    for line in file:
        print(line)
                    
    return data_dict
    

    

def main ():
    file = open_file()
    read_file(file)
    

main()