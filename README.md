# Project Description 

This project is aimed at solving a simple one dimensional wave equation, which we are specifying here as a vibrating string fixed at both ends. We intend to simulate this system varying certain key parameters which influence the oscillations. 

# Scope and Complexity

**Description**

One of the most simple techniques to visualise a simulation which involves solving a PDE  with certain boundary conditions is
to save the string profile for certain time intervals and plot them against appropriate axes.One of the most fundamental 
conditions required to *initialise* a vibration, is to pluck it at some point which generates the wave. After this at every
time interval the old and new profiles of the string is updated through an iteration. The output we intend to achieve is to
visualise the wave pattern with varying frequencies and modes. 

**Requirements**

* Theoretical Skills 

A basic understanding of certain elementary topics in mechanics such as tension and displacements in elastic strings is
required. Additionally choice of material needed to run the computational simulation is needed. (For instance,if no boundary
conditions are specified on the ultimate strength of the material,the compiler will evaluate results which might not be
physically possible. The string can always snap off if the force magnitude is higher).Knowledge of Elliptic PDE's (and its 
solution interpretation) is an added bonus. 

* Computational skills

The program can be solved in any computational platform (such as MATLAB, Python(preferred), C++). Basic knowledge of 
iterators,pointers, arrays, vectors (in some languages), function (and function calling) is required to solve the problem.

* Team Interaction 

In class discussion and using social platforms such as Slack etc. 

**Possible Improvements**

*This section mainly talks about what we consider as out of scope for the project*

We are evaluating the problem assuming the wave to be at steady state and slowly progressing with time.An additional
manipulation could have been introducing a friction coefficient and calculating the time rate of decay of the wave.Another
interesting application could have been visualising the transient state of the wave profile and the time it takes to 
transform from a non periodic wave profile to a periodic one. 

------
# Project Outline 

## Read Input

## Solve Physics 

- ### Setup Problem

- ### Loop Over Time Steps 
      
- #### Build Matrix
  
  ##### Loop over First time step [#7](https://github.com/auddya/springProject2018String/issues/7)
         
  ###### Working algorithm:
  
 - Initially we load our initial condition into u_1 (Solution array at one time level back)
 - Update u with special function that utilised u_1.
 - Switch variables before next step

```
 def special_function_for_first_time_step(solution arrays, initial condition, other parameters):

 This function lets us initialise the solution array and solve the equation for the first time step
 We need this step as according to our FD equation, when n = 0, one of the indices have a -1 term in 
 its index which requires some algebraic manipulation to build a new equation only for the first time step

	Input
	------ 
	- solution arrays: Solution arrays for present time and one and two steps behind needed for the simulation
	- initial condition: For t = 0, the condition of the string needs to be stored in the array
	- other parameters: Total number of nodes in spatial domain

	Output
	------
	- Updated u and switched variables as an input for the next function

```
- #### Solve Matrix and Update Time step

  ##### Loop over all time steps,solve the problem and update time step [#8](https://github.com/auddya/springProject2018String/issues/8)
	
  ###### Working algorithm
  
  - Loop over temporal intervals
  - Loop over spatial intervals
  - Apply finite difference formula
  - Insert boundary conditions after each time step
  - Switch variables before next time step

```
 def main_function_simulation(arrays, other parameters):
	
 This functions fills up the solution arrays using loops and FD equations

	Input
	------
	- arrays: Arrays from the previous function which will be used in the algorithm
	- other parameters: Needed for the FD equation
	
	Output
	------
	- Array containing the solution of our problem for a given PDE, IC and BC

```

- ## Write/View Output





