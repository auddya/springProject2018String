import math

def special_function_for_first_time_step(u, t, user_input):
   
    s1 = floor(user_input['Time Steps']/user_input['frequency'])
    
    for i in range(s1):
        u[i,0] = sin(2*pi*user_input['frequency']*t[i])

    return u


