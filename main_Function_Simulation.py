from def_Courant_Number import def_Courant_Number

def main_Function_Simulation(user_input, u):

    c = def_Courant_Number(user_input['Time Step'],user_input['Space Step'],user_input['Wave Speed'])

    u1 = u
    u2 = u

    for i in range(user_input['Spatial Nodes']-1):
        u[2,i] =u[1,i]+ 0.5 * c*c*(u[1,i+1] - 2*u[1,i]+ u[1,i-1]); #solution for the first time step
    
    for j in range(2,int(user_input['Temporal Nodes'])-1):
        for i in range(1,int(user_input['Spatial Nodes'])-1):
            u1[j,i] = 2 * u[j-1,i] - u[j-2,i]
            u2[j,i] = u[j-1,i-1] - 2*u[j-1,i] + u[j-1,i+1]
            u[j,i] = u1[j,i] + c*c*u2[j,i]

    return u




