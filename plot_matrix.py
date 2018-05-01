import numpy as np
import matplotlib.pyplot as plt
import pdb

def plot_string(displ_time_position, user_data ):
    """
    This function plots the string discplacement at spec times:

    inputs:
    --------
    - displ_times_position: (np.array) A matrix with the displacement at specific times 
                           and position.
    - user_data: Dictionary with the user inserted information.
    

    
    """
    time_nodes = []
    simul_time = user_data["Time"]
    user_times = user_data["Plotting Times"]
    rows, columns = np.shape(displ_times_position)
    number_of_nodes = rows - 1 #this is pyhthonized: 1 means nodes 0 and 1 then 2 nodes
    
    #pdb.set_trace()   
    for time in user_times: 
        time_nodes +=  [round(time*number_of_nodes/simul_time) ]
    i=1
    for node in time_nodes:
        plt.figure(i)
        plt.title('Time: ' + str(user_times[i-1]) + ' seconds' )
        #pdb.set_trace()
        plt.plot(displ_time_position[node][:])
        i+=1
    plt.show()  



