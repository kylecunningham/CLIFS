#CLIFS/main.py
#A part of the command line flight simulator.
#Copyright (c) 2014 ks-salutions.
import handler
handle = handler.handler ()
def manual_flight():
	"""
This function asks the user which direction to fly in and at which speed. I'll probably update handle.py to include this.
	"""
	print ("Welcome to manual flight.\n")
	print("Enter a direction.")
	dir = input()
	print("Now, enter a speed.")
	speed = input()
	return_value = handle.go(dir, speed)
	if return_value == -1:
		print ("Error: This is not a valid direction.")
		main_menu()

def automatic_flight():
	"""
This function is essentially the same as the last, with one extra peramitor. Again, I will probably update handle.py.
	"""
	print ("Welcome to the automatic flight system.\n")
	print("Enter a direction.")
	dir = input()
	print("Now, enter a speed.")
	speed = input()
	print("Finally, enter a distance.")
	distance = input()
	return_value = handle.go_ex(dir, distance, speed)
	if return_value == -1:
		print ("Error: This is not a valid direction.")
		main_menu()

def display_credits():
	"""
Displays game credits. I like modular functions!
	"""
	print ("C L I F S credits.\n")
	print ("Some code copyright (C) 2014 Kyle Cunningham.\nHandler.py copyright (C) Ethin Probst.")

def main_menu ():
	print("Welcome to C L I F S\n")
	print("A command line flight simulator\n")
	print("Copyright (C) Ks-Salutions\n")
	invalue = ""
	while invalue != "q":
		print("Enter input: M for manual flight, A for automatic flight, C to display credits, or Q to quit.\n")
		invalue = input()
		if invalue=="q":
			break
		if invalue=="m":
			manual_flight()
		if invalue=="a":
			automatic_flight()
		if invalue=="c":
			display_credits()

main_menu()
