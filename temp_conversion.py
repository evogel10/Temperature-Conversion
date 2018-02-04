#!/usr/bin/env python3

# Import the use of regular expresion operation
import re

# Opens file to write to
file = open('Question_3_Output.txt','w')

# User input for the temperature scale
user_scale = raw_input('Please enter a temperature scale (F or C): ').upper()

# Uses regex to check if the user entered either F/f for Fahrenheit or C/c for Celsius
while not re.match(r'F|C', user_scale):
	user_scale = raw_input('Invalid temperature scale. Please enter a correct temperature scale (F or C): ').upper()

# User input for the number of degrees
user_temp = raw_input('Please enter a number of degrees: ')

# Uses regex to check if the user entered a digit
while not re.match(r'^-?[0-9]*\.?[0-9]+$',user_temp):
	user_temp = raw_input('Invalid number of degrees. Please enter a correct number of degrees: ')

# Converts the input temperature to a float to be used in function
user_temp = float(user_temp)

# Function used to converent between Fahrenheit and Celsius
def convert_temp(scale = None, source_temp = None):

	# Uses regex to check whether to convert to Fahrenheit or Celsius
	if re.match(r'F', scale):
		return(source_temp - 32.0) * (5.0/9.0)
	elif re.match(r'C', scale):
		return(source_temp * (9.0/5.0)) + 32.0

# Variable to hold converted temperature
temp = convert_temp(user_scale, user_temp)

# Empty variable to hold converted scale
convert_scale = ''

# Uses regex to check whether to use Fahrenheit or Celsius
if re.match(r'F', user_scale):
	convert_scale = 'C'
elif re.match(r'C', user_scale):
	convert_scale = 'F'

# Writes the converent temperature and scale to the output file
output = "%.1f degrees %s is equal to %.1f degrees %s" % (user_temp, user_scale, temp, convert_scale)
file.write(output)
file.close()