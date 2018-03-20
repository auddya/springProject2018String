#! /usr/bin/python

def get_length(): 

   print('\nLength of string:')
   string_length = raw_input('> ')

   try: 
      string_length = float(string_length)
   except ValueError:
      print('Please enter a number...')
      string_length = get_length()
   
   return string_length

def get_pluck_position(string_length):

   print('\nPosition of pluck:')
   pluck_position = raw_input('> ')

   try:
      pluck_position = float(pluck_position)
   except ValueError:
      print('Please enter a number...')
      pluck_position = get_pluck_position(string_length)

   if (pluck_position <= 0) or (pluck_position >= string_length):
      print('Choose a position between 0 and '+str(string_length))
      pluck_position = get_pluck_position(string_length)
   
   return pluck_position

def get_pluck_displacement():

   print('\nDisplacement of pluck')
   pluck_displacement = raw_input('> ')

   try:
      pluck_displacement = float(pluck_displacement)
   except ValueError:
      print('Please enter a number...')
      pluck_displacement = get_pluck_displacement()

   return pluck_displacement

def get_time():

   print('\nTime elapsed during calculation:')
   time = raw_input('> ')

   try:
      time = float(time)
   except ValueError:
      print('Please enter a number...')
      time = get_time()

   return time

def get_yield_strength():

   print('\nYield strength of string:')
   yield_strength = raw_input('> ')

   try:
      yield_strength = float(yield_strength)
   except ValueError:
      print('Please enter a number...')
      yield_strength = get_yield_strength()

   return yield_strength


def main():
   string_length = get_length()
   pluck_position = get_pluck_position(string_length)
   pluck_displacement = get_pluck_displacement()
   time = get_time()
   yield_strength = get_yield_strength()

   output = (string_length, pluck_position, pluck_displacement,
             time, yield_strength)
   return output
