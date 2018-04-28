#! /usr/bin/python
import argparse

def check_pluck_position(string_length, pluck_position):

    if string_length <= pluck_position:
        print("The position of the pluck is greater than the string length." +
              "\nProgram ended.")
        exit()
    elif pluck_position <= 0:
        print("The position of the pluck is less than zero." +
              "\nProgram terminated.")
        exit()


def check_pluck_displacement(string_length, pluck_position, pluck_displacement,
                             yield_stress, youngs_modulus):

    length_1 = (pluck_position**2 + pluck_displacement**2)**0.5
    length_2 = ((string_length - pluck_position)**2 + pluck_displacement**2)**0.5
    strain = (length_1 + length_2 - string_length) / string_length
    stress = youngs_modulus * strain

    if stress > yield_stress:
        print("The pluck displacement for this material is too large." +
              "\nProgram ended.")
        exit()


def check_plotting_times(sim_time, plot_times):

    for time in plot_times:
        if time > sim_time:
            print("At least one plotting time was greater than the "
                  "simulation time.\nProgram ended.")
            exit()
        elif time < 0:
            print("At least one plotting time was less than t=0." +
                  "\nProgram ended.")
            exit()


def check_courant_number(courant_number):

    if courant_number >= 1 or courant_number <= 0:
        print("The courant number entered is not valid.\nProgram ended.")
        exit()


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--string_length", type=float, default=100,
                        required=False, help="Length of the guitar string.")

    parser.add_argument("-pp", "--pluck_position", type=float, default=50,
                        required=False, help="Position of the pluck.")

    parser.add_argument("-pd", "--pluck_displacement", type=float, default=5,
                        required=False, help="Displacement of the pluck.")

    parser.add_argument("-t", "--time", type=float, default=50, required=False,
                        help="Time of solution.")

    parser.add_argument("-pt", "--plot_times", nargs='+', type=float,
                        required=False,
                        help="Times at which to plot the solution.")

    parser.add_argument("-dt", "--time_steps", type=float, default=100,
                        required=False,
                        help="The number of time nodes in the solution.")

    parser.add_argument("-y", "--yield_stress", type=float, default=215,
                        required=False,
                        help="Yield strength of string material.")

    parser.add_argument("-cn", "--courant_number", type=float, default=0.75,
                        required=False, help="The Courant Number is " +
                        "u*dt*dx and must be less than 1.")

    parser.add_argument("-v0", "--initial_velocity", type=float, default=0,
                        required=False, help="Initial velocity of the " +
                        "string at the pluck position")

    parser.add_argument("-c", "--wave_speed", type=float, default=330,
                        required=False, help="Speed of the wave in meters" +
                        " per second.")

    parser.add_argument("-E", "--youngs_modulus", type=float, default=190000,
                        required=False, help="Young's modulus of material.")

    args = parser.parse_args()

    check_pluck_position(args.string_length, args.pluck_position)
    check_pluck_displacement(args.string_length, args.pluck_position,
                             args.pluck_displacement, args.yield_stress,
                             args.youngs_modulus)
    check_courant_number(args.courant_number)
    check_plotting_times(args.time, args.plot_times)

    user_input = {'String Length': args.string_length,
                  'Pluck Position': args.pluck_position,
                  'Pluck Displacement': args.pluck_displacement,
                  'Time': args.time,
                  'Time Steps': args.time_steps,
                  'Plotting Times': args.plot_times,
                  'Courant Number': args.courant_number,
                  'Initial Velocity': args.initial_velocity,
                  'Wave Speed': args.wave_speed}

    return user_input


if __name__ == "__main__":

    main()
