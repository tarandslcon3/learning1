planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet, end=' ')
# loud_short_planets = [planet.upper() + '!'
#  for planet in planets 
#  if len(planet) < 6]
# print(loud_short_planets)

# print([32 for planet in planets])

def count_negatives(nums):
    return len([num for num in nums if num < 0])

# def count_negatives(nums):
#     n_negative = 0
#     for num in nums:
#         if num < 0:
#            n_negative = n_negative + 1
#     return n_negative
nums = [1, -2, 3, -4, 5]
print(count_negatives(nums))


# short_planets = [planet for planet in planets if len(planet) <= 7]
# print(short_planets)


# multiplicands = (2, 2, 2, 3, 3, 5)
# product = 1
# for mult in multiplicands:
#     product = product * mult
# print(product)