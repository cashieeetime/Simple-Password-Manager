use_hardcoded_filename = True

def open_file ():
    '''repeatedly prompts for a file until one is successfully opened'''
    if use_hardcoded_filename:
        file = open("cashie_passwords.txt")
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
    print("Hello. Welcome to the password manager. To get started, we need the name of the file that is holding your data.\n")
    file = open_file()
    read_file(file)
    cont = "y"

    while cont == "y":
        print("What would you like to do today? \n1. View a complete list of websites, emails and passwords. \n2. View a list of just the websites. \n3. Look up login information for a specific website. \n4. Add and save a new entry to your data.")
        answer = str(input())
        print()
        if answer.strip() == "1":
            print("This function hasn't been defined yet.\n")
        elif answer.strip() == "2":
            print("This function hasn't been defined yet.\n")
        elif answer.strip() == "3":
            print("This function hasn't been defined yet.\n")
        elif answer.strip() == "4":
            print("This function hasn't been defined yet.\n")
        else:
            print("I didn't understand that. Try again?")

        print("Would you like to start over? (yes/no)")
        answer = str(input())
        if answer.lower() == "no":
            cont = "n"
            print("\nThank you for using the password manager. We will now close the program.")
            file.close()
        elif answer.lower() == "yes":
            print()
        else:
            print("\nI didn't understand that. Try again?")


main()