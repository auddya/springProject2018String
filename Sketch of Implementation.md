**Input data in the problem:**

* Initial condition u( x , 0 ) = I(x): initial string shape

* Initial condition u_t( x , 0 ) = 0: string starts from rest

* c=v(T/?): velocity of waves on the string
(T is the tension in the string, ? is density of the string)

* Two boundary conditions on u: u= 0 means fixed ends (no displacement)

**Step 1: Discretizing the domain**

* Mesh in time:
  
  0 = t_0 < t_1 < t_2 < ? < t_N_t-1 < t_N_t = T

* Mesh in space:
  
  0 = x_0 < x_1 < x_2 < ? < x_N_x-1 < x_N_x = L

* Uniform mesh with constant mesh spacings ?t and ?x:
  
  x_i=i*?x, i=0, … ,N_x, t_i = n*?t , n=0, … ,Nt


**Step 2: Fulfilling the equation at the mesh points**

  Let the PDE be satisfied at all interior mesh points

  for i = 1, … ,N_x - 1 and n = 1 , … , N_t-1.

  For n = 0 we have the initial conditions u = I(x) and u_t = 0, and at the          boundaries i = 0,Nx we have the boundary condition u = 0

**Step 3(a): Replacing derivatives by finite differences**

**Step 3(b): Rewriting the Algebraic version of the PDE**

**Step 3(c): Algebraic version of the initial conditions** 
 
  * Need to replace the derivative in the initial condition ut(x,0)=0 by a finite      difference approximation

  * Use a centered difference for u_t( x , 0 )

    [D_2t(u)](n,i) = 0, n = 0  ?  u(n-1,i) = u(n+1,i) , i = 0 , … , Nx
  

**Step 4: Formulating a recursive algorithm**

 * Nature of the algorithm: compute u in space at t=?t,2?t,3?t,...

 * Three time levels are involved in the general discrete equation: n+1, n, n-1

 * Solve for u( n+1 , i )

**Step 5: Defining the The Courant Number**

  * C=c * ( ?t / ?x ), is known as the (dimensionless) Courant number

  * There is only one parameter, C, in the discrete model: C lumps mesh parameters     ?t and ?x with the only physical parameter, the wave velocity c. The value C       and the smoothness of I(x) govern the quality of the numerical solution. 

**Step 6: Defining the stencil for the first time level**

  * Problem: the stencil for n=1 involves u( -1 , i ) , but time t=-?t is outside     the mesh and is undefined for the problem

  * Remedy: use the initial condition u_t = 0 together with the stencil to     eliminate  u( -1 , i )

**Step 7: The working algorithm

 If u(n,i) be a general solution of any point within the domain (0,T]x (0,L)  

* Compute u( 0 , i )=I( x ( i ) ) for i=[ 0 , Nx ]
* Compute u( 1 , i ) and set u( 1 , i ) = 0 for the boundary points i=0 and i=Nx, for n=1,2,. . .,N-1,
* For each time level n=1,2,. . .,Nt-1
   * find u( n+1 , i ) for i=1,. . .,Nx-1
   * set u( n+1 , i ) = 0 for the boundary points i=0 and i=Nx.



