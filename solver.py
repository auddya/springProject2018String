import numpy as np
 
def solver(user_input):

    x = np.zeros(user_input['Spatial Nodes'])
    t = np.zeros(user_input['Temporal Nodes'])
    u = np.zeros((x,t))

    return u, x, t   
	
	 

    
	
  
