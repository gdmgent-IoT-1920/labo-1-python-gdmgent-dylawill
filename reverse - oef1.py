# Schrijf een programma dat de gebruiker vraagt naar een ​​lange reeks woorden bevat. Geef als output de woorden terug, maar in omgekeerde volgorde.


# Ask the user to enter a sentence
sentence = input('Enter a sentence you want to reverse: ')

# Split the sentence on spaces
reversed_sentence = sentence.split(' ')
# Reverse the sentence
reversed_sentence.reverse()

# Show output
print('Your sentence reversed: ')
# Join reversed words
print(' '.join(reversed_sentence))
