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
    print()

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