#CLIFS/main.py
#A part of the command line flight simulator.
#Copyright (c) 2014 ks-salutions.
import handler

def manual_flight():
	"""
This function asks the user which direction to fly in and at which speed. I'll probably update handler.py to include this.
	"""
	print "Welcome to manual flight.\n"
	print "Enter a direction."
	dir = raw_input()
	print "Now, enter a speed."
	speed = raw_input()
	handler.go(dir, speed)


def automatic_flight():
	"""
This function is essentially the same as the last, with one extra peramitor. Again, I will probably update handler.py.
	"""
	print "Enter a direction."
	dir = raw_input()
	print "Now, enter a speed."
	speed = raw_input()
	print "Finally, enter a distance."
	distance = raw_input()
	handler.go_ex(dir, distance, speed)

print "Welcome to C L I F S\n"
print "A command line flight simulator\n"
print "Copyright (C) Ks-Salutions\n"
invalue = ""
while invalue != "q":
	print "Enter input: M for manual flight, A for automatic flight, or Q to quit.\n"
	invalue = raw_input()
	if invalue=="q":
		break
	if invalue=="m":
		manual_flight()
	if invalue=="a":
		automatic_flight()

