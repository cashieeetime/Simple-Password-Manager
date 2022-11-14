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
