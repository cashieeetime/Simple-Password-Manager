from asyncore import read

#
# debugging functions
#
def default_fp ():
    '''default file for debugging purposes; can also be used by the user for their own file'''
    fp = "example_password_format.txt"
    return fp

#
# file functions
#
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

#
# basic dictionary and text format functions
#
def build_dict (fp):
    '''Reads the file and splits lines, then calls a function to form the dictionary'''
    file = read_file(fp)

    data_dict = {}
    for line in file:   
        line = line.strip().replace(" ", "")
        line_list = line.split("|")
        linelist = [line_list[1], line_list[2], line_list[3]]        
        site = line_list[0]
        data_dict[site] = linelist

    file.close()
    return data_dict

def count_char (data_dict):
    '''loops through the file to find the keyword with the largest number of characters per  category, then returns those number'''
    w = 0     #len for websites
    e = 0     #len for emails
    u = 0     #len for usernames
    p = 0     #len for passwords

    for key in data_dict:
        w_len = len(key)
        e_len = len(data_dict[key][0])
        u_len = len(data_dict[key][1])
        p_len = len(data_dict[key][2])

        if w_len > w:
            w = w_len
        if e_len > e:
            e = e_len
        if u_len > u:
            u = u_len
        if p_len > p:
            p = p_len 

    return w, e, u, p

def pretty_print (output, data_dict):
    w, e, u, p = count_char(data_dict)

    '''takes output from a function and formats the result for printing'''
    print("    {:{w}s} | {:{e}s} | {:{u}s} | {:{p}s}".format("Website", "Email", "Username", "Password", w = w, e = e, u = u, p = p))
    print("    {:{w}s}   {:{e}s}   {:{u}s}   {:{p}s}".format("-------", "-----", "--------", "--------", w = w, e = e, u = u, p = p))

    for key in output:
        print("    {:{w}s} | {:{e}s} | {:{u}s} | {:{p}s}".format(key, output[key][0], output[key][1], output[key][2], w = w, e = e, u = u, p = p))

#
# program action functions
#
def print_all (data_dict):
    '''sorts dictionary keys and stores it oin a new variable to return'''
    output = {}
    for key in sorted((data_dict)):
        keylist = [data_dict[key][0], data_dict[key][1], data_dict[key][2]]
        output[key] = keylist
    pretty_print(output, data_dict)

def print_sites (data_dict):
    '''prints out the dictionary keys in alphabetical order'''
    print("    Website\n    -------")
    for key in sorted(data_dict):
        print("   ", key)

def p_lookup (data_dict, choice):
    '''takes a website name as an argument, and searches the dictionary for that key; if unable to find key, function suggests related websites'''
    choice = input("What website would you like to search for?\n-> ")
    output = {}
    alt_output = {}
    for key in sorted(data_dict):
        if choice.lower() == key.lower():
            linelist = [data_dict[key][0], data_dict[key][1], data_dict[key][2]]
            output[key] = linelist

        if key.lower().startswith(choice.lower()):
            linelist = [data_dict[key][0], data_dict[key][1], data_dict[key][2]]
            alt_output[key] = linelist

    if output != {}:
        pretty_print(output, data_dict)
    else:
        print("We couldn't find any websites with that name. Do any of these similar websties match what you are looking for?\n")
        pretty_print(alt_output, data_dict)

def add_entry (fp, data_dict):
    '''add an entry to the original file'''
    print("We will now ask you to input the necessary login information. Type \"n/a\" for any fields you'd like to leave blank.\n")
    website = input("What is the name of the website? \n-> ")
    email = input("What is the email address? \n-> ")
    username = input("What is the username? \n-> ")
    password = input("What is the password? \n-> ")

    file = write_file(fp)

    linelist = [email, username, password]
    data_dict[website] = linelist
    spacer = " | "
    file.write("\n" + website + spacer + email + spacer + username + spacer + password)
    file.close()
    print("\nYour data has been sucessfully saved to your file.")

def edit_entry(file):
    '''edit an already existing entry in the file'''
    print("This function hasn't been defined yet.")

#
# program base
#
def program_intro():
    print("\nHello. Welcome to the password manager.\n")

    while True:
        
        answer = input("To get started, we need the name of the file that is holding your data. Would you like to:\n    1. Provide the name of an already exisiting text file with your data\n    2. Create a new text file to store your data\n    3. Use the default file name stored in the program\n-> ")
        print()

        if answer.strip() == "1":
            fp = initialize_file()
            return fp
        
        elif answer.strip() == "2":
            fp = str(input("What would you like your file to be called? Please include the \".txt\" in your file name.\n-> "))
            open(fp, "r")
            return fp
        
        elif answer.lower() == "3":
            fp = default_fp()
            return fp

        else:
            print("I didn't understand that.\n")
            continue

def question_one(fp):
    while True:
    
        data_dict = build_dict(fp) 
        answer = input("What would you like to do today?\n    1. View a complete, alphabetized list of websites, emails and passwords.\n    2. View an alphabetized list of just the websites.\n    3. Look up login information for a specific website.\n    4. Add and save a new entry to your data.\n    5. Edit an already existing entry in the database.\n-> ")
        print()

        if answer.strip() == "1":
            print_all(data_dict)
            break
            
        elif answer.strip() == "2":
            print_sites(data_dict)
            print()
            break
            
        elif answer.strip() == "3":
            print()
            p_lookup(data_dict)
            break
            
        elif answer.strip() == "4":
            add_entry(fp, data_dict)
            break

        elif answer.strip() == "5":
            edit_entry(fp, data_dict)
            break
              
        else:
            print("I didn't understand that.\n")
            continue


def cont_question():
    while True:

        answer = input("\nWould you like to start over? (yes/no)\n-> ")
        
        if answer.lower() == "no":
            print("\nThank you for using the password manager. We will now close the program.\n")
            return False
        
        elif answer.lower() == "yes":
            print()
            return True
        
        else:
            print("\nI didn't understand that.")
            continue

#
# main
#
def main():
    cont = True
    program_intro()
    while cont == True:
        question_one()
        cont = cont_question()

main()