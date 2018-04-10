 import numpy as np
 
 def solver(I , V , c , L , dt , C , T , user_action=None):
    Nt = int(round(T/dt))
    t = np.linspace(0 , Nt*dt, Nt+1)  #Mesh Points in Time
    dx = dt * c/float(C)
    Nx = int(round(L/dx))
    x = np.linspace(0, L, Nx+1)
    C1 = C**2
    if V is None or V == 0:
       V = lambda x: 0

    u = np.zeros(Nx + 1)          # Solution array at new time level
    u_1 = np.zeros(Nx + 1) 	  # Solution array at 1 time level back
    u_2 = np.zeros(Nx + 1)        # Solution array at 2 time levels back
	

    for i in range(0,Nx + 1):     # Load initial conditions into u_1
       u_1[i] = I(x[i])
    
    if user_action is not None:
       user_action(u_1, x, t, 0)

    n = 0                         # Special formula for first time step   
    for i in range(1, Nx):
       u[i] = u_1[i] + dt * V(x[i]) + 0.5 * C1 * (u_1[i-1] - 2*u_1[i] + u_1[i+1])
    u[0] = 0 ; u[Nx] = 0

    if user_action is not None:
       user_action(u, x, t, 1)

    u_2[:] = u_1;  u_1[:] = u     # Switching variables before next step

    for n in range(1 , Nt): 
       for i in range(1 , Nx):
          u[i] = - u_2[i] + 2 * u_1[i] + C1 * (u_1[i-1] - 2*u_1[i] + u_1[i+1])
       	
       u[0] = 0;   u[Nx] = 0      # Insert boundary conditions
       
       if user_action is not None:
          if user_action(u, x, t, n+1):
	     break
       
       u_2[:] = u_1;   u_1[:] = u # Switching variables before next time step

    return u, x, t   
	
	 

    
	
  
