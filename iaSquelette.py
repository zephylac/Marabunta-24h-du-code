from wrapper import Protocol
from Comment import comment


def antIA(ant):
	# ANT PROGRAM
	return

def nestIA(nest):
	# NEST PROGRAM
	return

while True:
	nameEntity, entity = Protocol.readInput()
	if nameEntity == 'ANT':
		antIA(entity)
	elif nameEntity == 'NEST':
		nestIA(entity)
	Protocol.exit()
