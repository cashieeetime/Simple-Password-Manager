use_hardcoded_filename = True 

def open_file ():
    '''repeatedly prompts for a file until one is successfully opened'''
    if use_hardcoded_filename:
        file = open("sample_passwords.txt")
        #file = open("cashie_passwords.txt")
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
        line = line.strip().replace(" ", "")
        line_list = line.split("|")
        linelist = [line_list[1], line_list[2], line_list[3]]        
        site = line_list[0]
        data_dict[site] = linelist
    return data_dict

def count_char (data_dict):
    '''loops through the whole file to find the item with the largest number of characters, then stores and returns that number'''
    char_count = 0

    for key in data_dict:
        key_char = len(key)
        if key_char > char_count:
            char_count = key_char
        for item in key:
            item_char = len(item)
            if item_char > char_count:
                char_count = item_char

    return char_count

def print_all (data_dict):
    '''prints out an alphabetical list of the dictionary's keys and it's corresponding values'''
    print("{:20s} {:1s} {:20s} {:1s} {:20s} {:1s} {:20s}".format("Website", "|", "Email", "|", "Username", "|", "Password"))

    for key in sorted(data_dict):
        print("{:20s} {:1s} {:20s} {:1s} {:20s} {:1s} {:20s}".format(key, "|", data_dict[key][0], "|", data_dict[key][1], "|", data_dict[key][2]))

def print_sites (data_dict):
    '''prints out the dictionary keys in alphabetical order'''
    print("Website \n--------")
    for key in sorted(data_dict):
        print(key)

def p_lookup (data_dict, ):
    '''takes a website name as an argument, and searches the dictionary for that key'''
    pass

def add_entry (file):
    '''add an entry to the original file'''
    pass

def edit_entry(file):
    '''edit an already existing entry in the file'''
    pass

def main ():
    print("\nHello. Welcome to the password manager. To get started, we need the name of the file that is holding your data.\n")
    file = open_file()
    data_dict = build_dict(file)
    char_count = count_char(data_dict)
    cont = True

    while cont == True:
        q1_repeat = True
        q2_repeat = True
        while q1_repeat == True:
            print("What would you like to do today? \n1. View a complete, alphabetized list of websites, emails and passwords. \n2. View an alphabetized list of just the websites. \n3. Look up login information for a specific website. \n4. Add and save a new entry to your data. \n5. Edit an already existing entry in the database.")
            answer = str(input())
            print()
            
            if answer.strip() == "1":
                print_all(data_dict)
                #print("This function hasn't been defined yet.\n")
                q1_repeat = False

            elif answer.strip() == "2":
                print_sites(data_dict)
                q1_repeat = False
            
            elif answer.strip() == "3":
                # p_lookup(data_dict)
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
            print("\nWould you like to start over? (yes/no)")
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
                print("\nI didn't understand that.")
                q2_repeat = True


main()