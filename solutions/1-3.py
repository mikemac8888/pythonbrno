# Print out a list of all the unique destinations ryanair flies to from czech republic
destinations = set()
for _, v in czech_ryanair.items():
    destinations = destinations | set(v)
destinations