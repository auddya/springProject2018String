#!/usr/bin/python

from get_user_input import main as get_input 
from solver import solver
from source_function import special_function_for_first_time_step as first_step 
from main_Function_Simulation import main_Function_Simulation
import plot_matrix
#from solution_to_file import solution_to_file 

def main():
 
    inputs = get_input()
    u, x, t = solver(inputs)
    u1 = first_step(u, t, inputs)
    u = main_Function_Simulation(inputs, u1)
    plot_matrix.plot_string(u, inputs)
    print(u)
    print(u1)
    #solution_to_file(u, x, t)


if __name__ == "__main__":
    
    main()

