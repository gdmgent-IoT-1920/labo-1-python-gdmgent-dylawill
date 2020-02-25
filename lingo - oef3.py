# Maak het programma LINGO.
# Genereer een willekeurig 4-cijferig nummer.
# Kip = correct cijfer op juiste plaats
# Ei = correct cijfer op verkeerde plaats

import random

# Loop over alle ingegeven nummer
def kipOfEi():
	userGuess = str(input("Raad het juiste getal: "))
	kip = 0
	kipei = 0

# 4 getallen ingeven + raden
	for i in range(4):
		if num[i] == userGuess[i]:
			kip += 1

# Cijfer op juiste plaats?
	for i in num:
		if i in userGuess:
			kipei += 1

# Komt het cijfer overeen?
	ei = kipei - kip

	print("{} kippen, {} eieren".format(kip,ei))

	return kip

# Start het spel
if __name__== '__main__': 
	num = str(random.randrange(1000,10000))
	# Het te raden nummer
	print("NUMMER:", num)
	print()

	print("LINGO-BINGO: Welkom bij het kip en eieren spel")
	print("Kip = juiste plaats, ei = verkeerde plaats")
	print()
	
	print("Geef een viercijferig getal in")
	kip = 0
	count = 0
	while kip != 4:
		count += 1
		kip = kipOfEi()

	print("Je had {} poging(en) nodig".format(count))