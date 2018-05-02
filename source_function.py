import numpy as np
import math

def special_function_for_first_time_step(u, t, user_input):
   
    #initial_source_time = math.floor(user_input['Temporal Nodes']/user_input['Frequency'])
    
    for i in range(int(user_input['Temporal Nodes'])):
        if i != 0:
            t[i] += t[i-1] + user_input['Time Step']
        u[i,0] = math.sin(2*math.pi*user_input['Frequency']*t[i])

    return u

   
    
