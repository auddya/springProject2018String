#! /usr/bin/python
import argparse

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

    parser.add_argument("-t", "--time", type=float, default=10, required=False,
                        help="Time of solution.")

    parser.add_argument("-pt", "--plot_times", nargs='+', type=float,
                        required=False,
                        help="Times at which to plot the solution.")

    parser.add_argument("-dt", "--time_step", type=float, default=0.01,
                        required=False,
                        help="The time step of the solution.")

    parser.add_argument("-c", "--wave_speed", type=float, default=330,
                        required=False, help="Speed of the wave in meters" +
                        " per second.")

    parser.add_argument("-f", "--frequency", type=float, default=10,
                        required=False, help="Source frequency.")

    parser.add_argument("-x", "--space_step", type=float, default=1,
                        required=False, help="Step size in space.")

    args = parser.parse_args()

    check_plotting_times(args.time, args.plot_times)

    temporal_nodes = args.time / args.time_step
    spatial_nodes = args.string_length / args.space_step

    user_input = {'String Length': args.string_length,
                  'Spatial Nodes': spatial_nodes
                  'Time': args.time,
                  'Time Step': args.time_step,
                  'Temporal Nodes': temporal_nodes,
                  'Plotting Times': args.plot_times,
                  'Wave Speed': args.wave_speed,
                  'Frequency': args.frequency,
                  'Space Step': args.space_step}

    return user_input


if __name__ == "__main__":

    main()
