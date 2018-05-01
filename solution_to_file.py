import csv


def solution_to_file(u, x, t):
    """
    Take the solution matrix of displacement (u), the time mesh (t), and the length mesh (x) and generate a .csv 
    file.

    input:
    ------
    Matrix of displacement (u)
    Time mesh (t)
    Length mesh (x)

    output:
    -------
    Input data organized in .csv file type
    """
    """
    def write_seq_dict_txt(filename, seq_dict):
        with open(filename,"w") as outfile:
        outfile.write("\n".join(["{0} : {1}".format(key,val) for key,val in seq_dict.items()]))


    def write_seq_dict_csv(filename, seq_dict):
        seq_length = len(list(seq_dict.values())[0])
        seq_header = ['initial','length'] + ["S" + str(idx) for idx in range(seq_length)]

        with open(filename,"w") as csvfile:
            seq_writer = csv.writer(csvfile, delimiter=",")
            seq_writer.writerow(seq_header)
            for key, val in seq_dict.items():
                seq_writer.writerow(list(key) + val)

    

    def write_seq_dict_hdf5(filename, seq_dict):

        f = tb.open_file(filename, 'w')
        f.create_group('/', 'sequences', "My Sequences")
        seq_idx = 0
        for key, val in seq_dict.items():
            seq_name = "seq" + str(seq_idx)

            seq_array = f.create_array('/sequences', seq_name, val)
            seq_array.attrs.init = key[0]
            seq_array.length = key[1]

            seq_idx += 1

    """
    #Build header row of each value in t
    #Write header row into file
    #For each data row include the 
    #    Attach x-value to displacement data
    #    Write data row
    time_length = len(t) #Number of time nodes and "x" entries in csv file
    sol_header = [" "] + [t[idx] for idx in range(time_length)] #Building of header file
    
    with open("solution.csv","w") as csvfile:
        sol_writer = csv.writer(csvfile, delimiter=",")
        sol_writer.writerow(sol_header)
        for idx in range(len(x)):
            sol_writer.writerow([x[idx]] + [u[idx][col] for col in range(time_length)])
        
    
    
