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
        print(stress)
        exit()
    elif pluck_position <= 0:
        print("The position of the pluck is less than zero." +
              "\nProgram terminated.")
        exit()


def check_plotting_times(sim_time, plot_times):

    if isinstance(plot_times,list):
        for time in plot_times:
            if time > sim_time:
                print("At least one plotting time was greater than the "
                      "simulation time.\nProgram ended.")
                exit()
            elif time < 0:
                print("At least one plotting time was less than t=0." +
                      "\nProgram ended.")
                exit()


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--string_length", type=float, default=100,
                        required=False, help="Length of the guitar string.")

    parser.add_argument("-pp", "--pluck_position", type=float, default=50,
                        required=False, help="Position of the pluck.")

    parser.add_argument("-pd", "--pluck_displacement", type=float, default=1,
                        required=False, help="Displacement of the pluck.")

    parser.add_argument("-t", "--time", type=float, default=10, required=False,
                        help="Time of solution.")

    parser.add_argument("-pt", "--plot_times", nargs='+', type=float,
                        required=False,
                        help="Times at which to plot the solution.")

    parser.add_argument("-dt", "--time_step", type=float, default=0.001,
                        required=False,
                        help="The time step of the solution.")

    parser.add_argument("-y", "--yield_stress", type=float, default=215,
                        required=False,
                        help="Yield strength of string material.")

    parser.add_argument("-c", "--wave_speed", type=float, default=330,
                        required=False, help="Speed of the wave in meters" +
                        " per second.")

    parser.add_argument("-E", "--youngs_modulus", type=float, default=190000,
                        required=False, help="Young's modulus of material.")

    parser.add_argument("-f", "--frequency", type=float, default=10,
                        required=False, help="Source frequency.")

    parser.add_argument("-x", "--space_step", type=float, default=1,
                        required=False, help="Step size in space.")

    args = parser.parse_args()

    check_pluck_position(args.string_length, args.pluck_position)
    check_pluck_displacement(args.string_length, args.pluck_position,
                             args.pluck_displacement, args.yield_stress,
                             args.youngs_modulus)
    check_plotting_times(args.time, args.plot_times)

    temporal_nodes = args.time / args.time_step

    user_input = {'String Length': args.string_length,
                  'Pluck Position': args.pluck_position,
                  'Pluck Displacement': args.pluck_displacement,
                  'Time': args.time,
                  'Time Step': args.time_step,
                  'Temporal Nodes': temporal_nodes,
                  'Plotting Times': args.plot_times,
                  'Wave Speed': args.wave_speed,
                  'Frequency': args.frequency}

    return user_input


if __name__ == "__main__":

    main()
