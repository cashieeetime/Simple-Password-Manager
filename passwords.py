use_hardcoded_filename = True

def open_file ():
    '''repeatedly prompts for a file until one is successfully opened'''
    if use_hardcoded_filename:
        file = open("c-passwords.txt")
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
    next(file)
    next(file)
    for line in file:   
        line = line.strip().replace(" ", "")
        line_list = line.split("|")
        linelist = [line_list[1], line_list[2], line_list[3]]        
        site = line_list[0]
        data_dict[site] = linelist        
    return data_dict
    

    

def main ():
    file = open_file()
    read_file(file)
    
    file.close()
    

main()