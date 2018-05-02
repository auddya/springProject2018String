import numpy as np
import math

def special_function_for_first_time_step(u, t, user_input):
   
    initial_source_time = math.floor(user_input['Temporal Nodes']/user_input['Frequency'])
    
    for i in range(int(initial_source_time)):
        u[i,0] = math.sin(2*math.pi*user_input['Frequency']*t[i])
        u[i,1] = math.sin(2*math.pi*user_input['Frequency']*t[i])

    return u


