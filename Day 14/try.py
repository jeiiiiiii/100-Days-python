from GameData import data
import random


def profile():
  random_number = random.randint(0, 49)
  name = data[random_number]['name']
  follower_count = data[random_number]['follower_count']
  description = data[random_number]['description']
  country = data[random_number]['country']
  compare = (f"{name}, a {description}, from {country}.")
  print(compare, follower_count)

profile()