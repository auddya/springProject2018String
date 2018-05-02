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
        
    
    
