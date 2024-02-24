planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet, end=' ')
loud_short_planets = [planet.upper() + '!'
 for planet in planets 
 if len(planet) < 6]
print(loud_short_planets)



# short_planets = [planet for planet in planets if len(planet) <= 7]
# print(short_planets)


# multiplicands = (2, 2, 2, 3, 3, 5)
# product = 1
# for mult in multiplicands:
#     product = product * mult
# print(product)