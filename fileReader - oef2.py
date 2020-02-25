# Gegeven een .txt-bestand met een lijst met een aantal namen, tel dan hoeveel van elke naam er in het bestand is en druk de resultaten af op het scherm.

from collections import Counter

file = open("namen.txt", "r")

data = file.read()

# Split the words
words = data.split()

counts = Counter(words)

print("\n" + str(counts) + "\n")

# Close the file
file.close()