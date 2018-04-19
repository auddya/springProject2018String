#! /usr/bin/python
import argparse

def check_pluck_position(string_length, pluck_position):

    if string_length <= pluck_position:
        print("The position of the pluck is greater than the string length.\nProgram ended.")
    elif  pluck_position <= 0:
        print("The position of the pluck is less than zero.\nProgram terminated.")
        exit()
    pass

def check_string_length(string_length, pluck_position, pluck_displacement, yield_strength): 

    pass

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--string_length", type=float, default=20, required=False,
                        help="Length of the guitar string.")

    parser.add_argument("-pp", "--pluck_position", type=float, default=10, required=False,
                        help="Position of the pluck.")

    parser.add_argument("-pd", "--pluck_displacement", type=float, default=10, required=False,
                        help="Displacement of the pluck.")

    parser.add_argument("-t", "--time", type=float, default=50, required=False,
                        help="Time of solution.")

    parser.add_argument("-y", "--yield_strength", type=float, default=250, required=False,
                        help="Yield strength of string.")

    args = parser.parse_args()

    check_pluck_position(args.string_length, args.pluck_position)
    check_string_length(args.string_length, args.pluck_position, args.pluck_displacement, args.yield_strength)

    user_input = {'String Length' : args.string_length, 'Pluck Position' : args.pluck_position,
              'Pluck Displacement' : args.pluck_displacement, 'Time' : args.time, 
              'Yield Strength' : args.yield_strength}

    return user_input 

if __name__ == "__main__":
   
    main()
