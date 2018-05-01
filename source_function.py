import numpy as np
import math

def special_function_for_first_time_step(u, t, user_input):
   
    initial_source_time = floor(user_input['Temporal Nodes']/user_input['Frequency'])
    
    for i in range(initial_source_time):
        u[i,0] = sin(2*pi*user_input['Frequency']*t[i])

    return u


