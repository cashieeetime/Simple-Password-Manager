use_hardcoded_filename = False

def open_file ():
    '''repeatedly prompts for a file until one is successfully opened'''
    if use_hardcoded_filename:
        file = open("sample_passwords.txt")
        return file
    
    else:
        while True:
            fp = input("Enter a file name: ")
            try:
                file = open(fp, "r")
                return file

            except FileNotFoundError:
                print("Error: File not found.")
                continue 

def build_dict (file):
    ''' Reads the file and separates lines, then calls a function to form the dictionary'''
    data_dict = {}
    for line in file:   
        #line = line.strip().replace(" ", "")
        line_list = line.split()
        linelist = [line_list[1], line_list[2], line_list[3]]        
        site = line_list[0]
        data_dict[site] = linelist
    return data_dict

def print_all (file):
    pass

def print_sites (file):
    pass

def p_lookup (file):
    pass

def add_entry (file):
    pass

def edit_entry(file):
    pass

def main ():
    print("Hello. Welcome to the password manager. To get started, we need the name of the file that is holding your data.\n")
    file = open_file()
    build_dict(file)
    cont = True

    while cont == True:
        q1_repeat = True
        q2_repeat = True
        while q1_repeat == True:
            print("What would you like to do today? \n1. View a complete list of websites, emails and passwords. \n2. View a list of just the websites. \n3. Look up login information for a specific website. \n4. Add and save a new entry to your data. \n5. Edit an already existing entry in the database.")
            answer = str(input())
            print()
            
            if answer.strip() == "1":
                # print_all(file)
                print("This function hasn't been defined yet.\n")
                q1_repeat = False

            elif answer.strip() == "2":
                # print_sites(file)
                print("This function hasn't been defined yet.\n")
                q1_repeat = False
            
            elif answer.strip() == "3":
                # p_lookup(file)
                print("This function hasn't been defined yet.\n")
                q1_repeat = False

            elif answer.strip() == "4":
                # add_entry(file)
                print("This function hasn't been defined yet.\n")
                q1_repeat = False
            
            elif answer.strip() == "5":
                # edit_entry(file)
                print("This function hasn't been defined yet.\n")
                q1_repeat = False

            else:
                print("I didn't understand that.\n")


        while q2_repeat == True:
            print("Would you like to start over? (yes/no)")
            answer = str(input())

            if answer.lower() == "no":
                cont = False
                print("\nThank you for using the password manager. We will now close the program.\n")
                file.close()
                q2_repeat = False

            elif answer.lower() == "yes":
                print()
                q1_repeat = True
                q2_repeat = False

            else:
                print("\nI didn't understand that.\n")
                q2_repeat = True


main()