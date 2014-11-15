#CLIFS/main.py
#A part of the command line flight simulator.
#Copyright (c) 2014 ks-salutions.
import handler

print "Welcome to C L I F S\n"
print "A command line flight simulator\n"
print "Copyright (C) Ks-Salutions\n"
invalue = ""
while invalue != "q":
	print "Enter input: M for manual flight, A for automatic flight, or Q to quit.\n"
	invalue = raw_input()
	if invalue=="q":
		break