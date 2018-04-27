def main_Function_Simulation(user_input, u):

    c = def_Courant_Number(user_input['Time Steps'],user_input['Space Steps'],user_input['Wave Speed'])
    
    for j in range(2,user_input['Temporal Nodes']):
        for i in range(1,user_input['Spatial Nodes']):
            u1[j,i] = 2 * u[j-1,i] - u[j-2,i]
            u2[j,i] = u[j-1,i-1] - 2*u[j-1,i] + u[j-1,i+1]
            u[j,i] = u1[j,i] + c*c*u2[j,i]
    return u




