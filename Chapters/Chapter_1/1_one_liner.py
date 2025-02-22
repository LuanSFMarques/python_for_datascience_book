txt = "Eight dollars a week or a million on a year - what is the difference? A mathematiciar or a with would give you the wrong answer. The magi brought valuable gifts, but that was not among them. - The Gift of the Magi, O'Henry"

word_lists = [[w.replace(',','') for w in line.split() if w != '-'] for line in txt.replace("?",".").split(".")]

print(*[f"{i}: {line}" for i, line in enumerate(word_lists)], sep="\n") # printing with the index
