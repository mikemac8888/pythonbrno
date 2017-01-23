# Which destinations are accessible from Prague (PRG)?
czech_ryanair['PRG']

# Construct a list of all the destinations ryanair flies to from czech republic
destinations = []
for _, v in czech_ryanair.items():
    destinations += v
destinations